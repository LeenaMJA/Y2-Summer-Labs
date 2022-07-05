from flask import Flask, jsonify, request, render_template
import random

app = Flask( eBay,)
	template_folder='templates',  "index.html",
	static_folder='static' 
            
 @app.route('/login')
def login():
  return render_template('home.html')          

@app.route('/')
def shopname():
  return render_template("eBay")

@app.route('/')
def shopdescription():
  return render_template("We are an amzing shop")

@app.route('/')
def shoppic1():
  return render_template("converse.jpg")

@app.route('/shopsection1')
def shopsection1():
  return render_template("shoes")


@app.route('/')
def app.py():
  return render_template("product.html")

@app.route('/')
def prroducttitle():
  return render_template("LouisVuitton purse")

@app.route('/')
def productimage():
  return render_template("bag.jpg")

@app.route('/')
def Productdescription():
  return render_template("Louis Vuitton second hand bag, in great condition")

@app.route('/')
def Productprice():
  return render_template("400$")

@app.route('/')
def back_to_home_page():
  return render_template("home.html")

app.run (debug = True )

@app.route('/')
def app.py():
  return render_template("cart.html")

#stuckkkk
#again image situation


  