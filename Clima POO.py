#Control del clima POO
class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        return response.json()


class WeatherDisplay:
    @staticmethod
    def display(weather_data):
        if weather_data['cod'] != 200:
            print("Error al obtener los datos del clima")
            return

        main = weather_data['main']
        weather = weather_data['weather'][0]
        print(f"Clima en {weather_data['name']}, {weather_data['sys']['country']}")
        print(f"Temperatura: {main['temp']}°C")
        print(f"Humedad: {main['humidity']}%")
        print(f"Condiciones: {weather['description'].capitalize()}")


class WeatherApp:
    def __init__(self, api_key):
        self.weather_api = WeatherAPI(api_key)
        self.weather_display = WeatherDisplay()

    def run(self):
        city = input("Ingresa el nombre de la ciudad: ")
        weather_data = self.weather_api.get_weather(city)
        self.weather_display.display(weather_data)


if __name__ == "__main__":
    api_key = 'tu_api_key_aqui'  # Reemplaza con tu propia clave API de OpenWeatherMap
    app = WeatherApp(api_key)
    app.run()
