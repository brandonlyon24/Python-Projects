

import sqlite3

rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))

with sqlite3.connect('Roster1_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", rosterValues)



##with sqlite3.connect('Roster_database.db') as connection:
##    connection=(':memory')
##    c.executescript("""DROP TABLE IF EXISTS Roster;
##                    CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT);
##                    INSERT INTO Roster VALUES('Jean-Baptiste Zorg', 'Human', 122);
##                    """)
##    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", rosterValues)



c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", rosterValues)
