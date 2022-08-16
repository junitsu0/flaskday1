from app import app
from flask import render_template


@app.route('/')
def index():
    movies = ['Oldboy','The Matrix','Big Trouble in Little China', 'Ip Man', 'The Other Guys']
    return render_template('index.html', movies=movies)

@app.route('/home')
def home():
    return 'Welcome Home'

@app.route('/test')
def test():
    return render_template('test.html')