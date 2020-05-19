################################################
# SINIFIN TANIMLANMASI
################################################
# Sınıf tanımında () olabilir/olmayabilir fark etmez
class HarfSayacı:
    #Sınıf ilk çalıştırıldığında 1 kez otomatik olarak
    #çalışan initialize metodu
    def __init__(self):
        self.sesli_harfler = 'aeıioöuü'
        self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
        self.sayaç_sesli = 0
        self.sayaç_sessiz = 0

    # Örnek metodu (self yerine başka ifade de olabilir)
    def kelime_sor(self):
        return input('Bir kelime girin: ')

    # Örnek metodu (self yerine başka ifade de olabilir)
    def seslidir(self, harf):
        return harf in self.sesli_harfler

    # Örnek metodu (self yerine başka ifade de olabilir)
    def sessizdir(self, harf):
        return harf in self.sessiz_harfler

    # Örnek metodu (self yerine başka ifade de olabilir)
    def artır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayaç_sesli += 1
            if self.sessizdir(harf):
                self.sayaç_sessiz += 1
        return self.sayaç_sesli, self.sayaç_sessiz

    # Örnek metodu (self yerine başka ifade de olabilir)
    def ekrana_bas(self):
        sesli, sessiz = self.artır()
        mesaj = "{} kelimesinde {} sesli {} sessiz harf var."
        print(mesaj.format(self.kelime, sesli, sessiz))

    # Örnek metodu (self yerine başka ifade de olabilir)
    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

################################################
# PROGRAMIN ÇALIŞTIRILMASI
################################################
#Program çalıştırma ifadesi
if __name__ == '__main__':
    # Sınıftan bir örnek oluştur
    sayaç = HarfSayacı()
    # Örnekten çalıştır() metodunu çağırarak programı çalıştır
    sayaç.çalıştır()