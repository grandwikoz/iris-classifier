from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"MLProcess": "ez pz"}

# @app.get('/greetings')

@app.post('/post-greetings')
async def post_greetings(request: Request):
    # load data request
    data = await request.json()
    
    return data