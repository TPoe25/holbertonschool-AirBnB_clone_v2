#!/usr/bin/python3
""" this is the module to route hbnb"""
from flask import Flask, render_template
from werkzeug.utils import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ shows message on root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ shows message on hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """" Returns 'C' with value of text variable """
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """ shows 'Python ' followed by value"""
    return 'Python {}'.format(escape(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ shows 'n is a number' only if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ returns an HTML page if n is an int"""
    return render_template('5-number.html', n=escape(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)