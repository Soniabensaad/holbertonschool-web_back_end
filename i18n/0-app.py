#!/usr/bin/env python3
"""0. Basic Flask app
"""

from flask import Flask, render_template

app = Flask(__name)

@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    return render_template('0-ondex.html')

if __name__ == '__main__':
    app.run()
