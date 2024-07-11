#!/usr/bin/python3
from flask import Flask, render_template
from operator import attrgetter
from models import storage
from models.state import State
""" flask script for states list """
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
   states = sorted(storage.all(State).values(), key=attrgetter('name'))
   print(states)
   return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(exc):
    """ closes current session """
    storage.close() 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
