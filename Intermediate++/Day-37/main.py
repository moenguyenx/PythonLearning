import requests
from datetime import datetime
USERNAME = "moenguyenx"
TOKEN = "asscracker69wassupdude"
pixela_endpoint = " https://pixe.la/v1/users"
graph_id = "graph1"

today = datetime.now()

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
pixel_params = {
    "date": f"{today.strftime('%Y%m%d')}",
    "quantity": input("How many Km did u run today? "),
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)


# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     "id": "graph1",
#     "name": "Running Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "shibafu"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

