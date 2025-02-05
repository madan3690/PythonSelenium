import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response=requests.get(url)
# print(response.text)
# print(response.content)
print("HEADERS-------------")
print(response.headers)
print(response.headers.get('Content-Type'))
print("STATUS-------------------------")
print(response.status_code)
print('CONTENT-----------------')
json_res=json.loads(response.text)

print(json_res)
print(json_res.get('id'))
# ids=jsonpath.jsonpath(json_res,'id')
# print(ids)
# print(ids[0])
print(json_res.get('total_pages'))


pages =jsonpath.jsonpath(json_res,'total_pages')
print(pages)
print(pages[0])
# assert pages[0] == 2

