while True:
    sayı = int(input("Bir sayı girin: "))
    if sayı == 0:
        print("0 girildi. Çıkılacak")
        break
    elif sayı < 0:
        print("Negatif sayı girildi. Devam edilecek.")
        pass
    else:
        print("Pozitif sayı girildi. Ekrana yazılacak")
        print(sayı)