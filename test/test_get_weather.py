from datetime import date, time, datetime
from test_utils import client_fixture


def test_get_weather(client_fixture):
    resp = client_fixture.get("weather", params={"city_name": "New York", "date": "2023-02-21"})
    assert resp.json()["city_name"] == "New York"
    assert len(resp.json()["weather_info"]) == 24


def test_get_weather_london(client_fixture):
    resp = client_fixture.get("weather", params={"city_name": "London", "date": "2023-02-21"})
    assert resp.json()["city_name"] == "London"
    assert len(resp.json()["weather_info"]) == 24


def test_get_weather_no_date(client_fixture):
    resp = client_fixture.get("weather", params={"city_name": "London"})
    assert resp.json()["city_name"] == "London"
    assert len(resp.json()["weather_info"]) == 24
    assert resp.json()["weather_info"][0]["datetime"] == datetime.combine(date.today(), time()).isoformat()
