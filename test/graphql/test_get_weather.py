from datetime import date, time, datetime

from schema import schema

query = """
    query GetWeather($cityName: String!, $date: String!){
        getWeather(cityName: $cityName, date: $date) {
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
    query GetWeather($cityName: String!){
        getWeather(cityName: $cityName, date: null) {
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


def test_get_weather():
    result = schema.execute_sync(
        query,
        variable_values={"cityName": "New York", "date": "2023-02-21"},
    )

    assert result.errors is None
    assert result.data["getWeather"]["cityName"] == "New York"
    assert len(result.data["getWeather"]["weatherInfo"]) == 24


def test_get_weather_london():
    result = schema.execute_sync(
        query,
        variable_values={"cityName": "London", "date": "2023-02-21"},
    )

    assert result.errors is None
    assert result.data["getWeather"]["cityName"] == "London"
    assert len(result.data["getWeather"]["weatherInfo"]) == 24


def test_get_weather_not_found():
    result = schema.execute_sync(
        query,
        variable_values={"cityName": "afkjcnpa", "date": "2023-02-21"},
    )

    assert result.errors is not None


def test_get_weather_no_date():
    result = schema.execute_sync(
        query_no_date,
        variable_values={"cityName": "London"},
    )

    assert result.errors is None
    assert result.data["getWeather"]["cityName"] == "London"
    assert result.data["getWeather"]["weatherInfo"][0]["datetime"] == datetime.combine(date.today(), time()).isoformat()
    assert len(result.data["getWeather"]["weatherInfo"]) == 24
