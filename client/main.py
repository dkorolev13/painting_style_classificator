from aiogram import Bot, types, Dispatcher
from aiogram.types import ContentType
from aiogram.utils import executor
import requests

bot = Bot(token='5057381153:AAHPgJ3HpqDKkjrBq4CH1Me0dgClypbqYQk')

dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentType.PHOTO)# фото
async def get_message(message: types.Message):
    #chat_id = message.chat.id
    #file_id = message.file_id
    print(message)
    print(message.from_user)
    print(message.photo[0].file_id)

    features = {
        "file_id": message.photo[0].file_id
    }

    resp = requests.post(
        "http:// 172.18.0.1:35800/predict",
        json=features
    )

    text = 'это фото'
    await message.answer(text=text)

executor.start_polling(dp)