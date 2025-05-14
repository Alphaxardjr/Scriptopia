# This is the data that is sent in the body of the HTTP requst

# The data is sent in the body of the HTTP request, and it can be in various formats such as JSON, XML, or form data.
# The format of the data is specified in the Content-Type header of the request.
# examples:
import requests
import json
# json data
url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post(url, json=data)
print(response.request.body)

# form data
response = requests.post(url, data=data)
print(response.request.body)
# xml data
xml_data = '''<?xml version="1.0"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>    


</note>'''  

response = requests.post(url, data=xml_data, headers={'Content-Type': 'application/xml'})
print(response.request.body)
