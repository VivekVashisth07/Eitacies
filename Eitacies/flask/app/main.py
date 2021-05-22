from flask import *

app=Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome Welcom Welcome!!!</h1><h2><a href="/next">next page</a></h3>'
    

@app.route('/next')
def next():
    name=["Vivek Sharma"]
    return render_template("template1.html",name=name)