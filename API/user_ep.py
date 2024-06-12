from flask import Blueprint, jsonify, request, abort
from Models.user import User
from Models.review import Review

user_bp = Blueprint("user", __name__)


@user_bp.route("/users", methods=["POST"])
def create_user():
    """create a user"""
    data = request.json
    if data is None:
        abort(400, description="No data provided (must be JSON)")
    fields = ["email", "password", "first_name", "last_name"]
    for field in fields:
        if field not in data:
            abort(400, description=f"Missing {field}")
    if data["email"] in User.emails:
        abort(400, description="Email already exists")
    user = User.create(data["first_name"], data["last_name"],
                       data["email"], data["password"])
    return jsonify(user.to_dict()), 201


@user_bp.route("/users", methods=["GET"])
def get_users():
    """get all users"""
    users = User.all()
    if not users:
        abort(404, description="No users found")
    data = [user.to_dict() for user in users]
    return jsonify(data), 200


@user_bp.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    """get a user"""
    user = User.get(user_id)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user.to_dict()), 200


@user_bp.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    """update a user"""
    user = User.get(user_id)
    if user is None:
        abort(404, description="User not found")
    data = request.json
    if data is None or not data:
        abort(400, description="No data provided (must be JSON)")
    if "email" in data:
        user.email = data["email"]
    if "password" in data:
        user.password = data["password"]
    if "first_name" in data:
        user.first_name = data["first_name"]
    if "last_name" in data:
        user.last_name = data["last_name"]
    user.update()
    return jsonify(user.to_dict()), 200


@user_bp.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """delete a user"""
    user = User.get(user_id)
    if user is None:
        abort(404, description="User not found")
    user.delete()
    return "User deleted", 204


@user_bp.route("/users/<user_id>/reviews", methods=["GET"])
def get_reviews(user_id):
    """get all reviews for a user"""
    reviews = Review.all()
    if not reviews:
        abort(404, description="No reviews found")
    user_reviews = [review.to_dict() for review in reviews
                    if review.user_id == user_id]
    if not user_reviews:
        abort(404, description="User has no reviews")
    return jsonify(user_reviews), 200
