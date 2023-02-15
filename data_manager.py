import requests
from pprint import pprint
sheety_endpoint="https://api.sheety.co/c17c927a9220b5060a269000ebd594fb/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
   
    def __init__(self):
        self.destination_data={}
        # self.destination_data=self.get_destination_data()
        
    def get_destination_data(self):
        response=requests.get(url=sheety_endpoint)
        data=response.json()
        self.destination_data=data["prices"]
        # pprint(self.destination_data)

        return self.destination_data
        # self.destination_data=data["prices"]
        
        
        #return self.destination_data
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data={
                "price":{
                    "iataCode":city["iataCode"]

                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
            )
            # print(response.text)
    def get_customer_emails(self):
        customers_endpoint="https://api.sheety.co/c17c927a9220b5060a269000ebd594fb/flightDeals/users"
        response=requests.get(url=customers_endpoint)
        data=response.json()
        self.customer_data=data["users"]
        return self.customer_data
            


