#!/usr/bin/env python3
"""
    i18n Flask Babel module
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config.from_object('config.Config')
babel = Babel(app)
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'


@app.route('/', strict_slashes=False)
def greet():
    """return index from template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
