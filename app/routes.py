from flask import Flask, render_template, session, redirect, url_for
from app import app
from app.firebase_connect import Get_Polls,Prev_Polls

@app.route('/')
@app.route('/index')
def index():
	if 'username' in session:
		user=session['username']
		gp=Get_Polls()
		pp=Prev_Polls()
		polls=gp.get_poll_by_group(session['group'])
		prev_polls=pp.get_previous_polls(user)
		return render_template('index.html',all_polls=polls, prev_polls=prev_polls)
	else:
		return redirect(url_for('signin'))

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/signin')
def signin():
	return render_template('login.html')