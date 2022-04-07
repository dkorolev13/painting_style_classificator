from fastapi import FastAPI, UploadFile
from fastai.train import load_learner
from fastai.vision import open_image
from torch import topk
from aiogram import Bot
import shutil

app = FastAPI()
learner = load_learner('./', 'model.pkl')
bot = Bot(token='5057381153:AAHPgJ3HpqDKkjrBq4CH1Me0dgClypbqYQk')


def print_pred_probs(pred, k):
    topk_pred = topk(pred[2], k)
    #return f'{learner.data.classes[topk_pred.indices[0]]}: {100 * topk_pred.values[0]:.2f}%' - работает
    res = [f'{learner.data.classes[topk_pred.indices[i]]}: {100 * topk_pred.values[i]:.2f}%' for i in range(3)]

    # res = {}
    # for i in range(3):
    #     res = {f'{learner.data.classes[topk_pred.indices[i]]}': f'{100 * topk_pred.values[i]:.2f}%'}
    #     #print(f'{learner.data.classes[topk_pred.indices[i]]}: {100 * topk_pred.values[i]:.2f}%')
    return res


@app.get("/")
async def root():
    return {"message": "Hello, my 13 best friend"}


@app.get("/{file_id}")
async def get_file_id(file_id: str):
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, 'image_for_prediction.jpg')

    painting = open_image('image_for_prediction.jpg')
    pred = learner.predict(painting)
    #res = print_pred_probs(pred, 3)
    res = print_pred_probs(pred, 3)
    res_str = '\n'.join(res)
    return res_str

# @app.post("/imgs/")
# async def root2(img: UploadFile):
#     #with open('test.jpeg', "wb") as buffer:
#         #shutil.copyfileobj(img.file, buffer)
#
#     painting = open_image(img.file)
#     pred = learner.predict(painting)
#     res=print_pred_probs(pred, 3)
#
#     await {"file_name": res}
