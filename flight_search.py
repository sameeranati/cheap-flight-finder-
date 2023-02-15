import requests
from flight_data import FlightData
TEQUILA_ENDPOINT="https://api.tequila.kiwi.com"
TEQUILA_API_KEY="GDiDUdo1LHTSWJwWlQi6yXTneK25AQGs"
# https://api.tequila.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self,city_name):
        params={
            "term":city_name,
            "location_types":"city"
        }
        headers={
            "apikey":TEQUILA_API_KEY
        }
        response=requests.get(url=TEQUILA_ENDPOINT,headers=headers,params=params)
        results=response.json()["locations"]
        
        code=results[0]["code"]
        return code
    def check_flights(self,origin_city_code,destination_city_code,from_time,to_time):
        headers={"apikey":TEQUILA_API_KEY}
        query = {
            "fly_from":origin_city_code,
            "fly_to":destination_city_code,
            "dateFrom":from_time.strftime("%d/%m/%Y"),
            "dateTo":to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"

        }
        response=requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",headers=headers,params=query)
        # print(response.json()["data"][0])
        try:
            data=response.json()["data"][0]
            
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None
        else:
            flight_data=FlightData(price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0])
            # print(f"{flight_data.destination_city}:£{flight_data.price}")  
        return flight_data