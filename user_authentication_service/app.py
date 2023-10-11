#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)

AUTH = Auth()
data = {
    "message": "Bienvenue"
}


@app.route("/", methods=["GET"])
def hello():
    return jsonify(data)

@app.route("/users", methods=["POST"])
def register_user():
    try:
        email = request.form.get("email")
        password = request.form.get("password")
    except KeyError:
        abort(400)

    try:
        new_user = AUTH.register_user(email, password)
        msg = {"email": new_user.email, "message": "user created"}
        return jsonify(msg)
    except ValueError as e:
        msg = {"message": "email already registered"}
        return jsonify(msg), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
