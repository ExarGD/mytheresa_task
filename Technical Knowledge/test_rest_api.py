import requests
import json

url = "https://www.food2fork.com/api/search?key=e676ea4152b2077f7e7bef634e232fff"

response = requests.post(url)
print(response.text)
