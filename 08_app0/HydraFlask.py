from flask import Flask
app = Flask(__name__)

#website used to figure routes out 
#https://www.rithmschool.com/courses/flask-fundamentals/routing-with-flask

@app.route("/")
def test1():
    print(__name__)
    return "test 1"

@app.route("/test2") #naming scheme is done with /<funct name>
def test2():
    print(__name__)
    return "test 2"

@app.route("/test3") #to use route, type in the url the route tag
def test3():
    print(__name__)
    return "test 3"

if __name__ == "__main__":
    app.debug = True
    app.run()
