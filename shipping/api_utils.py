import requests


def get_weather(city):
    api_key = '42a5aaacceca41fb9ad0b58f8807a650'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"  # Используем градусы Цельсия

    response = requests.get(complete_url)
    data = response.json()

    # Проверяем код ответа от API
    if data.get('cod') != 200:
        return {'error': 'Error fetching weather data'}

    # Проверяем наличие необходимых данных в ответе
    if 'main' in data and 'weather' in data:
        main = data['main']
        weather = data['weather'][0]
        return {
            'city': city,
            'temperature': main['temp'],
            'description': weather['description'],
        }
    else:
        return {'error': 'Invalid data received from the weather API'}
