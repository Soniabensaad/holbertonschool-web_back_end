#!/usr/bin/env python3
"""Hash password"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """you will define a _hash_password"""
    in_bytes_password = password.encode('utf-8')

    # generate salt to hash password
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(in_bytes_password, salt)
    return password_hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register user"""
        try:
            find = self._db.find_user_by(email=email)
            if find:
                raise ValueError(f"User <{find.email}> already exists")
        except NoResultFound:
            password_hash = _hash_password(password)
            user = self._db.add_user(email, password_hash)
        return user
    
    def valid_login(self, email:str, password: str) -> bool:
        """Credentials validation"""
        if not email or not password:
            return False
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        
        check = bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
        return check
