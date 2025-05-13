import requests
url = "https://api.github.com/"

# response = requests.get(url)
# print(response.headers)

# the headers also can be passed as a dictionary
headers = {
    "User-Agent": "my-app",
    "Accept": "application/vnd.github.v3+json"
}
response = requests.get(url, headers=headers)

#  the headers is a dictionary like object hence each property can be accessed

print(response.headers["Content-Type"])