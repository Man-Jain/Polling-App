from flask import Flask, render_template, session, url_for, escape, request, redirect
from app import app
from app.firebase_connect import *
import json, random

@app.route('/group1', methods=['POST'])
def group1():
	choice_array=[]
	poll_dict={}
	user_data=request.form
	ques=request.form['question_g1']
	i=0
	for choice in user_data.keys():
		choice_dict={'number':i,'string':user_data[choice], 'votes':0}
		if not choice=='question_g1':
			choice_array.append(choice_dict)	
			i+=1
	choice_array={'question':ques,'choices':choice_array}
	g1=Add_Poll()
	g1.add_poll(choice_array,session['group'])
	return json.dumps({'status':'OK'})

@app.route('/fbsignup', methods=['POST'])
def fbsignup():
	email=request.form['email_id']
	passwd=request.form['passwd']
	user_name=request.form['user-name']
	user_group=request.form['user-group']
	s=SignUp()
	s.signup_user(email,passwd,user_name,user_group)
	return redirect(url_for('signin'))

@app.route('/login', methods=['POST'])
def login():
	error_msg='Wrong Email/Password'
	user_login=request.form
	user_name=user_login['username']
	passwd=user_login['password']
	user=db.child('users').child(user_name).get()
	try:
		email=user.val()['email']
		group=user.val()['group']
		s=SignIn()
		user_data=s.signin_user(email,passwd)
		session['username'] = user_name
		session['group'] = group
	except:
		return render_template('login.html',error_msg=error_msg)

	return redirect(url_for('index'))

@app.route('/vote', methods=['POST'])
def vote():
	poll_data=request.form
	g1=Poll_Vote()
	result=g1.submit_vote(poll_data['choice-radio'], poll_data['poll-id'],session['group'],session['username'])
	return json.dumps({'status':result,'poll-data':poll_data})

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))