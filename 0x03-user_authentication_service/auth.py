#!/usr/bin/env python3
"""Authentication module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Generates a hashed password
    """
    password = password.encode()
    return bcrypt.hashpw(password, bcrypt.gensalt())
