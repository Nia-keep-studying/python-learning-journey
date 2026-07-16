#定义一个字典 字典名 = {key：value，....}
# person =  {'name':"孙家祥","age":24,"phone_number":13407680992,"gender":"男" }
# print(person)
# #增
# person["home"]="临沂"
# print(person)
# #删除
# del person["age"]
# print(person)
# #改
# person["phone_number"]=10086
# print(person)
# #查
# print(person["phone_number"])

# person.clear() #删除所有元素
# print(person)
# print(type(person))

#字典的嵌套
# p1 = {
#     "name":"张三",
#     "gender":"男",
#     "friends":["李四","王五","马六"],
#     "scores":{"语文":65,"数学":89,"英语":70,"计算机":80}
# }
# # print(p1["scores"]["计算机"])
# # print(p1["friends"][1])
# print(p1)
# print(p1.items())
#如果想看语文成绩的话
# 逐层索引即可，用两次方括号：


# print(p1["scores"]["语文"])
# 拆开来看：

# p1["scores"] → 拿到内层字典 {"语文":65, "数学":89, "英语":70, "计算机":80}
# 再 ["语文"] → 拿到对应 value 65


# a = {1:"damn",2:"shit"}

# print(a.items())
# print(set(a))  #自动去掉value值，相当于 set(a.keys())
# print(set(a.items()))
# print(type(set(a.items())))

#字典嵌套练习

# person1 = {"name":"sam","gender":"man","age":"18"}
# person2 = {"name":"john","gender":"man","age":"20"}
# person3 = {"name":"ashly","gender":"female","age":"16"}

# people = [person1,person2,person3]

# for person in people:
#     print(f"\n{person["name"]}'s information is\n{person.items()}")

# pet1 = {"name":"paopao","kind":"cat","owner":"lixing"}
# pet2 = {"name":"doller","kind":"dog","owner":"majiang"}
# pet3 = {"name":"maimai","kind":"dog","owner":"yiyuan"}

# pets = [pet1,pet2,pet3]

# for pet in pets:
#     print(f"name-{pet["name"]}\tkind-{pet["kind"]}\towner-{pet["owner"]}\n")

# favorite_places = {"lixing":["quanzhou","huizhou","shenzhen"],"sjx":["dali","lijiang"],"wujiale":["haerbin"]}

# for name,place in favorite_places.items():
#     print(f"{name}喜欢的地方是{place}")

# cities = {"linyi":{"country":"china","population":200000,"fact":"the home of wxz"},
#           "xini":{"country":"aus","population":100000,"fact":"tha capital of aus"},
#           "LA1":{"country":"us","population":150000,"fact":"basketballgame"}
#           }

# for city,infomation in cities.items():
#     print(f"\n{city} information is {infomation.items()}")
