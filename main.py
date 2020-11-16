from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
import psycopg2
load_dotenv()
app = Flask(__name__)

connection = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST")
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()

# basic get
@app.route("/home", methods=["GET"])
@app.route("/", methods=["GET"])
def page_get():
    return "GET function contents"

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


@app.route("/books", methods=["GET"])
def book_index():
    # Return all books
    pass


@app.route("/books", methods=["POST"])
def book_create():
    # Create a new book
    pass


@app.route("/books/<int:id>", methods=["GET"])
def book_show(id):
    # Return a single book
    pass


@app.route("/books/<int:id>", methods=["PUT", "PATCH"])
def book_update(id):
    # Update a book
    pass


@app.route("/books/<int:id>", methods=["DELETE"])
def book_delete(id):
    # Delete a book
    pass
