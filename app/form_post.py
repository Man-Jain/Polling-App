from flask import Flask, render_template, request
from app import app
from app.firebase_connect import Add_Poll, SignUp, db, SignIn

@app.route('/group1', methods=['POST'])
def group1():
	d={}
	try:
		ques=request.form['question_g1']
		choice1=request.form['poll-c1']
		choice2=request.form['poll-c2']
		choice3=request.form['poll-c3']
		choice4=request.form['poll-c4']
		d={"ques":ques,"c1":choice1,"c2":choice2,"c3":choice3,"c4":choice4}
		g1=Add_Poll()
		g1.add_poll_group1(d)
		return '<div class="alert">Group 1 Poll Added</div>'

	except Exception as e:
		return '<h1>No Done</h1>'

@app.route('/group2', methods=['POST'])
def group2():
	d={}
	try:
		ques=request.form['question_g2']
		choice1=request.form['poll-c1']
		choice2=request.form['poll-c2']
		choice3=request.form['poll-c3']
		choice4=request.form['poll-c4']
		d={"ques":ques,"c1":choice1,"c2":choice2,"c3":choice3,"c4":choice4}
		g2=Add_Poll()
		g2.add_poll_group2(d)
		return '<div class="alert">Group 2 Poll Added</div>'

	except Exception as e:
		return '<h1>No Done</h1>'+str(e)

@app.route('/fbsignup', methods=['POST'])
def fbsignup():
	email=user_data['email_id']
	passwd=request.form['passwd']
	user_name=request.form['user-name']
	user_group=request.form['user-group']

	s=SignUp()
	s.signup_user(email,passwd,user_name,user_group)
	return '<div class="alert">Sign Up Successful</div>'

@app.route('/login', methods=['POST'])
def fbsignin():
	user_name=request.form['username']
	passwd=request.form['password']
	user=db.child("users").child(user_name).get()
	email=user.val()['email']
	s=SignIn()
	user_data=s.signin_user(email,passwd)
	print(user_data)
	get_polls=db.child("polls-data").child("group").child("group1").get()
	return render_template('index.html',user=user_data,polls=get_polls.val())