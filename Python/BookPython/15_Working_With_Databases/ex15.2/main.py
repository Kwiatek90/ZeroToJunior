#1. Create a new database with a table named Roster that has three
#fields: Name, Species and IQ. The Name and Species columns should
#be text fields, and the IQ column should be an integer field.
#2. Populate your new table with the following values:
#Name Species IQ
#Jean-Baptiste Zorg Human 122
#Korben Dallas Meat Popsicle 100
#Ak’not Mangalore -5
#3. Update the Species of Korben Dallas to be Human.
#4. Display the names and IQs of everyone in the table classified as
#Human.

import sqlite3

roster_values = (
    ("Jean-Baptiste Zorg", "Human", 122),
    ("Korben Dallas Meat", "Popsicle", 100),
    ("Ak’not", "Mangalore", -5))

with sqlite3.connect("ex_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE Roster(
                        Name TEXT,
                        Species TEXT,
                        IQ INT
                        );
                   """)
    cursor.executemany("INSERT INTO Roster VALUES(?,?,?)", roster_values)
    cursor.execute("UPDATE Roster SET Species=? WHERE Name=?;", ("Human", "Korben Dallas Meat"))
    cursor.execute("SELECT Name, IQ FROM Roster WHERE Species=?;", ("Human",))
    
    for row in cursor.fetchall():
        print(row)
    
    
    
    

