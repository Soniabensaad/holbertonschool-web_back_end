#!/usr/bin/env python3
"""New view for Session Authentication"""
from api.v1.auth.auth import Auth
from models.user import User
from api.v1.views import app_views
from flask import abort, jsonify, request
import os
from os import getenv

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Session Authentication"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({ "error": "password missing" }), 400
    try:
        found = User.search({"email": email})
    except Exception:
        return jsonify ({ "error": "no user found for this email" }), 404
    for user_found in found:
        if User.is_valid_password(password):
            return jsonify({ "error": "wrong password" }), 401
    from api.v1.app import auth
    final_user = found[0]
    session_id = auth.create_session(final_user.id)

    SESSION_NAME = getenv("SESSION_NAME")

    response = jsonify(final_user.to_json())
    response.set_cookie(SESSION_NAME, session_id)

    return response
