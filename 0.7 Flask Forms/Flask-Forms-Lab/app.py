from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/login', methods=['GET', 'POST'])  
def login(login):
	if request.method == 'POST':
		if username == request.form['username']
			 password == request.form['password']
			 return render_template('home.html', username = username)
  else:
  	return render_template(login.html)
  

@app.route('/')
def home():
	redirect(url_for('home'))

@app.route('/')
def facebook_friends (myUL):
	return render_template(home.html)


@app.route('/friend_exists/<string:name>')
def friend_exists(name):
	return render_template(
		'friend_exists.html', m = name)




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)