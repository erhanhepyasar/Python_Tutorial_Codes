# metin = "python programlama eğitimi"
# for karakter in metin:
#     print(karakter)

# sayilar = "123456789"
# for sayi in sayilar:
#     print(int(sayi) * 2)

# for i in range(7):
#     print(sayilar[i])

# isim = input("isminiz: ")
# for i in range(len(isim)):
#     print("isminizin {}. harfi: {}".format(i + 1, isim[i]))


###################################################
# dir() ile fonksiyonları listeleme
###################################################
# print(*dir(str), sep="\n")
# print(*dir(int), sep="\n")
# print(*dir(float), sep="\n")
# Metot listesi içinde bizi ilgilendirenler basında veya sonunda _ isareti olmayanlardır
for i in dir(""):
    if "_" not in i[0]:
        print(i)