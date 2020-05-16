print("""
Basit bir hesap makinesi uygulaması.
İşleçler:
+ toplama
- çıkarma
* çarpma
/ bölme
Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")
izinli_karakterler = "0123456789+-/*= "
while True:
    islem_metni = input("İşleminiz: ")
    if islem_metni == "q":
        print("q ya basarak çıkış yaptınız")
        break
    for s in islem_metni:
        if s not in izinli_karakterler:
            print("İzinli olmayan karakter bulundu! Çıkılıyor.")
            quit() # programdan çıkar
    sonuc = eval(islem_metni) # verilen metni icra eder
    print("Sonuç: ", sonuc)

# izinli karakter listesi kullanılarak eval() ile tehlikeli işlem yapılması önlendi