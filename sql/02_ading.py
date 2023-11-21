import sqlite3

connection=sqlite3.connect("some.db")
cursor=connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS OSM(NAME VARCHAR,KEY VARCHAR,LINK VARCHAR)")
def ading(name,key,link):
    cursor.execute('INSERT INTO OSM(NAME,KEY,LINK) VALUES (?,?, ?)', (name,key,link))
    
ading("bhargav","ndroid","this is  link")
ading("bhargav","andrd","this is  link1")
ading("bharav","androd","this is  link2")
ading("bhagav","andoid","this is  3link")
ading("bhrgav","android","this is3  link")
ading("bargav","andrid","this is 3 link")
ading("hargav","android","this is  3link")
ading("bharga","adroid","this is  3link")
ading("jeet2","android","thid 123is link")


query='select * from OSM where KEY="android"'

cursor.execute(query)
rows=cursor.fetchall()

for row in rows:
    print(row)

connection.commit()
connection.close()