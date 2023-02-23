from fastapi import APIRouter
from typing import List
from models import WeatherResponse
from clients.db_client import save_favorite_city
from clients.weather_client import fetch_weather, fetch_weather_for_favorites

router = APIRouter()

@router.get("/getWeather")
def get_weather(self, city_name: str, date: str) -> WeatherResponse:
    # TODO: default to today if no date passed
    return WeatherResponse(city_name=city_name, weather_info=fetch_weather(city_name, date))

@router.get("/getFavoriteWeather")
def get_weather_for_favorites(self, user_id: int, date: str) -> List[WeatherResponse]:
    return fetch_weather_for_favorites(user_id, date)

@router.put("/addFavorite")
def add_favorite(self, city_name: str, user_id: int) -> str:
    save_favorite_city(city_name=city_name, user_id=user_id)
