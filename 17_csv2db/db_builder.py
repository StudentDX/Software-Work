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
#x# command = "CREATE TABLE data(Test int)"
#x# ^^ how to create the table

#c# Reading CSV
def readToDatabase(filename):
  with open(filename) as file:
    reader = csv.DictReader(file)
    keychain = returnKeys(reader);
    name = (filename[5:-4])
    #c# create table based off file name"
    buildTable(name, keychain)
    #x# print (returnKeys(reader))
    #c# put info into table
    for row in reader:
      #x# print(keychain[0], row[keychain[0]], keychain[1], row[keychain[1]], keychain[2], row[keychain[2]])
      addTo(name, keychain[1], row[keychain[0]])
      
#c# calls c.execute(command)
def comm(command):
  c.execute(command)

#c# create table and remove table if exists
#c# takes in a filename and the keys
def buildTable(name, kc):
  #x# print (filename[5:-3])
  comm("DROP TABLE if exists {}".format(name))
  comm("CREATE TABLE {}({} TEXT, {} INTEGER, {} INTEGER)".format(name, kc[0],kc[1], kc[2]))

#c# returns the dict of keys    
def returnKeys(reader):
  for row in reader:
    return list((row.keys()))
    
#c# adds value to key
def addTo(table, tag ,data):
  comm("INSERT INTO {}({}) VALUES {}".format(table, tag ,data))
    
readToDatabase('data/courses.csv')

command = ""          # test SQL stmt in sqlite3 shell, save as string

#x# command = "INSERT INTO data VALUES (10)"

c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
