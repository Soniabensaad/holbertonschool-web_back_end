#!/usr/bin/env python3
import re
from typing import List, Tuple
""" Regex-ing"""
def filter_datum(fields: List, redaction: str, message: str, separator: str):
    """Write a function called filter_datum that
    returns the log message obfuscated"""
    for f in fields:
        return (re.sub(r"(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]*)", lambda match: match.group(1) + "=" + redaction
                       if match.group(1) in fields else match.group(0), message)
)
