from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/vars")
async def read_root():
    environment_vars = os.environ
    return environment_vars