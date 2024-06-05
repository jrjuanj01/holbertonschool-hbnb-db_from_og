from flask import Flask
from user_ep import user_bp


app = Flask("HBnB")

@app.route("/")
def hello():
    """Home page for HBNB"""
    return "Welcome to HBNB!"

app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)