import os
from app import app
from app import db
from app.forms import SignUpForm, LoginForm, RecipeForm, IngredientForm
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

@app.route('/create_ingredient',methods=["GET","POST"])
def newIngredient():
    form = IngredientForm(request.form)
    return render_template("ingredient.html",form=form)

@app.route('/users',methods=["GET"])
def users():
    connection = engine.connect()
    result = connection.execute("select user.user_firstname,user_lastname from user")
    users = []
    for row in result:
        users.append(row['user_firstname']+" "+row['user_lastname'])
    connection.close()
    return users

@app.route('/recipes', methods=["GET"])
def recipes():
    connection = engine.connect()
    result = connection.execute("select recipe.recipe_name from recipe")
    recipes = []
    for row in result:
        recipes.append(row['recipe_name'])
    connection.close()
    return recipes

@app.route('/measurements',methods=["GET"])
def measurements():
    connection = engine.connect()
    result = connection.execute("select measurement.measurement_name from measurement")
    measurements = []
    for row in result:
        measurements.append(row['measurement_name'])
    connection.close()
    return jsonify({"measurements":measurements})

@app.route('/ingredients',methods=["GET"])
def ingredients():
    connection = engine.connect()
    result = connection.execute("select ingredient.ingredient_name from ingredient")
    ingredients = []
    for row in result:
        ingredients.append(row['ingredient_name'])
    connection.close()
    return ingredients

@app.route('/restrictions',methods=["GET"])
def restrictions():
    connection = engine.connect()
    result = connection.execute("select userrestriction.restriction_name from userrestriction")
    restrictions = []
    for row in result:
        restrictions.append(row['restriction_name'])
    connection.close()
    return restrictions

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
