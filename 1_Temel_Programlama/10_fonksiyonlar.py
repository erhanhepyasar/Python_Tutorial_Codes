########################################################
# Fonksiyon tanımlama ve kullanma
########################################################
# def selamla():
#     print("Hello World!")

# selamla()



########################################################
# Sistem Bilgilerini Gösteren Fonksiyon
########################################################
# def sistem_bilgisi_goster():
#     import sys
#     print("\nSistemde kurulu Python'ın;")
#     print("\tana sürüm numarası:", sys.version_info.major)
#     print("\talt sürüm numarası:", sys.version_info.minor)
#     print("\tminik sürüm numarası:", sys.version_info.micro)
#     print("\nKullanılan işletim sisteminin;")
#     print("\tadı:", sys.platform)
#
# sistem_bilgisi_goster()

########################################################
# Parametre Alan Fonksiyon
########################################################
# ÖRNEK: KARESİNİ BULMA
# def kare_bul(i):
#     cikti = "{} sayısının karesi {} sayısıdır"
#     print(cikti.format(i, i**2))
#
# kare_bul(5)
# kare_bul(9)
# kare_bul(10)

# ÖRNEK: KAYIT OLUŞTURMA
# def kayit_olustur(isim, soyisim, isletimSistemi, sehir):
#     print("-"*30)
#     print("isim : ", isim)
#     print("soyisim : ", soyisim)
#     print("işletim sistemi: ", isletimSistemi)
#     print("şehir : ", sehir)
#     print("-"*30)
#
# kayit_olustur("Fırat", "Özgül", "Ubuntu", "İstanbul")
# kayit_olustur("Mehmet", "Öztaban", "Debian", "Ankara")
#
# # Isimli Parametreler istenen sırada yazılabilir:
# kayit_olustur(soyisim="Öz", isim="Ahmet", isletimSistemi="Debian", sehir= "Ankara")

########################################################
# Varsayılan Değerli Fonksiyon
########################################################
# def kaydet(isim="Ahmet Yilmaz"):
#     print("{} isimli kayit olusturuldu!".format(isim))
#
# kaydet() # Varsayılan değer kullanılır
# kaydet("Hasan Bulut")


########################################################
# Sınırsız Sayıda Parametre Alan Fonksiyon
########################################################
# Ornek:
# def fonksiyon(*parametreler):
#     print(parametreler)
#
# fonksiyon(1, 2, 3)
# fonksiyon(1, 2, 3, 4, 5, 6, 7, 8, 9)

# Ornek:
# def carp(*sayilar):
#     sonuc = 1
#     for i in sayilar:
#         sonuc *= i
#     print(sonuc)
#
# carp(1, 2, 3)
# carp(1, 2, 3, 5, 10, 2)

########################################################
# Değer Döndüren Fonksiyon
########################################################
# def ismin_ne():
#     isim = input("ismin ne? ")
#     return isim
#
# girilenIsim = ismin_ne()
# print("Girilen isim: ", girilenIsim)