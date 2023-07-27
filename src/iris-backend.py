# import library
from fastapi import FastAPI
from fastapi import Request
import pickle
import uvicorn

# init app
app = FastAPI()

# check status [GET]


# load model function 


# check model with api [GET]


# predict with api [POST]
@app.post("/predict")
async def predict(request: Request):
    # get data from request

    
    # load model & label
    model = load_model()
    label = ['setosa', 'versicolor', 'virginica']


    # validation
    

    # predict
    

    # return response

