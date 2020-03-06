#David Xiedeng
#SoftDev1 pd 1
#K09 -- Yummy Mongo Py
#2020-02-28

from pymongo import MongoClient
import json
from bson.json_util import loads

#creating MongoClient
#uses default perameters of local host
client = MongoClient()

#creates Mongo database
#does not create or save at the start
#saves when first document is inserted
db = client.newBInfo

#creates Mongo collection
#does not create or save at the start
#saves when first document is inserted
collection = db.addresses

def convertJSONtoMongoDB(filename):
    f = open(filename, "r")
    data = json.load(f)

    info = json.dumps(data[1], indent = 2)
    print (type(data), type(info))
    #print(json.dumps(info, indent = 2))

    bsoninfo = loads(info)
    print (bsoninfo)
    #collection.insert_one(info)

convertJSONtoMongoDB("primer-dataset.json")
