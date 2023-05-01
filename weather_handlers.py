import asyncio
from aiogram import types, Dispatcher
import aiogram.utils.markdown as fmt
from load import dp, bot, owm, PASCAL_TO_MMHG
from weather import get_weather


@dp.message_handler(commands='weather')
async def get_weather_by_city(message: types.Message):
    city = message.text.split()
    if not (len(city) > 1):
        await message.answer(
        'Пожалуйста, после /weather введите город или просто скиньте геолокацию')
    else:
        city = city[1]
        msg = get_weather(city=city)
        if msg:
            await message.answer(msg, parse_mode='HTML')
        else:
            await message.answer('К сожалению, информация о погоде в этом месте не найдена')

@dp.message_handler(content_types=['location'])
async def get_weather_by_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    msg = get_weather(lat=lat, lon=lon)
    if msg:
        await message.answer(msg, parse_mode='HTML')
    else:
        await message.answer('К сожалению, информация о погоде в этом месте не найдена')

def register_weather_handlers(dp: Dispatcher):
    dp.register_message_handler(get_weather_by_city)
    dp.register_message_handler(get_weather_by_location)
