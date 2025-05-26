import requests
BASE_URL = "http://127.0.0.1:5000/"

data = {
    "name":"konde",
    "likes":20,
    "views":34,
    "gender":"male"
}
response = requests.put(BASE_URL+"artists/konde",json= data)
print(response.status_code)
# input()
# response = requests.get(BASE_URL+"artists/konde")
# response = requests.delete(BASE_URL+"artists/kiba")
