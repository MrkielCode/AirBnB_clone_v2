#!/usr/bin/python3
""" To route and display the states and relate cities data"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_states_and_cities():
    """ sorting and routing data"""
    all_states = storage.all(State).values()
    all_states = sorted(all_states, key=lambda state: state.name)
    for state in all_states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=all_states)


if __name__ == "__main__":
    app.run()
