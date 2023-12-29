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


if __name__ == "__main__":
    app.run()
