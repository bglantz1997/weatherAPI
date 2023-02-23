import strawberry
from typing import List


@strawberry.type
class WeatherInfo:
    datetime: str
    temp: str
    humidity: str

    def __init__(self, datetime, temp, humidity):
        self.datetime = datetime
        self.temp = temp
        self.humidity = humidity


@strawberry.type
class WeatherResponse:
    date: str
    city_name: str
    weather_info: List[WeatherInfo]
