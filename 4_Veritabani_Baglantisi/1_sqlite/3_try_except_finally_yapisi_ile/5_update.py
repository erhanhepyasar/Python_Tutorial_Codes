import sqlite3 as lit

db = lit.connect('employee.db')

with db:
    newName = "David"
    userId = 1
    cur = db.cursor()
    cur.execute("UPDATE users SET name = ? WHERE id = ?", (newName, userId))
    db.commit()
    print("UPDATE işlemi başarılı bir şekilde yapıldı")