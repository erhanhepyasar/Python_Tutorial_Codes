import datetime

# Şu anki tarih - saat bilgisini alma
x = datetime.datetime.now()

print(x)
print("Yıl:",x.year)

# formatlama:
print("Gün:",x.strftime("%A")) # Gün
print("Ay:",x.strftime("%B")) # Ay

# Tüm format listesi:
# https://www.w3schools.com/python/python_datetime.asp

# Kendimiz tarih belirleme
x = datetime.datetime(2020, 5, 17)

print(x)