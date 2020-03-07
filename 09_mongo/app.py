#David Xiedeng
#SoftDev1 pd 1
#K09 -- Yummy Mongo Py
#2020-02-28

from pymongo import MongoClient
import json
from bson.json_util import loads

'''
#creating MongoClient
#uses default perameters of local host
client = MongoClient()
#creates Mongo database
#does not create or save at the start
#saves when first document is inserted
#db = client.newBInfo

#creates Mongo collection
#does not create or save at the start
#saves when first document is inserted
#collection = db.addresses
'''
def convertJSONtoMongoDB(filename):
    #opens connection
    client = MongoClient()
    db = client.newBInfo
    collection = db.addresses

    #clears collection
    collection.delete_many({})

    f = open(filename, "r")
    data = json.load(f)
    for entry in data:
        addEntryinAddresses(entry,collection)
    '''
    x = 0
    while x < 10:
        addEntryinAddresses(data[x],collection)
        x+=1
    '''




#accepts a part of
def addEntryinAddresses(entry, collection):
    #converts json entry into proper json format
    info = json.dumps(entry, indent = 2)
    #print (type(data), type(info))

    #converts into usable bson format
    bsoninfo = loads(info)
    #print (bsoninfo)
    collection.insert_one(bsoninfo)

convertJSONtoMongoDB("primer-dataset.json")
