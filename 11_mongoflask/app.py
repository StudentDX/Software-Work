#David Xiedeng
#SoftDev1 pd 1
#K11 -- Ay Mon Go Git It From Yer Flask
#2020-03-15

from pymongo import MongoClient
import json
from bson.json_util import loads

def convertJSONtoMongoDB(filename):
    #opens connection
    collname = filename[:-5]
    client = MongoClient()
    db = client.flaskMongo
    collection = db[collname]

    #clears collection
    collection.delete_many({})

    print(filename)
    f = open(filename, "r")
    try:
        f.seek(0)
        data = json.load(f)
    except json.decoder.JSONDecodeError:
        #print (f.readline())
        #print (f.read())
        f.seek(0)
        data = f.readlines()
        print (data)
        data = data[0].split("},{")
        print (data)
        print()
        print(data[1])
        print (len(data))

    '''
    #numberofdocs = 0
    for entry in data:
        addEntryinAddresses(entry,collection)
        #numberofdocs += 1
        #print (numberofdocs)
    print (f"All data added from {collname}!")
    '''

def addEntryinAddresses(entry, collection):
    #converts json entry into proper json format
    info = json.dumps(entry, indent = 2)
    #converts into usable bson format
    bsoninfo = loads(info)
    #print (bsoninfo)
    collection.insert_one(bsoninfo)

convertJSONtoMongoDB("southpark.json")
