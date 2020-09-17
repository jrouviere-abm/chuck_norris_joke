import requests
import json

url = "https://api.chucknorris.io/jokes/random"

payload = {}
headers = {
  'Cookie': '__cfduid=d24fdb543080a721250d3b536b6c13c6a1600373166'
}

response = requests.request("GET", url, headers=headers, data = payload)

#print(response.text.encode('utf8'))

joke = response.json()
joke_text = joke['value']
print(joke_text)