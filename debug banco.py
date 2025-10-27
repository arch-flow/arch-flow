import sqlite3

conn = sqlite3.connect("./data/db/archflow.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", [t[0] for t in tables])

for table in tables:
    print(f"\n== Schema: {table[0]} ==")
    for row in cursor.execute(f"PRAGMA table_info({table[0]});"):
        print(row)

conn.close()
