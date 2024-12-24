from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class Users(BaseModel):
    id: int
    name: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Management System"}

@app.get("/users/")
def read_users():
    try:
        df = pd.read_csv("users.csv")
        users = df.to_dict(orient='records')
        return users
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="User file doesn't exist in server")
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=500, detail="user file is empty")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/add_user/")
def add_user(user: Users):
    try:
        df = pd.read_csv("users.csv")
        new_user = pd.DataFrame({"id": [user.id], "name": [user.name]})
        df_updated = pd.concat([df, new_user], ignore_index=True)
        df_updated.to_csv("users.csv", index=False)
        return {"message": "User added successfully", "user": user.dict()}
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="User file doesn't exist in server")
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=500, detail="user file is empty")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete("/delete_user/")
def delete_user(user: Users):
    try:
        df = pd.read_csv("users.csv")
        del_user = df.drop(df[(df['id'] == id) & (df['name'] == user)].index, inplace=True)
        df.to_csv("users.csv", index=False)
        return {"message": "User deleted successfully"}
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="User file doesn't exist in server")
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=500, detail="user file is empty")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.put("/update_user/")
def update_user(user: Users):
    try:
        df = pd.read_csv("users.csv")
        df.loc[df["id"] == user.id, "name"] = user.name
        df.to_csv("users.csv", index=False)
        return {"message": "User updated successfully", "user": user.dict()}
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="User file doesn't exist in server")
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=500, detail="user file is empty")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000, host="127.0.0.1")