#Michael Lin and David Xiedeng
#SoftDev1 pd1
#K12 -- Echo Echo Echo
#2019-09-27

from flask import Flask, render_template, request

app = Flask(__name__)

h = ("Mike is for Micycle - David Xiedeng, Michael Lin", "SoftDev1 pd1", "K12 -- Echo Echo Echo", "2019-09-27")
@app.route("/")
def hello_world():
    print (app)
    return "<a href = \"http://127.0.0.1:5000/rendering\">Link</a>"

@app.route("/rendering")
def formRender():
    return render_template("form.html",
            heading = h)

@app.route("/auth")
def authenticate():
    print("app:", app)
    print("request:", request)
    print("request.args:", request.args) #immutable dict
    print(request.method)
    #print("header",request.headers)
    return render_template("response.html",
            heading= h,
            username = request.args['username'],
            method = request.method)


if __name__ == "__main__":
    app.debug = True
    app.run()