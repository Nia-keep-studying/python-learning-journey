/* ============================================
   calc.js — 全部计算函数
   所有函数均为纯函数：相同输入 → 相同输出，无副作用
   ============================================ */

var FIT = FIT || {};

// ============================================================
// 1. 计算 BMI
// ============================================================

FIT.calcBMI = function(weight, heightCm) {
    var heightM = heightCm / 100;
    return weight / (heightM * heightM);
};

/** 返回 BMI 分类 */
FIT.getBMICategory = function(bmi) {
    if (bmi < 18.5) return { category: "under", label: "偏瘦" };
    if (bmi < 24.0) return { category: "normal", label: "正常" };
    if (bmi < 28.0) return { category: "over", label: "偏重" };
    return { category: "obese", label: "肥胖" };
};

// ============================================================
// 2. 计算基础代谢率 (BMR) — Mifflin-St Jeor 公式
// ============================================================

FIT.calcBMR = function(weight, heightCm, age, gender) {
    var bmr = 10 * weight + 6.25 * heightCm - 5 * age;
    if (gender === "male") {
        bmr += 5;
    } else {
        bmr -= 161;
    }
    return Math.round(bmr);
};

// ============================================================
// 3. 计算每日总消耗 (TDEE)
// ============================================================

FIT.calcTDEE = function(bmr, activityLevel) {
    return Math.round(bmr * activityLevel);
};

// ============================================================
// 4. 计算热量缺口 & 每日摄入目标
// ============================================================

FIT.calcDeficit = function(tdee, targetKg, weeks) {
    var totalDeficit = targetKg * 7700;          // 总共需要消耗的热量
    var days = weeks * 7;
    var deficitPerDay = Math.round(totalDeficit / days);
    var dailyTarget = tdee - deficitPerDay;

    // 安全底线
    var minCal = 1200;  // 最低摄入
    var warning = null;
    var isHealthy = true;

    if (dailyTarget < minCal) {
        warning = "每日摄入量过低（" + dailyTarget + " kcal），不建议低于 " + minCal + " kcal。建议延长减脂时间或减小目标体重。";
        isHealthy = false;
    } else if (deficitPerDay > 1000) {
        warning = "每日热量缺口偏大（" + deficitPerDay + " kcal），建议缺口控制在 300~800 kcal，健康减脂不急于一时。";
        isHealthy = false;
    }

    return {
        totalDeficit: totalDeficit,
        deficitPerDay: deficitPerDay,
        dailyTarget: dailyTarget,
        isHealthy: isHealthy,
        warning: warning
    };
};

// ============================================================
// 5. 计算三大宏营养素分配
//    蛋白质: 1.8g/kg 体重
//    脂肪  : 总热量 × 25%
//    碳水  : 剩余热量
// ============================================================

FIT.calcMacros = function(dailyCalories, weight) {
    // 蛋白质
    var proteinG = Math.round(weight * 1.8);
    var proteinCal = proteinG * 4;

    // 脂肪 (25% of total)
    var fatCal = Math.round(dailyCalories * 0.25);
    var fatG = Math.round(fatCal / 9);

    // 碳水 = 剩余
    var carbsCal = dailyCalories - proteinCal - fatCal;
    var carbsG = Math.round(carbsCal / 4);

    return {
        proteinG: proteinG,
        carbsG: carbsG,
        fatG: fatG,
        proteinCal: proteinCal,
        carbsCal: carbsCal,
        fatCal: fatCal,
        proteinPct: Math.round((proteinCal / dailyCalories) * 100),
        carbsPct:   Math.round((carbsCal   / dailyCalories) * 100),
        fatPct:     Math.round((fatCal     / dailyCalories) * 100)
    };
};

// ============================================================
// 6. 预测减脂完成日期
// ============================================================

FIT.estimateGoalDate = function(targetKg, deficitPerDay) {
    var totalDays = Math.ceil((targetKg * 7700) / deficitPerDay);
    var today = new Date();
    var goalDate = new Date(today);
    goalDate.setDate(today.getDate() + totalDays);
    return {
        daysNeeded: totalDays,
        weeksNeeded: Math.round(totalDays / 7),
        goalDate: goalDate
    };
};

// ============================================================
// 7. 运动消耗计算
//    公式: MET × 3.5 × 体重(kg) ÷ 200 = kcal/min
// ============================================================

FIT.calcExerciseBurn = function(met, weightKg, minutes) {
    return Math.round((met * 3.5 * weightKg / 200) * minutes);
};

/** 推荐 4 种运动及其时长，合计燃烧约 50% 每日缺口 */
FIT.recommendExercises = function(weight, deficitPerDay) {
    // 选4种代表不同强度的运动
    var picks = [
        { id:"briskWalk", min:30 },   // 快走 30min
        { id:"strength",  min:20 },   // 力量 20min
        { id:"run",       min:15 },   // 跑步 15min
        { id:"yoga",      min:15 }    // 瑜伽 15min
    ];

    var plan = picks.map(function(p) {
        var exercise = FIT.getExerciseById(p.id);
        var calBurn = FIT.calcExerciseBurn(exercise.met, weight, p.min);
        return {
            exercise: exercise,
            minutes: p.min,
            caloriesBurned: calBurn
        };
    });

    var totalBurn = plan.reduce(function(sum, p) { return sum + p.caloriesBurned; }, 0);

    return {
        exercises: plan,
        totalBurn: totalBurn,
        targetBurn: Math.round(deficitPerDay * 0.5)
    };
};
