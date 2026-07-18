import search_function as s

def status_code(search_username):
    """判断状态码 查看操作执行的状态码"""
    if s.search_user_from_github(search_username).status_code == 200:
        print("成功执行 200")
    else:
        print(f"状态码错误 {search_username.status_code}")

def get_user_info(username):
    """把用户的信息和序列号对应 并且打印出来 序列号-名称"""
    user_dict = s.return_all_results_dict(username)
    if user_dict:
        for key,value in user_dict.items():
            print(f"{key} - {value['login']}")
        number = input("请输入想要查找用户的序列号： ")
        if number in user_dict:
            print(
                f"login - {user_dict[number]['login']}\n"
                f"id - {user_dict[number]['id']}\n"
                f"url - {user_dict[number]['url']}\n"
            )
        else:
            print("没有该序号")
    else: 
        print("找不到结果")


def get_all_info_list(username):
    """打印所有用户的 序号-列表 对应关系的字典"""
    user_dict = s.return_all_results_dict(username=username)
    if user_dict:
        for key,value in user_dict.items():
            print(f"{key} - {value['login']}")
    else:
        print("没有找到用户信息")


def show_all_info(username):
    user_dict = s.return_all_results_dict(username=username)
    get_all_info_list(username=username)
    number = input("请输入想要查找用户信息的序列号： ")

    if number in user_dict:
        for key,value in user_dict[number].items():
            print(f"{key} - {value}")
    else:
        print("没有此序列号")