from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    #
    user = {'username':'Site Administrator'}
    #
    posts = [
        {
            'author':{'username': 'User One'},
            'body':'Content from user one'
        },
        {
            'author':{'username': 'User Two'},
            'body':'Content from user two'
        }
    ]
    #
    return render_template('index.html',title='Home',user=user,posts=posts)

@app.route('/test')

def test():
    #
    return "<h1> This is a test </h1>"

