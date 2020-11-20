from dotenv import load_dotenv
load_dotenv()

from flask import Flask
app = Flask(__name__)

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


