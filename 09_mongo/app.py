#David Xiedeng
#SoftDev1 pd 1
#K09 -- Yummy Mongo Py
#2020-02-28 

from pymongo import MongoClient
import json

def convertJSONtoMongoDB(filename):
    f = open(filename, "r")
    data = json.load(f)
    for el in data:
        print (el)

convertJSONtoMongoDB("primer-dataset.json")