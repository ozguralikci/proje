# otomatik_guncelleme_modulu.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime

kripto_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
tcmb_url = "https://www.tcmb.gov.tr/kurlar/today.xml"

def kripto_veri_cek():
    response = requests.get(kripto_url)
    if response.status_code == 200:
        data = response.json()
        for coin, details in data.items():
            print(f"{coin.capitalize()} Fiyat: {details['usd']} USD")
    else:
        print("Kripto verisi alınamadı:", response.status_code)

def doviz_ve_altin_verisi_cek():
    response = requests.get(tcmb_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'xml')
        for currency in soup.find_all('Currency'):
            isim = currency.find('Isim').text
            satis_fiyati = currency.find('ForexSelling').text
            if satis_fiyati:
                print(f"{isim} Satış Fiyatı: {satis_fiyati} TRY")
    else:
        print("Döviz verisi alınamadı:", response.status_code)

def veri_guncelle():
    print("Veriler güncelleniyor...")
    kripto_veri_cek()
    doviz_ve_altin_verisi_cek()
    print(f"{datetime.now()} - Veriler başarıyla güncellendi!")

if __name__ == "__main__":
    veri_guncelle()