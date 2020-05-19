import sqlite3 as lit

def main():
    try:
        db = lit.connect('employee.db')
        print("Veritabanı oluşturuldu")

    except:
        print("Veritabani olusturma hatası")

    finally:
        db.close()

if __name__ == '__main__':
    main()
