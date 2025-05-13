# requests also supports other HTTP methods like PUT, DELETE, PATCH, etc.
# examples of using these methods are shown below.
import requests
import json
# PUT request
url = 'https://jsonplaceholder.typicode.com/posts/1'
data = { 
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.put(url,json=data)
print('PUT request:')
# print('Status Code:', response.status_code)
print('Response Body:', response.json())
# PATCH request
patch_data = {
    'title': 'updated title'
}
patch_response = requests.patch(url, json=patch_data)
print('\nPATCH request:')
print('Response Body:', patch_response.json())

# DELETE request
delete_response = requests.delete(url)
print('\nDELETE request:')
print('Response Body:', delete_response.json())