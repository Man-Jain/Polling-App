from flask import Flask
from app import app

@app.route('/test')
def test():
    return 'Test'
