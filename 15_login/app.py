#David Xiedeng
#SoftDev1 pd 1
#K15 -- Do I Know You?
#2019-10-02

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def login(): 
  return render_template("login.html")
  
@app.route("/auth")
def loginAccepted():
  """
  print("request:", request)
  print("request.args:", request.args)
  print("request.method:", request.method)
  print("request.headers:", request.headers)
  """
  username = request.args["username"]
  print ("User:", username)
  if username == "cleancoal" and request.args["password"] == "co2":
    return render_template("profile.html", 
      User = username)
  else:
    return redirect("/static/error.html")
    
if __name__ == "__main__":
  app.debug = True
  app.run() 