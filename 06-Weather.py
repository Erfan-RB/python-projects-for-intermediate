#Weather
import requests
from pprint import pprint

API_Key = ''
city = input("Enter your city ?")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city
weater_data = requests.get(base_url).json()
pprint(weater_data)
