from flask import Blueprint, jsonify, request, abort
from Models.country import Country
from Models.city import City


cc_bp = Blueprint("cc", __name__)


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


@cc_bp.route("/countries/<country_code>/cities", methods=["GET"])
def get_cities_in_country(country_code):
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


@cc_bp.route("/cities", methods=["GET"])
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
