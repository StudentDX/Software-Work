'''
David Xiedeng
Softdev pd 1
K18 -- Come Up For Air
2020-04-19
'''

from flask import Flask, render_template
import json

app = Flask(__name__)

def readJSON(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data

@app.route("/")
def start():
    data = readJSON("static/meteorites.json")
    #print (data)
    return render_template(
        "index.html",
        info = data)

if __name__ == "__main__":
    app.debug = True
    app.run()
