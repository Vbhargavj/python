import sqlite3


def store_user(id,uname,name):
    connection = sqlite3.connect('database.db')

    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS userinfo (id INTEGER PRIMARY KEY, uname TEXT, name TEXT)")
    try:
        print(cursor.execute(
            "INSERT INTO userinfo (id,uname,name) VALUES (?,?, ?)", (id, uname, name)))
        connection.commit()
    except:
        print("bhargav")
    connection.close()
