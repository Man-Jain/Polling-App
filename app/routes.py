from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user={'username':'Manank'}
    posts=[{'author':{'username':'John'},'body':'What a great day'},{'author':{'username':'Mandy'},'body':'What a great night'}]
    return render_template('index.html',title='home',user=user,posts=posts)
