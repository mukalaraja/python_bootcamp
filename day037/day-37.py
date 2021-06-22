import requests
from datetime import datetime
USERNAME = "raja"
TOKEN = "123456rpmy789"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "mukala"
user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
  "id": GRAPH_ID,
  "name": "Python Practice",
  "unit": "Mins",
  "type": "int",
  "color": "kuro"
}
headers = {
  "X-USER-TOKEN": TOKEN
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_data = {
  "date": today.strftime("%Y%m%d"),
  "quantity": input("How many mins did you practice python today?")
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
  "quantity": "240"
}
#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)