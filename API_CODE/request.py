import requests

# url = "https://api.github.com/search/repositories"
# url += "?q=language:python+sort:stars+stars:>10000"

url = "https://jsonplaceholder.typicode.com/posts"

headers = {"Accept":"application/vnd.github.v3+json"} #这个就是请求头，改了里面的Accept，没提到的都是默认
r = requests.get(url,headers=headers)
print(f"status code{r.status_code}") #status_code : 状态码

#把json数据变成python能处理的字典    .json是requests里的方法，等于内置的.json.loads(r.readtext())
# response_dict = r.json()
# print(response_dict.keys())

# print(f"Total count{response_dict["total_count"]}")
# # print(f"complete results{response_dict["incomplete_results"]}")

# # print(f"unit 1 {response_dict["items"][0]["name"]}")

# #查看显示的 items里的项目的长度（个数）
# repo_dicts = response_dict["items"]
# print(len(repo_dicts))

# #打印第一个项目的具体信息 键值对
# repo_dict1 = repo_dicts[0]
# print(f"\nkey: {len(repo_dict1.keys())}")

# for key,value in sorted(repo_dict1.items()):
#     print(f"{key} - {value}")


p = requests.post(url,data={"username":"ax","password":"ajax"})
print(f"status code {p.status_code}")
print(p.json())