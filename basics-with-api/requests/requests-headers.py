import requests
url = "https://api.github.com/"

response = requests.get(url)
# print(response.headers)

#  the headers is a dictionary like object hence each property can be accessed

print(response.headers["Content-Type"])