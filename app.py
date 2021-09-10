from flask import Flask, session, flash, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MYSECRETKEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


db.drop_all()
db.create_all()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        row = User(first_name=fname, last_name=lname, email=email)
        db.session.add(row)
        db.session.commit()
        flash('successful')
        return redirect(url_for('register'))
    else:
        return render_template('register.html')


@app.route('/view', methods=['POST', 'GET'])
def view():
    if request.method == 'POST':
        row = User.query.filter_by(email=request.form['email']).first()
        return render_template('view.html', user=row)
    return render_template('view.html')


if __name__ == '__main__':
    app.run(debug=True)
