#!/usr/bin/env python3
""" Defines filter_datum """
import logging
import re
from typing import List


PII_FIELDS = ["name", "phone", "email", "ssn", "password"]


def filter_datum(
        fields: List[str],
        redaction: str, message: str, separator: str) -> str:
    """ Returns an obfuscated log message """
    for key in fields:
        message = re.sub(f'{key}=.*?{separator}',
                         f'{key}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters in incoming records """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """Returns a log object"""
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    log.addHandler(stream_handler)
    return log
