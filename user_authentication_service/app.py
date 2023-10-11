#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, jsonify
app = Flask(__name__)

data = {
    "message": "Bienvenue"
}

@app.route("/", methods=["GET"])
def hello():
    return jsonify(data)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
