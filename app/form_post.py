from flask import Flask
from app import app
from flask import request
from app.Data import Add_Poll

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
