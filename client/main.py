from aiogram import Bot, types, Dispatcher
from aiogram.types import ContentType
from aiogram.utils import executor

import requests

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_message(message: types.Message):
    public_ip = "http://130.162.33.39:5000/"
    file_id = message.photo[-1].file_id
    resp = requests.get(public_ip + file_id)
    await message.answer(text=resp.json())


executor.start_polling(dp)
