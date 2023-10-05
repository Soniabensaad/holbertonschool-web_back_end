#!/usr/bin/env python3
"""Basic auth"""
from api.v1.auth.auth import Auth
from base64 import b64decode, binascii


class BasicAuth(Auth):
    """ Basic Auth class """

    def extract_base64_authorization_header(
                                            self,
                                            authorization_header: str
                                            ) -> str:
        """
            Extract header in base64

            Args:
                authorization_header: string in base64

            Return:
                Header in base64 or None
        """
        if authorization_header is None\
           or type(authorization_header) != str\
           or not authorization_header.startswith('Basic ')\
           and not authorization_header.endswith(' '):

            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """
        returns the decoded value of
        a Base64 string base64_authorization_header:
        """
        if base64_authorization_header is None\
           or type(base64_authorization_header) != str:
            return None
        try:
            decode_bytes = b64decode(base64_authorization_header)
        except binascii.Error as error:
            return None
        return decode_bytes.decode('utf-8')
