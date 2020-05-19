# otomobilListesi = ["bmw", "mercedes", "ferrari"]
# print(otomobilListesi)
# print(type(otomobilListesi))

# Birden fazla veri tipi alabilir
# liste = ["Ahmet", "Mehmet", 23, 65, 3.2]
# print(liste)

# liste içinde liste
# liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]
# print(liste)
# for eleman in liste:
#     print("{} adlı öğenin veri tipi: {}".format(eleman, type(eleman)))

# split() metodu da liste döner
# kardiz = "İstanbul Büyükşehir Belediyesi"
# print(kardiz.split())
# print(type(kardiz.split()))

# len() metodu ile listenin uzunluğunu öğrenme
# diller = ["İngilizce", "Fransızca", "Türkçe", "İtalyanca", "İspanyolca"]
# print(len(diller))
# print(diller[len(diller)-1])

# list() metodu ile listeye çevirme
# alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
# harf_listesi = list(alfabe)
# print(harf_listesi)

# list() metodu ile range fonksiyonu sayı aralığını ekrana basmak
# for i in range(10):
#     print(i)
# print(*range(10))
# print(list(range(10)))

# listelerin elemanlarına erişmek
# meyveler = ["elma", "armut", "çilek", "kiraz"]
# print(meyveler[0])
# print(meyveler[-1])
# print(meyveler[0:2])
# print(meyveler[::-1]) # listeyi tersine çevirmek
# for meyve in meyveler:
#     print(meyve)

# gömülü listenin elemanlarına erişmek
# liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]
# print(liste[2][1])
# yeni_liste = liste[2]
# print(yeni_liste)


# listenin elemanlarını değiştirmek
# renkler = ["kırmızı", "sarı", "mavi", "yeşil", "beyaz"]
# renkler[0] = "siyah"
# print(renkler)

# birden fazla elemanı bir kerede değiştirme
# liste = [1, 2, 3]
# liste[0:len(liste)] = 5, 6, 7
# print(liste)
# liste[:] = 10, 11, 12 # ilk ve son sıradakileri belirtmeye gerek yoktur
# print(liste)

#listeye eleman eklemek
# liste = [2, 4, 5, 7]
# liste + [8] # Eklenecek eleman da liste tipinde olmalıdır
# liste + 8 # TypeError
# print(liste)

# listeleri birleştirmek
# derlenen_diller = ["C", "C++", "C#", "Java"]
# yorumlanan_diller = ["Python", "Perl", "Ruby"]
# programlama_dilleri = derlenen_diller + yorumlanan_diller
# print(programlama_dilleri)

# del ile listeden eleman silmek
# liste = [1, 5, 3, 2, 9]
# del liste[1]
# print(liste)

# del ile listeyi tamamen silme
# liste = [1, 5, 3, 2, 9]
# del liste
# print(liste)

# liste kopyalamak
# adres atanırsa aynı listeyi gosterirler
# li1 = ["elma", "armut", "erik"]
# li2 = li1
# print(li1)
# print(li2)
# li1[0] = "xxxxx"
# print(li1) # ikisi de değişti çünkü aslında ikisi aynı tek bir liste
# print(li2)
# print(id(li1)) #adresler aynı
# print(id(li2))

# list() metodu ile liste farklı bir adrese kopyalanabilir
# liste1 = ["ahmet", "mehmet", "özlem"]
# liste2 = list(liste1)
# print(liste1)
# print(liste2)
# liste1[0] = "--------"
# print(liste1) # sadece biri değişti çünkü ikisi de farklı adreslerde tutulan listeler
# print(liste2)
# print(id(liste1)) # farklı adresler
# print(id(liste2))

# liste üreteçleri (list comprehensions)
# liste = [i for i in range(15)]
# print(liste)
#
# liste = list(range(20))
# print(liste)
#
# liste = [i for i in range(50) if i % 2 == 0]
# print(liste)

################################################################
# LİSTELERİN METODLARI
################################################################

################################################################
# append() ile sona eleman eklemek
################################################################
# liste = ["elma", "armut", "çilek"]
# liste.append("erik")
# print(liste)

################################################################
# extend() ile listeyi genişletmek
################################################################
# li1 = [1, 3, 4]
# li2 = [10, 11, 12]
# li1. append(li2) # listenin içine liste olarak ekliyor
# print(li1)
#
# li1 = [1, 3, 4]
# li2 = [10, 11, 12]
# li1. extend(li2) # listeyi genişleterek eleman olarak ekliyor
# print(li1)

################################################################
# insert() ile liste içinde istenen konuma ekleme
################################################################
# liste = ["elma", "armut", "çilek"]
# liste.insert(2, "xxxx")
# print(liste)

################################################################
# remove() ile istenen elemanı silme
################################################################
# liste = ["elma", "armut", "çilek"]
# liste.remove("elma")
# print(liste)

################################################################
# pop() ile elemanı silme ve sildiği elemanın değerini döndürme
################################################################
# liste = ["elma", "armut", "çilek", "kayisi", "karpuz"]
# print(liste.pop())
# print(liste.pop(1))

################################################################
# reverse() ile listeyi tersine çevirme
################################################################
# liste = ["elma", "armut", "çilek"]
# liste.reverse()
# print(liste)

################################################################
#reversed() ile listeyi tersine çevirme
################################################################
# isimler = ['ahmet', 'mehmet', 'veli', 'ayşe', 'çiğdem', 'ışık']
# print(list(reversed(isimler)))

################################################################
# sort() ile sıralama
################################################################
# uyeler = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep',
# 'Abdullah', 'Kadir', 'Kemal', 'Kamil', 'Selin', 'Senem',
# 'Sinem', 'Tayfun', 'Tuna', 'Tolga']
# uyeler.sort()
# print(uyeler)
# uyeler.sort(reverse=True)
# print(uyeler)

# sayilar = [1, 0, -1, 4, 10, 3, 6]
# sayilar.sort()
# print(sayilar)
# sayilar.sort(reverse=True)
# print(sayilar)


################################################################
# sorted() ile sıralama
################################################################
# print(sorted(('elma', 'armut', 'kiraz', 'badem')))
# isimler = ['ahmet', 'çiğdem', 'ışık', 'şebnem', 'zeynep', 'selin']
# print(sorted(isimler))


################################################################
# index() ile elemanın index ini öğrenme
################################################################
# liste = ["elma", "armut", "çilek"]
# print(liste.index("elma"))

################################################################
# count() ile bir elemanın listede kaç kez yer aldığını öğrenme
################################################################
# liste = ["elma", "armut", "elma", "çilek"]
# print(liste.count("elma"))

################################################################
# copy() ile liste kopyalamak
################################################################
# liste1 = ["ahmet", "mehmet", "özlem"]
# liste2 = liste1.copy()
# print(liste1)
# print(liste2)

# liste1[0] = "xxxxx"
# print(liste1)
# print(liste2)

# print(id(liste1)) # farklı id ler
# print(id(liste2))

################################################################
# clear() ile listenin içeriğini silme
################################################################
# liste = [1, 2, 3, 5, 10, 20, 30, 45]
# liste.clear()
# print(liste)






