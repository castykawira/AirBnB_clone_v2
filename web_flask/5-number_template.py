#!/usr/bin/python3
"""This script starts a Flask web application with six routes"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display 'Hello HBNB!' when the root path is accessed"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when the /hbnb path is accessed"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """Display 'C ', followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """Display 'Python ', followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """Display 'n is a number' only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """Display an HTML page with 'Number: n' inside the H1 tag"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run()
