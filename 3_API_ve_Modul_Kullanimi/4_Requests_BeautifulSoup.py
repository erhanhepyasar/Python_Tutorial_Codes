##############################################################
# Internetten bilgi çekmek
# ------------------------------------------------------------
# IMDB Top 250 sayfasının ayrıştırarak film isimlerini çekme
##############################################################
import requests
from bs4 import BeautifulSoup

# Sayfa kaynağını alalım (IMDB Top 250 filmler):
imdb_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
r = requests.get(imdb_url)

# Alınan sayfa kaynağını görüntüleme:
# print(r.content)

#Çıktı görünümünü güzelleştirme
soup = BeautifulSoup(r.content, features="html.parser")
#print(soup.prettify())

# öncelikle filmlerin içinde yer aldığı ana tabloyu çekliyoruz
gelen_veri = soup.find_all("table", {"class":"chart full-width"})

# ana tablonun içinden filmlerin olduğu kısmı alıyoruz
filmtablosu = gelen_veri[0].contents[len(gelen_veri[0].contents)-2]
# print(filmtablosu)

# filmlerin bulunduğu <tr> bölümlerini alıyoruz
filmtablosu = filmtablosu.find_all("tr")
print(len(filmtablosu)) # 250 film

# her bir filimin başlıklarının olduğu kısımlarını alıyoruz
# başlıkların içinden film ismini alıyoruz
# film ismi içindeki satır başı karakterlerini kaldırıp düzgün gösteriyoruz
for film in filmtablosu:
    filmbasliklari = film.find_all("td", {"class":"titleColumn"})
    filmismi = filmbasliklari[0].text
    filmismi = filmismi.replace("\n","")
    print(filmismi)




