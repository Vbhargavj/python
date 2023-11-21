import sqlite3


def display():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM userinfo")
    rows = cursor.fetchall()
    connection.close()

    result = ''
    print(rows)
    if rows:
        for row in rows:
            result += ', '.join(str(item) for item in row) + '\n'
            
        
    else:
        result= "No data available"
    return result


def display_info(id):
    connection = sqlite3.connect("database2.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT key FROM info")
    rows = cursor.fetchall()
    connection.close()

    result = ''
    print(rows)
    if rows:
        for row in rows:
            result += ', '.join(str(item) for item in row) + '\n'

    else:
        result = "No data available"
    return result
