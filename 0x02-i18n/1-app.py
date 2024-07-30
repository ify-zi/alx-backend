#!/usr/bin/env python3
"""
    i18n Flask Babel module
"""

from flask import Flask, render_template
from flask_babel import Babel
from pytz import UTC


class Config:
    """default parameters in babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object('Config')

@app.route('/', strict_slashes=False)
def greet():
    """return index from template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
