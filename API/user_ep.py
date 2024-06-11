from flask import Blueprint, jsonify, request, abort
from Models.user import User
from Models.review import Review

user_bp = Blueprint("user", __name__)


@user_bp.route("/users", methods=["POST"])
def create_user():
    """create a user"""
    if "email" not in request.json or "password" not in request.json:
        abort(400)
    # missing email database checker
    email = request.json["email"]
    password = request.json["password"]
    return jsonify(User.create(email, password)), 201


@user_bp.route("/users", methods=["GET"])
def get_users():
    """get all users"""
    return jsonify(User.all()), 200


@user_bp.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    """get a user"""
    return jsonify(User.get(user_id)), 200


@user_bp.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    """update a user"""
    user = User.get(user_id)
    if not user:
        abort(404)
    if "email" not in request.json or "password" not in request.json:
        abort(400)
    email = request.json["email"]
    password = request.json["password"]
    user.email = email
    user.password = password
    user.update()
    return jsonify(user), 200


@user_bp.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """delete a user"""
    return jsonify(User.delete(user_id)), 204


@user_bp.route("/users/<user_id>/reviews", methods=["GET"])
def get_reviews(user_id):
    """get all reviews for a user"""
    reviews = [review for review in Review.data_manager.all("Review")
               if review.user_id == user_id]
    return jsonify(reviews), 200
