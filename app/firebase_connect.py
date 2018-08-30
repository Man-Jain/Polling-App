import pyrebase

config = {
    "apiKey": "AIzaSyCHyxuD7e8MBGlvn8HZsteayRLMDeG2dFw",
    "authDomain": "polling-app-6df2f.firebaseapp.com",
    "databaseURL": "https://polling-app-6df2f.firebaseio.com",
    "projectId": "polling-app-6df2f",
    "storageBucket": "polling-app-6df2f.appspot.com",
    "messagingSenderId": "482250806175"
 }

firebase = pyrebase.initialize_app(config)

db = firebase.database()
auth = firebase.auth()

class Add_Poll:
	def add_poll_group1(self, poll_data):
		db.child("polls-data").child("group").child("group1").push(poll_data)
		return "Done"
	def add_poll_group2(self, poll_data):
		db.child("polls-data").child("group").child("group2").push(poll_data)
		return "Done"

class Get_Polls:
	def get_poll_group1(self):
		get_polls=db.child("polls-data").child("group").child("group1").get()
		return get_polls.val()
	def get_poll_group2(self):
		get_polls=db.child("polls-data").child("group").child("group1").get()
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