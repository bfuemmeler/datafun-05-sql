"""Python script to create a new SQLite database, create tables, and insert data from CSV files."""

import sqlite3
import pandas as pd
import pathlib
from utils_logger import logger

db_file = pathlib.Path("db.sqlite")

def create_db():
    """Create a new SQLite database. If the file doesn't exist, it will be created.
    Close the connection to the database when done."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        logger.info(f"Database created: {db_file}")
    except sqlite3.Error as e:
        logger.error("Error creating database:", e)


def drop_tables():
    """Function that reads and executes SQL statements to drop tables."""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("datafun-05-sql", "sql_create", "01_drop_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logger.info("Tables dropped")
    except sqlite3.Error as e:
        logger.error("Error dropping tables:", e)


def create_tables():
    """Read and execute SQL statements to create tables."""
    # Drop tables first
    drop_tables()
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("datafun-05-sql", "sql_create", "02_create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logger.info("Tables created")
    except sqlite3.Error as e:
        logger.error("Error creating tables:", e)


def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("datafun-05-sql", "data", "authors.csv")
        book_data_path = pathlib.Path("datafun-05-sql", "data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # Use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)


def main():
    create_db()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()