import requests

response = requests.get("https://www.bing.cn")

print(response.content.decode())
