import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"
res = requests.delete(url)


# print(res.status_code)
assert res.status_code == 204