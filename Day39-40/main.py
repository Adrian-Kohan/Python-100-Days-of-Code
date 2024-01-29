from data_manager import DataManager
from flight_search import FlightSearch
import requests

# data_manager = DataManager()
# sheet_data = data_manager.data["prices"]
# for flight in sheet_data:
#     if flight["iataCode"] == "":
#         flight_search = FlightSearch()
#         params = {
#             "price": {
#                 "iataCode": flight_search.something()
#             }
#         }
#         endpoint = f"https://api.sheety.co/3572120969531d095607c3bd34a0d71b/flightDeals/prices/{flight['id']}"
#         response = requests.put(url=endpoint, json=params)

print("Welcome to Flight Club")
print("We find the best flight deals and email you")
name = input("What is your first name?\n")
last = input("What is your last name?\n")
email = input("Whet is your email?\n")
email_repeat = input("Type your email again.\n")
if email == email_repeat:
    print("You're in the club!")
    params = {
                "user": {
                    "firstName": name,
                    "lastName": last,
                    "email": email
                }
             }
    endpoint = "https://api.sheety.co/3572120969531d095607c3bd34a0d71b/flightDeals/users"
    response = requests.post(url=endpoint, json=params)
