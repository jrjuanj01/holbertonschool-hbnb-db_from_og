from flask import Blueprint, jasonify, request, abort
from models import Country, City

cc_bp = Blueprint("cc", "cc")


@cc_bp.route("/countries", methods=["GET"])
def get_countries():
    countries = Country.query.all()
    return jasonify(countries)


@cc_bp.route("/countries/<country_code>", methods=["GET"])
def get_country(country_code):
    country = Country.query.filter_by(country_code=country_code).first()
    if not country:
        abort(404)
    return jasonify(country)


@cc_bp.route("/countries/<country_code>/cities", methode=["GET"])
def get_cities(country_code):
    country = Country.query.filter_by(country_code=country_code).first()
    if not country:
        abort(404)
    return jasonify(country.cities)


@cc_bp.route("/cities", methods=["POST"])
def create_city(country_code):
    country = Country.query.filter_by(country_code=country_code).first()
    if not country:
        abort(404)
    city = City(
        name=request.json.get("name"),
        country_code=country_code
    )
    db.session.add(city)
    db.session.commit()
    return jasonify(city), 200


@cc_bp.route("/cities", method=["GET"])
def get_cities():
    cities = City.query.all()
    return jasonify(cities)


@cc_bp.route("/cities/<city_id>", methods=["GET"])
def get_city(city_id):
    city = City.query.filter_by(city_id=city_id).first()
    if not city:
        abort(404)
    return jasonify(city)


@cc_bp.route("/cities/<city_id>", methods=["PUT"])
def update_city(city_id):
    city = City.query.filter_by(city_id=city_id).first()
    if not city:
        abort(404)
    city.name = request.json.get("name", city.name)
    city.country_code = request.json.get("country_code", city.country_code)
    db.session.commit()
    return jasonify(city)


@cc_bp.route("/cities/<city_id>", methods=["DELETE"])
def delete_city(city_id):
    city = City.query.filter_by(city_id=city_id).first()
    if not city:
        abort(404)
    db.session.delete(city)
    db.session.commit()
    return jasonify(city)
