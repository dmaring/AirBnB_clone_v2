#!/usr/bin/python3
"""
Flask module that returns a Flask app
"""
from flask import Flask, escape, render_template
from models import storage

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ A route that displays Hello HBNB! """
    return "Hello HBNB!"


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


@app.route('/states_list')
def states_list():
    """ A route that displays a template and number only if an int is input """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """ A route that displays states and their cities """
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/', defaults={'s_id': None})
@app.route('/states/<s_id>')
def states(s_id):
    """ A route that displays states by id if passed """
    states = storage.all('State')
    if s_id:
        s_id = "{}.{}".format('State', s_id)
    return render_template('9-states.html',
                           states=states, s_id=s_id)


@app.route('/hbnb_filters')
def hbnb_filters():
    """ A route that displays the popover search filter options """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.route('/hbnb')
def hbnb():
    """ A route that displays the main hbnb page """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    users = storage.all('User')
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities,
                           places=places, users=users)


@app.teardown_appcontext
def close_db(error):
    """Closes the database at the end of the request."""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
