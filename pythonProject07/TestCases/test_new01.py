import requests
import json
import jsonpath

def test_get_new():
    url = "https://reqres.in/api/users?page=2"

    response = requests.get(url)
    # print(response.text)
    # print(response.content)
    print("HEADERS-------------")
    print(response.headers)
    print(response.headers.get('Content-Type'))
    print("STATUS-------------------------")
    print(response.status_code)
    print('CONTENT-----------------')
    json_res = json.loads(response.text)

    print(json_res)
    print(json_res.get('id'))
    # ids=jsonpath.jsonpath(json_res,'id')
    # print(ids)
    # print(ids[0])
    print(json_res.get('total_pages'))

    pages = jsonpath.jsonpath(json_res, 'total_pages')
    print(pages)
    print(pages[0])
    # assert pages[0] == 2

def test_get_02():
    url = "https://reqres.in/api/users?page=2"

    response = requests.get(url)

    assert response.status_code == 200
    print(response.headers)
    print(response.headers.get('Connection'))
    json_response = json.loads(response.text)
    print(response.text)
    print(json_response)
    ids = jsonpath.jsonpath(json_response, 'total')
    print(ids[0])

