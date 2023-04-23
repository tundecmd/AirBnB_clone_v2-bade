#!/usr/bin/python3
"""
A script that starts a Flask web app on
0.0.0.0 and port 5000
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
"""
from flask import Flask

""" Create a new Flask web application instance """
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ A view functions that returns a greeting message """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ A view function that returns the text 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    """
    A view function that returns a string with "C "
    followed by the value of the text variable
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python_is_cool(text='is cool'):
    """
    A view function returns a string with "Python "
    followed by the value of the text variable
    (default is "is cool").
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def Is_Number(n):
    """
    A view function that display 'n is a number' only
    if n is an integer
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


""" Run the application if this script is executed directly """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
