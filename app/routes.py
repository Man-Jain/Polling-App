from flask import Flask, render_template, session, redirect, url_for
from app import app
from app.firebase_connect import Get_Polls,Prev_Polls, Get_Members

gp=Get_Polls()
pp=Prev_Polls()
gm=Get_Members()

@app.route('/')
@app.route('/index')
def index():
	if 'username' in session:
		user=session['username']
		group=session['group']
		polls=gp.get_poll_by_group(session['group'])
		prev_polls=pp.get_previous_polls(user)
		members=gm.get_group_members(user, group)
		return render_template('index.html',all_polls=polls, prev_polls=prev_polls, members=members)
	return redirect(url_for('signin'))

@app.route('/forms')
def forms():
	if 'username' in session:
		members=gm.get_group_members(session['username'],session['group'])
		return render_template('forms.html',  members=members)
	return redirect(url_for('signin'))

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/signin')
def signin():
	return render_template('login.html')