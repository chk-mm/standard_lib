import requests
from pprint import pprint
import datetime
from collections import Counter


url = 'https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&daily=temperature_2m_max&forecast_days=14'
response = requests.get(url)
date_predict = datetime.datetime.now()  + datetime.timedelta(days=7)
print(date_predict)
values_of_prediction =  response.json()
print(values_of_prediction['daily']['temperature_2m_max'])
max_weather = 0

for x in values_of_prediction['daily']['temperature_2m_max']:
    if x > max_weather :
        max_weather = x

indexofday = values_of_prediction['daily']['temperature_2m_max'].index(max_weather)
# test = values_of_prediction['daily']['time'][indexofday]
print(max_weather,values_of_prediction['daily']['time'][indexofday])
# datetime.fromisoformat(test)
# pprint(response.json())
