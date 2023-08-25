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
        "PASS": app_pass,
        "KEY": key
    }