import os
import json
from asyncio import get_event_loop

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

# Init environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.getenv('BOT_TOKEN')
OWM_TOKEN = os.getenv('OWM_TOKEN')
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM(OWM_TOKEN, config_dict)
PASCAL_TO_MMHG = 0.750062
manager = owm.weather_manager()

with open('char_id.json') as f:
    char_to_id = json.load(f)

with open('name_id.json') as file:
    name_to_id = json.load(file)

loop = get_event_loop()
bot = Bot(TOKEN, loop=loop)
dp = Dispatcher(bot)
