# fetch_weather.py
import requests
#from config.settings import API_KEY, CITIES

API_KEY = '55b474db1644cb12662c3db486ca81e2'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
def fetch_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    #print(data)
    temp = data['main']['temp']
    temp = temp - 273.15         #converting to celsius
    
    feels_like = data['main']['feels_like']
    feels_like = feels_like - 273.15              #to celsius
    return {
        'city': city,
        'main': data['weather'][0]['main'],
        'temp': temp,
        'feels_like': feels_like,
        'dt': data['dt']
    }

def fetch_all_cities_weather():
    weather_data = []
    for city in CITIES:
        weather_data.append(fetch_weather(city))
    return weather_data

