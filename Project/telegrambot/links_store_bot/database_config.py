import sqlite3

def config():

    # Connect to the SQLite database (or create a new one if it doesn't exist)
    connection = sqlite3.connect("database.db")

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute an SQL query
    cursor.execute("CREATE TABLE IF NOT EXISTS info (id INTEGER, key TEXT, content TEXT)")

    # Close the connection
    connection.close()