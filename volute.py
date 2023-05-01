from datetime import datetime

import requests
from bs4 import BeautifulSoup
import aiogram.utils.markdown as fmt

def get_currency_by_id(cur_id: str):
    today = datetime.today()

    url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req={}' \
    .format(today.strftime('%d/%m/%Y'))
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    volute = soup.find(id=cur_id)
    if not volute:
        return None

    msg = fmt.text(
            fmt.text(fmt.hbold(volute.find('nominal').text),
                fmt.hitalic(volute.find('name').text)),
            fmt.text('='),
            fmt.text(round(float(volute.find('value').text.replace(',', '.')), 2), 'рублей'),
            sep='\n')
    return msg
