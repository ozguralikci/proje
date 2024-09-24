import pandas as pd
import requests
from haber_cek import finansal_haberleri_cek, haberlerden_duygu_analizi  # Haber çekme ve duygu analizi fonksiyonları

# Mevcut veri çekme fonksiyonu (CoinGecko API, Exchange Rates API ve BIST için)
def get_current_prices():
    # Kripto paralar için CoinGecko API
    kripto_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether,binancecoin,solana&vs_currencies=usd"
    kripto_response = requests.get(kripto_url)
    kripto_prices = kripto_response.json()

    # Döviz kurları için Exchange Rates API (Örnek URL)
    doviz_url = "https://api.exchangerate-api.com/v4/latest/USD"
    doviz_response = requests.get(doviz_url)
    doviz_prices = doviz_response.json()

    # Emtialar ve BIST 100 için sabit veriler
    emtia_bist_data = {
        'Gold': 1800, 'Silver': 25, 'Brent Oil': 70, 
        'BIST_100': {'AKBNK': 7.2, 'GARAN': 8.3, 'ISCTR': 5.1, 'THYAO': 15.5, 'TUPRS': 18.0}
    }

    return kripto_prices, doviz_prices, emtia_bist_data

# Strateji fonksiyonu (fiyat ve genel haber analizine göre strateji belirleme)
def strateji_olustur(degisim, olumlu_sayi, olumsuz_sayi):
    if olumlu_sayi > olumsuz_sayi and degisim > 2:
        return "Kısa vadeli kar hedefi"
    elif olumsuz_sayi > olumlu_sayi and degisim < -1:
        return "Riskli yatırım"
    else:
        return "Uzun vadeli yatırım önerisi"

# Yatırım stratejisi fonksiyonu (Sadece mevcut varlıklar ve haber analizleriyle birlikte)
def yatirim_stratejisi_olustur():
    print("Yatırım stratejisi önerileri hesaplanıyor...")

    # Mevcut verileri alalım
    kripto_prices, doviz_prices, emtia_bist_data = get_current_prices()

    # Finansal haberleri çekelim
    haberler = finansal_haberleri_cek()

    # Genel haber duygu analizini yapalım
    olumlu_toplam, olumsuz_toplam, notr_toplam = 0, 0, 0
    for haber in haberler:
        olumlu, olumsuz, notr = haberlerden_duygu_analizi(haber['title'])  # Genel haber başlıklarını analiz ediyoruz
        olumlu_toplam += olumlu
        olumsuz_toplam += olumsuz
        notr_toplam += notr

    # Mevcut varlık verileri
    data = {
        'Varlık': ['Bitcoin', 'Ethereum', 'Tether', 'BNB', 'Solana',
                   'EUR/USD', 'GBP/USD', 'TRY/USD',  # Dövizler
                   'Gold', 'Silver', 'Brent Oil',  # Emtialar
                   'AKBNK', 'GARAN', 'ISCTR', 'THYAO', 'TUPRS'],  # BIST 100
        'Fiyat': [
            kripto_prices['bitcoin']['usd'], kripto_prices['ethereum']['usd'], kripto_prices['tether']['usd'], 
            kripto_prices['binancecoin']['usd'], kripto_prices['solana']['usd'], 
            doviz_prices['rates']['EUR'], doviz_prices['rates']['GBP'], doviz_prices['rates']['TRY'],
            emtia_bist_data['Gold'], emtia_bist_data['Silver'], emtia_bist_data['Brent Oil'], 
            emtia_bist_data['BIST_100']['AKBNK'], emtia_bist_data['BIST_100']['GARAN'], 
            emtia_bist_data['BIST_100']['ISCTR'], emtia_bist_data['BIST_100']['THYAO'], 
            emtia_bist_data['BIST_100']['TUPRS']
        ],
        'Değişim (%)': [2.5, -1.8, 0.0, 3.1, 5.2,  # Kripto
                        0.3, -0.4, 1.2,  # Döviz
                        -0.8, 1.5, 2.0,  # Emtia
                        1.0, 2.5, -0.7, 0.9, 3.3]  # BIST 100
    }

    df = pd.DataFrame(data)

    # Strateji sütununu ekleyelim
    df['Strateji'] = df.apply(lambda row: strateji_olustur(row['Değişim (%)'], olumlu_toplam, olumsuz_toplam), axis=1)

    # Excel'e kaydet
    df.to_excel('yatirim_stratejisi_raporu.xlsx', index=False)
    print("\nYatırım stratejisi raporu Excel dosyasına kaydedildi.")
    print(df)

if __name__ == "__main__":
    yatirim_stratejisi_olustur()