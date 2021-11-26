import sqlite3
from sqlite3 import Error
from console import Console

console = Console(True)

def create_connection(db_file):
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect("./Data/"+db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn

def create_suggestion(message_id: int, author_id: int, suggestion: str):
    """Create a new suggestion in the database."""
    conn = create_connection("suggestions.db")
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO suggestions (id, author, text) VALUES (?, ?, ?)", (message_id, author_id, suggestion))
        conn.commit()

def get_author(message_id: int):
    """Get the author of a suggestion."""
    conn = create_connection("suggestions.db")
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT author FROM suggestions WHERE id=?", (message_id,))
        try:
            results = cur.fetchall()[0]
            (a,) = results
            return a
        except IndexError:
            return None

def delete_suggestion(message_id: int):
    """Updates the db to set the status of the suggestion to deleted."""
    conn = create_connection("suggestions.db")
    with conn:
        cur = conn.cursor()
        cur.execute("UPDATE suggestions SET deleted=? WHERE id=?", (True, message_id))
        conn.commit()