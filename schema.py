import strawberry
from typing import List, Optional
from models import WeatherResponse
from clients.db_client import save_favorite_city
from clients.weather_client import fetch_weather, fetch_weather_for_favorites, date_or_today


@strawberry.type
class Query:
    @strawberry.field
    def get_weather(self, city_name: str, date: Optional[str]) -> WeatherResponse:
        return WeatherResponse(date= date_or_today(date),city_name=city_name, weather_info=fetch_weather(city_name, date_or_today(date)))

    @strawberry.field
    def get_weather_for_favorites(self, user_id: int, date: Optional[str]) -> List[WeatherResponse]:
        return fetch_weather_for_favorites(user_id, date_or_today(date))


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_favorite(self, city_name: str, user_id: int) -> str:
        save_favorite_city(city_name=city_name, user_id=user_id)
        return "Success"


schema = strawberry.Schema(query=Query, mutation=Mutation)