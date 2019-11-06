import sqlite3 as sq

conn = sq.connect('database.db')
cur = conn.cursor()
cur.execute('SELECT * FROM users ORDER BY lname')
users = cur.fetchall()
for u in users:
    print(f'{u[1]} {u[2]}')