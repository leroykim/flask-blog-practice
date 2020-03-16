# Refer the page below for ci command
# https://pythonhosted.org/Flask-CI/
# > set FLASK_APP=hello
# > flask run
# Auto reload
# > set FLASK_DEBUG=1

from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    # http://localhost:5000/?name=leroy
    name = request.args.get("name", "World")
    return f'<h1>Hello, {escape(name)}?</h1>'


@app.route('/about')
def about():
    return f'<h1>About</h1>'


if __name__ == '__main__':
    app.run(debug=True)
