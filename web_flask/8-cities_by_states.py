#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """method to handle"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_l():
    """display a HTML page"""
    state = storage.all(State).values()
    return render_template('7-states_list.html', states=state)


@app.route("/cities_by_states", strict_slashes=False)
def cities():
    """display a HTML page"""
    states_city = {
        'states': storage.all(State).values(),
        'cities': storage.all(City).values()
    }

    return render_template('8-cities_by_states.html', **states_city)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
