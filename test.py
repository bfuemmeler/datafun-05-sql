# Import from Python Standard Library first
import sqlite3
import pathlib

# Import from external packages
import pandas as pd

# Define paths using joinpath
db_file_path = pathlib.Path(r"C:/Projects/datafun-05-sql/data").resolve().joinpath("db.sqlite")
sql_file_path = pathlib.Path(r"C:/Projects/datafun-05-sql/sql").resolve().joinpath("create_tables.sql")
author_data_path = pathlib.Path("data").joinpath("authors.csv")
book_data_path = pathlib.Path("data").joinpath("books.csv")
