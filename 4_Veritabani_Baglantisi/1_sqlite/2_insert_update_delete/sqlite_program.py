import sqlite3
import random
import time
import datetime


con = sqlite3.connect("dersler.db")

cursor = con.cursor()

def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 (zaman REAL, tarih TEXT, anahtarkelime TEXT, deger REAL)")
    print("----------- CREATE TABLE yapıldı ------------")

def rasgeleDegerEkle():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarKelime = "Python SQLite"
    deger = random.randrange(0, 10)
    cursor.execute("INSERT INTO Tablo1 (zaman, tarih, anahtarkelime, deger) VALUES(?, ?, ?, ?)", (zaman, tarih, anahtarKelime, deger))
    print("--------- INSERT yapıldı ---------")

def degerleriAl(sqlText):
    cursor.execute(sqlText)
    data = cursor.fetchall()
    for i in data:
        print(i)

def guncelle():
    cursor.execute("UPDATE Tablo1 SET deger = 15 WHERE deger = 12,")
    print("----------- UPDATE yapıldı -----------------")

def sil():
    cursor.execute("DELETE FROM Tablo1 WHERE deger = 0")
    print("----------- DELETE yapıldı -----------------")
#########################################################
# Tablo Oluşturma
#########################################################
# tabloOlustur()

#########################################################
# INSERT ile veri girişi yapma (Rasgele 10 deger ekleme)
#########################################################
# for i in range(0,10):
#     rasgeleDegerEkle()
#     time.sleep(1) # 1 saniye bekleyelim ki INSERT ile yazdigimiz zaman bilgisi değissin

#########################################################
# SELECT Sorguları
#########################################################
# sqlText = "SELECT anahtarKelime, deger FROM Tablo1"
# sqlText = "SELECT * FROM Tablo1"
# sqlText = "SELECT * FROM Tablo1 WHERE deger = 9.0"
# degerleriAl(sqlText)

#########################################################
# UPDATE ile güncelle
#########################################################
# degerleriAl(sqlText)
# guncelle()
# degerleriAl(sqlText)

#########################################################
# DELETE ile sil
#########################################################
# degerleriAl(sqlText)
# sil()
# degerleriAl(sqlText)

#########################################################
# db de kalıcı hale getir ve bağlantıyı kapat
#########################################################
con.commit()
con.close()