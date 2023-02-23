import datetime

from fastapi import APIRouter
from typing import List, Optional
from models import WeatherResponse
from clients.db_client import save_favorite_city
from clients.weather_client import fetch_weather, fetch_weather_for_favorites, date_or_today

router = APIRouter()


@router.get("/weather")
def get_weather(city_name: str, date: Optional[str] = None) -> WeatherResponse:
    return WeatherResponse(city_name=city_name, weather_info=fetch_weather(city_name, date_or_today(date)))


@router.get("/weather/favorites")
def get_weather_for_favorites(user_id: int, date: Optional[str] = None) -> List[WeatherResponse]:
    return fetch_weather_for_favorites(user_id, date_or_today(date))


@router.put("/favorites")
def add_favorite(city_name: str, user_id: int):
    save_favorite_city(city_name=city_name, user_id=user_id)
