import requests
from pprint import pprint
import datetime
from datetime import datetime as dt
from collections import Counter


url = 'https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&daily=temperature_2m_max&forecast_days=14'
response = requests.get(url)
date_predict = dt.now()  + datetime.timedelta(days=7)
values_of_prediction =  response.json()
max_weather = 0

for x in values_of_prediction['daily']['temperature_2m_max']:
    if x > max_weather :
        max_weather = x

indexofday = values_of_prediction['daily']['temperature_2m_max'].index(max_weather)
test = values_of_prediction['daily']['time'][indexofday]
txt_to_datetime = test.split('-')
date_format = dt(int(txt_to_datetime[0]),int(txt_to_datetime[1]),int(txt_to_datetime[2]))
as_iso = date_format.isoformat()

hottest_date = dt.fromisoformat(as_iso)
print(hottest_date," is the hottest date which temp is:",max_weather)