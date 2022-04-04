from aiogram import Bot, types, Dispatcher
from aiogram.types import ContentType
from aiogram.utils import executor
import requests
from config import BOT_TOKEN



bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentType.PHOTO)  # фото
async def get_message(message: types.Message):
    # print(message)
    # print(message.from_user)
    # print(message.photo[0].file_id)

    resp = requests.get("http://127.0.0.1/" + message.photo[-1].file_id)

    await message.answer(text=resp.json())


executor.start_polling(dp)
