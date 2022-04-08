from fastapi import FastAPI, UploadFile
from fastai.train import load_learner
from fastai.vision import open_image
from torch import topk
from aiogram import Bot

#from client.config import BOT_TOKEN
#from client.main import bot
from config import BOT_TOKEN

app = FastAPI()
learner = load_learner('./', 'model.pkl')
bot = Bot(token=BOT_TOKEN)
#bot = Bot(token="5057381153:AAHPgJ3HpqDKkjrBq4CH1Me0dgClypbqYQk")

@app.get("/{file_id}")
async def get_file_id(file_id: str):
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, 'image_for_prediction.jpg')

    painting = open_image('image_for_prediction.jpg')
    pred = learner.predict(painting)
    # res = print_pred_probs(pred, 3)
    res = print_pred_probs(pred, 3)
    res_str = '\n'.join(res)
    return res_str


def print_pred_probs(pred, k):
    topk_pred = topk(pred[2], k)
    # return f'{learner.data.classes[topk_pred.indices[0]]}: {100 * topk_pred.values[0]:.2f}%' - работает
    res = [f'{learner.data.classes[topk_pred.indices[i]]}: {100 * topk_pred.values[i]:.2f}%' for i in range(3)]
    return res
