import json, requests
import pickle
# TODO Insert youre API_KEY from keys.py
from keys import API_KEY
# Создать приложение "Погода"
# Пользователь вводит название города, программа отображает текущую погоду
URL ='https://api.openweathermap.org/data/2.5/weather'
# API_KEY = '71617ce9d345727f4f3eae0111db81a5'
city ="Kiev" 
# input('City: ')
QUERY_CITY = f"?q={city}&appid={API_KEY}"
weather = None
weatherPickle = None 
request = URL + QUERY_CITY.format(city, API_KEY)
response = requests.get(request)
if response.status_code == 200:
    weather = json.loads(response.text)
    weatherPickle = pickle.dumps(weather)

print("В городе", city)
temp1= int(weather['main']['temp'])- 273.15
print("Текущая температура :","%.2f" %temp1, '°C')
# print("Clouds:", weather['wind']['clouds']['all'],'%')
temp_min= weather['main']['temp_min']- 273.15
temp_max= weather['main']['temp_max']- 273.15
print("Температура min:", "%.2f" %temp_min, '°C')
print("Температура max:","%.2f" %temp_max, '°C' )
print("Cкорость ветра:", weather['wind']['speed'],'м/с')
