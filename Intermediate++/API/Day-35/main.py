import requests

MY_LON = 105.877075
MY_LAT = 21.040441
API_KEY = "93c760ac78005878ee8f22c605817ee4"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
print(data)