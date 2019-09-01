#!/usr/bin/python3
"""
Flask module that returns a Flask app
"""
from flask import Flask, escape, render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ A route that displays Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ A route that displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ A route that displays C and input text """
    return "C %s" % escape(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ A route that displays python and input text """
    return "Python %s" % escape(text.replace("_", " "))


@app.route('/number/<int:number>', strict_slashes=False)
def is_number(number):
    """ A route that displays input number only if an int is input """
    return "%s is a number" % escape(number)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template(n):
    """ A route that displays a template and number only if an int is input """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ A route that displays a template and number only if an int is input """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
