from fastapi import FastAPI
import enum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/users/{user_name}")
def get_user_name(user_name: str):
    return {"user_name": user_name}

@app.get("/diff_user/{user_name:path}")
async def get_user_name(user_name: str):
    return {"user_name": user_name}