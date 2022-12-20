#Нужно вывести температуру, влажность воздуха, скорость
# ветра, атмосферное давление, состояние
import re
import urllib.request
from datetime import datetime
city = input()
site = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f').read().decode()
pattern_temp = r'(?:temp\":)([-.\d]+)(?:,)'
pattern_humidity = r'(?:humidity\":)([-.\d]+)(?:,)'
pattern_wind_speed = r'(?:speed\":)([-.\d]+)(?:,)'
pattern_pressure = r'(?:pressure\":)([-.\d]+)(?:,)'
pattern_condition = r'(?:description\":\")([^\"]+)'

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
with open('logs.txt', mode='a+', encoding = 'utf-8') as logs:
    logs.write(f'[{current_time} Запрос погоды в городе: {city}\n')
    logs.write(f'Температура: {re.findall(pattern_temp,site)[0]}, {re.findall(pattern_condition,site)[0]}\n')
    logs.write(f'Влажность воздуха: {re.findall(pattern_humidity, site)[0]}%\n')
    logs.write(f'Скорость ветра: {re.findall(pattern_wind_speed, site)[0]} м/с\n')
    logs.write(f'Атмосферное давление: {re.findall(pattern_pressure, site)[0]} мм рт. ст.\n\n\n')

print(f'[{current_time}] Запрос погоды в городе: {city}')
print(f'Температура: {re.findall(pattern_temp,site)[0]}, {re.findall(pattern_condition, site)[0]}')
print(f'Влажность воздуха: {re.findall(pattern_humidity, site)[0]}%')
print(f'Скорость ветра: {re.findall(pattern_wind_speed, site)[0]} м/с')
print(f'Атмосферное давление: {re.findall(pattern_pressure, site)[0]} мм рт. ст.')







