from flask import Blueprint, jsonify, request, abort
from models import Country, City

cc_bp = Blueprint("cc", "cc")


@cc_bp.route("/countries", methods=["GET"])
def get_countries():
    """get all countries""" 
    countries = Country.query.all()
    return jsonify(countries), 200


@cc_bp.route("/countries/<country_code>", methods=["GET"])
def get_country(country_code):
    """get specific country information"""
    country = Country.query.filter_by(country_code=country_code).first()
    if not country:
        abort(404)
    return jsonify(country), 200


@cc_bp.route("/countries/<country_code>/cities", methode=["GET"])
def get_cities(country_code):
    """get all cities for a specific country"""
    country = Country.query.filter_by(country_code=country_code).first()
    if not country:
        abort(404)
    return jsonify(country.cities), 200


@cc_bp.route("/cities", methods=["POST"])
def create_city(country_code):
    """create a city"""
    country = Country.query.filter_by(country_code=country_code).first()
    if not country:
        abort(404)
    city = City(
        name=request.json.get("name"),
        country_code=country_code
    )
    return jsonify(city), 200


@cc_bp.route("/cities", method=["GET"])
def get_cities():
    """get all cities"""
    cities = City.query.all()
    return jsonify(cities), 200


@cc_bp.route("/cities/<city_id>", methods=["GET"])
def get_city(city_id):
    """get specific city information"""
    city = City.query.filter_by(city_id=city_id).first()
    if not city:
        abort(404)
    return jsonify(city), 200


@cc_bp.route("/cities/<city_id>", methods=["PUT"])
def update_city(city_id):
    """update a city"""
    city = City.query.filter_by(city_id=city_id).first()
    if not city:
        abort(400)
    city.name = request.json.get("name", city.name)
    city.country_code = request.json.get("country_code", city.country_code)
    return jsonify(city), 200


@cc_bp.route("/cities/<city_id>", methods=["DELETE"])
def delete_city(city_id):
    """delete a city"""
    city = City.query.filter_by(city_id=city_id).first()
    if not city:
        abort(404)
    return jsonify(city), 204
