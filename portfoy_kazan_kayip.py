import requests
import pandas as pd

# CoinGecko API ile kripto para fiyatlarını çekiyoruz
def kripto_fiyatlarini_cek(coin_ids):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': ','.join(coin_ids),
        'vs_currencies': 'usd'
    }
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Veri çekilemedi, hata kodu: {response.status_code}")
        return None

# Kazanç/kayıp hesaplama fonksiyonu
def kazanc_kayip_hesapla(fiyatlar, portfoy, onceki_fiyatlar):
    kazanc_kayip_listesi = []
    toplam_kazanc = 0
    for coin, miktar in portfoy.items():
        if coin in fiyatlar and coin in onceki_fiyatlar:
            simdiki_fiyat = fiyatlar[coin]['usd']
            onceki_fiyat = onceki_fiyatlar[coin]
            kazanc = (simdiki_fiyat - onceki_fiyat) * miktar
            toplam_kazanc += kazanc
            kazanc_kayip_listesi.append({
                'Coin': coin.capitalize(),
                'Miktar': miktar,
                'Önceki Fiyat': onceki_fiyat,
                'Güncel Fiyat': simdiki_fiyat,
                'Kazanç/Kayıp': round(kazanc, 2)
            })

    print(f"Toplam kazanç/kayıp: {toplam_kazanc:.2f} USD")
    return kazanc_kayip_listesi

# Sonuçları Excel dosyasına kaydetme
def kazanc_kayip_sonuclarini_kaydet(sonuclar):
    df = pd.DataFrame(sonuclar)
    with pd.ExcelWriter('finansal_analiz_projesi.xlsx', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='Portföy Kazanç/Kayıp', index=False)
    print("Portföy kazanç/kayıp sonuçları başarıyla kaydedildi!")

# Portföy Kazanç/Kayıp Modülü
if __name__ == "__main__":
    portfoy = {
        'bitcoin': 0.5,  # Örnek Bitcoin miktarı
        'ethereum': 1.0  # Örnek Ethereum miktarı
    }
    
    onceki_fiyatlar = {
        'bitcoin': 45000,  # Örnek önceki Bitcoin fiyatı
        'ethereum': 3000   # Örnek önceki Ethereum fiyatı
    }

    coin_ids = list(portfoy.keys())
    fiyatlar = kripto_fiyatlarini_cek(coin_ids)
    
    if fiyatlar:
        kazanc_kayip_sonuclari = kazanc_kayip_hesapla(fiyatlar, portfoy, onceki_fiyatlar)
        kazanc_kayip_sonuclarini_kaydet(kazanc_kayip_sonuclari)