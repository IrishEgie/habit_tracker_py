from config import *
import requests as rq
from datetime import datetime as dt
USERNAME = "ejarao"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":pixela_token,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes",

}
# response = rq.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_header = {"X-USER-TOKEN": pixela_token}
graph_params = {
    "id": "graph1",
    "name": "cycling",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

# response = rq.post(url=graph_endpoint, json=graph_params, headers=graph_header)
# print(response.text)

user_response = input("Write 'y' to post a pixel to your endpoint: ")

if user_response == "y":

    pixel_params = {
        "date": dt.now().strftime("%Y%m%d"),
        "quantity": "9.43",
    }
    post_pixel = rq.post(url=f"{graph_endpoint}/{graph_params['id']}", headers=graph_header, json=pixel_params)
    print(pixel_params["date"])
    print(post_pixel.text)
else:
    print("No input detected")