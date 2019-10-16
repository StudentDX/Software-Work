#David Xiedeng
#SoftDev1 pd 1
#K18 -- Average
#2019-10-15

import sqlite3

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

#==========================================================

#d# calls c.execute(command)
def comm(command):
  c.execute(command)  

q = 'SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;'
  
comm(q)

#c# method to recieve info from query
data = c.fetchall()

#x# print (data)
#x# print(type(data))

#d# returns list of students (name, id, mark) per class
def findStudentGrades(name):
  storage = []
  for row in data:
    if (row[0] == name):
      storage.append(row)
  return storage    

#x# print (findStudentGrades("alison"))
#==========================================================

db.commit() #save changes
db.close()  #close database