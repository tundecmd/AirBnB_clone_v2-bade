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
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ A view function that returns the text 'HBNB' """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    return ("C {}".format(text.replace('_', ' ')))


""" Run the application if this script is executed directly """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
