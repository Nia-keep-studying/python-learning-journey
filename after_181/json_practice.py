from pathlib import Path
import json

# list = [1,2,3,4,5]
# path1 = Path(__file__).parent/"number_list.json"
# path1.write_text(json.dumps(list))

# print(path1.read_text())

# print(json.loads(path1.read_text()))
# print(type(json.loads(path1.read_text())))

#写一个记住用户名字的程序，写入json，如果是第一次就转换为注册
#第二次修改，（重构） 把这个改为一个函数
# def get_username():
#     path_name = Path(__file__).parent/"username.json"
#     if path_name.exists():
#         print(f"welcome back {json.loads(path_name.read_text())} !")
#     else:
#         username = input("请输入你的名字: ")
#         path_name.write_text(json.dumps(username))
#         print(f"we'll remember you, {username} !")

# get_username()

#重构可以把上面的那些代码拆分成三个函数，这样逻辑性更高，参考书中185页，回头我会自己写一下的

# def get_username():
#     path_get_username = Path(__file__).parent/"username.json"
#     if path_get_username.exists():
#         return json.loads(path_get_username.read_text())
#     else:
#         return None

# def write_username():
#     name = input("请输入你的名字: ")
#     path_new_name = Path(__file__).parent/"username.json"
#     path_new_name.write_text(json.dumps(name))
#     print(f"we'll remember you when you come back {name} !")

    

# def greet_user():
#     path_username = Path(__file__).parent/"username.json"
#     if path_username.exists():  #username = get_username()直接get_username()方法里就检查了
#         print(f"welcome back {get_username()}") #if username:  #检查得到的值是不是空,再+前面那一句
#     else:
#         write_username()
# #小更改，可以只检查一次,以及path_username这个文件可以放到全局，多看书185页写法 
# greet_user()




#10.11 喜欢的数 and 10.12 记住喜欢的数(我直接把10.12的写出来了，因为我想写的完整一点)
# favorite_number = Path(__file__).parent/"favorite_number.json"
# if favorite_number.exists():
#     print(f"I know your favorite number! Its {json.loads(favorite_number.read_text())}")
# else:
#     try:
#         get_favorite_number = int(input("请输入一个喜欢的数字"))
#     except ValueError:
#         print("要输入数字！数字！")
#     else:
#         favorite_number.write_text(json.dumps(get_favorite_number))
#         print(f"I will remember {get_favorite_number} as your favorite number")



def get_username():
    path_get_username = Path(__file__).parent/"username.json"
    if path_get_username.exists():
        return json.loads(path_get_username.read_text())["name"]
    else:
        return None
# try:
#     print(f"welcome back {get_username()} !")
# except FileNotFoundError:
#     write_username()

def write_username():
    user_data = write_userinfomation()
    path_new_name = Path(__file__).parent/"username.json"
    path_new_name.write_text(json.dumps(user_data))
    print(f"we'll remember you when you come back {user_data['name']} !")

def write_userinfomation():
    name = input("请输入您的名字")
    age = input("请输入你的年龄")
    gender = input("请输入性别")
    user_infomation = {"name":name,"age":age,"gender":gender}
    return user_infomation

def greet_user(): 
    if get_username():   #name = get_username 这样装一下就不用调用两次了
        print(f"welcome back {get_username()}") 
    else:
        write_username()

def print_user_data():
    path_user = Path(__file__).parent/"username.json"
    for key,value in json.loads(path_user.read_text()).items():
        print(f"{key} - {value}")

greet_user()
print_user_data()