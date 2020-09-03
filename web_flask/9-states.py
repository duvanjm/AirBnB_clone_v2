#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """method to handle"""
    storage.close()


@app.route("states_list", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def state_l():
    """display a HTML page"""
    state = storage.all(State).values()
    return render_template('7-states_list.html', states=state)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """/states/<id>: display a HTML page:"""
    states = storage.all(State)
    item = "State.{}".format(id)
    if item in states:
        state = states[item]
    else:
        state = None
    return render_template("9-states.html", state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
