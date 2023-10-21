#!/usr/bin/env python3
"""2. Get locale from request"""
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name)
babel = Babel(app)

class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get locale from request""""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def hello_world():
    """ Greeting

        Return:
            Initial template html
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run()
