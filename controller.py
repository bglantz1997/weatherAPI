from fastapi import APIRouter
from typing import List, Optional

from errors import (
    NotFound,
    raise_conflict_favorite,
    raise_not_found_user,
    Conflict,
    raise_not_found_city,
)
from models import WeatherResponse
from clients.db_client import save_favorite_city
from clients.weather_client import (
    fetch_weather,
    fetch_weather_for_favorites,
    date_or_today,
)

router = APIRouter()


@router.get("/weather")
def get_weather(city_name: str, date: Optional[str] = None) -> WeatherResponse:
    try:
        return WeatherResponse(
            date=date_or_today(date),
            city_name=city_name,
            weather_info=fetch_weather(city_name, date_or_today(date)),
        )
    except NotFound:
        raise_not_found_city(city_name)


@router.get("/weather/favorites")
def get_weather_for_favorites(
    user_id: int, date: Optional[str] = None
) -> List[WeatherResponse]:
    try:
        return fetch_weather_for_favorites(user_id, date_or_today(date))
    except NotFound:
        raise_not_found_user(user_id)


@router.put("/favorites")
def add_favorite(city_name: str, user_id: int):
    try:
        save_favorite_city(city_name=city_name, user_id=user_id)
    except NotFound:
        raise_not_found_user(user_id)
    except Conflict:
        raise_conflict_favorite(city_name, user_id)
