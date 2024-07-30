#!/usr/bin/env python3
"""
    i18n Flask Babel module
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greet():
    """return index from template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
