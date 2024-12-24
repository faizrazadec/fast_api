from fastapi import FastAPI, HTTPException, Query, Path
from typing import Annotated
import pandas as pd

app = FastAPI()

@app.get("/")
def read_users():
    try:
        with open("users.csv",  "r") as file:
            users = file.readlines()
    except Exception as e:
        raise HTTPException(status_code=500, detail = "Internal Server Error")
    else:
        return users
    
@app.get("/users/{id}")
def read_users(id: int):
    try:
        df = pd.read_csv("users.csv")
        userr = df.loc[id-1, 'name']
    except Exception as e:
        raise HTTPException(status_code=500, detail = "Internal Server Error")
    else:
        return {"id": id, "name": userr}

@app.post("/add_user")
def add_user(
    id: Annotated[int, Query(deprecated=True, alias="user-id", title="User id required here", description="This require the user id which is associate with you just")],
    user: Annotated[str, Query(description= "this require the user name that is registered in the system", alias="user-name", title="User name required here")]
):
    try:
        df = pd.read_csv("users.csv")

        new_user = pd.DataFrame({"id": [id], "name": [user]})
        df_updated = pd.concat([df, new_user], ignore_index=True)
        df_updated.to_csv("users.csv", index=False)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="User file doesn't exist in server")
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=500, detail="user file is empty")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return {"message": "User added successfully", "user": {"id": id, "name": user}}

@app.delete("/delete_user")
def delete_user(
    id: Annotated[int, Query(deprecated=True, alias="user-id", title="User id required here", description="This require the user id which is associate with you just")],
    user: Annotated[str, Query(description= "this require the user name that is registered in the system", alias="user-name", title="User name required here")]
):
    try:
        df = pd.read_csv("users.csv")
        del_user = df.drop(df[(df['id'] == id) & (df['name'] == user)].index, inplace=True)
        df.to_csv("users.csv", index=False)

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="User file doesn't exist in server")
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=500, detail="user file is empty")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    return {"message": "User deleted successfully", "user": {"id": id, "name": user}}


@app.put("/update_user")
def update_user(
    id: Annotated[int, Query(deprecated=True, alias="user-id", title="User id required here", description="This require the user id which is associate with you just")],
    user: Annotated[str, Query(description= "this require the user name that is registered in the system", alias="user-name", title="User name required here")]
):
    try:
        df = pd.read_csv("users.csv")
        df.loc[df["id"] == id, "name"] = user
        df.to_csv("users.csv", index=False)

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="User file doesn't exist in server")
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=500, detail="user file is empty")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    return {"message": "User updated successfully", "user": {"id": id, "name": user}}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, port=8000, host="127.0.0.1")