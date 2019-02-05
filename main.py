from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/request')
def req():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is %s</h1>' % user_agent


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
