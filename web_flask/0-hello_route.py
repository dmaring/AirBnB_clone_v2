#!/usr/bin/python3
"""
Flask module that returns a route at /
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=None)
def hello_hbnb():
    """ A route that displays Hello HBNB! """
    return "Hello HBNB!"

app.run()
