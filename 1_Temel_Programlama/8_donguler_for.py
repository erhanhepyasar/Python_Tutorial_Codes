# metin = "python programlama eğitimi"
# for karakter in metin:
#     print(karakter)

# sayilar = "123456789"
# for sayi in sayilar:
#     print(int(sayi) * 2)

#############################################
# for ile if birlikte kullanımı
#############################################
# sayılar = "123456789"
# for i in sayılar:
#     if int(i) > 3:
#         print(i)

# Örnek
# tr_harfler = "şçöğüİı"
# parola = input("Parolanız: ")
# for karakter in parola:
#     if karakter in tr_harfler:
#         print("parolada Türkçe karakter kullanılamaz: ", karakter)


#############################################
# range kullanımı
#############################################
# 0 dahil, 10 hariç
# for i in range(0, 10):
#     print(i)

#0 dan başlayınca yazmaya gerek yok
# for i in range(10):
#     print(i)

# range örnek
# sayilar = "123456789"
# for i in range(7):
#     print(sayilar[i])

# range örnek
# isim = input("isminiz: ")
# for i in range(len(isim)):
#     print("isminizin {}. harfi: {}".format(i + 1, isim[i]))

# range in if içinde kullanımı
# while True:
#     print("En az 3 en fazla 8 karakterlik bir parola belirleyin.")
#     parola = input("Parola: ")
#     if not parola:
#         print("parola bölümü boş geçilemez!")
#     elif len(parola) in range(3, 9): #eğer parolanın uzunluğu 3 ile 8 karakter
#         #aralığında ise...
#         print("Yeni parolanız", parola)
#         break
#     else:
#         print("parola en az 3 en fazla 8 karakter olmalı")


# atlama değeri ile range kullanımı
# for i in range(0, 10, 2):
#     print(i)

# sondan başa doğru range kullanımı
# for i in range(10, 0, -1):
#     print(i)

# print() içinde range kullanımı
# print(*range(10))
# print(*range(10), sep=", ")

###################################################
# dir() ile fonksiyonları listeleme
###################################################
# print(*dir(str), sep="\n")
# print(*dir(int), sep="\n")
# print(*dir(float), sep="\n")

# Metot listesi içinde bizim kullanacağımız basında veya sonunda _ isareti olmayanlardır
# for i in dir(""):
#     if "_" not in i[0]:
#         print(i)