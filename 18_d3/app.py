'''
David Xiedeng
Softdev pd 1
K18 -- Come Up For Air
2020-04-19
'''

import json

def readJSON(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        for el in data:
            print el

readJSON("meteorites.json")
