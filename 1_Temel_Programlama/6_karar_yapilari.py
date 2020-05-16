# n = 15
# if n > 10:
#     print("sayı 10 dan büyüktür")



#diğer int() yöntemi
# sayı = input("Bir sayı giriniz: ")
# sayı = int(sayı)

#parola işlemleri
# print("Lütfen parolayı giriniz: ")
# parola = input("Parola: ")
# if parola == "1234":
#     print("Sisteme Hoşgeldiniz!")

# çoklu if yapısı (1 den fazla koşul çalışabilir, örnek negatif sayı)
# yaş = int(input("Yaşınız: "))
# if yaş == 18:
#     print("18 iyidir!")
# if yaş < 0:
#     print("Yok canım, daha neler!...")
# if yaş < 18:
#     print("Genç bir kardeşimizsin!")
# if yaş > 18:
#     print("Eh, artık yaş yavaş yavaş kemale eriyor!")

#if - elif (sadece 1 koşul çalışır)
# yaş = int(input("Yaşınız: "))
# if yaş == 18:
#     print("18 iyidir!")
# elif yaş < 0:
#     print("Yok canım, daha neler!...")
# elif yaş < 18:
#     print("Genç bir kardeşimizsin!")
# elif yaş > 18:
#     print("Eh, artık yaş yavaş yavaş kemale eriyor!")

# if - elif - else yapısı (diğer tüm durumlar)
# cevap = input("Bir meyve adı söyleyin bana:")
# if cevap == "elma":
#     print("evet, elma bir meyvedir...")
# elif cevap == "karpuz":
#     print("evet, karpuz bir meyvedir...")
# elif cevap == "armut":
#     print("evet, armut bir meyvedir...")
# else:
#     print(cevap, "gerçekten bir meyve midir?")

# and kullanımı
# kullanıcı_adı = input("Kullanıcı adınız: ")
# parola = input("Parolanız: ")
# if kullanıcı_adı == "ali" and parola == "1234":
#     print("Programa hoşgeldiniz")
# else:
#     print("Yanlış kullanıcı adı veya parola!")

# or kullanımı
# kullanıcı_adı = input("Kullanıcı adınız: ").lower()
# if kullanıcı_adı == "ali" or kullanıcı_adı == "veli":
#     print("Programa hoşgeldiniz")
# else:
#     print("Yanlış kullanıcı adı !")


# and, or ve if-elif-else birlikte kullanımı
# x = int(input("Notunuz: "))
# if x > 100 or x < 0:
#     print("Böyle bir not yok")
# elif x >= 90 and x <= 100:
#     print("A aldınız.")
# elif x >= 80 and x <= 89:
#     print("B aldınız.")
# elif x >= 70 and x <= 79:
#     print("C aldınız.")
# elif x >= 60 and x <= 69:
#     print("D aldınız.")
# elif x >= 0 and x <= 59:
#     print("F aldınız.")

# and yerine "a < x < b" gösterimi
# x = int(input("Notunuz: "))
# if x > 100 or x < 0:
#     print("Böyle bir not yok")
# elif 90 <= x <= 100:
#     print("A aldınız.")
# elif 80 <= x <= 89:
#     print("B aldınız.")
# elif 70 <= x <= 79:
#     print("C aldınız.")
# elif 60 <= x <= 69:
#     print("D aldınız.")
# elif 0 <= x <= 59:
#     print("F aldınız.")

