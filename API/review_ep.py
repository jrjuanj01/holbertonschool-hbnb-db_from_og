from flask import Blueprint, jasonify, request, abort
from models import Review


review_bp = Blueprint("review", "review")


@review_bp.route("/places/<place_id>/reviews", methods=["POST"])
def create_review(place_id):
    """create a review"""
    if user_id not in request.json or text not in request.json:
        abort(400)
    user_id = request.json[user_id]
    text = request.json["text"]
    return jasonify(Review.create(place_id, user_id, text))


@review_bp.route("/users/<user_id>/reviews", methods=["GET"])
def get_reviews(user_id):
    """get all reviews"""
    return jasonify(Review.all(user_id))


@review_bp.route("/places/<place_id>/reviews", methods=["GET"])
def get_review(place_id):
    """get a review"""
    return jasonify(Review.get(place_id))


@review_bp.route("/review/<review_id>", methods=["GET"])
def get_review(review_id):
    """get a review"""
    return jasonify(Review.get(review_id))


@review_bp.route("/review/<review_id>", methods=["PUT"])
def update_review(review_id):
    """update a review"""
    if user_id not in request.json or text not in request.json:
        abort(400)
    user_id = request.json[user_id]
    text = request.json["text"]
    return jasonify(Review.update(review_id, user_id, text))


@review_bp.route("/review/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    """delete a review"""
    return jasonify(Review.delete(review_id))
