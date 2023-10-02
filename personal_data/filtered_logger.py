#!/usr/bin/env python3
"""Regex-ing"""
import re
from typing import List
import logging
import csv


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message.

    Args:
        fields (List[str]): List of strings representing fields to obfuscate.
        redaction (str): String representing the redaction value.
        message (str): String representing the log message.
        separator (str): String representing the character
        separating fields in the log message.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    for f in fields:
        return re.sub(r"(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]*)",
                      lambda match: match.group(1) + "=" + redaction
                      if match.group(1) in fields else match.group(0), message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)

def get_logger() -> logging.Logger:
    """Create logger"""
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False
    sh = logging.StreamHandler()
    sh.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(sh)
    return log
