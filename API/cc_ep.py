from flask import Blueprint, jasonify, request, abort
from models import Country, City

cc_bp = Blueprint("cc", "cc")

@cc_bp.route("/countries", methods=["GET"])
def get_countries():
    countries = Country.query.all()
    return jasonify(countries)