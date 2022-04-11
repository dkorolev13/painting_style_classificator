from fastapi import FastAPI

from fastai.train import load_learner
from fastai.vision import open_image
from torch import topk

from aiogram import Bot

from config import BOT_TOKEN


def pred_probs(predictions, k):
    topk_pred = topk(predictions[2], k)
    res = [f'{learner.data.classes[topk_pred.indices[i]]}: {100 * topk_pred.values[i]:.2f}%' for i in range(k)]
    return res

app = FastAPI()
learner = load_learner('./', 'model.pkl')
bot = Bot(token=BOT_TOKEN)

@app.get("/{file_id}")
async def get_file_id(file_id: str):
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, 'image_for_prediction.jpg')

    painting = open_image('image_for_prediction.jpg')
    predictions = learner.predict(painting)
    res = pred_probs(predictions, 3)
    res_str = '\n'.join(res)
    return res_str
