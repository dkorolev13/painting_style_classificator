from fastapi import FastAPI, UploadFile
from fastai.train import load_learner
from fastai.vision import open_image
from torch import topk
#from pydantic import BaseModel

app = FastAPI()
learner = load_learner('./', 'model.pkl')

def print_pred_probs(pred, k):
  topk_pred = topk(pred[2], k)
  for i in range(3):
    print(f'{learner.data.classes[topk_pred.indices[i]]}: {100*topk_pred.values[i]:.2f}%')

@app.get("/")
async def root():
    return {"message": "Hello, my best friend"}

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


# class MyClass(BaseModel):
#     img_id: str
#
# @app.post("/predict")
# async def root2(myclass: MyClass):
#
#    return {"message": myclass.img_id}