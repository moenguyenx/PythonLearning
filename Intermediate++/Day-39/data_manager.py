import requests
from pprint import pprint

sheety_endpoint = "https://api.sheety.co/385b85eb1987506a98a6bd19e8fbf6c9/flightDeals/sheet1"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.destination_data = data['sheet1']
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data)
            print(response.text)





