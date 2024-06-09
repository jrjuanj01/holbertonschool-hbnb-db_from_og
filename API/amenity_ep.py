from flask import Blueprint, jsonify, request, abort
from Models.amenity import Amenity

amenity_bp = Blueprint("amenity", __name__)


@amenity_bp.route("/ammenities", methods=["POST"])
def create_ammenity():
    """create an ammenity"""
    if "name" not in request.json:
        abort(409)
    name = request.json["name"]
    return jsonify(Amenity.create(name)), 201


@amenity_bp.route("/ammenities", methods=["GET"])
def get_ammenities():
    """get all ammenities"""
    return jsonify(Amenity.all()), 200


@amenity_bp.route("/ammenities/<ammenity_id>", methods=["GET"])
def get_ammenity(ammenity_id):
    """get specific ammenity information"""
    return jsonify(Amenity.get(ammenity_id)), 200


@amenity_bp.route("/ammenities/<ammenity_id>", methods=["PUT"])
def update_ammenity(ammenity_id):
    """update an ammenity"""
    if "name" not in request.json:
        abort(400)
    name = request.json["name"]
    return jsonify(Amenity.update(ammenity_id, name)), 200


@amenity_bp.route("/ammenities/<ammenity_id>", methods=["DELETE"])
def delete_ammenity(ammenity_id):
    """delete an ammenity"""
    return jsonify(Amenity.delete(ammenity_id)), 204
