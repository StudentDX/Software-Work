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

#d# create table and remove table if exists
#d# takes in a filename and the keys
def buildTable(name, kc):
  #x# print (filename[5:-3])
  #x# print(kc[0], kc[1], kc[2]) 
  comm("CREATE TABLE if not exists {}({} TEXT, {} INTEGER, {} INTEGER)".format(name, ''+kc[0],kc[1], kc[2]))
  comm("DELETE FROM {}".format(name))

#d# adds data to table
#d# whole row insertion
def addTo(table, c1, c2, c3):
  comm("INSERT INTO {} VALUES ({},{},{})".format(table,c1,c2,c3))

#==========================================================

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

#d# creates table with columns (name, id, grade) and adds
#d# student info to it
def createStudentInfoTable():
  #c# building table
  col = ["name", "id", "grade"]
  buildTable("stu_avg", col)
  #c# find list of Students
  names = []
  for row in data:
    if (row[0] not in names):
      names.append(row[0])
  #c# adding to table
  for name in names:
    SInfo = findStudentInfo(name)
    addTo("stu_avg", "\"{}\"".format(SInfo[0]), SInfo[1], SInfo[2])
  
#x# print (findStudentGrades("alison"))
#x# print (findStudentAverage("alison"))
#x# print (findStudentInfo("alison"))
createStudentInfoTable()

#==========================================================

db.commit() #save changes
db.close()  #close database