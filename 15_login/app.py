#David Xiedeng
#SoftDev1 pd 1
#K15 -- Do I Know You?
#2019-10-02

from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

#hardcoded username and password
username = "cleancoal"
password = "co2"

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
  print ("User:", username)
  """
  session["username"] = request.args["username"]
  session["password"] = request.args["password"]
  if username == session["username"] and password == session["password"]:
    return render_template("profile.html", 
      User = session[username])
  else:
    return redirect("/error")

@app.route("/error")
def badLogin():
  error = ""
  # checks for mistake in the entered information
  #print(username)
  #print(request.args)
  if username != session["username"] and password != session["password"]:
    error = "username and password"
  elif username != session["username"]:
    error = "username"
  else:
    error = "password"
  return render_template("error.html", mistake = error)
    
if __name__ == "__main__":
  app.debug = True
  app.run() 