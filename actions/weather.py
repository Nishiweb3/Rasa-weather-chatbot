import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
end_point = 'http://api.openweathermap.org/data/2.5/weather'
def get_weather(city):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'

    }
    response = requests.get(end_point, params=params)
    json_response = json.loads(response.content)
    main = json_response['weather'][0]['main']
    temp = json_response['main']['temp']
    feels_like = json_response['main']['feels_like']
    return main, temp, feels_like

