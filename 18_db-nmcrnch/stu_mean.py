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

#d# input of string name
#d# returns average of student over classes
def findStudentAverage(name):
  grades = findStudentGrades(name)
  gradeSum = 0
  numberOfClasses = 0
  for el in grades:
    gradeSum = gradeSum + el[2]
    numberOfClasses += 1
  return (gradeSum/numberOfClasses)

#d# input string name
#d# returns int, id
def findStudentID(name):
  for row in data:
    if (row[0] == name):
      return row[1]
  
#d# input string name
#d# returns list of student name, id, and average
def findStudentInfo(name):
  info = [name]
  info.append(findStudentID(name))
  info.append(findStudentAverage(name))
  return info    

#x# print (findStudentGrades("alison"))
#x# print (findStudentAverage("alison"))
#x# print (findStudentInfo("alison"))

#==========================================================

db.commit() #save changes
db.close()  #close database