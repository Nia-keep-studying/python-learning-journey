"""
语法结构 元组名=（元素1，元素2.。。。）
元组中只有一个元素时，必须使用逗号，
my_typle = （1，） 用逗号消除歧义
元组是一个不可变类型，一旦被定义，不能被修改
my_typle = (1,2,3,4)
"""

#访问元组
# my_typle = (1,)
# print(my_typle)
# my_typle2 = (1,2,3,4,5)
# print(my_typle2)

resturtant_foods = (
    "fired rise","tomato fried egg","dish3","dish4","fired chicken"
    )
for i in resturtant_foods:
    print(i)
# resturtant_foods[0] = "dish1" #不允许修改元素内容
print("\n")
resturtant_foods = ("dish1","dish2","frise","burger","hot pot")
for food in resturtant_foods:
    print(food)
print(len(resturtant_foods))
