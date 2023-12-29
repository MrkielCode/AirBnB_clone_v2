#!/usr/bin/python3
"""
This scripts displays Hello HBNB!

"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    function to display some string
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    function to display Hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ rounting to /c with parameter"""
    if '_' in text:
        text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ routing to /python with parameter"""
    if '_' in text:
        text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    app.run()
