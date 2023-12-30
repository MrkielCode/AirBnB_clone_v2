#!/usr/bin/python3
"""
This scripts displays Hello HBNB!

"""
from flask import Flask, app

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def HBNB():
    """
    function to display some string
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB1():
    """
    function to display Hbnb
    """
    return "HBNB"


if __name__ == "__main__":
    app.run()
