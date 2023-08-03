from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo de dados
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Lista de itens (simulando um banco de dados em memória)
items = [
    Item(name='Produto 1', description='Descrição do produto 1', price = 10.00, tax = 0.00),
    Item(name='Produto 2', description='Descrição do produto 2', price = 20.00, tax = 0.00),
    Item(name='Produto 3', description='Descrição do produto 3', price = 30.00, tax = 0.00),
]

@app.get('/item', response_model = Item)
def read_item(item_id: int):
    try:
        item = items[item_id - 1]
        return item
    except IndexError:
        raise HTTPException(status_code = 404, detail='Item not found')