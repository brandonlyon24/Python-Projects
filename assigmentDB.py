#   Assignment: For this assignment, you will need to write a script that creates a 
#               database and adds new data into that database.
#   Python 3
#   Author:     Brandon Lyon
#
#   Date: 12-5-20
#
import sqlite3
conn = sqlite3.connect('BrandonsNew.db')
#cur = conn.cursor()

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

"""
Your script will need to read from the supplied list of file
names at the bottom of this page and determine only the files
from the list which end with a “.txt” file extension.
Next, your script should add those file names from the list ending
with “.txt” file extension within your database.
Finally, your script should legibly print the qualifying text files to the
console
"""
conn = sqlite3.connect('BrandonsNew.db')

for x in fileList_tuple:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_string (col_string) VALUES (?)",(x,))
            print(x)
conn.close()








