#!/usr/bin/python3
"""
A script that starts a Flask application
The web application will be listening on 0.0.0.0, port 5000
Uses storage for fetching data from the storage engine (FileStorage or DBStorage) =>
    from models import storage and storage.all(...)
Removes the current SQLAlchemy Session after each request
Routes:
    /states_list: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present in
            DBStorage sorted by name (A->Z)
                    LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """
    renders a state list data
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def closure(exception):
    """
    Closes current session
    """
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
