from clients.db_client import FavoriteCity
from schema import schema
from test.test_utils import mongo_fixture

mutation = """
    mutation AddFavorite($cityName: String!, $userId: Int!) {
        addFavorite(cityName: $cityName, userId: $userId)
    }
"""


def test_save_favorite(mongo_fixture):
    result = schema.execute_sync(
        mutation,
        variable_values={"userId": 1, "cityName": "New York"}
    )

    assert result.errors is None
    assert (
        mongo_fixture.find_one(FavoriteCity, FavoriteCity.user_id == 1).city_name
        == "New York"
    )
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)


def test_save_favorite_no_city(mongo_fixture):
    result = schema.execute_sync(
        mutation,
        variable_values={"userId": 1}
    )

    assert result.errors is not None


def test_cannot_save_favorite_twice(mongo_fixture):
    schema.execute_sync(
        mutation,
        variable_values={"userId": 1, "cityName": "New York"}
    )

    assert (
        mongo_fixture.find_one(FavoriteCity, FavoriteCity.user_id == 1).city_name
        == "New York"
    )
    error_resp = schema.execute_sync(
        mutation,
        variable_values={"userId": 1, "cityName": "New York"}
    )
    assert error_resp.errors is not None
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)
