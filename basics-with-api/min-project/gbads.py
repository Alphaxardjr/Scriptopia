import requests
url = "https://gbadske.org/api/GBADsLivestockPopulation/faostat?year=2017&country=Canada&species=*&format=file"
response = requests.get(url)
print(response.content)