# Making request to api.github.com/user requires access token to be passed in the auth param
# example
import requests
from helperFunctions.custome_token_auth import TokenAuth
# Use a dummy token for demonstration purposes
dummy_token = "ghp_dummyToken1234567890"
url = "https://api.github.com/user"
auth = TokenAuth(dummy_token)
response = requests.get(url, auth=auth)
print(response.status_code)
print(response.json())