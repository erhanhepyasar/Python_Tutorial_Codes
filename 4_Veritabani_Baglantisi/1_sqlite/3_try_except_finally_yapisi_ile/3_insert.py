import sqlite3 as lit

myUsers = (
    (1, 'Parwiz', 'par@gmail.com'),
    (2, 'John', 'john@gmail.com'),
    (3, 'Tom', 'tom@gmail.com'),
    (4, 'Bob', 'bob@gmail.com'),
)

db = lit.connect('employee.db')

with db:
    cur = db.cursor()
    cur.executemany('INSERT INTO users VALUES (?,?,?)', myUsers)

    print("INSERT işlemi yapıldı")

# with, try a göre daha temiz bir yapı.
# close() işlemini kendi yönetiyor