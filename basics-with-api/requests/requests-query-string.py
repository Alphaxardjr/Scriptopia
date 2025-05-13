# query string parameters are used to send additional data to the server via the get method
import requests

# format of query string is key=value
# response = requests.get('https://api.example.com/data', params={'key1': 'value1', 'key2': 'value2'})
# lets search for github respostories with popular python

response = requests.get('https://api.github.com/search/repositories', params={'q': 'language:python', 'sort': 'stars'})
json_response = response.json()
print(json_response["items"][0])#first item