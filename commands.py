from main import db
from flask import Blueprint

# Create a blueprint for cli commands
db_commands = Blueprint("db", __name__)


@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted!")