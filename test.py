# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# @app.get("/users")
# def read_users():
#     try:
#         with open("users.csv", "r") as file:
#             users = file.readlines()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Internal Server Error")
#     else:
#         return users
    

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, port=8020, host="127.0.0.1")

import pandas as pd
df = pd.read_csv("users.csv")
user_id = 2
id = 8
user = "as"
df = pd.read_csv("users.csv")
del_user = df.drop(df[(df['id'] == id) & (df['name'] == user)].index, inplace=True)

df.to_csv("users.csv", index=False)
