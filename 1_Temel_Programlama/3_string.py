# language = "python"
# print(language)

###################################################
# len() fonksiyonu
###################################################
# print(len(language))
# print(len("Merhaba Python"))


###################################################
# type() fonksiyonu
###################################################
# print(type(language))


###################################################
# string birleştirme (concatenate)
###################################################
# language = "python" + " programlama" + " dili"
# print(language)



###################################################
# string = karakterler dizisi
###################################################
# metin = "selam"
# print(metin[1])

# Bir karakter dizisinin uzunlugunun 1 eksigi, o karakter dizisinin son ögesini verir.
# print(metin(5)) # error
# print(metin[len(metin)]) # error
# print(metin[len(metin) - 1])

# tersten sayma
# print(metin[-1])
# print(metin[-6]) #error




###################################################
# dilimleme
###################################################
# karakter_dizisi = "istanbul"
# print(karakter_dizisi[0:3])
# print(karakter_dizisi[2:])
# print(karakter_dizisi[:4])

#karakter_dizisi[ilk_karakter:son_karakter:atlama_sayısı]
# print(karakter_dizisi[2:8:2])
#print(karakter_dizisi[::-1]) # ters çevirme




###################################################
# sort() ile sıralama
###################################################
# print(sorted("kitap"))
# print(*sorted("kitap"), sep=" > ")




###################################################
# replace() ile değiştirme
###################################################
# kardiz = "elma"
# yeni_kardiz = kardiz.replace("e", "E")
# print(kardiz)
# print(yeni_kardiz)

# kardiz = "memleket"
# yeni_kardiz = kardiz.replace("e", "") # 1. parametre: mevcut metin  2.parametre: yeni metin
# print(yeni_kardiz)
#
# yeni_kardiz = kardiz.replace("e", "", 2) # 3.parametre: kaç tane değiştireceği
# print(yeni_kardiz)




###################################################
# split() ile dilimleme
###################################################
# kardiz = "İstanbul Büyükşehir Belediyesi"
# print(kardiz.split())
# print(*kardiz.split(), sep=", ")

# metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
# tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
# Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
# düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
# gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
# komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
# adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
# dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
# halini almıştır diyebiliriz."""
# print(metin.splitlines())
# print(*metin.splitlines(), sep="\n")




###################################################
# partition() ile üçe bölme
###################################################
# a = "istanbul"
# print(a.partition("an"))



###################################################
# lower() ve upper()
###################################################
# metin = "Pyhton Programlama Dili"
# print(metin.lower())
# print(metin.upper())

# print("merhaba".islower())
# print("MERHABA".isupper())
# print("mERHABA".isupper()) # hepsi true olursa sonuç true olur
# print(metin.islower())
# print(metin.isupper())




###################################################
# capitalize() ve title() ile ilk harfleri büyütme
###################################################
# metin = "pyhton programlama dili"
# print(metin.capitalize()) # sadece ilk harf
# print(metin.title())  # tüm kelimelerin ilk harfleri




###################################################
# swapcase() ile harfleri tersine çevirme
###################################################
# metin = "Pyhton Programlama Dili"
# print(metin.swapcase())




###################################################
# startswith() ve endswith() ile kontrol etme
###################################################
# kardiz = "istanbul"
# print(kardiz.startswith("i"))
# print(kardiz.endswith("ul"))




###################################################
# strip(), lstrip(), rstrip() ile gereksiz boşlukları silme
###################################################
# kardiz = " istanbul "
# print(kardiz)
# print(kardiz.strip())
# print(kardiz.lstrip())
# print(kardiz.rstrip())

# kardiz = "istanbul"
# print(kardiz.strip("i"))


###################################################
# count() ile istenen karakteri sayma
###################################################
# sehir = "Kahramanmaras"
# print(sehir.count("a"))

# kardiz = "python programlama dili"
# print(kardiz.count("a", 15, 17))  # 15 ile 17 arası ara



###################################################
# index() ile karakterin index ini öğrenme
###################################################
# kardiz = "python"
# print(kardiz.index("p"))

# kardiz = "adana"
# print(kardiz.index("a", 3)) # kaçıncı karakterden itibaten arayacağı





###################################################
# isalpha(), isdigit() ve isalnum() ile harf-rakam kontrolü
###################################################
# a = "kezban"
# print(a.isalpha())

# b = "k3zb6n"
# print(b.isalpha())

# a = "12345"
# print(a.isdigit())
#
# b = "123445b"
# print(b.isdigit())

# a = "123abc"
# print(a.isalnum())

# b = "123abc>"
# print(b.isalnum())

###################################################
# isdecimal() ile ondalık sayı kontrolü
###################################################
# a = "123"
# print(a.isdecimal())
#
# a = "123.3"
# print(a.isdecimal())



###################################################
# format() ile biçimlendirme
###################################################
# print("{} ve {} iyi bir ikilidir!".format("Django", "Python"))