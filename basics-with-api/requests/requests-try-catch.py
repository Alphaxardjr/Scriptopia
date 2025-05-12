import requests
from requests.exceptions import HTTPError
# from pprint import pprint
# by using requests .raise_for_status() to raise HTTPError

url = "https://api.github.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
except HTTPError as http_error:
    print(f" HTTP error occured : {http_error}")
except Exception as err:
    print(f"Other error occured: {err}")
else:
    print("Success!")
    # getting the content from the payload
    # print(response.content) # for byte
    # print(response.text) # for text/string content
    print(response.json())  # for dict/ json data

