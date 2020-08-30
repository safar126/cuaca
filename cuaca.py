import requests as r
from bs4 import BeautifulSoup as s
import json,re,os
session = r.Session()
url = "https://www.accuweather.com/id/browse-locations/asi/id"
hed ={
"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; CPH1701) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
}
logo = """#Author : Safar              #
#Support : My Team           #
#Team : From XiuzCode        #
#Tool : Cek Cuaca            #
#My Contact : +6282288231535 #"""
def awal():
	os.system('clear') 
	print('='*30)
	print(logo)
	print('='*30)
	kontol = input("Tekan Enter jika sudah membaca.....")
	main()

def main():
	b = session.get(url,headers=hed)
	data = []
	nomor = -1
	sop = s(b.content, 'html.parser')
	for x in sop("a", class_="search-result"):
		nomor += 1
		data.append([x.text, x['href']])
		print(str([nomor]),x.text)
	inp = int(input('[√] Pilih No provinsi : '))
	v = data[inp][1]
	z = r.get("https://www.accuweather.com/"+v,headers=hed)
	daa = []
	nomor = -1
	sp = s(z.content, 'html.parser')
	for xe in sp("a", class_="search-result"):
		nomor += 1
		daa.append([xe.content, xe['href']])
		print(str([nomor]),xe.text)
	inp = int(input('[√] Pilih No Daerah : '))
	m = daa[inp][1]
	h = r.get("https://www.accuweather.com/"+m, headers=hed)
	sg = s(h.text, 'html.parser')
	nomor = 0
	for xc in sg("div",class_="card weather-card content-module non-ad"):
		nomor = 1
		x = xc.text
		z = x.strip()
		print(str(nomor),z)
	it = input("Tekan Enter untuk Kembali Ke menu...")
	main()
	
	

awal()
