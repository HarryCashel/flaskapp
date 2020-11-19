import psycopg2
import os
from dotenv import load_dotenv

connection = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST")
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()
