import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
url = "https://meteostat.p.rapidapi.com/point/monthly"

querystring = {"lat":"52.5244","lon":"13.4105","alt":"43","start":"2020-01-01","end":"2020-12-31"}
headers = {
	"x-rapidapi-key": api_key,
	"x-rapidapi-host": "meteostat.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())