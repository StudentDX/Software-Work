#David Xiedeng
#SoftDev1 pd 1
#K 25 -- Getting More REST
#2019-11-13 

from flask import Flask, render_template
import urllib.request
from urllib.parse import quote
import json
import random

app = Flask(__name__)

class API(object):
    key: str
    url: str
    def __init__(self, key, url):
        self.key = key
        self.url = url
    
    def get_url(self, query="") -> str:
        query = quote(query)
        return self.url.format(_key = self.key, _query = query)
    
WOLFRAM = API('P4747E-2545R4KKGK', 'http://api.wolframalpha.com/v2/query?appid={_key}&input={_query}&output=json')



APIs = {
    "Wolfram Alpha API":"/wolframAlpha",
    "Metropolitan Museum of Art Collection API":"/met"
    }

@app.route("/")
def TOC():
    return render_template("TOC.html", list=APIs)

@app.route("/wolframAlpha")    
def wolframAlpha():
    # Wolfram's API
    query = 'picasso'
    query_link = WOLFRAM.get_url(query)

    request = urllib.request.urlopen(query_link)
    response = request.read()
    data = json.loads(response)['queryresult']
    img = data['pods'][0]['subpods'][0]['img']
    print(img)
    return render_template('img.html',img_title = img['title'], img_link = img['src'])
    
@app.route("/met")
def metropolitan():
    #find list of all objects
    request = urllib.request.urlopen("https://collectionapi.metmuseum.org/public/collection/v1/objects")
    response = request.read()
    objectIDs = json.loads(response)["objectIDs"]
    #chooses on object
    chosenObject = objectIDs[(random.randrange(len(objectIDs)))]
    #gets info on object
    request = urllib.request.urlopen("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(chosenObject))
    response = request.read()
    data = json.loads(response)
    #objectName
    #medium
    #artistDisplayName
    #objectDate
    #primaryImage
    #additionalImages
    return render_template("metropolitan.html", name=data["objectName"], \
        medium = data["medium"], artist = data["artistDisplayName"], \
        data = data["objectDate"], main_img=data["primaryImage"], \
        more_images=data["additionalImages"], image_url = data["primaryImage"])

if __name__ == "__main__":
    app.debug = True
    app.run()