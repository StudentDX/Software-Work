from flask import Flask
app = Flask(__name__)

@app.route("/")
def hell():
    print(__name__)
    app.route("/static/Page1.html")
    return "test"

@app.route("/static/Page1.html")
def hello():
    print(__name__)
    return "test 1"



if __name__ == "__main__":
    app.debug = True
    app.run()
