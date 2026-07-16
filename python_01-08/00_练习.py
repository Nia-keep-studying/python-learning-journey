# from random import randint
# #邀请三个人
# list_guest = ["吴家乐","李星","傅树元"]
# print(f"可以邀请{list_guest}和我共进晚餐么")
# guest_busy = list_guest.pop(0)
# list_guest.append("狒狒")
# print(f"{guest_busy}不有事情来不了")
# print(list_guest)
# print("我找到了一个更大的餐桌！")
#
#
# list_guest.insert(0,"李金泽")
# list_guest.insert(2,"韦卓燃")
# list_guest.append("小铭")
# print(f"现在需要邀请的名单是{list_guest}")
# for i in list_guest:
#     print(f"{i},可以邀请你来共进晚餐么")
# print("餐桌不够了，只能邀请两个人！")
# for i in range(0,len(list_guest)-2):
#     del1 = list_guest.pop(randint(0,len(list_guest)-2))
#     print(f"抱歉{del1},位置不够不能邀请你了")
# for i in list_guest:
#     print(f"{i}依然在受邀之列")
#
# del list_guest[0]
# del list_guest[0]
# print(list_guest)




# list_place = ["yunnan","chongqing","newzealand","shanghai"]
# print(list_place)
# print(sorted(list_place))
# print(list_place)
# print(sorted(list_place,reverse=True))


#if 语句的练习
import random
alien_color = (random.choice(["green","yellow","red"]))
if alien_color == "green":
    print("恭喜你获得了五分")
elif alien_color == "yellow":
    print("恭喜你获得了十分")
else:
    print("恭喜你获得了十五分")