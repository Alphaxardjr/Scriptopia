import requests
BASE_URL = "http://127.0.0.1:5000/"

data = {
    "name":"konde",
    "likes":20,
    "views":34
}
# response = requests.put(BASE_URL+"artists/konde",json= data)
response = requests.get(BASE_URL+"artists/konde")
print(response.json(),response.status_code)