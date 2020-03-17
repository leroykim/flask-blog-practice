# Refer the page below for ci command
# https://pythonhosted.org/Flask-CI/
# > set FLASK_APP=hello
# > flask run
# Auto reload
# > set FLASK_DEBUG=1

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationFrom, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '33a6d89745efb0d7e4f219430aa6672d'

posts = [
    {
        'author': 'Leroy Kim',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 15, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 16, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    # Name of variable does not matter
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
