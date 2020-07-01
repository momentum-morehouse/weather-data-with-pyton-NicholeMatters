import requests

url = "https://api.climacell.co/v3/weather/realtime"

response = requests.request("GET", url)

print(response.text)