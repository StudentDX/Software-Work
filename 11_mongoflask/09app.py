
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
db = client.newBInfo

#creates Mongo collection
#does not create or save at the start
#saves when first document is inserted
collection = db.addresses
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
    numberofdocs = 0
    for entry in data:
        addEntryinAddresses(entry,collection)
        numberofdocs += 1
        #print (numberofdocs)
    print ("All data added!")

#accepts a part of a json object
def addEntryinAddresses(entry, collection):
    #converts json entry into proper json format
    info = json.dumps(entry, indent = 2)
    #print (info)
    #converts into usable bson format
    bsoninfo = loads(info)
    #print (bsoninfo)
    collection.insert_one(bsoninfo)

# takes string by borough
def searchByBorough(borough):
    search = searchDB({"borough": borough})
    displayQuery(search, 10)

def searchByZIP(zipcode):
    search = searchDB({"address.zipcode": zipcode})
    #print (search)
    displayQuery(search, 10)

def searchByZIPandGrade(zipcode, grade):
    search = searchDB({"$and":[
        {"address.zipcode": zipcode},
        {"grades.grade":
            {"$in":
                [grade]
            }
        }
        ]})
    displayQuery(search, 10)

def searchByZIPwithScoreLT(zipcode, score):
    search = searchDB(
        {"$and":
            [
                {"address.zipcode": zipcode
                },
                {"grades.score":
                    {"$lt": score
                    }
                }
            ]
        }
    )
    print (search)
    print (search.count())
    displayQuery(search,1)


#takes in tuple of order
def searchDB(input):
    collection = MongoClient().newBInfo.addresses
    return (collection.find(input))

#takes in Mongo cursor
def displayQuery(cursor, displayLength):
    x = 0
    for document in cursor:
        print (document)
        x += 1
        if (x >= displayLength):
            break

#==================================================

#convertJSONtoMongoDB("primer-dataset.json")
#searchByBorough("Brooklyn")
#searchByZIP(11214)
#searchByZIP("11214")
#searchByZIPandGrade("10282", "A")
searchByZIPwithScoreLT("11214", 1000)
