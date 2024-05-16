import requests
from main import WeatherApiBase


class OneMeteo(WeatherApiBase):
    def __init__(self, latitude, longitude, **kwargs):
        self.longitude = longitude
        self.latitude = latitude

    def get_parametr_temperature(self):
        param = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "current_weather": True,
        }
        result = requests.get("https://api.open-meteo.com/v1/forecast", params=param)
        result_json = result.json()
        return result_json["current_weather"]["temperature"]


if __name__ == "__main__":
    open_meteo_obj = OneMeteo(35.69, 50.41)
    temp = open_meteo_obj.get_current_temperature()
    print(temp)
