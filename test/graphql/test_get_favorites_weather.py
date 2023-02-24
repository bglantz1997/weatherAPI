import datetime
from datetime import datetime, date, time

from clients.db_client import FavoriteCity
from schema import schema
from test.test_utils import mongo_fixture
from test_save_favorite import mutation as save_fav_mutation


query = """
    query GetFavoriteWeather($userId: Int!, $date: String!){
        getWeatherForFavorites(userId: $userId, date: $date) {
            cityName
            date
            weatherInfo {
                datetime
                temp
                humidity  
            }
        }  
    }
"""


query_no_date = """
    query GetFavoriteWeather($userId: Int!){
        getWeatherForFavorites(userId: $userId, date: null) {
            cityName
            date
            weatherInfo {
                datetime
                temp
                humidity  
            }
        }  
    }
"""


def add_favorite(city: str = "New York"):
    schema.execute_sync(
        save_fav_mutation,
        variable_values={"userId": 1, "cityName": city}
    )


def test_get_weather_for_favorite(mongo_fixture):
    add_favorite()
    result = schema.execute_sync(
        query,
        variable_values={"userId": 1, "date": "2023-02-21"}
    )

    assert result.errors is None
    assert result.data["getWeatherForFavorites"][0]["cityName"] == "New York"
    assert len(result.data["getWeatherForFavorites"][0]["weatherInfo"]) == 24
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)


def test_get_weather_for_favorite_no_date(mongo_fixture):
    add_favorite()
    result = schema.execute_sync(
        query_no_date,
        variable_values={"userId": 1}
    )

    assert result.errors is None
    assert result.data["getWeatherForFavorites"][0]["cityName"] == "New York"
    assert len(result.data["getWeatherForFavorites"][0]["weatherInfo"]) == 24
    assert result.data["getWeatherForFavorites"][0]["weatherInfo"][0]["datetime"] == datetime.combine(date.today(), time()).isoformat()
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)


def test_get_weather_for_user_with_multiple_favorites(mongo_fixture):
    add_favorite()
    add_favorite("Tampa")
    result = schema.execute_sync(
        query_no_date,
        variable_values={"userId": 1}
    )

    assert result.errors is None
    assert len(result.data["getWeatherForFavorites"]) == 2
    mongo_fixture.remove(FavoriteCity, FavoriteCity.user_id == 1)


def test_get_weather_for_user_without_favorite(mongo_fixture):
    result = schema.execute_sync(
        query_no_date,
        variable_values={"userId": 1}
    )

    assert result.errors is None
    assert len(result.data["getWeatherForFavorites"]) == 0
