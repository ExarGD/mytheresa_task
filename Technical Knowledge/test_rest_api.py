import requests
import json

search_request = "tetris+language:assembly"
url = "https://api.github.com/search/repositories?q=" + search_request + "&sort=stars&order=desc"

response = requests.get(url)
assert response.status_code == 200

data = response.text

assert "total_count" in data
assert "incomplete_results" in data
assert "items" in data

print(response.json()["total_count"])
print(len(response.json()["items"]))
# should be equal to total_count if total_count <= 30, or equal to 30 if total_count > 30

with open("response.json", "w") as f:
  f.write(response.text)

