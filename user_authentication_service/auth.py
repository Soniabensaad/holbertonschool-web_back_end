#!/usr/bin/env python3
"""Hash password"""


import bcrypt
import uuid
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


def _generate_uuid() -> str:
    """ Generate UUIDs"""
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Credentials validation"""
        if not email or not password:
            return False
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        check = bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
        return check

    def create_session(self, email: str) -> str:
        """ Get session ID"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """Find user by session ID"""
        if not session_id:
            return
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user.email
        except NoResultFound:
            return

    def destroy_session(self, user_id: int) -> None:
        """Destroy session"""
        user = self._db.find_user_by(id=user_id)
        self._db.update_user(user.id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Generate reset password token"""
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError
 
    def update_password(self, reset_token: str, password: str) -> None:
        """ Update Password
        """
        if reset_token is None or password is None:
            return None

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except (NoResultFound):
            raise ValueError

        new_passwd = _hash_password(password)

        self._db.update_user(
            (user.id), hashed_password=new_passwd,
            reset_token=None)

        return None
