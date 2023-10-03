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
        return False

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
