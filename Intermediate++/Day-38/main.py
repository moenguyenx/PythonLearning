import requests
from datetime import datetime

today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")
MY_HEIGHT = 174
MY_WEIGHT = 69
MY_AGE = 20
MY_GENDER = "male"

NUTRITION_appID = "919bd472"
NUTRITION_KEY = "ca1963d7721462c28820534ae2bc22d5"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/385b85eb1987506a98a6bd19e8fbf6c9/myWorkouts/sheet1"

nutrition_headers = {
    "x-app-id": NUTRITION_appID,
    "x-app-key": NUTRITION_KEY,
    "x-remote-user-id": "0",
}
sheety_header = {
    "Authorization": "Bearer hellomotherfucker"
}

nutrition_body = {
    "query": input("What exercise did you do today?\n"),
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE
}
nutrition_response = requests.post(url=exercise_endpoint, headers=nutrition_headers, json=nutrition_body)
result = nutrition_response.json()

for exercise in result["exercises"]:
    sheet_input = {
        "sheet1": {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, headers=sheety_header, json=sheet_input)
    print(sheety_response.text)
