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
def register_user() -> str:
    try:
        
        email = request.form["email"]
        password = request.form["password"]
    except KeyError:
        abort(400)

    try:
        new_user = AUTH.register_user(email, password)
    except ValueError as e:
        msg = {"message": "Email already registered"}
        return jsonify(msg), 400

    msg = {"email": new_user.email, "message": "User created"}
    return jsonify(msg)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
