secenekler = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) karesini hesapla
(6) karekök hesapla
"""
print(secenekler)
secilenIslem = input("Yapmak istediğiniz işlemin numarasını girin: ")

if secilenIslem == "1":
    sayi1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
    sayi2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
    print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
elif secilenIslem == "2":
    sayi1 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
    sayi2 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
    print(sayi1, "-", sayi2, "=", sayi1 - sayi2)
elif secilenIslem == "3":
    sayi1 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
    sayi2 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
    print(sayi1, "x", sayi2, "=", sayi1 * sayi2)
elif secilenIslem == "4":
    sayi1 = int(input("Bölme işlemi için ilk sayıyı girin: "))
    sayi2 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
    print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
elif secilenIslem == "5":
    sayi1 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
    print(sayi1, "sayısının karesi =", sayi1 ** 2)
elif secilenIslem == "6":
    sayi1 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
    print(sayi1, "sayısının karekökü = ", sayi1 ** 0.5)
else:
    print("Yanlış giriş.")
    print("Aşağıdaki seçeneklerden birini giriniz:", secenekler)