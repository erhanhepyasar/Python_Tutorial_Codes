import sqlite3 as lit

db = lit.connect('employee.db')

with db:
    cur = db.cursor()
    selectQuery = "SELECT * FROM users"
    cur.execute(selectQuery)
    rows = cur.fetchall()

    for data in rows:
        print(data)