import sqlite3 as lit

def main():
    try:
        db = lit.connect('employee.db')
        cur = db.cursor()

        tablequery = "CREATE TABLE users (id INT, name TEXT, email TEXT)"

        cur.execute(tablequery)
        print("Tablo başarıyla oluşturuldu")

    except:
        print("Tablo oluşturulamadı !")

    finally:
        db.close()

if __name__ == '__main__':
    main()