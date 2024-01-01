#!/usr/bin/python3
""" script to route to state_list and display
and display some states from database"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the current SQLAlchemy session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_state():
    """ render data from storage """
    all_states = storage.all(State).values()
    sorted_states = sorted(all_states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run()
