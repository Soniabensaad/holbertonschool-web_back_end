from flask import Flask
from flask_babel import Babel

app = Flask(__name)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object('1-app.Config')

app.config.from_object(Config)
babel = Babel(app)
