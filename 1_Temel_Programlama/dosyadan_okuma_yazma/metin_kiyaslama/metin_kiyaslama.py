# isimler1.txt dosyasındaki satırlar isimler2.txt dosyasında var mı kontrolü yapan program

d1 = open("isimler1.txt", encoding="utf-8") # dosyayı açıyoruz
d1_satırlar = d1.readlines() # satırları okuyoruz

d2 = open("isimler2.txt", encoding="utf-8")
d2_satırlar = d2.readlines()

for i in d1_satırlar:
    if not i in d2_satırlar:
        print(i)

d1.close()
d2.close()

# Eger Windows’ta Türkçe karakterleri hala düzgün görüntüleyemiyorsanız encoding
# parametresinde ‘utf-8’ yerine ‘cp1254’ adlı dil kodlamasını kullanmayı deneyebilirsiniz: