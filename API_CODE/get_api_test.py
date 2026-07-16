import requests
from random import randint

# url = "https://api.github.com/search/users"
# url += "?q=jax+in:login"

# headers = {"Accept":"application/vnd.github+json"}

# r = requests.get(url,headers=headers)
# print(f"status code {r.status_code}")

# dict1 = r.json()
# print(f"total count - {dict1['total_count']}\nincomplete_result {dict1['incomplete_results']}")


# all_item = dict1["items"]

# for i in range(3):
#     # print(all_item[i])
#     for key,value in all_item[i].items():
#         print(f"{key} - {value}")
#     print("\n")



#获取我自己的github的主页api（通过get查找用户）
url = "https://api.github.com/search/users"
url += "?q=Nia-keep-studying+in:login"

headers = {"Accept":"application/vnd.github+json"}
response = requests.get(url,headers=headers)
print(response.status_code)

repo_dict = response.json()
print(repo_dict.keys())

# print(f"totalcount:{repo_dict["total_count"]}\nresults{repo_dict["incomplete_results"]}")

user = repo_dict["items"][0]

print(
    f"login: {user['login']}\n"
    f"id: {user['id']}\n"
    f"url: {user['url']}"
)