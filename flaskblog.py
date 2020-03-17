# Refer the page below for ci command
# https://pythonhosted.org/Flask-CI/
# > set FLASK_APP=hello
# > flask run
# Auto reload
# > set FLASK_DEBUG=1

from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationFrom, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '33a6d89745efb0d7e4f219430aa6672d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}, '{self.image_file})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted})"


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

'''
> python
>>> from flaskblog import db
>>> db.create_all()
'''
'''
>>> from flaskblog import db
>>> db.create_all()
>>> from flaskblog import User, Post
>>> user_1 = User(username='Leroy', email='L@demo.com', password='password')
>>> db.session.add(user_1)
>>> user_2 = User(username='JaneDoe', email='jd@demo.com', password='password')
>>> db.session.add(user_2)
>>> db.session.commit()
>>> User.query.all()
[User('Leroy', 'L@demo.com), 'default.jpg, User('JaneDoe', 'jd@demo.com), 'default.jpg]
>>> User.query.first()
User('Leroy', 'L@demo.com), 'default.jpg
>>> User.query.filter_by(username='Leroy').all()
[User('Leroy', 'L@demo.com), 'default.jpg]
>>> user = User.query.filter_by(username='Leroy').first()
>>> user.id
1
>>> user = User.query.get(1)
>>> user
User('Leroy', 'L@demo.com), 'default.jpg
>>> user.posts
[]
'''
'''
>>> post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
>>> post_2 = Post(title='Blog 2', content='Second Post Content!', user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.add(post_2)
>>> db.session.commit()
>>> user.posts
[Post('Blog 1', '2020-03-17 17:19:27.983161), Post('Blog 2', '2020-03-17 17:19:27.997123)]
>>> for post in user.posts:
...     print(post.title)
...
Blog 1
Blog 2
>>> post = Post.query.first()
>>>
>>> post
Post('Blog 1', '2020-03-17 17:19:27.983161)
>>> post.user_id
1
>>> post.author
User('Leroy', 'L@demo.com), 'default.jpg
'''
'''
>>> db.drop_all()
>>> db.create_all()
>>> User.query.all()
[]
>>> Post.query.all()
[]
'''