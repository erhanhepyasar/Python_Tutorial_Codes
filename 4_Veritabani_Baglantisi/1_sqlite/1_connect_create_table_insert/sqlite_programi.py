import sqlite3

# "dersler.db" adlı db yoksa oluşur varsa bağlantı yapılır
con = sqlite3.connect("dersler.db")

#sql sorgularını çalıştırabilmek için bir cursor oluşturuyoruz
cursor = con.cursor()


def tabloOlustur():
    # ogrenciler tablosu yoksa oluştur
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT, soyad TEXT, numara INT, notu INT)")



def degerEkle():
    cursor.execute("INSERT INTO ogrenciler VALUES ('Hasan', 'Yilmaz', 1234, 86)")

#Bu metod çağırılınca "dersler.db" dosyası oluşur
# "db browser for sqlite" programı ile SQLite veritabanı içeriğine bakılabilir
tabloOlustur()
degerEkle()
con.commit() # sorgu sonucunun DB de kalici hale gelmesi için
con.close()

