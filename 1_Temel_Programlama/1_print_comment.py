###########################################
# 1.   print() fonksiyonu
###########################################
# print("Merhaba Python")
# print("Python" + "programlama" + "dersi")
# print("Python", "programlama", "dersi", 2020)
# print("Python", "programlama", "dersi", 2020, sep="-")  # default: sep=" "
# print("Merhaba " * 5)
# print("birinci satır\nikinci satır\nüçüncü satır")  # '\n' newline karakteri
# print("Bugün günlerden Salı", end=".\n") # default: end="\n"
# print(*"Galatasaray") # * : karakterlere ayırma
# print(*"Galatasaray", sep=", ")
# print(*"TBMM", sep=".")
# print(*"abcdefghijklmnopqrstuvwxyz", sep="/")

###########################################
# 2. Satırı yoruma çevirme
###########################################
# ALTGR + 3  : Tek satır
# CTRL + /   : Tek ya da çok satır  (PyCharm)

###########################################
# 3. Tırnak kullanımı
###########################################
# print('Python programlama dili')          #Tek tırnak
# print("Python programlama dili")          #Çift tırnak
# print("""Python programlama dili""")      #3 tane çift tırnak

# Tek tırnak örnek
# print("Python programlama dilinin adı "piton" yılanından gelmez")
# print('Python programlama dilinin adı "piton" yılanından gelmez')

# Çift tırnak örnek
# print('İstanbul'un 5 günlük hava durumu tahmini')
# print("İstanbul'un 5 günlük hava durumu tahmini")

# 3 tane çift tırnak örnek
# print("""Python programlama dilinin adı "piton" yılanından gelmez. İstanbul'un 5 günlük hava durumu tahmini""")

# print("""
#          [P]=========PYTHON========[-][o][x]
#          |                                 |
#          |    Programa Hoşgeldiniz!        |
#          |    Sürüm 2.1                    |
#          |    Devam etmek için herhangi    |
#          |    bir tuşa basın.              |
#          |                                 |
#          |=================================|
# """)

###########################################
# ÖRNEK PROGRAM: Aylık yol masrafı hesaplama
###########################################
# 1. Ayda 22 gün çalısıyoruz. (Cumartesi-Pazar günleri çalışmıyoruz)
# 2. Evden ise gitmek: 4 TL
# 3. Isten eve dönmek: 3.5 TL



# Matematiksel Formül:
# masraf = gün sayısı x (gidiş ücreti + dönüş ücreti)

# Program Kısım-1: Hesaplama
# gun = 22
# gidisUcreti = 4
# donusUcreti = 3.5
# masraf = gun * (gidisUcreti + donusUcreti)

# Program Kısım-2: Ekrana yazdırma - basit versiyon
# print(masraf)

# Program Kısım-2: Ekrana yazdırma - detaylı versiyon
# print("-" * 35)
# print("çalışılan gün sayısı\t:", gun)
# print("işe gidiş ücreti\t\t:", gidisUcreti)
# print("işten dönüş ücreti\t\t:", donusUcreti)
# print("-" * 35)
# print("AYLIK YOL MASRAFI\t\t:", masraf)
# print("AYLIK YOL MASRAFI\t\t:", 22 * (4 + 3.5))
# print("-" * 35)