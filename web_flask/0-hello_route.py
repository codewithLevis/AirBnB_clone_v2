#!/usr/bin/python3
"""
A script that starts a simple Flask web application
Use the route 0.0.0.0@port => 5000
Routes:
    /: display “Hello HBNB!”
    uses: strict_slashes=False
"""
from flask import Flask

app = Flask(__name__, template_folder="HTML", static_folder="statics")


@app.route('/')
def home():
    """
    View function for the route home
    Args: none
    returns a welcome info
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
