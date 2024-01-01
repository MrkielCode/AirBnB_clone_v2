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
@app.route('/states', strict_slashes=False)
@app.route('/states/<int:id>', strict_slashes=False)
def list_states_and_cities(id=None):
    """Sorting and routing data"""
    all_states = list(storage.all(State).values())
    if id is not None:
        state = next((state for state in all_states if state.id == id), None)
        if state:
            state.cities.sort(key=lambda city: city.name)
            all_states = [state]
        else:
            all_states = []
    else:
        all_states.sort(key=lambda state: state.name)
        for state in all_states:
            state.cities.sort(key=lambda city: city.name)

    return render_template('9-states.html',
                           states=all_states,
                           id=id,
                           len=len(all_states))


if __name__ == "__main__":
    app.run()
