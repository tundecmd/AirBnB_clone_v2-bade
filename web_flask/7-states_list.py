#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def get_states():
    """ Displays a HTML page of all State objects in storage """
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """tear down session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
