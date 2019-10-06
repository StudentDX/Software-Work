#David Xiedeng
#SoftDev1 pd 1
#K15 -- Do I Know You?
#2019-10-02

from flask import Flask, render_template, request, redirect, url_for, session, flash
app = Flask(__name__)

#hardcoded username and password
username = "cleancoal"
password = "co2"

#session setup
file = open("sessionKey.txt", "r")
app.secret_key = file.readline()

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
  #check username and password to hardcoded; either cached or entered
  if username == session.get("username") and password == session.get("password"):
    return render_template("profile.html", 
      User = session.get("username"))
  #if does not match hardcode, change session to request and recurse
  elif session.get("username") != request.args["username"] or session.get("password") != request.args["password"]:
    session["username"] = request.args["username"]
    session["password"] = request.args["password"]
    return loginAccepted()
  else:
    flash("error")  
    return redirect("/error")

@app.route("/error")
def badLogin():
  error = ""
  # checks for mistake in the entered information
  if username != session.get("username") and password != session.get("password"):
    error = "username and password"
  elif username != session.get("username"):
    error = "username"
  else:
    error = "password"
  return render_template("error.html", mistake = error)
    
@app.route("/logout")
def logout():
  session.pop("username")
  session.pop("password")
  return redirect("/")
    
if __name__ == "__main__":
  app.debug = True
  app.run() 