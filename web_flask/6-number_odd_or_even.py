#!/usr/bin/python3
"""starts a flask web app"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """"returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """prints C is <text> depending on text given"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """prints Python followed by text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """prints n is a number if n is a number"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def templates(n):
    """calls up a HTML page if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numeven(n):
    """calls up HTML page if n is an integer and even or odd"""
    if n % 2 == 0:
        even = 'even'
    else:
        even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, even=even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
