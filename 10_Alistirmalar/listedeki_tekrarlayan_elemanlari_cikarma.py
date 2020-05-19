mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

# Açıklama:
# dict veri tipi tekrar içermediği için kendisine verilen listedeki
# tekrarları otomatik olarak çıkarır