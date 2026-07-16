/* ============================================
   mealplan.js — 每日食谱生成算法
   分类贪婪填充 + 分量钳位 + 确定性轮换
   ============================================ */

var FIT = FIT || {};

// ============================================================
// 三餐结构定义
// 每餐由多个 "槽位" 组成，每个槽位指定：
//   category  → 从哪个食材库取
//   ratio     → 占本餐热量的比例
//   count     → 这个槽位选几份（通常1份，蔬菜可以2份）
// ============================================================

var MEAL_STRUCTURE = {
    breakfast: [
        { category:"staples",  ratio:0.30 },
        { category:"proteins", ratio:0.35 },
        { category:"proteins", ratio:0.15 },  // 第二份蛋白（如牛奶）
        { category:"fruits",   ratio:0.20 }
    ],
    lunch: [
        { category:"staples",  ratio:0.30 },
        { category:"proteins", ratio:0.35 },
        { category:"veggies",  ratio:0.10 },
        { category:"veggies",  ratio:0.10 },
        { category:"fats",     ratio:0.15 }
    ],
    dinner: [
        { category:"staples",  ratio:0.25 },
        { category:"proteins", ratio:0.40 },
        { category:"veggies",  ratio:0.10 },
        { category:"veggies",  ratio:0.15 },
        { category:"fats",     ratio:0.10 }
    ]
};

// ============================================================
// 辅助函数
// ============================================================

/** 计算食物在目标热量下的克数 */
FIT._gramsForCalories = function(food, targetCal) {
    // food.kcal 是每100g的热量
    var calPerGram = food.kcal / 100;
    if (calPerGram === 0) return food.portionMin;  // 几乎零热量的食物（如黄瓜）
    return Math.round(targetCal / calPerGram);
};

/** 钳位到合理范围 */
FIT._clamp = function(value, min, max) {
    return Math.max(min, Math.min(max, value));
};

/** 计算一份食物实际的热量和营养素 */
FIT._calcFoodActual = function(food, grams) {
    var factor = grams / 100;
    return {
        food:    food,
        grams:   grams,
        kcal:    Math.round(food.kcal    * factor),
        protein: Math.round(food.protein * factor * 10) / 10,
        carbs:   Math.round(food.carbs   * factor * 10) / 10,
        fat:     Math.round(food.fat     * factor * 10) / 10
    };
};

// ============================================================
// 主函数：生成一日三餐
// ============================================================

/**
 * @param {number} dailyCalories   每日摄入目标 (kcal)
 * @param {object} macros          宏营养素目标 { proteinG, carbsG, fatG }
 * @param {object} userInfo        用户信息 { weight, heightCm, age, gender }
 * @param {number} dayIndex        第几天（控制食材轮换，同输入同输出）
 * @returns {object} { breakfast:[], lunch:[], dinner:[], totals:{} }
 */
FIT.generateMealPlan = function(dailyCalories, macros, userInfo, dayIndex) {
    if (!dayIndex) dayIndex = 1;

    var mealSplits = {
        breakfast: { ratio: 0.30, items:[] },
        lunch:     { ratio: 0.40, items:[] },
        dinner:    { ratio: 0.30, items:[] }
    };

    var grandTotals = { kcal:0, protein:0, carbs:0, fat:0 };

    // ----- 逐餐生成 -----
    var meals = ["breakfast", "lunch", "dinner"];

    meals.forEach(function(mealName) {
        var mealCalories = Math.round(dailyCalories * mealSplits[mealName].ratio);
        var structure = MEAL_STRUCTURE[mealName];
        var remainingCal = mealCalories;
        var items = [];

        // 对每个槽位，选食材 + 算克数
        structure.forEach(function(slot, idx) {
            var slotCal = Math.round(mealCalories * slot.ratio);

            // 确定性选食材（用 dayIndex + 槽位号做种子）
            var catFoods = FIT.getFoodsByCategory(slot.category);
            var food = catFoods[(dayIndex + idx) % catFoods.length];

            // 算克数
            var grams = FIT._gramsForCalories(food, slotCal);

            // 钳位
            grams = FIT._clamp(grams, food.portionMin, food.portionMax);

            // 计算实际营养值
            var actual = FIT._calcFoodActual(food, grams);

            items.push(actual);
            remainingCal -= actual.kcal;
        });

        // 汇总本餐
        var mealTotals = { kcal:0, protein:0, carbs:0, fat:0 };
        items.forEach(function(item) {
            mealTotals.kcal    += item.kcal;
            mealTotals.protein += item.protein;
            mealTotals.carbs   += item.carbs;
            mealTotals.fat     += item.fat;
        });

        mealSplits[mealName].items = items;
        mealSplits[mealName].totals = mealTotals;

        grandTotals.kcal    += mealTotals.kcal;
        grandTotals.protein += mealTotals.protein;
        grandTotals.carbs   += mealTotals.carbs;
        grandTotals.fat     += mealTotals.fat;
    });

    return {
        breakfast: mealSplits.breakfast,
        lunch:     mealSplits.lunch,
        dinner:    mealSplits.dinner,
        totals:    grandTotals
    };
};
