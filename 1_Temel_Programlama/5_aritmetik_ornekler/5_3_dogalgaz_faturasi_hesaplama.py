#Her bir ayın kaç gün çektiğini tanımlıyoruz
ocak = mart = mayis = temmuz = agustos = ekim = aralik = 31
nisan = haziran = eylul = kasim = 30
subat = 28

#Doğalgazın vergiler dahil metreküp fiyatı
birimFiyat = 0.79

#Kullanıcı ayda ne kadar doğalgaz tüketmiş?
aylikSarfiyat = input("Aylık doğalgaz sarfiyatınızı metreküp olarak giriniz: ")

#Kullanıcı hangi aya ait faturasını öğrenmek istiyor?
donem = input("""Hangi aya ait faturayı hesaplamak istersiniz?
(Lütfen ay adını tamamı küçük harf olacak şekilde giriniz)\n""")

#Yukarıdaki input() fonksiyonundan gelen veriyi
#Python'ın anlayabileceği bir biçime dönüştürüyoruz
ay = eval(donem)

#Kullanıcının günlük doğalgaz sarfiyatı
günlükSarfiyat = int(aylikSarfiyat) / ay

#Fatura tutarı
fatura = birimFiyat * günlükSarfiyat * ay
print("günlük sarfiyatınız: \t", günlükSarfiyat, " metreküp\n",
"tahmini fatura tutarı: \t", fatura, " TL", sep="")