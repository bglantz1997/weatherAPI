from clients.db_client import FavoriteCity
from test_utils import client_fixture, mongo_fixture


def test_save_favorite(client_fixture, mongo_fixture):
    client_fixture.put("favorites", params={"user_id": "1", "city_name": "New York"})
    assert mongo_fixture.find_one(FavoriteCity, FavoriteCity.user_id == 1).city_name == "New York"
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)


def test_save_favorite_no_city(client_fixture, mongo_fixture):
    response = client_fixture.put("favorites", params={"user_id": "1"})
    assert response.is_error
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)


def test_cannot_save_favorite_twice(client_fixture, mongo_fixture):
    client_fixture.put("favorites", params={"user_id": "1", "city_name": "New York"})
    assert mongo_fixture.find_one(FavoriteCity, FavoriteCity.user_id == 1).city_name == "New York"
    error_resp = client_fixture.put("favorites", params={"user_id": "1", "city_name": "New York"})
    assert error_resp.is_error
    assert error_resp.json()["detail"] == "New York has already been added as favorite by user 1"
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)
