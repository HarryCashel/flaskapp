from main import ma
from models.Book import Book


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book


book_schema = BookSchema()
books_schema = BookSchema(many=True)
