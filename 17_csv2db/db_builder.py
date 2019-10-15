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
#x command = "CREATE TABLE data(Test int)"
#x ^^ how to create the table

#c Reading CSV
def readToDatabase(filename):
  #c create table based off file name"
  #x print (filename[5:-3])
  name = (filename[5:-4])
  command = "CREATE TABLE {}(Test int)".format(name)
  print (command)
  c.execute(command)
  #c put info into table
  with open(filename) as file:
    reader = csv.DictReader(file)
    #x print (returnKeys(reader))

#returns the dict of keys    
def returnKeys(reader):
  for row in reader:
    return (row.keys())
    
readToDatabase('data/courses.csv')
command = ""          # test SQL stmt in sqlite3 shell, save as string

command = "INSERT INTO data VALUES (10)"

c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
