import sqlite3

with sqlite3.connect("test_database.db") as connection:
    people = (
        ("Ron", "Obvious", 42),
        ("Luigi", "Vercotti", 43),
        ("Arthur", "Belling", 28)
        )
    
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO People VALUES(?,?,?)", people)
    
