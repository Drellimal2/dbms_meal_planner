import os
from app import app
from app import db
from flask import render_template, request, redirect, url_for, jsonify, Response
from .forms import WishlistForm,ItemForm
import time
from app.models import Profile, Wishlist, Item
import requests
import BeautifulSoup
import urlparse
import validators

app.secret_key ="REST SECRET"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("index.html")
    


"""
    API SYSTEM
"""
@app.route('/api/user/register', methods=['POST'])
def api_register():
    # Run Insert here
    return "Registered"
    
@app.route('/api/user/login', methods=['POST'])
def api_login():
    # Run query user 
    return "Login"



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")