# Import from Python Standard Library first
import sqlite3

conn = sqlite3.connect(r"C:\Projects\datafun-05-sql\data\db.sqlite")
cursor = conn.cursor()

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()