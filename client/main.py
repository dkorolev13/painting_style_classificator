from aiogram import Bot, types, Dispatcher
from aiogram.types import ContentType
from aiogram.utils import executor
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

bot = Bot(token='5057381153:AAHPgJ3HpqDKkjrBq4CH1Me0dgClypbqYQk')

dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentType.PHOTO)# фото
async def get_message(message: types.Message):

    # print(message)
    # print(message.from_user)
    # print(message.photo[0].file_id)

    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    resp = session.get('http://127.0.0.1:80/')


    ans = resp.json()
    #text = 'это фото'
    await message.answer(text=ans)

executor.start_polling(dp)