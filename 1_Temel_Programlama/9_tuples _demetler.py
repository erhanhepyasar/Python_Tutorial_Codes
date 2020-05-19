##############################################################
# tuple tanımlama
##############################################################

# normal parantez ile tanımlama
# demet = ("ahmet", "mehmet", 23, 45)
# print(demet)
# print(type(demet))

# parantezsiz tanımlama
# demet = "ahmet", "mehmet", 23, 45
# print(demet)
# print(type(demet))

# tuple() metodu ile tanımlama
# t = tuple('abcdefg')
# print(t)

# tuple() ile listeyi tuple a dönüştürme
# liste = ["ahmet", "mehmet", 34, 45]
# print(type(liste))
# print(liste)
# t = tuple(liste)
# print(type(t))
# print(t)

# tuple elemanlarına erişmek
# demet = ('elma', 'armut', 'kiraz')
# print(demet[0])
# print(demet[-1])
# print(demet[:2])

# tek elemanlı bir demet oluşturmak
# demet = ('ahmet') # yanlış yöntem, aslında karakter dizisi oluşur
# print(type(demet)) # str
#
# demet = ('ahmet', ) # doğru yöntem, ',' koymak gerekir
# print(type(demet)) # tuple

# demetler immutable dır yani değiştirilemez
# ancak yeni bir demete kaydedilebilir
# demet = ('elma', 'armut', 'kiraz')
# demet[0] = 'karpuz' #TypeError

# demete eleman ekleme (immutable)
# demet = ('ahmet', 'mehmet')
# demet = demet + ('selin',) # tek elemanlı ise sonuna ',' koyularak karakter dizisi oluşması önlenir
# print(demet)

#########################################################
# DEMETLERİN (TUPLES) METODLARI
#########################################################
# sadece index() ve count() var
# çünkü immutable olduğundan değiştirme metodları yok
# metodlar = dir(tuple)
# for metod in metodlar:
#     if not metod.startswith("__") and not metod.endswith("__"):
#         print(metod)


################################################################
# index() ile elemanın index ini öğrenme
################################################################
# demet = ("elma", "armut", "çilek")
# print(demet.index("armut"))

################################################################
# count() ile elemanın listede kaç kez yer aldığını öğrenme
################################################################
demet = ("elma", "armut", "elma", "çilek")
print(demet.count("elma"))





