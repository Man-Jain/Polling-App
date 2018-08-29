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

class Add_Poll:
	def add_poll_group1(self, poll_data):
		db.child("polls-data").child("group").child("group1").push(poll_data)
		return "Done"
	def add_poll_group2(self, poll_data):
		db.child("polls-data").child("group").child("group2").push(poll_data)
		return "Done"