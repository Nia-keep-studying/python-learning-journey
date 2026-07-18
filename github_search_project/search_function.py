from pathlib import Path
import requests

def search_user_from_github(username):
    """搜索用户的信息,并return 搜索到的信息"""
    url = "https://api.github.com/search/users"
    params = {"q":f"{username} in:login"}
    response = requests.get(url,params=params)
    return response

def return_all_results_dict(username):
    """把搜索到的所有用户信息转化成字典  并用自增的键和用户一一对应"""
    users_list = search_user_from_github(username=username).json()["items"]
    if users_list:
        result_dict = {}
        number = 1
        for user in users_list:
            # print(number,user)
            result_dict[str(number)] = user
            number +=1
    else:
        return None
    return result_dict
