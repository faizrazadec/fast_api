from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=5)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/itemss/")
async def read_items(q: Annotated[str | None, Query(max_length=5)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
        return results

@app.get("/items_/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/hidden_query/")
async def read_items(
    hidden_query: Annotated[
        str | None,
        Query(
            include_in_schema=False,
        ),
    ] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "No query parameter"}