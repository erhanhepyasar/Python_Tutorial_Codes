
########################################################################
# Örnek: Yanlış veri girişi
########################################################################
# Hata-1: Kullanıcı sayı yerine harf girebilir (ValueError)
# Hata-2: Kullanıcı ikinci sayıyı 0 girebilir  (ZeroDivisionError)
########################################################################
# ilk_sayi = input("ilk sayı: ")
# ikinci_sayi = input("ikinci sayı: ")
# ilk_sayi = int(ilk_sayi)
# ikinci_sayi = int(ikinci_sayi)
# print(ilk_sayi, "/", ikinci_sayi, "=", ilk_sayi / ikinci_sayi)

########################################################################
# Hata Yönetimi (try... except... as...)
########################################################################
# while True:
#     ilk_sayi = input("ilk sayı (Programdan çıkmak için q tuşuna basın): ")
#
#     if ilk_sayi == "q":
#       break
#     ikinci_sayi = input("ikinci sayı: ")
#
#     try:
#         ilk_sayi = int(ilk_sayi)
#         ikinci_sayi = int(ikinci_sayi)
#         print(ilk_sayi, "/", ikinci_sayi, "=", ilk_sayi / ikinci_sayi)
#     except ValueError:
#         print("Sadece sayı giriniz.")
#     except ZeroDivisionError:
#         print("Bir sayı 0'a bölünemez")
    # except (ValueError, ZeroDivisionError) as hata:  # tüm hatalar için aynı işlem
    #     print("Bir hata oluştu!: ", hata)



########################################################################
# Hata Yönetimi (try... except... else...) - hatalara göre bölümlere ayırmak
########################################################################
# while True:
#     ilk_sayi = input("ilk sayı (Programdan çıkmak için q tuşuna basın): ")
#
#     if ilk_sayi == "q":
#       break
#     ikinci_sayi = input("ikinci sayı: ")
#
#     try: # Burada sadece sayı tipi hatası yönetiliyor
#         ilk_sayi = int(ilk_sayi)
#         ikinci_sayi = int(ikinci_sayi)
#     except ValueError:
#         print("Sadece sayı giriniz.")
#     else:
#         try: # Burada sadece 0'a bölme hatası yönetiliyor
#             print(ilk_sayi, "/", ikinci_sayi, "=", ilk_sayi / ikinci_sayi)
#         except ZeroDivisionError:
#             print("Bir sayı 0'a bölünemez")


########################################################################
# Hata Yönetimi (try... except... finally...) - her durumda çaılşacak kısım
########################################################################
# Dosya işlemlerinde, hata olsa da olmasa da, açılan dosya kapatılmalıdır
# try:
#     dosya = open("dosyaadı", "r")
#     # dosyaya yazma işlemleri
# except IOError:
#     print("bir hata oluştu!")
# finally:
#     dosya.close()


########################################################################
# Hata Yönetimi (raise...) - Duruma özgü hata mesajı
########################################################################
# bolunen = int(input("bölünecek sayı: "))
#
# if bolunen == 15:
#     raise Exception("15 sayısını girmeyiniz")
#
# bolen = int(input("bölen sayı: "))
# print(bolunen / bolen)

