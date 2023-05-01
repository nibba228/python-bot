import asyncio

from aiogram import Dispatcher
from aiogram.utils.executor import start_polling

from volute_handlers import register_volute_handlers
from weather_handlers import register_weather_handlers
from load import dp

async def on_startup(dp: Dispatcher):
    register_weather_handlers(dp)
    register_volute_handlers(dp)

if __name__ == '__main__':
    asyncio.run(start_polling(dp, on_startup=on_startup))
