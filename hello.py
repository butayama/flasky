from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/<int:number>')
def user_number(number):
    comments = ["comment1","comment2", "comment3", "comment4", "comment5", "comment6"]
    return render_template('user_number.html', number=number, comments=comments)
