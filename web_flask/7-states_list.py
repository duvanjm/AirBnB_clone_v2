#!/bin/usr/python3
"""starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """method to handle"""
    storage.close()


@app.route("/states_list")
def state_l():
    """display a HTML page"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", li=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
