import sqlite3

connection=sqlite3.connect("this.db")

cursor=connection.cursor()
try:
    query='CREATE TABLE IF NOT EXISTS VBJ("fname" varchar, "mname" varchar,"lname" varchar)'
    print(query+"Executed successfully")
except Exception as e:
    print(e)

cursor.execute(
        'INSERT INTO VBJ ("fname","mname","lname") VALUES ("vadukar","bhargav","jentibhai")')
connection.commit()
    
query="SELECT * FROM VBJ"

cursor.execute(query)
rows=cursor.fetchall()

for row in rows:
    print(row)