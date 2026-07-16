from pathlib import Path
import requests

def search_user_from_github():
    username = input("请输入要查找的用户名: ")
    url = "https://api.github.com/search/users"
    params = {"q":f"{username} in:login"}
    response = requests.get(url,params=params)
    users_search_result = response.json()
    return users_search_result["items"]

def show_all_results():
    users_list = search_user_from_github()
    result_dict = {}
    number = 1
    for i in users_list:
        print(number,i)
        result_dict[str(number)] = i
        number +=1
    return result_dict

def get_user_info():
    user_dict = show_all_results()
    for key,value in user_dict.items():
        print(f"{key} - {value["login"]}")
    number = input("请输入想要查找用户的序列号： ")
    print(
        f"login - {user_dict[number]['login']}\n"
        f"id - {user_dict[number]['id']}\n"
        f"url - {user_dict[number]['url']}\n"
    )

    # print(user_dict)
    # number = input("请输入想要查找用户的序列号： ")
    # for i in user_dict.keys():
    #     if number == user_dict[f"{i}"]:
    #         print(
    #             f"login - {user_dict['user_list']['login']}"
    #             f"id - {user_dict['user_list']['id']}"
    #             f"url - {user_dict['user_list']['url']}"
    #         )
