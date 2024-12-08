from datetime import datetime

import requests

from models import Weather


class APIInterface:
    def __init__(
            self,
            api_key,
            api_url='http://dataservice.accuweather.com/'
    ):
        self.api_url = api_url
        self.api_key = api_key

    def location_key(self, city_name):
        request = requests.get(url=f'{self.api_url}locations/v1/cities/search?apikey={self.api_key}&q={city_name}'
                               f'&details=true&language=en-us')
        response = request.json()
        return response[0]['Key']

    def weather(self, city_name):
        location_key = self.location_key(city_name)
        request = requests.get(url=f'{self.api_url}forecasts/v1/daily/5day/{location_key}?apikey={self.api_key}'
                               f'&details=true&metric=true&language=en-us',)
        response = request.json()
        weather = list()
        for day_part in ['Day', 'Night']:
            for day in response['DailyForecasts']:
                item = Weather(day=datetime.fromisoformat(day['Date']).date(),
                            day_part=day_part,
                            location=city_name,
                            rain_probability=day[day_part]['RainProbability'],
                            humidity=day[day_part]['RelativeHumidity']['Average'],
                            wind_speed=day[day_part]['Wind']['Speed']['Value'],
                            temperature=(day['Temperature']['Minimum']['Value'] +
                                         day['Temperature']['Maximum']['Value']) / 2)
                weather.append(item)
        return weather
