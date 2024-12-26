from fastapi import FastAPI, HTTPException, Query
from psycopg import connect
from pydantic import BaseModel
from typing import Annotated

db_name = "postgres"
db_user = "faizrazadec"

class User(BaseModel):
    id: int
    name: str
    email: str

def connectdb():
    conn = connect("dbname=postgres user=faizrazadec")
    return conn

def querydb(query, params):
    conn = connectdb()
    cur = conn.cursor()
    if params is None:
        cur.execute(query)
    else:
        cur.execute(query, params)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

app = FastAPI()

@app.get("/")
async def read_all_table():
    try:
        query = "SELECT * FROM users"
        results = querydb(query, params=None)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/users/")
async def read_filter_table(limit: Annotated[int, Query(ge=1)] = 10, offset: Annotated[int, Query(ge=0)] = 0):
    try:
        query = "SELECT * FROM users LIMIT %s OFFSET %s"
        params = (limit, offset)
        results = querydb(query, params)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/users/{user_id}")
async def read_user_id(user_id: int):
    try:
        query = "SELECT * FROM users WHERE id = %s"
        params = (user_id,)
        results = querydb(query, params)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/users/", status_code=201)
def add_user(user: User):
    try:
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        params = (user.name, user.email)
        results = querydb(query, params)
        return results
        return {
            "status_code": 201,
            "endpoints": "/users/",
            "message": "User added successfully",
            "data": user}
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status_code": str(e),
            "endpoints": "/users/",
            "message": "User added failed",
            "data": user})
    
@app.put("/users/", status_code=200)
def update_user(user: User):
    try:
        conn = connectdb()
        cur = conn.cursor()
        cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (user.name, user.email, user.id))
        cur.close()
        conn.commit()
        conn.close()
        return {
            "status_code": 200,
            "endpoints": "/users/",
            "message": "User updated successfully",
            "data": user}
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status_code": str(e),
            "endpoints": "/users/",
            "message": "User updated failed",
            "data": user})
    
@app.delete("/users/", status_code=204)
def delete_user(user: User):
    try:
        conn = connectdb()
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id = %s", (user.id,))
        cur.close()
        conn.commit()
        conn.close()
        return {
            "status_code": 204,
            "endpoints": "/users/",
            "message": "User updated successfully",
            "data": user}
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status_code": str(e),
            "endpoints": "/users/",
            "message": "User updated failed",
            "data": user})
