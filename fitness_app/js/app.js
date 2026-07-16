/* ============================================
   app.js — 事件处理 + DOM 渲染 + 应用编排
   依赖（按加载顺序）：data.js → calc.js → mealplan.js
   ============================================ */

var FIT = FIT || {};

// ============================================================
// 全局状态
// ============================================================

FIT.state = {
    gender: "male",
    dayIndex: 1               // 食谱种子，每次"换食谱"+1
};

// ============================================================
// 初始化（DOM 加载完成后执行）
// ============================================================

FIT.init = function() {
    // --- DOM 引用 ---
    FIT.el = {
        genderBtns:    document.querySelectorAll("#genderToggle .toggle-btn"),
        height:        document.getElementById("height"),
        weight:        document.getElementById("weight"),
        age:           document.getElementById("age"),
        activity:      document.getElementById("activity"),
        targetKg:      document.getElementById("targetKg"),
        weeks:         document.getElementById("weeks"),
        bmiDisplay:    document.getElementById("bmiDisplay"),
        btnCalculate:  document.getElementById("btnCalculate"),
        btnNewPlan:    document.getElementById("btnNewPlan"),
        warningBanner: document.getElementById("warningBanner"),
        statBmr:       document.getElementById("statBmr"),
        statTdee:      document.getElementById("statTdee"),
        statTarget:    document.getElementById("statTarget"),
        macroContent:  document.getElementById("macroContent"),
        timelineContent: document.getElementById("timelineContent"),
        mealGrid:      document.getElementById("mealGrid"),
        mealSection:   document.getElementById("mealSection"),
        exerciseList:  document.getElementById("exerciseList"),
        exerciseSection: document.getElementById("exerciseSection"),
        noResults:     document.getElementById("noResults"),
        resultsCol:    document.getElementById("resultsCol"),
        heightHint:    document.getElementById("heightHint"),
        weightHint:    document.getElementById("weightHint")
    };

    // --- 绑定事件 ---
    FIT._bindEvents();

    // --- 从 LocalStorage 恢复上次输入 ---
    FIT._loadFromStorage();

    // --- 初始 BMI 显示 ---
    FIT._updateBMI();
};

// ============================================================
// 事件绑定
// ============================================================

FIT._bindEvents = function() {
    var el = FIT.el;

    // 性别切换
    el.genderBtns.forEach(function(btn) {
        btn.addEventListener("click", function() {
            el.genderBtns.forEach(function(b) { b.classList.remove("active"); });
            btn.classList.add("active");
            FIT.state.gender = btn.dataset.value;
        });
    });

    // BMI 实时更新
    el.height.addEventListener("input", FIT._updateBMI);
    el.weight.addEventListener("input", FIT._updateBMI);

    // 表单验证
    el.height.addEventListener("input", FIT._validateForm);
    el.weight.addEventListener("input", FIT._validateForm);
    el.age.addEventListener("input", FIT._validateForm);
    el.targetKg.addEventListener("input", FIT._validateForm);
    el.weeks.addEventListener("input", FIT._validateForm);

    // 计算按钮
    el.btnCalculate.addEventListener("click", FIT._handleCalculate);

    // 换食谱按钮
    el.btnNewPlan.addEventListener("click", FIT._handleNewPlan);
};

// ============================================================
// 收集表单数据
// ============================================================

FIT._collectData = function() {
    var el = FIT.el;
    return {
        gender:        FIT.state.gender,
        heightCm:      parseFloat(el.height.value),
        weightKg:      parseFloat(el.weight.value),
        age:           parseInt(el.age.value),
        activityLevel: parseFloat(el.activity.value),
        targetKg:      parseFloat(el.targetKg.value),
        weeks:         parseInt(el.weeks.value)
    };
};

// ============================================================
// 计算按钮处理
// ============================================================

FIT._handleCalculate = function() {
    if (!FIT._validateForm()) return;

    var d = FIT._collectData();

    // --- 核心计算 ---
    var bmr    = FIT.calcBMR(d.weightKg, d.heightCm, d.age, d.gender);
    var tdee   = FIT.calcTDEE(bmr, d.activityLevel);
    var deficitInfo = FIT.calcDeficit(tdee, d.targetKg, d.weeks);
    var macros = FIT.calcMacros(deficitInfo.dailyTarget, d.weightKg);
    var goal    = FIT.estimateGoalDate(d.targetKg, deficitInfo.deficitPerDay);

    // --- 食谱 ---
    var mealPlan = FIT.generateMealPlan(deficitInfo.dailyTarget, macros, d, FIT.state.dayIndex);

    // --- 运动 ---
    var exercisePlan = FIT.recommendExercises(d.weightKg, deficitInfo.deficitPerDay);

    // --- 汇总 ---
    var result = {
        bmr: bmr,
        tdee: tdee,
        deficitInfo: deficitInfo,
        macros: macros,
        goal: goal,
        mealPlan: mealPlan,
        exercisePlan: exercisePlan
    };

    // --- 保存到 LocalStorage ---
    FIT._saveToStorage(d);

    // --- 渲染 ---
    FIT._renderResults(result);

    // --- 滚动到结果区 ---
    document.getElementById("calculator").scrollIntoView({ behavior: "smooth" });
};

// ============================================================
// 渲染结果
// ============================================================

FIT._renderResults = function(r) {
    var el = FIT.el;

    // --- 隐藏占位，显示结果 ---
    el.noResults.style.display = "none";

    // --- 状态卡片 ---
    el.statBmr.textContent    = r.bmr.toLocaleString();
    el.statTdee.textContent   = r.tdee.toLocaleString();
    el.statTarget.textContent = r.deficitInfo.dailyTarget.toLocaleString();
    if (r.deficitInfo.isHealthy) {
        el.statTarget.style.color = "";
    } else {
        el.statTarget.style.color = "var(--red)";
    }

    // --- 宏营养素条 ---
    var m = r.macros;
    var targetCal = r.deficitInfo.dailyTarget;
    var proteinPct = Math.round((m.proteinCal / targetCal) * 100);
    var carbsPct   = Math.round((m.carbsCal   / targetCal) * 100);
    var fatPct     = Math.round((m.fatCal     / targetCal) * 100);

    el.macroContent.innerHTML =
        '<div class="macro-list">' +
            '<div class="macro-row">' +
                '<span class="macro-label">蛋白质</span>' +
                '<div class="macro-bar-wrap"><div class="macro-bar protein" style="width:' + proteinPct + '%">' + proteinPct + '%</div></div>' +
                '<span class="macro-value">' + m.proteinG + 'g (' + m.proteinCal + ' kcal)</span>' +
            '</div>' +
            '<div class="macro-row">' +
                '<span class="macro-label">碳水</span>' +
                '<div class="macro-bar-wrap"><div class="macro-bar carbs" style="width:' + carbsPct + '%">' + carbsPct + '%</div></div>' +
                '<span class="macro-value">' + m.carbsG + 'g (' + m.carbsCal + ' kcal)</span>' +
            '</div>' +
            '<div class="macro-row">' +
                '<span class="macro-label">脂肪</span>' +
                '<div class="macro-bar-wrap"><div class="macro-bar fat" style="width:' + fatPct + '%">' + fatPct + '%</div></div>' +
                '<span class="macro-value">' + m.fatG + 'g (' + m.fatCal + ' kcal)</span>' +
            '</div>' +
        '</div>';

    // --- 时间线 ---
    var now = new Date();
    var totalDays = r.goal.daysNeeded;
    var daysPassed = 0;
    var percent = Math.min(100, Math.round((daysPassed / totalDays) * 100));

    el.timelineContent.innerHTML =
        '<div class="timeline-row">' +
            '<div class="timeline-date">今天 → ' + r.goal.goalDate.toLocaleDateString("zh-CN", {year:"numeric", month:"long", day:"numeric"}) + '</div>' +
            '<div class="timeline-weeks">约 ' + Math.round(totalDays / 7) + ' 周</div>' +
        '</div>' +
        '<div style="margin-top:12px;">' +
            '<div class="progress-wrap"><div class="progress-bar" style="width:' + percent + '%"></div></div>' +
            '<div style="display:flex;justify-content:space-between;font-size:11px;color:var(--text-dim);margin-top:4px;">' +
                '<span>今天 · Day 1</span>' +
                '<span>目标 · Day ' + totalDays + '</span>' +
            '</div>' +
        '</div>';

    // --- 每日缺口提示 ---
    el.timelineContent.innerHTML +=
        '<p style="margin-top:10px;font-size:13px;color:var(--accent);">' +
            '每日热量缺口 <strong>' + r.deficitInfo.deficitPerDay + ' kcal</strong> · ' +
            '累计需消耗 <strong>' + r.deficitInfo.totalDeficit.toLocaleString() + ' kcal</strong>' +
        '</p>';

    // --- 警告横幅 ---
    if (r.deficitInfo.warning) {
        el.warningBanner.style.display = "block";
        el.warningBanner.textContent = "⚠️ " + r.deficitInfo.warning;
    } else {
        el.warningBanner.style.display = "none";
    }

    // --- 食谱 ---
    FIT._renderMealPlan(r.mealPlan);

    // --- 运动 ---
    FIT._renderExercises(r.exercisePlan);
};

// ============================================================
// 渲染食谱
// ============================================================

FIT._renderMealPlan = function(mealPlan) {
    var el = FIT.el;
    el.mealSection.style.display = "block";

    var mealNames = {
        breakfast: { icon:"🌅", name:"早餐", cal:"" },
        lunch:     { icon:"☀️", name:"午餐", cal:"" },
        dinner:    { icon:"🌙", name:"晚餐", cal:"" }
    };

    var html = "";

    ["breakfast", "lunch", "dinner"].forEach(function(mealName) {
        var meal = mealPlan[mealName];
        var info = mealNames[mealName];

        html += '<div class="meal-card">';
        html += '<div class="meal-card-header">';
        html += '<div class="meal-name">' + info.icon + ' ' + info.name + '（30% / 40% / 30%）</div>';
        html += '<span class="meal-cal">目标 ' + meal.totals.kcal + ' kcal</span>';
        html += '</div>';

        meal.items.forEach(function(item) {
            html += '<div class="meal-item">';
            html += '<span class="meal-food-name">' + item.food.name + '</span>';
            html += '<span class="meal-food-grams">' + item.grams + 'g</span>';
            html += '<span class="meal-food-cal">' + item.kcal + ' kcal</span>';
            html += '</div>';
        });

        html += '</div>';
    });

    el.mealGrid.innerHTML = html;
};

// ============================================================
// 渲染运动推荐
// ============================================================

FIT._renderExercises = function(exercisePlan) {
    var el = FIT.el;
    el.exerciseSection.style.display = "block";

    var html = "";

    exercisePlan.exercises.forEach(function(plan) {
        var ex = plan.exercise;
        var calMin = Math.round(plan.caloriesBurned / plan.minutes);
        html += '<div class="exercise-card">';
        html += '<div class="exercise-icon">' + ex.icon + '</div>';
        html += '<div class="exercise-name">' + ex.name + '</div>';
        html += '<div class="exercise-meta">' + plan.minutes + ' 分钟 · ~' + calMin + ' kcal/min</div>';
        html += '<div class="exercise-cal">🔥 消耗 ≈ ' + plan.caloriesBurned + ' kcal</div>';
        html += '</div>';
    });

    // 汇总
    html += '<div class="exercise-card" style="border-color:var(--accent);background:rgba(110,207,138,0.04);">';
    html += '<div style="font-size:28px;margin-bottom:10px;">📊</div>';
    html += '<div class="exercise-name">运动合计</div>';
    html += '<div class="exercise-meta">占总缺口的 50%</div>';
    html += '<div class="exercise-cal">🔥 ' + exercisePlan.totalBurn + ' kcal</div>';
    html += '</div>';

    el.exerciseList.innerHTML = html;
};

// ============================================================
// 换食谱按钮
// ============================================================

FIT._handleNewPlan = function() {
    FIT.state.dayIndex++;
    FIT._handleCalculate();
};

// ============================================================
// BMI 实时更新
// ============================================================

FIT._updateBMI = function() {
    var el = FIT.el;
    var weight = parseFloat(el.weight.value);
    var height = parseFloat(el.height.value);

    if (!weight || !height || height <= 0) {
        el.bmiDisplay.textContent = "—";
        el.bmiDisplay.className = "bmi-display";
        return;
    }

    var bmi = FIT.calcBMI(weight, height);
    var cat = FIT.getBMICategory(bmi);

    el.bmiDisplay.textContent = bmi.toFixed(1) + " · " + cat.label;
    el.bmiDisplay.className = "bmi-display " + cat.category;
};

// ============================================================
// 表单验证
// ============================================================

FIT._validateForm = function() {
    var el = FIT.el;
    var valid = true;

    var height = parseFloat(el.height.value);
    var weight = parseFloat(el.weight.value);
    var age    = parseInt(el.age.value);
    var target = parseFloat(el.targetKg.value);
    var weeks  = parseInt(el.weeks.value);

    // 身高
    if (el.height.value && (isNaN(height) || height < 100 || height > 250)) {
        el.heightHint.textContent = "身高范围 100-250 cm";
        valid = false;
    } else {
        el.heightHint.textContent = "";
    }

    // 体重
    if (el.weight.value && (isNaN(weight) || weight < 30 || weight > 300)) {
        el.weightHint.textContent = "体重范围 30-300 kg";
        valid = false;
    } else {
        el.weightHint.textContent = "";
    }

    // 必填检查
    var required = [
        { el:el.height,   name:"身高" },
        { el:el.weight,   name:"体重" },
        { el:el.age,      name:"年龄" },
        { el:el.targetKg, name:"减重目标" },
        { el:el.weeks,    name:"计划周数" }
    ];

    required.forEach(function(field) {
        if (!field.el.value) {
            valid = false;
        }
    });

    if (!valid) {
        el.btnCalculate.style.opacity = "0.5";
    } else {
        el.btnCalculate.style.opacity = "1";
    }

    return valid;
};

// ============================================================
// LocalStorage 持久化
// ============================================================

FIT._saveToStorage = function(data) {
    try {
        localStorage.setItem("fitcalc_input", JSON.stringify(data));
    } catch(e) {
        // 隐私模式或存储满，静默失败
    }
};

FIT._loadFromStorage = function() {
    try {
        var raw = localStorage.getItem("fitcalc_input");
        if (!raw) return;
        var d = JSON.parse(raw);

        var el = FIT.el;
        if (d.heightCm)      el.height.value    = d.heightCm;
        if (d.weightKg)      el.weight.value    = d.weightKg;
        if (d.age)           el.age.value       = d.age;
        if (d.activityLevel) el.activity.value  = d.activityLevel;
        if (d.targetKg)      el.targetKg.value  = d.targetKg;
        if (d.weeks)         el.weeks.value     = d.weeks;

        if (d.gender) {
            FIT.state.gender = d.gender;
            el.genderBtns.forEach(function(b) {
                b.classList.toggle("active", b.dataset.value === d.gender);
            });
        }

        // 恢复后更新 BMI
        FIT._updateBMI();
    } catch(e) {
        // 静默失败
    }
};

// --- DOM 加载完成后初始化 ---
document.addEventListener("DOMContentLoaded", FIT.init);
