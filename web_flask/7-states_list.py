#!/usr/bin/python3
""" A script starts a Flask web application """

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Displays a HTML page of all State objects in storage """
    states = sorted(storage(State).all().Values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """tear down session"""
    storage.close()
