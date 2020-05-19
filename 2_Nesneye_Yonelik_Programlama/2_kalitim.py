####################################################
# Parent Class Tanımlama
####################################################
#Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Person class ı kullanarak object oluştur ve metodu kullan
# john = Person("John", "Doe")
# john.printname()

####################################################
# Child Class Tanımlama ve Adımlar Halinde Geliştirme
####################################################
#----------------------------------
# Adım-1
#----------------------------------
#Child Class
# class Student(Person):
#     pass

# #Child class tan bir obje tanımlama
# ayse = Student("Ayse", "Yilmaz")
# # Child class a ait obje ile parent class ın metodlarını kullanma
# ayse.printname()

#----------------------------------
# Adım-2
#----------------------------------
# # Child class a  init metodu eklenmesi
# # Ayrıca parent-child ilişkisini bozmamak için Person.__init__ in çağrılması
# class Student(Person):
#     def __init__(self, fname, lname):
#        Person.__init__(self, fname, lname)

#----------------------------------
# Adım-3
#----------------------------------
# Parent class ın adını kullanmak yerine super() keyword u kullanılabilir
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)

#----------------------------------
# Adım-4
#----------------------------------
# child class a property eklenmesi
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#         self.graduationYear = 2015

#----------------------------------
# Adım-5
#----------------------------------
# # child class a eklenen property nin dışarıdan alınan değişkenle atanması
# class Student(Person):
#     def __init__(self, fname, lname, gradYear):
#         super().__init__(fname, lname)
#         self.graduationYear = gradYear
#
# # nesne tanımı
# baris = Student("Baris", "Akarsu", 2008)
# baris.printname()

# #----------------------------------
# # Adım-6
# #----------------------------------
# # child class a metod ekleme
# class Student(Person):
#     def __init__(self, fname, lname, gradYear):
#         super().__init__(fname, lname)
#         self.graduationYear = gradYear
#
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of",self.graduationYear)
#
# # nesne tanımı
# baris = Student("Baris", "Akarsu", 2008)
# baris.welcome()

#----------------------------------
# Adım-7
#----------------------------------
# parent class taki metodu ezme (override)
# class Student(Person):
#     def __init__(self, fname, lname, gradYear):
#         super().__init__(fname, lname)
#         self.graduationYear = gradYear
#
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of",self.graduationYear)
#
#     def printname(self):
#         print(self.firstname, self.lastname, "- override method")
#
# # nesne tanımı
# baris = Student("Baris", "Akarsu", 2008)
# baris.printname()
