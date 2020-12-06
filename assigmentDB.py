#   Assignment: For this assignment, you will need to write a script that creates a 
#               database and adds new data into that database.
#   Python 3
#   Author:     Brandon Lyon
#
#   Date: 12-5-20
#
import sqlite3
conn = sqlite3.connect('BrandonsNew.db')
cur = conn.cursor()

fileList = ('information.dox','Hello.text','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.hpg')        

"""
Your database will require 2 fields:
an auto-increment primary integer
field and a field with the data type "string"
"""
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_string(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_string TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('BrandonsNew.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_string(col_string) VALUES (?)",('fileList'))
    cur.execute("SELECT * FROM tbl_string WHERE col_string LIKE '_txt'")
    conn.commit()
conn.close


