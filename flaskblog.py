# Refer the page below for ci command
# https://pythonhosted.org/Flask-CI/
# > set FLASK_APP=hello
# > flask run
# Auto reload
# > set FLASK_DEBUG=1

from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
