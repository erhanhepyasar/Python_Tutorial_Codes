####################################################
# En Basit Haliyle Bir Sınıf ve Nesne Tanımlaması
####################################################
# class MyClass:
#     x = 5
#
# myObject = MyClass()
#
# print(myObject.x)
#
# # x bir sınıf değişkeni olduğu için sınıf adıyla da erişilebilir
# print(MyClass.x)

####################################################
# Başka bir basit sınıf tanımlama örneği
####################################################
# class Siparis():
#     firma = ''
#     miktar = 0
#     sipariş_tarihi = ''
#     teslim_tarihi = ''
#     stok_adedi = 0
#
# deterjan = Siparis()
# deterjan.firma = 'Migros'
# deterjan.miktar = 2
# deterjan.sipariş_tarihi = "15.04.2020"
# deterjan.teslim_tarihi = "16.04.2020"
# deterjan.stok_adedi = 100


####################################################
# init ve self içeren bir Sınıf Tanımlaması
####################################################
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# # Nesne tanımlanması ve nesne değişkenlerinin kullanımı
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)

####################################################
# Nesne Metodları
####################################################
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
# p1.myfunc()


####################################################
# self yerine başka kelime kullanılabilir
####################################################
# class Person:
#   def __init__(nesnereferansim, isim, yas):
#     nesnereferansim.isim = isim
#     nesnereferansim.yas = yas
#
#   def myfunc(abc):
#     print("Merhaba benim adım " + abc.isim)
#     print("Yasim:", abc.yas)
#
# p1 = Person("John", 36)
# p1.myfunc()


####################################################
# Kapsamlı Bir Sınıf Tanımlaması
####################################################
# class Calisan:
#     calisanSayaci = 0
#
#     def __init__(self, isim, maas):
#         self.isim = isim
#         self.maas = maas
#         Calisan.calisanSayaci += 1
#
#     def sayaciGoster(self):
#         print("Toplam Çalışan: ", Calisan.calisanSayaci)
#
#     def calisaniGoster(self):
#         print("Isim : ", self.isim, ", Maas: ", self.maas)


# Nesne tanımlanması
# hulya = Calisan("Hulya Soyer", 5000)

####################################################
# Sınıf Tanımlaması - Açıklamalar Eklenmiş
####################################################
# class Calisan:
#     # Sınıf değişkeni
#     # Tüm örnekler (instance) erişebilir
#     calisanSayaci = 0
#
#     # Class constructor / initialization method
#     # Her yeni instance oluşturulduğunda çağırılır
#     def __init__(self, isim, maas):
#         self.isim = isim # instance variable (örnek değişkeni) tanımlanıyor
#         self.maas = maas # instance variable (örnek değişkeni) tanımlanıyor
#         Calisan.calisanSayaci += 1 # sınıf değişkeninin değeri değiştiriliyor
#
#     # Örnek-nesne metodu (Instance method) (self var)
#     def sayaciGoster(self):
#         print("Toplam Çalışan: ", Calisan.calisanSayaci)
#
#     # Örnek-nesne metodu (Instance method) (self var)
#     def calisaniGoster(self):
#         print("Isim : ", self.isim, ", Maas: ", self.maas)


# Nesne Tanımlaması ve Metodların Kullanımı
# Employee class ından hasan isimli object üretiyoruz
# hasan = Calisan("Hasan Yildiz", 5000)

# hasan objesinin instance method larını çağırıyoruz
# self parametresi için birşey yazmamız gerekmiyor, Python kendi ekliyor
# hasan.sayaciGoster()
# hasan.calisaniGoster()

# Employee class ının class variable (sınıf değişkenini) okuyoruz
# print("Sayaç: " + str(Calisan.calisanSayaci))

# constructor 2 parametreli olduğundan sadece bu şekilde nesne üretilir
# TypeError: __init__() missing 2 required
# positional arguments: 'name' and 'salary'
# emrah = Employee()

####################################################
# Sınıf Metodları Tanımlama - @classmethod , cls
####################################################
# class Çalışan():
#     #Sınıf değişkeni (liste)
#     personel = []
#
#     #Sınıf ilk çalıştırıldığında 1 kez otomatik olarak
#     #çalışan initialize metodu
#     def __init__(self, isim):
#         self.isim = isim
#         self.kabiliyetleri = []
#         self.personele_ekle()
#
#     #Sınıf metodu (cls yerine başka ifade de olabilir)
#     @classmethod
#     def personel_sayısını_görüntüle(cls):
#         print("Personel sayısı:", len(cls.personel))
#
#     # Sınıf metodu (cls yerine başka ifade de olabilir)
#     @classmethod
#     def personeli_görüntüle(cls):
#         print('Personel listesi:')
#         for kişi in cls.personel:
#             print(kişi)
#
#     #Örnek metodu (self yerine başka ifade de olabilir)
#     def personele_ekle(self):
#         self.personel.append(self.isim)
#         print('{} adlı kişi personele eklendi'.format(self.isim))
#
#
#
#     # Örnek metodu (self yerine başka ifade de olabilir)
#     def kabiliyet_ekle(self, kabiliyet):
#         self.kabiliyetleri.append(kabiliyet)
#
#     # Örnek metodu (self yerine başka ifade de olabilir)
#     def kabiliyetleri_görüntüle(self):
#         print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
#         for kabiliyet in self.kabiliyetleri:
#             print(kabiliyet)
#
#     # Örnek metodu (self yerine başka ifade de olabilir)
#     def ismi_görüntüle(self):
#         print("İsim: ", self.isim)
#
#
# # Sınıftan örnekler tanımlama
# ahmet = Çalışan('Ahmet')
# mehmet = Çalışan('Mehmet')
#
# #Sınıf metodunu çağırma
# Çalışan.personel_sayısını_görüntüle()
# Çalışan.personeli_görüntüle()
#
# #Örnek metodlarını çağırma
# ahmet.ismi_görüntüle()
# mehmet.ismi_görüntüle()
# ahmet.kabiliyet_ekle('ingilizce')
# ahmet.kabiliyet_ekle('excel')
# mehmet.kabiliyet_ekle('proje yönetimi')
# mehmet.kabiliyet_ekle('satış')
# ahmet.kabiliyetleri_görüntüle()
# mehmet.kabiliyetleri_görüntüle()


