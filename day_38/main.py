import requests
import datetime as dt
import os

API_KEY = "4ea406c1d68ca0934178bef0e92786ab"
APP_ID = "255d9d88"
NUTRI_END = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT = 95
HEIGHT = 167
AGE = 33
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
exercise_text = input("Tell me which exercises you did: ")
params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
today = dt.datetime.today()

response = requests.post(url=NUTRI_END, json=params, headers=headers)
result = response.json()
print(result)
exercise = result["exercises"][0]["user_input"]
print(exercise)
SHEETY_POST_API = "https://api.sheety.co/202c0c6a43671773ef2da9d816fa896e/copyOfMyWorkouts/workouts"

sheety_params = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": result["exercises"][0]["user_input"],
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"]
    }
}
SHEETY_USER = "abcdef"
SHEETY_PASS = "abcdef12345"
shty_headers = {
    "Authorization": f"Basic {os.environ['AUTHORIZATION_KEY']}"
}
#/copyOfMyWorkouts/workouts
#https://api.sheety.co/202c0c6a43671773ef2da9d816fa896e/copyOfMyWorkouts/workouts - get
#https://api.sheety.co/202c0c6a43671773ef2da9d816fa896e/copyOfMyWorkouts/workouts - post
shty_response = requests.post(url=SHEETY_POST_API, json=sheety_params, headers=shty_headers)
print(shty_response)
print(shty_response.text)