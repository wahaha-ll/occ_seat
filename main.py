import requests

response = requests.get("https://www.bing.com")

print(response.content.decode())

while True:
  pass
