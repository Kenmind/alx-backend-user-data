#!/usr/bin/env python3
""" Defines hash_password """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Creates a hash password using bcrypt """
    password = bytes(password, encoding='utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates a hashed password"""
    hashed_password = hash_password(password)
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hashed_password):
        return True
    return False
