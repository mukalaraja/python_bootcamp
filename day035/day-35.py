import requests

owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "1fbfb986b9abe324c8b89f500a5a0d45"

weather_params = {
  "lat": 20.593683,
  "lon": 78.962883,
  "appid": api_key,
  "exculde": "current,minute,daily"
}
response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
  condition_code = hour_data["weather"][0]["id"]
  if int(condition_code) < 700:
    will_rain = True

if will_rain:
  print("Bring umbrella")
    






#print(weather_data["hourly"][0]["weather"][0]["id"])