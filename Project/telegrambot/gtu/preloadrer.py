import sqlite3

def pre():
    connection=sqlite3.connect('tele.db')

    cursor=connection.cursor()

    sql='CREATE TABLE IF NOT EXISTS pre(key INT NOT NULL AUTO_INCREMENT , value VARCHAR)'

    cursor.execute(sql)
    
def adding(value):
    connection = sqlite3.connect("tele.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO pre (value) VALUES (?)", (value))
    connection.commit()
    connection.close()
    


def fetch():
    connection = sqlite3.connect("tele.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pre")
    rows = cursor.fetchall()
    
    data = [[row[0]] for row in rows]
    print(data)
    connection.close()
    return data



def update():
    pass
fetch()