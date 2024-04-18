# import sqlite3


# def adder(table, key):
#     connection = sqlite3.connect("database.db")
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO  it(key) VALUES (?)", (key))
#     connection.commit()
#     connection.close()


# def creater(table):
#     connection = sqlite3.connect("tele.db")

#     cursor = connection.cursor()

#     sql = f"CREATE TABLE IF NOT EXISTS {table}(key INT NOT NULL AUTO_INCREMENT , value VARCHAR)"

#     cursor.execute(sql)
#     connection.commit()
#     connection.close()


# def fetch(table):
#     connection = sqlite3.connect("tele.db")
#     cursor = connection.cursor()
#     cursor.execute(f"SELECT * FROM {table}")
#     rows = cursor.fetchall()

#     data = [[row[0]] for row in rows]

#     connection.close()
#     return data


import json

def fetch():


# Attempt to load JSON data from the file
    try:
        with open("data.json", "r") as file:
            return json.load(file)
            # print(data)  # Output loaded JSON data
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
    except FileNotFoundError:
        print("File not found or path incorrect.")
    except Exception as ex:
        print("Error:", ex)
    
def display(level):
    
    data=fetch()
    
    print(data)
    