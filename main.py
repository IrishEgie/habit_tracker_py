from config import *
import requests as rq

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

graph_params = {
    "id": "graph1",
    "name": "cycling",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

response = rq.post(url=graph_endpoint, json=graph_params)