#!/usr/bin/env python3
""" Defines filter_datum """
import logging
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str, message: str, separator: str) -> str:
    """ Returns an obfuscated log message """
    for key in fields:
        message = re.sub(f'{key}=.*?{separator}',
                         f'{key}={redaction}{separator}', message)
    return message
