#!/usr/bin/python3
"""
starts flask web app
"""



from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/states')
def states():
    """Display a HTML page with a list of states."""
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)

    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def state_cities(id):
    """Display a HTML page with cities of a specific state."""
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
