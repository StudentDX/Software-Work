'''
David Xiedeng
Softdev pd 1
K18 -- Come Up For Air
2020-04-19
'''

from flask import Flask, render_template, redirect
import json

app = Flask(__name__)

def readJSON(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data

@app.route("/")
def start():
    print (type(readJSON("meteorites.json")))
    return redirect("/static/index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
