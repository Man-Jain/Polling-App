import pyrebase
from config import config

firebase = pyrebase.initialize_app(config)

db = firebase.database()
auth = firebase.auth()

class Add_Poll:
	def add_poll(self, poll_data, group):
		db.child("polls-data").child("group").child(group).push(poll_data)
		return "Done"

class Get_Polls:
	def get_poll_by_group(self, group):
		get_polls=db.child("polls-data").child("group").child(group).get()
		return get_polls.val()

class SignUp:
	def signup_user(self, email, password, user_name, user_group):
		user = auth.create_user_with_email_and_password(email, password)
		data = {"email": email,"group":user_group}
		results = db.child("users").child(user_name).set(data, user['idToken'])

class SignIn:
	def signin_user(self, email, password):
		user = auth.sign_in_with_email_and_password(email, password)
		return user

class Poll_Vote:
	def submit_vote(self, choice_no, poll_id,group,user_name):
		get_choice=db.child("polls-data").child("group").child(group).child(poll_id).child('choices').get()
		current_votes=get_choice.val()[int(choice_no)]['votes']
		updated_votes=current_votes+1
		user_polls=db.child("users").child(user_name).child("prev-polls").push({"id":poll_id})
		res=db.child("polls-data").child("group").child(group).child(poll_id).child('choices').child(choice_no).child('votes').set(updated_votes)
		return res

class Prev_Polls:
	def get_previous_polls(self, user_name):
		user_polls_array=[]
		user_polls=db.child("users").child(user_name).child("prev-polls").get()
		user_polls=user_polls.val()
		user_polls_array=[user_polls[poll]['id'] for poll in user_polls]
		return user_polls_array
