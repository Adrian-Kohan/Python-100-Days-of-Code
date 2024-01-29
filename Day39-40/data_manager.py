import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/3572120969531d095607c3bd34a0d71b/flightDeals/prices"
        self.response = requests.get(url=self.endpoint)
        self.data = self.response.json()