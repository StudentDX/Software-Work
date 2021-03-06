# From Eric "Morty" Lau
# David Xiedeng
# SoftDev1 pd1
# K24 -- A RESTful Journey Skyward
# 2019-11-12

from flask import Flask, request, render_template
import urllib
import json 

app = Flask(__name__)

@app.route("/")
def root():
    request = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=anvhiZGKBhZdJmFMCGBAmH7lDGCGkR9fl56lkAoV")
    response = request.read()
    data = json.loads(response)
    return render_template(
        "index.html",
        explanation = data['explanation'],
        pic = data['url']
    )

if __name__ == "__main__":
    app.debug = True
    app.run()