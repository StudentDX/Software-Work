#David Xiedeng
#SoftDev pd1
#K 17 -- No Trouble
#2019-10-08

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
#c Start Table
#x command = "CREATE TABLE data(Test int)"
#x ^^ how to create the table


command = ""          # test SQL stmt in sqlite3 shell, save as string

command = "INSERT INTO data VALUES (10)"

c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
