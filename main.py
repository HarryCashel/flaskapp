# Loading environment
from dotenv import load_dotenv
load_dotenv()

# Flask application object creation
from flask import Flask
app = Flask(__name__)

# Database connection via SQLAlchemy
from database import init_db
db = init_db(app)

# Setup Serialization and Deserialization
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

# Controller Registration
from controllers import registerable_controllers

for controller in registerable_controllers:
    app.register_blueprint(controller)



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


