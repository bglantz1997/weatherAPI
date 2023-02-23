from typing import List

from odmantic import SyncEngine, Model
from pymongo import MongoClient

from errors import Conflict

client = MongoClient("mongodb://localhost:27017/")
engine = SyncEngine(client=client, database="customer_db")


class FavoriteCity(Model):
    city_name: str
    user_id: int


def save_favorite_city(city_name: str, user_id: int):
    if engine.find_one(FavoriteCity, FavoriteCity.user_id == user_id and FavoriteCity.city_name == city_name) is None:
        engine.save(FavoriteCity(city_name=city_name, user_id=user_id))
    else:
        raise Conflict("city has already been added as favorite")


def get_favorites(user_id: int) -> List[FavoriteCity]:
    return list(engine.find(FavoriteCity, FavoriteCity.user_id == user_id))

