from flask import Flask, session
import os

app=Flask(__name__)
app.secret_key = 'whateveroyuthinksuitsyouthebest'

from app import routes,errors,form_post
