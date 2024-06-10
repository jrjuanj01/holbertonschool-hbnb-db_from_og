from flask import Blueprint, jsonify, request, abort
from Models.review import Review


review_bp = Blueprint("review", __name__)


@review_bp.route("/places/<place_id>/reviews", methods=["POST"])
def create_review(place_id):
    """create a review"""
    if "place_id" not in request.json:
        abort(404, description="Place not found")
    if "user_id" not in request.json or "text" not in request.json:
        abort(400, description="Missing user_id or text")
    user_id = request.json["user_id"]
    text = request.json["text"]
    return jsonify(Review.create(place_id, user_id, text)), 201


@review_bp.route("/review/<review_id>", methods=["GET"])
def get_review(review_id):
    """get a review"""
    review = Review.get(review_id)
    if not review:
        abort(404)
    return jsonify(review), 200


@review_bp.route("/review/<review_id>", methods=["PUT"])
def update_review(review_id):
    """update a review"""
    if "user_id" not in request.json or "text" not in request.json:
        abort(400, description="Missing user_id or text")
    user_id = request.json["user_id"]
    text = request.json["text"]
    review = Review.update(review_id, user_id, text)
    if not review:
        abort(404)
    return jsonify(review), 200


@review_bp.route("/review/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    """delete a review"""
    if not Review.delete(review_id):
        abort(404)
    return jsonify({}), 204
