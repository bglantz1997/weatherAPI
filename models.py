import strawberry
from typing import List


@strawberry.type
class WeatherInfo:
    date: str
    time: str
    temp: str
    humidity: str

    def __init__(self, date, time, temp, humidity):
        self.date = date
        self.time = time
        self.temp = temp
        self.humidity = humidity



@strawberry.type
class WeatherResponse:
    city_name: str
    weather_info: List[WeatherInfo]
