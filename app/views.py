import os
from app import app
from app import db
from app.forms import SignUpForm
from flask import render_template, request, redirect, url_for, jsonify, Response
import validators
from sqlalchemy import text

@app.route('/')
def home():
    sql = text('call GetAllUserRestrictions("John","Doe");')
    result = db.engine.execute(sql)
    # print result
    names = []
    for row in result:
        names.append(row[0])
    print names
    return render_template("index.html")
    

@app.route('/signup',methods=["GET","POST"])
def register():
    form = SignUpForm(request.form)
    if request.method=="POST":
        #gets from form, save file to uploads and make sql statements here, 
        return "Derp"
    else:
        return render_template("signup.html",form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    #maybe use tokens?, can then use ngCookies for some angular but dont have to
    return render_template("login.html")
    
@app.route('/create_recipe',methods=["GET","POST"])
def newRecipe():
    return render_template("")
    
@app.route('/recipes', methods=["GET"])
def recipes():
    return render_template("")
    
@app.route('/generate_mealplan',methods=[""])
def generateMealPlan():
    return render_template("")

@app.route('/kitchen',methods=[""])
def kitchen():
    return render_template("")
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")