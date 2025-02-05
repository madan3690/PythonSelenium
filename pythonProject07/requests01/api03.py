import json

import jsonpath
import requests

url = "https://reqres.in/api/users"

file=open("C://DataFiles/API/Neo007.json", 'r')
json_input=file.read()
print(json_input)

request_json=json.loads(json_input)
print(request_json)

response=requests.post(url,request_json)
print(response)
print(response.content)


assert response.status_code == 201
print(response.headers)
print(response.headers.get('Connection'))


response_json=json.loads(response.text)

# response_json=json.loads(response.content)
# response_json2=json.loads(response.text)
# assert response_json==response_json2
print(response_json.get('id'))

ids=jsonpath.jsonpath(response_json,'id')
print(ids[0])

