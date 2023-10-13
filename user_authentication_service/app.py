#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, jsonify, request, abort, redirect
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


@app.route("/sessions", methods=["POST"])
def login() -> str:
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({
            "email": email,
            "message": "logged in",
            "session_id": session_id
            })
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """ logout
       str: message
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=["GET"])
def profile() -> str:
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=["POST"])
def get_reset_password_token() -> str:
    email = request.form.get("email")
    user = AUTH.create_session(email)
    if not user:
        abort(403)
    else:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": f"{email}", "reset_token": f"{token}"}), 200

@app.route('/reset_password', methods=["PUT"])
def update_password() -> str:
    try:
        email = request.form.get('email')
        reset_token = request.form.get('reset_token')
        password = request.form.get('new_password')
    except KeyError:
        abort(403)

    try:
        AUTH.update_password(reset_token, password)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "message": "Password updated"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
