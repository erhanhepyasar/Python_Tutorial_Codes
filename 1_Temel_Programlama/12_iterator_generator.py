######################################################################
#       ITERATOR
######################################################################
# # liste tanımla
# my_list = [4, 7, 0, 3]
#
# # iter() fonksiyonunu kullanarak bir iterator al
# my_iter = iter(my_list)
#
# ## next() fonksiyonunu kullanarak elemanlar üzerinde iterate et
# print(next(my_iter)) # 4
# print(next(my_iter)) # 7
#
# ## next(obj) ile  obj.__next__()  aynıdır
# print(my_iter.__next__()) # 0
# print(my_iter.__next__()) # 3
#
# ## Hiç eleman kalmadığı için StopIteration hatası raise eder:
# next(my_iter)

###########################################################################
# for döngüsü ile daha kolay bir şekilde iterate edilebilir
###########################################################################
# my_list = [4, 7, 0, 3]
# for element in my_list:
#     print(element)

###########################################################################
# Iterator implemente etmek
###########################################################################
# __iter__() ve __next__() metodları implemente edilerek yapılır
# class PowTwo:
#     """Class to implement an iterator
#     of powers of two"""
#
#     def __init__(self, max = 0):
#         self.max = max
#
#     def __iter__(self):  # zorunlu
#         self.n = 0
#         return self
#
#     def __next__(self): # zorunlu
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration  # zorunlu

#--------------------------------------------------
# Kullanımı - iterator alarak:
#--------------------------------------------------
# a = PowTwo(4)
# i = iter(a) # iter() metodu ile iterator alınır: i
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

#--------------------------------------------------
# Kullanımı - for döngüsü ile:
#--------------------------------------------------
# for i in PowTwo(5):
#     print(i)



######################################################################
#       GENERATOR
######################################################################

# Basit bir generator fonksiyonu
# def my_gen():
#     n = 1 # n değişkenin son değeri fonksiyon her çağırıldığında hatırlanır
#     print('İlk yazılacak satır')
#     yield n # yield statement içerir
#
#     n += 1
#     print('İkinci yazılacak satır')
#     yield n
#
#     n += 1
#     print('Son yazılacak satır')
#     yield n

#--------------------------------------------------
# Kullanımı - iterator alarak:
#--------------------------------------------------
# Bir obje söder ama hemen icra etmeye başlamaz
# a = my_gen()
# next(a) # next() metodu ile elemanlar üzerinde iterate edilir
# next(a)
# next(a)
# next(a)

#--------------------------------------------------
# Kullanımı - for döngüsü ile:
#--------------------------------------------------
# for item in my_gen():
#     print(item)


######################################################################
# GENERATOR ÖRNEK: Metni ters çevirme
######################################################################
# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length - 1, -1, -1):
#         yield my_str[i]
#
#
# # For loop to reverse the string
# for char in rev_str("selam python"):
#     print(char)

######################################################################
#       GENERATOR EXPRESSION
######################################################################
# liste oluştur
# my_list = [1, 3, 6, 10]
#
# # her elemanın karesini al (list comprehension ile)
# list_ = [x**2 for x in my_list]
# print(list_)
#
# # Aynı işlem generator expression ile yapılabilir
# # Generator expression lar () parantezler ile çevrilidir
# # generator objesi oluşur (lazy evaluation: next() ile çağırılınca sonuç dönecek)
# generator = (x**2 for x in my_list)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator)) # StopIteration
