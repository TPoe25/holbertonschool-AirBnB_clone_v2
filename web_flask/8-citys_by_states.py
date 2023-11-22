#!/bin/usr/python3
"""
Function to genereate cities to the states
"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Removes the current SQLAlchemy Sesh."""
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """Displays HTML page with a list of states & cities."""
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
