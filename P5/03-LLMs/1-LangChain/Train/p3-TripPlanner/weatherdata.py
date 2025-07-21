import os
import requests
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
load_dotenv()

weather_api_key = os.environ["OPEN_WEATHER_API_KEY"]
def get_location(city_name:str) -> tuple:
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city_name)
    lat, lon = location.latitude, location.longitude
    return lat, lon

def get_weather_information(city_name:str):
    lat, lon = get_location(city_name=city_name)
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric"
    weather_information = requests.get(weather_url).json()
    if "main" in weather_information:
        mainly = weather_information["weather"][0]["main"] + f"({weather_information["weather"][0]["description"]})"
        temprature = str(weather_information["main"]["temp"]) + f"(feels like:{weather_information["main"]["feels_like"]})"
        temp_variance = "from " + str(weather_information["main"]["temp_min"]) + " to " + str(weather_information["main"]["temp_max"])
        humidity = weather_information["main"]["humidity"]
        result = f"The current weather in {city_name} is like [{mainly}] and the temprature is [{temprature}].\nTemprature varies [{temp_variance}] and humidity is [{humidity}]."
        return result
    else:
        result = f"We coudn't find information about weather using this tool. Unavailable."



