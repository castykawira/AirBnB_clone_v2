#!/usr/bin/python3
"""
This script starts a Flask web application with three routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when the root path is accessed"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when the /hbnb path is accessed."""
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display 'C ' followed by the value of the text variable."""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)
