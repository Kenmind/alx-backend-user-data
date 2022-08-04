#!/usr/bin/env python3
"""Authentication module
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid1

from user import User


def _hash_password(password: str) -> bytes:
    """Generates a hashed password
    """
    password = password.encode()
    return bcrypt.hashpw(password, bcrypt.gensalt())


def _generate_uuid() -> str:
    """UUID generator
    """
    return str(uuid1())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login info
        """
        user = None
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(
                        password.encode("UTF-8"), user.hashed_password,)
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        """Creates a session
        """
        user = None
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        if user is None:
            return None
        sess_id = _generate_uuid()
        self._db.update_user(user.id, session_id=sess_id)
        return sess_id
