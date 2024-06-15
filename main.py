import requests

response = requests.get("https://www.missav.com")

print(response.content.decode())
