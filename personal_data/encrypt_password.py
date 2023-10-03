#!/usr/bin/env python3
import bcrypt

""" Encrypting passwords"""
def hash_password(password):
    """expects one string argument name password"""
    
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    
    
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    return hashed_password
