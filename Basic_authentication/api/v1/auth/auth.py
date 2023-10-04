#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List


"""Auth class"""


class Auth:
    """Create the class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This method will be used for authentication logic.
        For now, it always returns False.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        if excluded_paths[-1] is not '/':
            path += '/'

    def authorization_header(self, request=None) -> str:
        """
        This method returns None for now.
        It will be used to handle authorization headers in the future.
        """
        return None

    def current_user(self, request=None):
        """
        This method returns None for now.
        It will be used to get the current user in the future.
        """
        return None
