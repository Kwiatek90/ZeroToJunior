import sqlite3

#connection = sqlite3.connect("test_database.db")
#cursor = connection.cursor()

#query = "SELECT datetime('now', 'localtime')"

#print(cursor.execute(query).fetchone()[0])

#connection.close()

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime')"
    print(cursor.execute(query).fetchone()[0])
    
      


