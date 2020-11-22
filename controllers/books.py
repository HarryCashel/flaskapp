from models.Book import Book
from main import db
from schemas.BookSchema import book_schema, books_schema
from flask import Blueprint, request, jsonify

books = Blueprint('books', __name__, url_prefix="/books")


@books.route("/", methods=["GET"])
def book_index():
    # Retrieve all books
    books = Book.query.all()
    return jsonify(books_schema.dump(books))


@books.route("/", methods=["POST"])
def book_create():
    # Create a new book
    book_fields = book_schema.load(request.json)

    new_book = Book()
    new_book.title = book_fields["title"]

    db.session.add(new_book)
    db.session.commit()

    return jsonify(book_schema.dump(new_book))


@books.route("/<int:id>", methods=["GET"])
def book_show(id):
    # Return a single book
    book = Book.query.get(id)
    return jsonify(book_schema.dump(book))


@books.route("/<int:id>", methods=["PUT", "PATCH"])
def book_update(id):
    # Update a book
    books = Book.query.filter_by(id=id)
    book_fields = book_schema.load(request.json)
    books.update(book_fields)
    db.session.commit()

    return jsonify(book_schema.dump(books[0]))


@books.route("/<int:id>", methods=["DELETE"])
def book_delete(id):
    # Delete a book
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
