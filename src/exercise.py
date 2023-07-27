from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {
        "message": "hi, congrats your api is up!"
    }

# coba post