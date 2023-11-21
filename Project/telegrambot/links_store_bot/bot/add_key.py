import sqlite3


def store_user(id, key, content):
    connection = sqlite3.connect('database2.db')

    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS info (id INTEGER , key TEXT, content TEXT)")
    try:
        cursor.execute(
            "INSERT INTO info (id,key,content) VALUES (?,?, ?)", (id, key, content))
        connection.commit()
    except:
        print("bhargav")
    connection.close()
