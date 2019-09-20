#David Xiedeng
#SoftDev1 pd 1
#K<n> -- <Title/Topic/Summary>
#2019-09-<dd> 

from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/")
 #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return "No hablo queso!"

coll = {0,1,2,3}

@app.route("/my_foist_template")
def test_tmplt():
    return render_template(
       'model_tmplt.html',
       foo="foooo",
       collection=coll
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
