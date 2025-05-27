from lib.db.connection import get_connection

with open("lib/db/schema.sql") as f:
    schema = f.read()

conn = get_connection()
conn.executescript(schema)
conn.commit()
conn.close()
