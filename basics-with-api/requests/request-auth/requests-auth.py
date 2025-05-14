#  to send authenticated requests to a web server one needs to provide credentials
# # to the server. The requests library provides a simple way to do this using the auth parameter.
#example format would be as follows:
import requests
from requests.auth import HTTPBasicAuth
# url = 'https://api.github.com/user'
# response = requests.get(url, auth=HTTPBasicAuth('username', 'password'))  

response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=HTTPBasicAuth('user', 'pass'))
print(response.status_code)
print(response.request.headers["Authorization"]) #Basic dXNlcjpwYXNz

# Note other form of authintication includes:
    # 1. HTTPDigestAuth
    # 2. HTTPProxyAuth

# What happens when you dont pass aut to real world apis?

# response = requests.get("https://api.github.com/user")
# print(response.status_code) # this return 401 error(unauthorized)