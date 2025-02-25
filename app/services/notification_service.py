from telegram import Bot
import os
from dotenv import load_dotenv

from app.config import get_bot_creds
conf = get_bot_creds()


async def send_telegram_message(message: str):
    token = conf["TOKEN"]
    chat_id = conf["ID"]
    print(token, chat_id)

    if not token or not chat_id:
        raise ValueError("Telegram bot token or chat ID is not set.")

    bot = Bot(token=token)

    await bot.send_message(chat_id=chat_id, text=message)



async def handle_user_registered_event(event: dict):
    if event['eventType'] == 'UserRegistered':


        telegram_message = f"Новый пользователь зарегистрирован: {event['email']}"
        await send_telegram_message(telegram_message)
