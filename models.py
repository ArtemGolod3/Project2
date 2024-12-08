class Weather:
    def __init__(self, location, day, day_part, temperature, wind_speed, rain_probability, humidity):
        self.location = location
        self.day = day
        self.day_part = day_part
        self.temp = temperature
        self.speed = wind_speed
        self.rain = rain_probability
        self.humidity = humidity

        self.msg = None
        self.validate()

    def validate(self):
        if self.temp < 0:
            self.msg = 'Температура слишком низкая'
            return
        elif self.temp > 35:
            self.msg = 'Температура слишком высокая'
        if self.speed > 50:
            self.msg = 'Ветер слишком быстрый'
            return
        if self.humidity < 20:
            self.msg = 'Влажность воздуха слишком низкая'
            return
        if self.rain > 70:
            self.msg = 'Скорее всего будет дождь'
            return
        self.msg = 'Всё отлично'
