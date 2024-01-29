import requests
from datetime import datetime

# address = https://pixe.la/v1/users/adriankohan/graphs/graphnum1.html
TOKEN = "asvajsda39q92qejla"
USERNAME = "adriankohan"
GRAPH_ID = "graphnum1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Study tracker",
    "unit": "hour",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = datetime.now()

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_params ={
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today?"),
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
update_params = {
    "quantity": "10",
}

# response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)


delete_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
