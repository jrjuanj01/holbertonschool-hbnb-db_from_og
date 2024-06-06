from flask import Blueprint, jasonify, request, abort
from models import User, Place, Review

place_bp = Blueprint("place", "place")


@place_bp.route("/places")
def get_places():
    """get all places"""
    return jasonify(Place.all())


@place_bp.route("/places/<place_id>")
def get_place(place_id):
    """get a place"""
    return jasonify(Place.get(place_id))


@place_bp.route("/places/<place_id>/reviews")
def get_reviews(place_id):
    """get all reviews for a place"""
    return jasonify(Review.all(place_id))


@place_bp.route("/places/<place_id>/reviews/<review_id>")
def get_review(place_id, review_id):
    """get a review for a place"""
    return jasonify(Review.get(place_id, review_id))


@place_bp.route("/places/<place_id>/reviews", methods=["POST"])
def create_review(place_id):
    """create a review for a place"""
    if "user_id" not in request.json or "text" not in request.json:
        abort(400)
    user_id = request.json["user_id"]
    text = request.json["text"]
    return jasonify(Review.create(place_id, user_id, text))


@place_bp.route("/places/<place_id>/reviews/<review_id>", methods=["PUT"])
def update_review(place_id, review_id):
    """update a review for a place"""
    if "text" not in request.json:
        abort(400)
    text = request.json["text"]
    return jasonify(Review.update(place_id, review_id, text))


@place_bp.route("/places/<place_id>/reviews/<review_id>", methods=["DELETE"])
def delete_review(place_id, review_id):
    """delete a review for a place"""
    return jasonify(Review.delete(place_id, review_id))
