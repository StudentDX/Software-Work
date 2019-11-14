#David Xiedeng
#SoftDev1 pd 1
#K 25 -- Getting More REST
#2019-11-13 

from flask import Flask, render_template
import urllib.request
from urllib.parse import quote
import json

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
    "Wolfram Alpha API":"/wolframAlpha"
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

if __name__ == "__main__":
    app.debug = True
    app.run()