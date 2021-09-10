from flask import Flask, session, flash, redirect, url_for, render_template, request
from flask.scaffold import F
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    data = request.args.get('data')
    # return render_template('register.html')
    return f'the data is {data}'


@app.route('/view')
def view():
    return render_template('view.html')


if __name__ == '__main__':
    app.run(debug=True)
