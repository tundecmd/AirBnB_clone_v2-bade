#!/usr/bin/python3
"""
A script that starts a Flask web app on
0.0.0.0 and port 5000
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
"""
from flask import Flask, render_template

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
    if n is an number
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def Is_Number_Template(n):
    """
    A view function that display 'n is a number' only
    if n is an integer
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def Is_Even_Or_Odd(n):
    """
    A view function that display 'n is a number' only
    if n is an even or odd
    """
    if n % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    return render_template(
                           '6-number_odd_or_even.html',
                           n=n, even_or_odd=even_or_odd
    )


""" Run the application if this script is executed directly """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
