##################################################
# Tüm sınıflar object sınıfının alt sınıfıdır
##################################################
# # Output: True
# print(issubclass(list,object))
# # Output: True
# print(isinstance(5.5,object))
# # Output: True
# print(isinstance("Hello",object))


##################################################
# Multiple Inheritance-1
##################################################
# class Class1:
#     def m(self):
#         print("In Class1")
#
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#
# # Önce Class2 olduğu için Class2 deki metod çalışır
# # Class3 başa gelirse ondaki metod çalışır
# class Class4(Class2, Class3):
#     pass
#
# obj = Class4()
# obj.m()

##################################################
# Multiple Inheritance-2
##################################################
# Python Program to depict multiple inheritance
# when method is overridden in one of the classes
# class Class1:
#     def m(self):
#         print("In Class1")
#
# class Class2(Class1):
#     pass
#
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#
# class Class4(Class2, Class3):
#     pass
#
# obj = Class4()
# obj.m()

##################################################
# Multiple Inheritance-3
##################################################
# Python Program to depict multiple inheritance
# when every class defines the same method
# class Class1:
#     def m(self):
#         print("In Class1")
#
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#
# class Class4(Class2, Class3):
#     def m(self):
#         print("In Class4")
#
# obj = Class4()
# obj.m()
#
# Class2.m(obj)
# Class3.m(obj)
# Class1.m(obj)

##################################################
# Multiple Inheritance-4
##################################################
# Python program to demonstrate super()
# class Class1:
#     def m(self):
#         print("In Class1")
#
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#         super().m()
#
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#         super().m()
#
# class Class4(Class2, Class3):
#     def m(self):
#         print("In Class4")
#         super().m()
#
# obj = Class4()
# obj.m()
