# print("hello world")  这些都是注释 以#开头 为单行注释
"""
这是多行注释 三个引号构成，多行注释 print
"""
# a = input("随便输入一个东西")
# print(type(a))

# number = input("测试输入")
#
# if type(number) is int:
#     number2 = int(number)
#     print(number2)
# else:
#     print("不是数字")

# a = 1
# b = 22
# c = 333
# d = 4444
#
# print(a, b, c, d,sep=',',end='.')

# a = 100
# b = 200
# max_value = a if a > b else b
# print(max_value)


# age = int(input("请输入年龄"))
#
# if age >= 18:
#     AnJian = (input("安检结果"))
#
#     if int(AnJian) == 0:
#         print("可以进站")
#     else:
#         print("不可进站")
# else:
#     print("年龄未满18岁")

#猜拳游戏
# Chu = input("输入出拳")
# if Chu == "1":
#     print("平局")
# elif Chu == "2":
#     print("你输了")
# elif Chu == "3":
#     print("你赢了")

# 石头剪刀布小游戏
# import random
# player = int(input("猜拳1=石头 2=剪刀 3=布"))
# computer = random.randint(1,3)
# print(computer)
# if player == computer:
#
#     print("平局")
# elif player == 1 and computer == 2:
#     print("你出石头，电脑出剪刀，你赢了")
# elif player ==1 and computer == 3:
#     print("你出石头，电脑出布，你输了")
# elif player == 2 and computer == 1:
#     print("你出剪刀，电脑出石头，你输了")
# elif player == 2 and computer == 3:
#     print("你出剪刀，电脑出布，你赢了")
# elif player == 3 and computer == 1:
#     print("你出布，电脑出石头，你赢了")
# elif player == 3 and computer == 2:
#     print("你出布，电脑出剪刀，你输了")

# a = range(0,20,2)
# for i in a:
#     print(i)


# 列表的相关操作

#增加元素 append(元素)  追加到末尾
#        insert(下标，元素) 将元素插入到指定下标位置，后面元素右移
# number_num = [1,3,5,7,9,11,13,17,19]
# number_num[3] = 300
# third = number_num[3]
# print(number_num)


# 列表名.count(元素)   数这个元素在列表中出现的个数
# 列表名.index(元素)   查询这个元素在列表中的下标     len() 查看长度，可以查看列表总共有多少


# 删除列表最后一个数据 列表名.pop()   删除指定下标的元素 列表名.pop(下标) 或者 def 列表名[下标]
# 删除指定元素值 列表名.remove(元素值)
# a = ["你","我","他","你们","我们","他们"]
# a.remove("他")
# print(a)


