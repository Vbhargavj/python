import sqlite3 

def display(id):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM info WHERE id={id}")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("no data available")
        
    
    connection.close()
    