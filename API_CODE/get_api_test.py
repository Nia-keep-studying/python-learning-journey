import requests
from random import randint

url = "https://api.github.com/search/users"
url += "?q=jax+in:login"

headers = {"Accept":"application/vnd.github+json"}

r = requests.get(url,headers=headers)
print(f"status code {r.status_code}")

dict1 = r.json()
print(f"total count - {dict1['total_count']}\nincomplete_result {dict1['incomplete_results']}")


all_item = dict1["items"]

for i in range(3):
    # print(all_item[i])
    for key,value in all_item[i].items():
        print(f"{key} - {value}")
    print("\n")