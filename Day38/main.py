import requests
from datetime import datetime
import os

APP_ID = os.environ["f0ba4105"]
API_KEY = os.environ["f1128b890acbd0823425736390ed9b0e"]
today = datetime.now()

nut_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["https://api.sheety.co/3572120969531d095607c3bd34a0d71b/workoutTracking/workouts"]


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
parameters = {
    "query": input("Tell me which exercises you did: ")
}

response = requests.post(url=nut_endpoint, json=parameters, headers=headers)
exercises = response.json()

for exercise in exercises["exercises"]:
    new_row = {
        "workout": {
            "date": today.strftime("%m/%d/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_header = {
        "Authorization": os.environ["Bearer dh;sj'plsqs[S.Q;X,WLENWQ'"]
    }

    new_response = requests.post(url=sheety_endpoint, json=new_row, headers=sheety_header)
    print(new_response.text)
