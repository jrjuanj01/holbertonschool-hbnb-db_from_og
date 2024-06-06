from flask import Blueprint, jasonify, request, abort
from models import User

user_bp = Blueprint("user", "user")


@user_bp.route("/users", methods=["POST"])
def create_user():
    """create a user"""
    if "email" in request.json:
        abort(400)
    email = request.json["email"]
    password = request.json["password"]
    return jasonify(User.create(email, password))


@user_bp.route("/users", method=["GET"])
def get_users():
    """get all users"""
    return jasonify(User.all())


@user_bp.route("/users/<user.id>", methods=["GET"])
def get_user(user_id):
    """get a user"""
    return jasonify(User.get(user_id))


@user_bp.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    """update a user"""
    if "email" not in request.json or "password" not in request.json:
        abort(400)
    email = request.json["email"]
    password = request.json["password"]
    return jasonify(User.update(user_id, email, password))


@user_bp.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """delete a user"""
    return jasonify(User.delete(user_id))
