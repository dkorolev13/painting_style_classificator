from aiogram import Bot, types, Dispatcher
from aiogram.types import ContentType
from aiogram.utils import executor
import requests
# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry

bot = Bot(token='5057381153:AAHPgJ3HpqDKkjrBq4CH1Me0dgClypbqYQk')

dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentType.PHOTO)# фото
async def get_message(message: types.Message):

    # print(message)
    # print(message.from_user)
    # print(message.photo[0].file_id)

    resp = requests.get("http://127.0.0.1/"+str(message.photo[0].file_id) + "/")

    await message.answer(text=resp.json())

executor.start_polling(dp)