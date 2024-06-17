#Control del clima

def get_weather(city):
    api_key = 'tu_api_key_aqui'  # Reemplaza con tu propia clave API de OpenWeatherMap
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    if weather_data['cod'] != 200:
        print("Error al obtener los datos del clima")
        return

    main = weather_data['main']
    weather = weather_data['weather'][0]
    print(f"Clima en {weather_data['name']}, {weather_data['sys']['country']}")
    print(f"Temperatura: {main['temp']}°C")
    print(f"Humedad: {main['humidity']}%")
    print(f"Condiciones: {weather['description'].capitalize()}")

if __name__ == "__main__":
    city = input("Ingresa el nombre de la ciudad: ")
    weather_data = get_weather(city)
    display_weather(weather_data)
