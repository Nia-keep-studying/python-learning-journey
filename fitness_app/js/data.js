/* ============================================
   data.js — 食材数据库 + 运动数据库
   使用全局命名空间 FIT，与其他 JS 文件共享
   ============================================ */

var FIT = FIT || {};

// ============================================================
// 食材数据库（25种常见中国食材）
// 营养值单位：每 100g 可食部分
// 数据来源：中国食物成分表（标准版）第六版
// ============================================================

FIT.foods = [
    // ----- 主食 (staples) -----
    { id:"rice",           name:"白米饭",   category:"staples",  kcal:116, protein:2.6,  carbs:25.9, fat:0.3,  portionMin:100, portionMax:250 },
    { id:"brownRice",      name:"糙米饭",   category:"staples",  kcal:111, protein:2.6,  carbs:23.0, fat:0.9,  portionMin:100, portionMax:250 },
    { id:"wholeWheatBread",name:"全麦面包", category:"staples",  kcal:247, protein:13.0, carbs:41.0, fat:3.4,  portionMin:50,  portionMax:150 },
    { id:"sweetPotato",    name:"蒸红薯",   category:"staples",  kcal:86,  protein:1.6,  carbs:20.1, fat:0.1,  portionMin:100, portionMax:300 },
    { id:"oatmeal",        name:"燕麦片",   category:"staples",  kcal:389, protein:16.9, carbs:66.3, fat:6.9,  portionMin:30,  portionMax:80  },
    { id:"steamedBun",     name:"馒头",     category:"staples",  kcal:221, protein:7.0,  carbs:44.2, fat:1.1,  portionMin:80,  portionMax:200 },
    { id:"buckwheatNoodles",name:"荞麦面(熟)",category:"staples",kcal:110, protein:4.4,  carbs:21.0, fat:0.4,  portionMin:100, portionMax:250 },

    // ----- 蛋白质 (proteins) -----
    { id:"chickenBreast",  name:"鸡胸肉",   category:"proteins", kcal:133, protein:31.0, carbs:0.0,  fat:1.2,  portionMin:80,  portionMax:200 },
    { id:"egg",            name:"鸡蛋(整)",  category:"proteins", kcal:155, protein:13.0, carbs:1.1,  fat:11.0, portionMin:50,  portionMax:150 },
    { id:"tofu",           name:"豆腐",     category:"proteins", kcal:76,  protein:8.0,  carbs:2.0,  fat:4.0,  portionMin:80,  portionMax:200 },
    { id:"leanBeef",       name:"瘦牛肉",   category:"proteins", kcal:125, protein:22.0, carbs:0.0,  fat:4.0,  portionMin:80,  portionMax:180 },
    { id:"salmon",         name:"三文鱼",   category:"proteins", kcal:208, protein:20.0, carbs:0.0,  fat:13.0, portionMin:80,  portionMax:180 },
    { id:"shrimp",         name:"虾仁",     category:"proteins", kcal:99,  protein:24.0, carbs:0.0,  fat:0.3,  portionMin:60,  portionMax:180 },
    { id:"leanPork",       name:"瘦猪肉",   category:"proteins", kcal:143, protein:20.0, carbs:0.0,  fat:7.0,  portionMin:80,  portionMax:180 },
    { id:"milk",           name:"纯牛奶",   category:"proteins", kcal:61,  protein:3.2,  carbs:4.8,  fat:3.3,  portionMin:150, portionMax:300 },

    // ----- 蔬菜 (veggies) -----
    { id:"broccoli",       name:"西兰花",   category:"veggies",  kcal:34,  protein:2.8,  carbs:6.6,  fat:0.4,  portionMin:80,  portionMax:200 },
    { id:"spinach",        name:"菠菜",     category:"veggies",  kcal:23,  protein:2.9,  carbs:3.6,  fat:0.4,  portionMin:80,  portionMax:200 },
    { id:"tomato",         name:"番茄",     category:"veggies",  kcal:18,  protein:0.9,  carbs:3.9,  fat:0.2,  portionMin:80,  portionMax:200 },
    { id:"cucumber",       name:"黄瓜",     category:"veggies",  kcal:15,  protein:0.7,  carbs:3.6,  fat:0.1,  portionMin:80,  portionMax:200 },
    { id:"carrot",         name:"胡萝卜",   category:"veggies",  kcal:41,  protein:0.9,  carbs:9.6,  fat:0.2,  portionMin:80,  portionMax:200 },
    { id:"bokChoy",        name:"小白菜",   category:"veggies",  kcal:13,  protein:1.5,  carbs:2.2,  fat:0.2,  portionMin:80,  portionMax:200 },

    // ----- 水果 (fruits) -----
    { id:"apple",          name:"苹果",     category:"fruits",   kcal:52,  protein:0.3,  carbs:13.8, fat:0.2,  portionMin:100, portionMax:250 },
    { id:"banana",         name:"香蕉",     category:"fruits",   kcal:89,  protein:1.1,  carbs:22.8, fat:0.3,  portionMin:80,  portionMax:200 },
    { id:"blueberry",      name:"蓝莓",     category:"fruits",   kcal:57,  protein:0.7,  carbs:14.5, fat:0.3,  portionMin:50,  portionMax:150 },

    // ----- 脂肪 (fats) -----
    { id:"oliveOil",       name:"橄榄油",   category:"fats",     kcal:884, protein:0.0,  carbs:0.0,  fat:100,  portionMin:3,   portionMax:12  }
];

// ============================================================
// 运动数据库（10种常见运动）
// MET = 代谢当量，越高越累
// 消耗公式：MET × 3.5 × 体重(kg) ÷ 200 = kcal/min
// ============================================================

FIT.exercises = [
    { id:"walk",       name:"散步",      met:2.5,  type:"cardio",       icon:"🚶" },
    { id:"briskWalk",  name:"快走",      met:3.8,  type:"cardio",       icon:"🚶‍♂️" },
    { id:"jog",        name:"慢跑",      met:7.0,  type:"cardio",       icon:"🏃" },
    { id:"run",        name:"跑步",      met:9.8,  type:"cardio",       icon:"🏃‍♂️" },
    { id:"cycle",      name:"骑自行车",  met:7.5,  type:"cardio",       icon:"🚴" },
    { id:"swim",       name:"游泳",      met:8.0,  type:"cardio",       icon:"🏊" },
    { id:"jumpRope",   name:"跳绳",      met:12.0, type:"cardio",       icon:"🪢" },
    { id:"hiit",       name:"HIIT",      met:8.0,  type:"cardio",       icon:"🔥" },
    { id:"strength",   name:"力量训练",  met:5.0,  type:"strength",     icon:"🏋️" },
    { id:"yoga",       name:"瑜伽",      met:3.0,  type:"flexibility",  icon:"🧘" }
];

// ============================================================
// 辅助查询函数
// ============================================================

/** 按类别筛选食材 */
FIT.getFoodsByCategory = function(cat) {
    return FIT.foods.filter(function(f) { return f.category === cat; });
};

/** 按类别获取随机食材（用 dayIndex + categoryIndex 做确定性选择）*/
FIT.getFoodByCategory = function(cat, index) {
    var list = FIT.getFoodsByCategory(cat);
    return list[index % list.length];
};

/** 按 id 获取运动 */
FIT.getExerciseById = function(id) {
    return FIT.exercises.find(function(e) { return e.id === id; });
};
