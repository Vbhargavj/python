import sqlite3


def add_record(id, key, content):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO info (id,key,content) VALUES (?,?, ?)", (id, key, content))
    connection.commit()
    connection.close()
