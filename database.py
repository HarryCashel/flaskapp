from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv()


def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"""postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:5432/{os.getenv("DB_NAME")}"""
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db


# import psycopg2
# import os
# from dotenv import load_dotenv
#
# connection = psycopg2.connect(
#     database=os.getenv("DB_NAME"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     host=os.getenv("DB_HOST")
# )
#
# cursor = connection.cursor()
#
# cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
# connection.commit()
