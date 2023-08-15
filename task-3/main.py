from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

items = [
    Item(name='Produto 1', description='Descrição do produto 1', price = 10.00, tax = 0.00),
    Item(name='Produto 2', description='Descrição do produto 2', price = 20.00, tax = 0.00),
    Item(name='Produto 3', description='Descrição do produto 3', price = 30.00, tax = 0.00),
]

@app.get('/item', response_model = Item)
def read_item(item_id: int):
    try:
        item = items[item_id - 1]

        # Acessar variáveis de ambiente
        database_url = os.getenv('DATABASE_URL')
        api_key = os.getenv('API_KEY')

        return {"item": item, "database_url": database_url, "api_key": api_key}
    except IndexError:
        raise HTTPException(status_code = 404, detail='Item not found')