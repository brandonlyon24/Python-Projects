#
#
#
#
#
#

##import sqlite3
##connection = sqlite3.connect("c:/Users/lyonb/Desktop/test_database.db")
##
##c = connection.cursor()
##
##c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
##
##c.execute("INSER INTO People VALUES('Ron', 'Obvious', 42)")
##connection.commit
##
##connection =sqlite3.connect(':memory')
##
##c.execute("DROP TABLE IF EXISTS People")
##
##connection.close()
##
##with sqlite3.connect("test_database.db") as connection:
    # Preform any SQL operations using connection here



#======PART 4==============

import sqlite3
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, AGE INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
                    """)


peopleValues = (('Luigi', 'Vercotti', 43), ('Arthor', 'Belling', 28))

c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)

    
