from flask import Blueprint, jsonify, request, abort
from Models.user import User
from Models.review import Review

user_bp = Blueprint("user", __name__)


@user_bp.route("/users", methods=["POST"])
def create_user():
    """create a user"""
    if "email" not in request.json or "password" not in request.json:
        abort(400, description="Missing Email & or Password")
    if "first_name" not in request.json or "last_name" not in request.json:
        abort(400, description="Missing First Name & or Last Name")
    if request.json["email"] in User.emails:
        abort(400, description="Email already exists")
    email = request.json["email"]
    password = request.json["password"]
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    User.emails.append(email)
    User.passwords.append(password)
    User.first_names.append(first_name)
    User.last_names.append(last_name)
    return jsonify(User.create(first_name, last_name, email, password)), 201


@user_bp.route("/users", methods=["GET"])
def get_users():
    """get all users"""
    #Check in database for already existing users
    if not User.all():
        abort(404, description="No users found")
    return jsonify(User.all()), 200


@user_bp.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    """get a user"""
    if "user_id" not in User.get(user_id):
        abort(404, description="User not found")
    return jsonify(User.get(user_id)), 200


@user_bp.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    """update a user"""
    #Check in database for already existing users
    if "user_id" not in User.get(user_id):
        abort(404, description="User not found")
    user = User.get(user_id)
    email = request.json["email"]
    password = request.json["password"]
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    user.email = email
    user.password = password
    user.first_name = first_name
    user.last_name = last_name
    return jsonify(User.update()), 200


@user_bp.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """delete a user"""
    #Check in database for already existing users
    if "user_id" not in User.get(user_id):
        abort(404, description="User not found")
    return jsonify(User.delete(user_id)), 204


@user_bp.route("/users/<user_id>/reviews", methods=["GET"])
def get_reviews(user_id):
    """get all reviews"""
    
    if "user_id" not in Review.all(user_id): #if user has not authored reviews
        abort(404, description="Reviews not Found")
    reviews = [review for review in Review.data_manager.all("Review")
               if review.user_id == user_id]
    return jsonify(reviews), 200
