import asyncio
from aiogram import types
import aiogram.utils.markdown as fmt
from load import dp, bot, manager, PASCAL_TO_MMHG

def get_weather(lat: int=None, lon: int=None, city: str=None):
    if city:
        response = manager.weather_at_place(city.title())
    else:
        response = manager.weather_at_coords(lat=lat, lon=lon)
    weather = response.weather

    status = weather.detailed_status

    temp_dict = weather.temperature('celsius')
    temp = str(round(temp_dict['temp'])) + ' °C'
    feels_like = str(round(temp_dict['feels_like'])) + ' °C'

    wind = weather.wind()
    speed = round(wind['speed'])

    pressure = weather.barometric_pressure()
    press = round(pressure['press'] * PASCAL_TO_MMHG)

    msg = fmt.text(
            fmt.text(fmt.hunderline(city.title())) if city else \
            fmt.text(fmt.hunderline('Погода по вашим координатам:')),
            fmt.text(fmt.hitalic(status.capitalize())),
            fmt.text(fmt.hbold(temp), 'ощущается как', feels_like),
            fmt.text('Ветер:', fmt.hbold(speed), 'м/с'),
            fmt.text('Давление:', fmt.hbold(press), 'мм. рт. ст.'), sep='\n')
    return msg
