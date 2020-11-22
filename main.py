from flask import Flask, jsonify
from marshmallow.exceptions import ValidationError

# Loading environment
from dotenv import load_dotenv
load_dotenv()

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    # Flask application object creation
    app = Flask(__name__)
    app.config.from_object("settings.app_config")

    # Setup Serialization and Deserialization
    # Database connection via SQLAlchemy
    # Register database and marshmallow with our app
    db.init_app(app)
    ma.init_app(app)

    # CLI registration
    from commands import db_commands
    app.register_blueprint(db_commands)

    # Controller Registration
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    # Error handler for
    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return jsonify(error.messages), 400

    return app

# basic get
# @app.route("/home", methods=["GET"])
# @app.route("/", methods=["GET"])
# def page_get():
#     return "GET function contents"

# basic POST
# @app.route("/", methods=["POST"])
# def page_post():
#     return "POST function contents"


# Queries
# @app.route("/", methods=["POST"])
# def page_post():
#     return f"Your name is {request.args['name']}"
#
#
# @app.route("/", methods=["POST"])
# def page_post():
#     return f"Your email is {request.form['email']}"
#
#
# @app.route("/", methods=["POST"])
# def page_post():
#     return f"Your phone is {request.json['phone']}"
#
#
# @app.route("/books/<id>")
# def book_page(id):
#     return f"You are looking for book {id}"
#
#
# @app.route("/books/<int:id>")
# def book_page(id):
#     return f"You are looking for book {id}"


