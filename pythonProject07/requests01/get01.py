
import json

import jsonpath
import requests

url="https://reqres.in/api/users?page=2"

response=requests.get(url)

assert response.status_code==200
print(response.headers)
print(response.headers.get('Connection'))
json_response=json.loads(response.text)
print(response.text)
print(json_response)
ids=jsonpath.jsonpath(json_response,'total')
print(ids[0])
