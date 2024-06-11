from flask import Blueprint, jsonify, request, abort
from Models.review import Review
from Models.place import Place


review_bp = Blueprint("review", __name__)


@review_bp.route("/places/<place_id>/reviews", methods=["POST"])
def create_review(place_id):
    """create a review"""
    if "place_id" not in request.json:
        abort(404, description="Place not found")
    if "user_id" not in request.json:
        abort(400, description="Missing User_id")
    if "text" not in request.json or "rating" not in request.json:
        abort(400, description="Missing review")
    place_id = place_id
    user_id = request.json["user_id"]
    place = Place.get(place_id)
    if user_id == place.user_id:
        abort(400, description="User cannot review their own place")
    text = request.json["text"]
    rating = request.json["rating"]
    return jsonify(Review.create(user_id, place_id, rating, text)), 201


@review_bp.route("/review/<review_id>", methods=["GET"])
def get_review(review_id):
    """get a review"""
    if "review_id" not in Review.get(review_id):
        abort(404, description="Review not found")
    review = Review.get(review_id)
    return jsonify(review), 200


@review_bp.route("/review/<review_id>", methods=["PUT"])
def update_review(review_id):
    """update a review"""
    if "review_id"  not in Review.get(review_id):
        abort(404, description="Review not found")
    if "text" not in request.json or "rating" not in request.json:
        abort(400, description="Missing review")
    review = Review.get(review_id)
    text = request.json["text"]
    rating = request.json["rating"]
    review.text = text
    review.rating = rating
    return jsonify(review), 200


@review_bp.route("/review/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    """delete a review"""
    if not Review.delete(review_id):
        abort(404)
    return jsonify({}), 204
