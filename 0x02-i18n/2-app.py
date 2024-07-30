#!/usr/bin/env python3
"""
    i18n Flask Babel module
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from pytz import UTC


class Config(object):
    """default parameters in babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get the best match for language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def greet():
    """return index from template"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
