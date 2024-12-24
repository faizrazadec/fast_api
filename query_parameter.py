from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def root():
    with open('data.json', 'r') as file:
        data = json.load(file)
        return data
    

@app.get("/items/{item_id}")
async def get_items(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/update_items/{item_id}")
async def read_users(item_id: int, q: str | None = None, short: bool = False):
    with open('data.json', 'r') as file:
        data = json.load(file)
    if q:
        data.update({"q": q})
    if not short:
        data.update({"description": "This is the amazing item that has a long description"})
    return data