from config import *
import requests as rq
from datetime import datetime as dt
USERNAME = "ejarao"

def validate_date_format(date_str):
    try:
        # Try to parse the input date in the format yyyyMMdd
        dt.strptime(date_str, "%Y%m%d")
        return True
    except ValueError:
        # Return False if it cannot be parsed
        return False


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

user_response = input("Write 'y' to post a pixel to your endpoint, 't' to edit, 'd' to delete: ")

pixel_params = {
    "date": "20240922", #dt.now().strftime("%Y%m%d")
    "quantity": "10.3",
}

if user_response == "y":

    post_pixel = rq.post(url=f"{graph_endpoint}/{graph_params['id']}", headers=graph_header, json=pixel_params)
    print(pixel_params["date"])
    print(post_pixel.text)

elif user_response == "t" or user_response == "d":
    while True:
        pixel_date = str(input("Please input a date to edit (format is yyyyMMdd): "))

        if validate_date_format(pixel_date):
            break
        else:
            print("Incorrect date format. Please try again (format: yyyyMMdd).")

    if user_response == "t":
        pixel_edit = input("Please input the new quantity: ")

        pixel_params["quantity"] = str(pixel_edit)  # Update the quantity in pixel_params
        post_pixel = rq.put(url=f"{graph_endpoint}/{graph_params['id']}/{pixel_date}", headers=graph_header, json=pixel_params) 
        post_pixel.raise_for_status()
    elif user_response == "d":
        post_pixel = rq.delete(url=f"{graph_endpoint}/{graph_params['id']}/{pixel_date}", headers=graph_header)
        
        # Check if the deletion was successful
        if post_pixel.status_code == 200:
            print(f"Pixel data for {pixel_date} successfully deleted.")
        else:
            print(f"Failed to delete pixel for {pixel_date}.")
            print("Response:", post_pixel.text)  # Provide more information in case of failure
        
    print("Date and quantity successfully updated.")
else:
    print("Incorrect input detected")