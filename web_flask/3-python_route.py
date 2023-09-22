#!/usr/bin/python3
"""
A script that starts a simple Flask web application
Use the route 0.0.0.0@port => 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the
        text variable (replaces underscore _ symbols with a space )
    /python/<text>: display “Python ”, followed by the value of the
        text variable (replace underscore _ symbols with a space )
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


@app.route('/c/<text>')
def c_route(text):
    """
    Description: view function that displays “C ”
        followed by the value of the text variable
    Args:
        text: text to display alongside C
    returns: a C-text-based info
    """

    return f'C {text.replace("_", " ")}'


@app.route('/python/<text>')
@app.route('/python/')
def python_route(text="is cool"):
    """
    Description: view function that displays “Python”
        followed by the value of the text variable
    Args:
        text: text to display alongside Python
    returns: a Python-text-based info
    """

    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
