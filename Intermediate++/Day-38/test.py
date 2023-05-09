import requests

header = {
    "Authorization": "Bearer hellomotherfucker"
}
response = requests.get(url="https://api.sheety.co/385b85eb1987506a98a6bd19e8fbf6c9/myWorkouts/sheet1", headers=header)
print(response.json())