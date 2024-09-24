import requests
from bs4 import BeautifulSoup
import pandas as pd

# Örnek web kazıma fonksiyonu
def kazima_veri_al(url, varlik_adi):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Örnek: Web sayfasında fiyat bilgisini çeken kod
    fiyat_elementi = soup.find('div', {'class': 'price'})
    fiyat = float(fiyat_elementi.text.strip().replace('$', '').replace(',', ''))

    print(f"{varlik_adi} için fiyat: {fiyat}")
    return fiyat

# BIST, kripto, döviz ve emtia verilerini web kazıma ile alma fonksiyonu
def web_kazima():
    varliklar = {
        'Bitcoin': 'https://example.com/bitcoin',
        'Ethereum': 'https://example.com/ethereum',
        'AKBNK': 'https://example.com/akbank',
        'Gold': 'https://example.com/gold'
        # Daha fazla varlık eklenebilir
    }

    fiyatlar = {}
    for varlik, url in varliklar.items():
        fiyatlar[varlik] = kazima_veri_al(url, varlik)

    # Verileri bir DataFrame'e dönüştürüp Excel'e kaydedelim
    df = pd.DataFrame(fiyatlar.items(), columns=['Varlık', 'Fiyat'])
    df.to_excel('web_kazima_verileri.xlsx', index=False)
    print("Web kazıma verileri başarıyla kaydedildi.")

if __name__ == "__main__":
    web_kazima()