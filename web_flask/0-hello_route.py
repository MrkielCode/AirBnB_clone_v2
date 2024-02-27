#!/usr/bin/python3
"""
This scripts displays Hello HBNB!

"""
from flask import Flask, app

app = Flask(__name__)

#define the route for the root URL'/'
@app.route('/airbnb-onepage/', strict_slashes=False)
def HBNB():
    """
    function to display some string
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
