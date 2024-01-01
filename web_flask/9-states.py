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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_states_and_cities(id=None):
    """ sorting and routing data"""
    all_states = storage.all(State)
    if id:
        state = all_states.get('State.{}'.format(id))
        all_states = [state] if state else []
    else:
        all_states = sorted(all_states.values(), key=lambda state: state.name)
        for state in all_states:
            state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-states.html',
                           states=all_states,
                           id=id,
                           len=len(all_states))


if __name__ == "__main__":
    app.run()
