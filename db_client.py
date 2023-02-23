from typing import List

from odmantic import SyncEngine, Model
from odmantic.engine import SyncCursor
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
engine = SyncEngine(client=client, database="example_db")


class FavoriteCity(Model):
    city_name: str
    user_id: int


def save_favorite(city: str, user_id: int):
    engine.save(FavoriteCity(city_name=city, user_id=user_id))


def get_favorites(user_id: int) -> List[FavoriteCity]:
    return list(engine.find(FavoriteCity, FavoriteCity.user_id == user_id))
