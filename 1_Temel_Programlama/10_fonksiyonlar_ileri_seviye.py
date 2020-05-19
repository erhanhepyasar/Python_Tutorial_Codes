############################################################
# 1. LAMBDA FONKSİYONLARI
############################################################
# fonk = lambda param1, param2: param1 + param2
# sonuc = fonk(2, 4)
# print(sonuc)

############################################################
# Örnek: Sayı çift mi?
############################################################
# Normal fonksiyon ile
# def cift_mi(sayı):
#     return sayı % 2 == 0
# print(cift_mi(100))

# Lambda fonksiyon ile
# l_cift_mi = lambda sayi: sayi % 2 == 0
# print(l_cift_mi(5))

############################################################
# Örnek: Listedeki sayıların karesini bulma
############################################################
# l = [2, 5, 10, 23, 3, 6]
# l_kare = lambda sayi: pow(sayi, 2)
# for i in l:
#     print(l_kare(i))

############################################################
# Örnek: Grafik arayüz işlemleri
############################################################
# import tkinter
# import tkinter.ttk as ttk
#
# pen = tkinter.Tk()
#
# # command parametresine doğrudan lambda fonksiyonu veriliyor,
# # ayrıca başka bir yerde normal fonksiyon tanımlamaya gerek kalmıyor
# btn1 = ttk.Button(text='SELAMLA !', command=lambda: print('Merhaba arkadaslar !!'))
# btn2 = ttk.Button(text='ISLEM YAP', command=lambda: print('Islem yapildi '))
# btn1.pack(padx=200, pady=20)
# btn2.pack(padx=0, pady=20)
#
# pen.mainloop()


############################################################
# 2. ÖZYİNELEMELİ (RECURSIVE) FONKSİYONLAR
############################################################

############################################################
# Örnek: Karakter azaltma
############################################################
# def azalt(s):
#     if len(s) < 1: #dip nokta
#         return s
#     else:
#         print(s)
#         return azalt(s[1:]) #recursion: ikinci karakterden itibaren alıyoruz
#
# print(azalt('0123456789'))

############################################################
# Örnek: Recursion ı anlamak
############################################################
# def azalt(s):
#     if len(s) < 1:
#         return s
#     else:
#         print('özyineleme sürecine girerken:', s)
#         azalt(s[1:])
#         print('özyineleme sürecinden çıkarken:', s)
#
# azalt('python programlama')


############################################################
# Örnek: Metni ters çevirme
############################################################
# def ters_cevir(s):
#     if len(s) < 1: # dip nokta
#         return s
#     else:
#         ters_cevir(s[1:])
#         print(s[0])
#
# ters_cevir('python')

# Özyinelemeli fonksiyonlar, özyineleme sürecine girerken yaptıgı isi, özyineleme
# sürecinden çıkarken tersine çevirir. Iste biz de bu özellikten yararlandık.
# Fonksiyonun kendini yineledigi noktanın çıkısına bir print() fonksiyonu yerlestirip,
# geri dönen karakterlerin ilk har1ni ekrana bastık. Böylece s adlı parametrenin
# tersini elde etmis olduk.

############################################################
# Örnek: Sayaç
############################################################
# def sayac(sayi, limit):
#     print(sayi)
#     if sayi == limit: # dip nokta, sonlandırma
#         print('son!')
#     else:
#         return sayac(sayi - 1, limit) # recursion
#
# sayac(10, 0)