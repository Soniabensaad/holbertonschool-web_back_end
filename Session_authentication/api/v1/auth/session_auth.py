#!/usr/bin/env python3
"""Empty session"""
from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ class SessionAuth that inherits from Auth"""
    user_id_by_session_id = {}
    def create_session(self, user_id: str = None) -> str:
        """Create an instance method """
        if user_id is None\
            or type(user_id) != str:
            return None
        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id
