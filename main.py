from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
import psycopg2
from database import cursor, connection

load_dotenv()
app = Flask(__name__)


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


@app.route("/books", methods=["GET"])
def book_index():
    # Return all books
    sql = "SELECT * FROM books"
    cursor.execute(sql)
    books = cursor.fetchall()
    return jsonify(books)


@app.route("/books", methods=["POST"])
def book_create():
    # Create a new book
    sql = "INSERT INTO books (title) VALUES (%s);"
    cursor.execute(sql, (request.json["title"],))
    connection.commit()

    sql = "SELECT * FROM BOOKS ORDER BY ID DESC LIMIT 1"
    cursor.execute(sql)
    book = cursor.fetchone()
    return jsonify(book)


@app.route("/books/<int:id>", methods=["GET"])
def book_show(id):
    # Return a single book
    sql = "SELECT * FROM books WHERE id = %s;"
    cursor.execute(sql, (id,))
    book = cursor.fetchone()
    return jsonify(book)


@app.route("/books/<int:id>", methods=["PUT", "PATCH"])
def book_update(id):
    # Update a book
    sql = "UPDATE books SET title = %s WHERE id = %s;"
    cursor.execute(sql, (request.json["title"], id))
    connection.commit()

    sql = "SELECT * FROM books WHERE id = %s"
    cursor.execute(sql, (id,))
    book = cursor.fetchone()
    return jsonify(book)


@app.route("/books/<int:id>", methods=["DELETE"])
def book_delete(id):
    # Delete a book
    sql = "SELECT * FROM books WHERE id = %s;"
    cursor.execute(sql, (id,))
    book = cursor.fetchone()

    if book:
        sql = "DELETE FROM books WHERE id = %s;"
        cursor.execute(sql, (id,))
        connection.commit()

    return jsonify(book)
