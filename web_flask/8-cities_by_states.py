#!/usr/bin/python3
from flask import Flask, render_template
from operator import attrgetter
from models import storage, storage_t
from models.state import State
""" flask script for states list """
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
   states = sorted(storage.all(State).values(), key=attrgetter('name'))
   return render_template('7-states_list.html', states=states)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    states = sorted(storage.all(State).values(), key=attrgetter('name'))
    return render_template('8-cities_by_states.html', states=states, storage_t=storage_t)

@app.teardown_appcontext
def close_session(exc):
    """ closes current session """
    storage.close() 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
