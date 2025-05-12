import requests
response = requests.get("https://api.github.com/")

# response abject is evaluated to true code < 400

if response:
    print("Succes")
else:
    raise Exception(f"Not a success status code : {response.status_code}")
