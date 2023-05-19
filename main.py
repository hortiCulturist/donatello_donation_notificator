import datetime
import requests
import db
import asyncio
from telegram import Bot

url = 'https://donatello.to/api/v1/donates'
headers = {'X-Token': '89dc8fd1a842300f562554c7fb159e21'}
db.start_db()

telegram_token = '6121333590:AAF6Dhx9GSZneix75kruazW7BuwmckGHiNg'
chat_id = '-1001538701484'


async def send_to_telegram(message):
    bot = Bot(token=telegram_token)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML')


async def main():
    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for item in data['content']:
                amount = item['amount']
                client_name = item['clientName']
                time = item['createdAt']
                text = item['message']
                pubId = item['pubId']
                order_date_time = time.split(" ")
                d_time = order_date_time[1].split(":")
                if db.add_id(pubId):
                    db.add_id(pubId)
                    await send_to_telegram(f'<b>🍩 {client_name}: {amount} грн.</b>\n'
                                           f'Коментар: {text}\n'
                                           f'{d_time[0]}:{d_time[1]}')
        else:
            print('Ошибка при выполнении запроса:', response.status_code)
        print("Data update...")
        await asyncio.sleep(5)


asyncio.run(main())
