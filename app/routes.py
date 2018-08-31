from flask import Flask, render_template
from app import app
from app.firebase_connect import Get_Polls

@app.route('/')
@app.route('/index')
def index():
	gp=Get_Polls()
	polls=gp.get_poll_group1()
	return render_template('index.html',all_polls=polls)

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/signin')
def signin():
	return render_template('login.html')