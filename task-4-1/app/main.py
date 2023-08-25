from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    try:
        app_pass = os.environ["PASS"]
    except KeyError:
        app_pass = "APP pass not set"

    try:
        key = os.environ["KEY"]
    except KeyError:
        key = "API Key not set"

    return {
        "DATABASE_URL": app_pass,
        "API_KEY": key
    }