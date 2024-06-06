from flask import Flask
from user_ep import user_bp
from place_ep import place_bp
from review_ep import review_bp
from cc_ep import cc_bp
from ammenities import ammenities_bp



app = Flask("HBnB")


@app.route("/")
def hello():
    """Home page for HBNB"""
    return "Welcome to HBNB!"


app.register_blueprint(user_bp)
app.register_blueprint(place_bp)
app.register_blueprint(review_bp)
app.register_blueprint(cc_bp)
app.register_blueprint(ammenities_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
