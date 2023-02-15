#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
# from flight_data import FlightData
from datetime import datetime, timedelta
from notification_manager import NotificationManager

datamanager=DataManager()
sheet_data=datamanager.get_destination_data()
flight_search=FlightSearch()
notification_manager=NotificationManager()
ORIGIN_CITY_IATA = "LON"
# print(sheet_data)
if sheet_data[0]["iataCode"]=="":
    
    # flight_search=FlightSearch()
    for row in sheet_data:
        row["iataCode"]=flight_search.get_destination_code(row['city'])
        # flight_data.flightdata((row["iataCode"]))
    # print(f"sheet_data:\n{sheet_data}")
    datamanager.destination_data=sheet_data
    datamanager.update_destination_codes()
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight=flight_search.check_flights(ORIGIN_CITY_IATA,destination["iataCode"],from_time=tomorrow,to_time=six_month_from_today)
    if flight is None:
        continue
    if flight.price<destination["lowestPrice"]:
        users=datamanager.get_customer_emails()
        emails=[row["email"] for row in users]
        names=[row["firstname"] for row in users]
        message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
        if flight.stop_overs>0:
            message+=f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        link=f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(emails,message,link)