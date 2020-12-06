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

fileList_tuple = ('information.dox','Hello.txt','myImage.png', \
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



for x in fileList_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_string (col_string) VALUES (?)",(x,))
        conn.close()








