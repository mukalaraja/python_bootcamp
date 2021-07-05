import requests
from datetime import datetime

GENDER = male
AGE = 20
HEIGHT_CM = 14
WEIGHT_KG = 54

APP_ID = ee725a73
API_KEY = b9d4862ef0b444183ff65d1ad0688b5e

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://dashboard.sheety.co/projects/60dc28e2bf06b2152a7a9f72/sheets/sheet1"


exercise_text = input("which exercise did you do today?")
headers = { 
  "x-app_id" : APP_ID,
  "x-api_key" : API_KEY,
}
parameters = {
  "query" : exercise_text,
  "gender" : GENDER,
  "age" : AGE,
  "height_cm" : HEIGHT_CM,
  "weight_kg" : WEIGHT_KG,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
  sheet_inputs = {
    "workout" : {
      "date": today_date,
      "time": now_time,
      "exercise": exercise["name"].title(),
      "duration": exercise["duration_min"],
      "calories": exercise["nf_calories"]
    } 
  }
  sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#  print(sheet_response.text)

  sheet_response = requests.post(
    sheet_endpoint, 
    json = sheet_inputs,
    auth = (
      ["username"],
      ["password"],
    )
  )

  bearer_headers = {
  "Authorization": "Bearer YOUR_TOKEN"
  }
  sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
  )
  print(sheet_response.text)