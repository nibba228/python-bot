import asyncio

from aiogram import types, Dispatcher
from load import dp, char_to_id, name_to_id, bot
from volute import get_currency_by_id


@dp.message_handler(commands='volute')
async def get_volute_course(message: types.Message):
    vol_code = None
    vol_name = None
    if len(args := message.text.split()) >= 2:
        if len(args[1]) == 3:
            vol_code = args[1]
        else:
            vol_name = ' '.join(args[1:])
    else:
        await message.answer(
        '''Пожалуйста, после /volute введите чаркод валюты (например, usd), \
        или ее полное название (например, /volute датская крона)''')
        return
    
    cur_id = None
    if vol_code:
        cur_id = char_to_id.get(vol_code.lower())
    else:
        cur_id = name_to_id.get(vol_name.lower())

    if not cur_id:
        await message.answer('Неправильный формат ввода')
        return

    msg = get_currency_by_id(cur_id)
    if not msg:
        await message.answer('К сожалению, информация по данной валюте не найдена')
        return
    
    await message.answer(msg, parse_mode='HTML')

def register_volute_handlers(dp: Dispatcher):
    dp.register_message_handler(get_volute_course)
