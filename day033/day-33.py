import requests
from datetime import datetime


#my_lat= 15.912900
#my_long = 79.739990

my_lat= 20.593683
my_long = 78.962883
#response = requests.get(url="http://api.open-notify.org/iss-now.json")
#response.raise_for_status()

#data = response.json()
#longitude = data["iss_position"]["longitude"]
#latitude = data["iss_position"]["latitude"]

#iss_position = (longitude, latitude)
#print(iss_position)

parameters = {
  "lat": my_lat, 
  "lng": my_long,
  "formatted": 0,
}

response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
 
time_now = datetime.now()
print(time_now.hour)