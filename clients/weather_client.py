from typing import List

import requests

from clients.db_client import get_favorites
from models import WeatherInfo, WeatherResponse

api_key = "3862753fcc93422fb6c224445232202"
base_url = "http://api.weatherapi.com/v1/history.json?"


def construct_url(city: str, date: str):
    return base_url + "key=" + api_key + "&q=" + city + "&dt=" + date


def fetch_weather(city_name: str, date: str) -> List[WeatherInfo]:
    url = construct_url(city_name, date)
    response = requests.get(url).json()
    weather_info = []

    for hr in response["forecast"]["forecastday"][0]["hour"]:
        weather_info.append(
            WeatherInfo(
                date,
                hr["time"].split(' ')[1],
                hr["humidity"],
                hr["temp_f"]
            )
        )

    return weather_info


def fetch_weather_for_favorites(user_id: int, date: str) -> List[WeatherResponse]:
    favorite_cities = get_favorites(user_id)

    favorites_weather = []
    for f in favorite_cities:
        favorites_weather.append(
            WeatherResponse(
                city_name=f.city_name,
                weather_info=fetch_weather(f.city_name, date)
            )
        )

    return favorites_weather if favorites_weather is not None else []
