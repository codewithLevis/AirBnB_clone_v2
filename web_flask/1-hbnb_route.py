#!/usr/bin/python3
"""
A script that starts a simple Flask web application
Use the route 0.0.0.0@port => 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    uses: strict_slashes=False
"""
from flask import Flask

app = Flask(__name__, template_folder="HTML", static_folder="statics")
app.config["STRICT_SLASHES"] = False


@app.route('/')
def hbnb_greet():
    """
    View function for the route hbnb greet
    Args: none
    returns a welcome info
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb_welcome():
    """
    View function for the route hbnb welcome
    Args: none
    returns a welcome info
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
