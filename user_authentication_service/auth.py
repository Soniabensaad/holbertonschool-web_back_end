#!/usr/bin/env python3
"""Hash password"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """you will define a _hash_password"""
    in_bytes_password = password.encode('utf-8')

    # generate salt to hash password
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(in_bytes_password, salt)
    return password_hashed
