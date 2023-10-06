#!/usr/bin/env python3
"""Empty session"""
from api.v1.auth.auth import Auth
from models.user import User

class SessionAuth(Auth):
    """ class SessionAuth that inherits from Auth"""
