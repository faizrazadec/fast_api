from fastapi import FastAPI, Path, Query
from typing import Annotated 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def get_items(item_id: Annotated[int, Path(alias="hehe", deprecated=True, description="The ID of the item to get")], q: int | None = Query(None, max_length=50, ge=0, le=10)):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results