import os
from app import app
from app import db
from app.forms import SignUpForm, LoginForm, RecipeForm
from flask import render_template, request, redirect, url_for, jsonify, Response
import validators
from sqlalchemy import text
from sqlalchemy import create_engine
from werkzeug import secure_filename
import json
import time

engine = create_engine('mysql://project:project@localhost:3306/epicmealplan')

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'gif','png'])

@app.route('/')
def launch():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/signup',methods=["GET","POST"])
def register():
    form = SignUpForm(request.form)
    if request.method=="POST":
        uploadedfile = request.files['uploadedfile']
        if uploadedfile and allowed_file(uploadedfile.filename):
            uploadedfilename = form.email.data + '_' + secure_filename(uploadedfile.filename)
            filepath = os.path.join(os.getcwd() + '/app/static/useruploads/',uploadedfilename)
            uploadedfile.save(filepath)
        connection = engine.raw_connection()
        cursor = connection.cursor()
        cursor.callproc("RegisterUser", [str(form.firstname.data),str(form.lastname.data),str(form.address.data),str(form.email.data),str(form.password.data),str(form.phonenumber.data),str(uploadedfilename),str(form.dob.data)])
        cursor.close()
        connection.commit()
        return redirect(url_for('home'))
    else:
        return render_template("signup.html",form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method=="POST":
        connection = engine.raw_connection()
        cursor = connection.cursor()
        cursor.callproc("LoginUser", [str(form.email.data),str(form.password.data)])
        cursor.close()
        connection.commit()
        return redirect(url_for('home'))
    else:
        return render_template("login.html",form=form)

@app.route('/create_recipe',methods=["GET","POST"])
def newRecipe():
    form = RecipeForm(request.form)
    if request.method=="POST":
        uploadedfile = request.files['uploadedfile']
        if uploadedfile and allowed_file(uploadedfile.filename):
            uploadedfilename = form.name.data + '_' + str(time.strftime("%Y-%m-%d-%H-%M-%S")) + "_" + secure_filename(uploadedfile.filename)
            filepath = os.path.join(os.getcwd() + '/app/static/recipeuploads/',uploadedfilename)
            uploadedfile.save(filepath)
        connection = engine.raw_connection()
        cursor = connection.cursor()
        cursor.callproc("AddRecipe", [str(form.name.data),str(form.recipetype.data),str(uploadedfilename),str(form.serving.data),str(form.preptime.data),str(time.strftime("%Y/%m/%d")),str(form.caloriecount.data)])
        cursor.close()
        connection.commit()
        return redirect(url_for('recipes'))
    else:
        return render_template("recipe.html",form=form)

@app.route('/recipes', methods=["GET"])
def recipes():
    return render_template("")

@app.route('/generate_mealplan',methods=[""])
def generateMealPlan():
    return render_template("")

@app.route('/kitchen',methods=[""])
def kitchen():
    return render_template("")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
