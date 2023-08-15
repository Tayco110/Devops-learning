from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class SecretValues(BaseModel):
    DATABASE_URL: str
    API_KEY: str

@app.get("/secrets", response_model=SecretValues)
def get_secret_values():
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    return SecretValues(DATABASE_URL=database_url, API_KEY=api_key)