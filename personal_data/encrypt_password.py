#!/usr/bin/env python3
""" Encrypting passwords"""
import bcrypt

""" Encrypting passwords"""


def hash_password(password: str = "") -> bytes:
    """expects one string argument name password"""
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check valid password"""
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
