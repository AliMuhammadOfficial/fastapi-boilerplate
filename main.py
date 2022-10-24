import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/")
def home():
    return {"message": f"Hello {os.getenv('APP_NAME', 'FastAPI Boilerplate')}"}