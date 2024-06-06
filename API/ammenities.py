from flask import Blueprint, jasonify, request, abort
from models import Amenity

ammenities_bp = Blueprint("ammenity", "ammenity")


@ammenities_bp.route("/ammenities", methods=["POST"])
def create_ammenity():
    """create an ammenity"""
    if "name" not in request.json:
        abort(409)
    name = request.json["name"]
    return jasonify(Amenity.create(name)), 201


@ammenities_bp.route("/ammenities", methods=["GET"])
def get_ammenities():
    """get all ammenities"""
    return jasonify(Amenity.all()), 200


@ammenities_bp.route("/ammenities/<ammenity.id>", methods=["GET"])
def get_ammenity(ammenity_id):
    """get specific ammenity information"""
    return jasonify(Amenity.get(ammenity_id)), 200


@ammenities_bp.route("/ammenities/<ammenity_id>", methods=["PUT"])
def update_ammenity(ammenity_id):
    """update an ammenity"""
    if "name" not in request.json:
        abort(400)
    name = request.json["name"]
    return jasonify(Amenity.update(ammenity_id, name)), 200


@ammenities_bp.route("/ammenities/<ammenity_id>", methods=["DELETE"])
def delete_ammenity(ammenity_id):
    """delete an ammenity"""
    return jasonify(Amenity.delete(ammenity_id)), 204
