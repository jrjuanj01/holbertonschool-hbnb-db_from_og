from flask import Blueprint, jsonify, request, abort
from models.amenity import Amenity

ammenities_bp = Blueprint("ammenity", __name__)


@ammenities_bp.route("/ammenities", methods=["POST"])
def create_ammenity():
    """create an ammenity"""
    if "name" not in request.json:
        abort(409)
    name = request.json["name"]
    return jsonify(Amenity.create(name)), 201


@ammenities_bp.route("/ammenities", methods=["GET"])
def get_ammenities():
    """get all ammenities"""
    return jsonify(Amenity.all()), 200


@ammenities_bp.route("/ammenities/<ammenity_id>", methods=["GET"])
def get_ammenity(ammenity_id):
    """get specific ammenity information"""
    return jsonify(Amenity.get(ammenity_id)), 200


@ammenities_bp.route("/ammenities/<ammenity_id>", methods=["PUT"])
def update_ammenity(ammenity_id):
    """update an ammenity"""
    if "name" not in request.json:
        abort(400)
    name = request.json["name"]
    return jsonify(Amenity.update(ammenity_id, name)), 200


@ammenities_bp.route("/ammenities/<ammenity_id>", methods=["DELETE"])
def delete_ammenity(ammenity_id):
    """delete an ammenity"""
    return jsonify(Amenity.delete(ammenity_id)), 204
