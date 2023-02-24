import datetime
from datetime import datetime, date, time

from clients.db_client import FavoriteCity
from test.test_utils import client_fixture, mongo_fixture


def test_get_weather_for_favorite(client_fixture, mongo_fixture):
    client_fixture.put("favorites", params={"user_id": "1", "city_name": "New York"})
    assert (
        mongo_fixture.find_one(FavoriteCity, FavoriteCity.user_id == 1).city_name
        == "New York"
    )
    resp = client_fixture.get(
        "weather/favorites", params={"user_id": "1", "date": "2023-02-21"}
    ).json()
    assert resp[0]["city_name"] == "New York"
    assert len(resp[0]["weather_info"]) == 24
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)


def test_get_weather_for_favorite_no_date(client_fixture, mongo_fixture):
    client_fixture.put("favorites", params={"user_id": "1", "city_name": "New York"})
    assert (
        mongo_fixture.find_one(FavoriteCity, FavoriteCity.user_id == 1).city_name
        == "New York"
    )
    resp = client_fixture.get("weather/favorites", params={"user_id": "1"}).json()
    assert resp[0]["city_name"] == "New York"
    assert len(resp[0]["weather_info"]) == 24
    assert (
        resp[0]["weather_info"][0]["datetime"]
        == datetime.combine(date.today(), time()).isoformat()
    )
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)


def test_get_weather_for_user_with_multiple_favorites(client_fixture, mongo_fixture):
    client_fixture.put("favorites", params={"user_id": "1", "city_name": "New York"})
    assert (
        mongo_fixture.find_one(FavoriteCity, FavoriteCity.user_id == 1).city_name
        == "New York"
    )
    client_fixture.put("favorites", params={"user_id": "1", "city_name": "Boston"})
    assert (
        mongo_fixture.find_one(
            FavoriteCity,
            FavoriteCity.user_id == 1 and FavoriteCity.city_name == "Boston",
        ).city_name
        == "Boston"
    )
    resp = client_fixture.get(
        "weather/favorites", params={"user_id": "1", "date": "2023-02-21"}
    ).json()
    assert len(resp) == 2
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)


def test_get_weather_for_user_without_favorite(client_fixture, mongo_fixture):
    resp = client_fixture.get(
        "weather/favorites", params={"user_id": "1", "date": "2023-02-21"}
    ).json()
    assert len(resp) == 0
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)
