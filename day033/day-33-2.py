import requests
from datetime import datetime
import smtplib
import time

my_email = "raja.mookala450@gmail.com"
password = "dhakshil@18"

my_lat = 20.593683
my_long = 78.962883
def is_iss_overhead():
  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  response.raise_for_status()
  data = response.json()

  iss_latitude = float(data["iss_position"]["latitude"])
  iss_longitude = float(data["iss_position"]["longitude"])

  #Your position is within +5 or -5 degrees of the ISS position.
  if my_lat-5 <= iss_latitude <= my_long+5 and my_long+5 <= iss_longitude <= my_long+5:
    return True

def is_night():
  parameters = {
      "lat": my_lat,
      "lng": my_long,
      "formatted": 0,
  }

  response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
  response.raise_for_status()
  data = response.json()
  sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

  time_now = datetime.now().hour
  if time_now >= sunset or time_now <= sunrise:
    return True

while True:
  time.sleep(30)
  if is_iss_overhead() and is_night:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, password)
    connection.sendemail(
      from_addrs=my_email,
      to_addrs=my_email,
      msg=f"subject:look it\n\n this iss is above the sky."
    )




