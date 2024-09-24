import requests
import datetime
import pandas as pd
import numpy as np
import time

# Binance API'den belirli bir tarih aralığında BTC fiyatlarını çekme
def binance_gecmis_veri_cek(baslangic_tarihi, bitis_tarihi):
    try:
        baslangic_unix = int(datetime.datetime.strptime(baslangic_tarihi, "%Y-%m-%d").timestamp() * 1000)
        bitis_unix = int(datetime.datetime.strptime(bitis_tarihi, "%Y-%m-%d").timestamp() * 1000)

        url = "https://api.binance.com/api/v3/klines"
        params = {
            'symbol': 'BTCUSDT',
            'interval': '1d',
            'startTime': baslangic_unix,
            'endTime': bitis_unix
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            veri = response.json()
            return veri
        else:
            print(f"Veri çekilemedi, hata kodu: {response.status_code}")
            return None
    except Exception as e:
        print(f"Hata: {e}")
        return None

# Fiyat değişim oranını hesaplama fonksiyonu
def fiyat_degisim_orani_hesapla(acilis_fiyati, kapanis_fiyati):
    try:
        degisim_orani = ((float(kapanis_fiyati) - float(acilis_fiyati)) / float(acilis_fiyati)) * 100
        return round(degisim_orani, 2)
    except ZeroDivisionError:
        return None

# Verileri Excel'e kaydetme fonksiyonu
def verileri_excel_kaydet(fiyatlar, baslangic_tarihi, bitis_tarihi):
    try:
        veri_listesi = []
        for fiyat in fiyatlar:
            tarih = datetime.datetime.fromtimestamp(fiyat[0] / 1000).strftime('%Y-%m-%d')
            acilis = fiyat[1]
            kapanis = fiyat[4]
            veri_listesi.append([tarih, acilis, kapanis])
        
        df = pd.DataFrame(veri_listesi, columns=["Tarih", "Açılış Fiyatı", "Kapanış Fiyatı"])
        dosya_adi = f"btc_fiyatlari_{baslangic_tarihi}_to_{bitis_tarihi}.xlsx"
        df.to_excel(dosya_adi, index=False)
        print(f"Veriler '{dosya_adi}' dosyasına kaydedildi!")
    except Exception as e:
        print(f"Hata: {e}")

# CoinGecko API'sinden BTC ve altcoin verilerini çekme fonksiyonu
def btc_altcoin_veri_cek():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False
    }
    
    response = requests.get(url, params=params)
    time.sleep(20)  # Bekleme süresini artırıyoruz (20 saniye)
    
    if response.status_code == 200:
        veri = response.json()
        return veri
    else:
        print("Veri çekilemedi:", response.status_code)
        return None

# CoinGecko API'den fiyat geçmişini çekme fonksiyonu (yeniden deneme limitli)
def coingecko_fiyat_gecmisi_cek(coin_id, gun_sayisi, max_deneme=3):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        'vs_currency': 'usd',
        'days': gun_sayisi,
        'interval': 'daily'
    }
    
    deneme_sayisi = 0
    while deneme_sayisi < max_deneme:
        response = requests.get(url, params=params)
        time.sleep(30)  # Her istek arasında 30 saniye bekle
        
        if response.status_code == 200:
            veri = response.json()
            return veri['prices']
        elif response.status_code == 429:
            print("API istek sınırına ulaşıldı. Lütfen biraz bekleyin.")
            deneme_sayisi += 1
        else:
            print(f"Veri çekilemedi, hata kodu: {response.status_code}")
            return None

    print(f"Veri çekme denemeleri ({max_deneme}) başarısız oldu.")
    return None

# Her kripto paranın kendi volatilitesini hesaplama
def coingecko_volatilite_hesapla(coin_id, gun_sayisi):
    fiyatlar = coingecko_fiyat_gecmisi_cek(coin_id, gun_sayisi)
    if fiyatlar:
        kapanis_fiyatlari = [fiyat[1] for fiyat in fiyatlar]
        volatilite = np.std(kapanis_fiyatlari)
        return round(volatilite, 2)
    else:
        return None

# Risk Skoru Hesaplama Fonksiyonu
def risk_skoru_hesapla(volatilite, degisim_orani):
    try:
        risk_skoru = abs(volatilite * degisim_orani / 100)
        return round(risk_skoru, 2)
    except Exception as e:
        print(f"Risk skoru hesaplanamadı: {e}")
        return None