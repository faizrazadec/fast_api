from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_users():
    with open("users.csv",  "r") as file:
        users = file.readlines()
    return users

@app.post("/add_user")
def add_user(id: int, user: str):
    with open("users.csv", "a") as file:
        file.write(f"{id},{user}\n")

    with open("users.csv",  "r") as file:
        users = file.read()
    return users

@app.delete("/delete_user")
def delete_user(id:int, user:str):
    id_str = str(id)
    output = id_str + "," + user + "\n"
    with open("users.csv", "r") as file:
        reader = file.readlines()
        print(reader)
        print(type(reader))
        reader.remove(output)
        print(reader)

    with open("users.csv", "w") as file:
        for line in reader:
            file.write(line)
    return 1


@app.put("/update_user")
def update_user(id:int, user:str):
    df = pd.read_csv("users.csv")
    df.loc[df["id"] == 1, "name"] = user
    df.to_csv("users.csv", index=False)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8020, host="127.0.0.1")