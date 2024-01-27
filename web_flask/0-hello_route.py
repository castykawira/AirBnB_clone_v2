#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' when the root path is accessed
    """
    return 'Hello HBNB, AirBnB one-page!'


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
