from fastapi import FastAPI
import json

import mysql
from mysql.connector import connect
from dotenv import load_dotenv
import os

app = FastAPI()


MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

# Connect to MySQL
def connect():
    return mysql.connector.connect(
        host = MYSQL_HOST,
        port = MYSQL_PORT,
        username = MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DB
    )

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def test():
    conn = connect()
    cursor=conn.cursor()
    query = "SELECT Host, User FROM user"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return {"table_data": json.dumps(rows)}