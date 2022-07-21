#!/usr/bin/env python3
""" Defines hash_password """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Creates a hash password using bcrypt """
    password = bytes(password, encoding='utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
