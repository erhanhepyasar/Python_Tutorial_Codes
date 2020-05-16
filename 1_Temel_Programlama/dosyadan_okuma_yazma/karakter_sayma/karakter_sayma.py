hakkinda = open("hakkinda.txt", encoding="utf-8")
harf = input("Sorgulamak istediğiniz harf: ")

sayi = 0
for karakter_dizisi in hakkinda:
    for karakter in karakter_dizisi:
        if harf == karakter:
         sayi += 1

print(harf, "harfinden", sayi, "adet bulundu.")
hakkinda.close()