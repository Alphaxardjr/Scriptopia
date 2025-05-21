# to include ssl or verify ssl certificate for the target server you need to include varify = true, which is by default
# Example 
import requests
requests.get("https://api.github.com",verify = True)