#!/usr/bin/env python3
"""1. Basic Babel setup
"""
from flask import Flask
from flask_babel import Babel


class Config(object):
    """ Configuration Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
