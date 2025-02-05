import json

import jsonpath
import requests

url="https://reqres.in/api/users"
file=open("C://DataFiles/API/Neo007.json",'r')
input=file.read()
print(input)
json_req=json.loads(input)
print(json_req)
# response=requests.post(url,"C://DataFiles/API/Neo007.json")
response=requests.post(url,json_req)
assert response.status_code==201

print(response.content)
print(response.headers)
print(response.headers.get("connection"))
json_response=json.loads(response.text)
print(json_response)
print(json_response.get('id'))
ids=jsonpath.jsonpath(json_response,'id')
print(ids)
print(ids[0])