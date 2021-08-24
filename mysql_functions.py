import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

from mysql.connector import cursor
from console import Console

console = Console()
load_dotenv()
env = os.environ

def connectDB():
    try:
        connection = mysql.connector.connect(
            user=env["USERNAME"],
            password=env["PASSWORD"],
            host=env["SERVER"],
            database=env["DATABASE"]
        )
        cursor = connection.cursor()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            console.error("Access denied into the database.")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            console.error("Database does not exist.")

        else:
            console.error(err)

        return

    return connection, cursor

def execute(query: str, data=None):
    conn, cur = connectDB()

    if data:
        cur.execute(query, data)
        conn.commit()

    else:
        cur.execute(query)
        return cursor

    cur.close()
    conn.close()