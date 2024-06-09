from flask import Blueprint, jsonify, request, abort
from Models.review import Review


review_bp = Blueprint("review", __name__)


@review_bp.route("/places/<place_id>/reviews", methods=["POST"])
def create_review(place_id):
    """create a review"""
    if user_id not in request.json or text not in request.json:
        abort(400)
    user_id = request.json[user_id]
    text = request.json["text"]
    return jsonify(Review.create(place_id, user_id, text)), 201


@review_bp.route("/review/<review_id>", methods=["GET"])
def get_review(review_id):
    """get a review"""
    return jsonify(Review.get(review_id)), 200


@review_bp.route("/review/<review_id>", methods=["PUT"])
def update_review(review_id):
    """update a review"""
    if user_id not in request.json or text not in request.json:
        abort(400)
    user_id = request.json[user_id]
    text = request.json["text"]
    return jsonify(Review.update(review_id, user_id, text)), 200


@review_bp.route("/review/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    """delete a review"""
    return jsonify(Review.delete(review_id)), 204
