#!/usr/bin/env python3
""" Flask app
"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", strict_slashes=False)
def index() -> str:
    """Index page
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def enter_user() -> str:
    """users post payload
    """
    email = request.form.get("email")
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login_user() -> str:
    """ Session post
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    sess_id = AUTH.create_session(email)
    resp = jsonify({"email": email, "message": "logged in"})
    resp.set_cookie("session_id", sess_id)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
