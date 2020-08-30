import requests as r
from bs4 import BeautifulSoup as s
import json,re
session = r.Session()
url = "https://www.accuweather.com/id/browse-locations/asi/id"
hed ={
"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; CPH1701) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
}
def pri():
	b = session.get(url,headers=hed)
	sop = s(b.content, 'html.parser')
	angka = 0
	daftar = []
	for x in sop("a", class_="search-result"),["href"]:
		angka += 1
		#print(str(angka),x.text)
		#print(x["href"])
		daftar.append(x)
		print(daftar.text)
	pilih = int(input(" >>> "))
	pilihan = daftar[pilih -1][1]
	print("anda memilih"+pilihan)
		#print(oo)
		





#(/id/browse-locations/asi/id/)(\w\w)
#https://www.accuweather.com/id/browse-locations/asi/id/ri

pri()










#div class="card weather-card content-module non-ad">


