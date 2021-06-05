import requests
import math


def get_weather():
	"""Takes user imput and request from API"""
	json_weather_format=json_data['weather'][0]['main']
	print(f"Today in {json_location.title()}, the weather will be {json_weather_format.upper()}.")

def get_temp():
	"""Takes user inuput and request temperature data."""
	json_temp=json_data['main']['temp']
	json_temp_format=math.floor((json_temp*1.8)-459.67)

	json_tempMin=json_data['main']['temp_min']
	json_tempMin_format=math.floor((json_tempMin*1.8)-459.67)

	json_tempMax=json_data['main']['temp_max']
	json_tempMax_format=math.floor((json_tempMax*1.8)-459.67)

	print(f"\tTEMPERATURE will be {json_temp_format}F.")
	print(f"\tHIGHS will be {json_tempMax_format}F.")
	print(f"\tLOWS will be {json_tempMin_format}F.")

while True:
	api_address='https://api.openweathermap.org/data/2.5/weather?appid=9bf5d7ebc2139eee959c5cb46a4b8b9f&q='

	location=input('Enter "q" to quit.\nEnter city name or zipcode: ')

	if location=='q' or location=='Q':
		break
	
	else:
		weather_data=api_address + location
		json_data=requests.get(weather_data).json()
		json_location=json_data['name']
		
		get_weather()
		get_temp()
