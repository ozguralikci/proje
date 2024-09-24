import pandas as pd
import datetime

# Örnek portföy performans verileri
portfoy_verileri = {
    'Gün': [1, 2, 3, 4],
    'Bitcoin': [50000, 51000, 49500, 52000],
    'Ethereum': [30000, 31000, 29500, 31500],
    'Tether': [10000, 10050, 10030, 10020],
    'BNB': [15000, 15200, 14900, 15300],
    'Solana': [5000, 5200, 5100, 5300]
}

# Veriler DataFrame'e dönüştürülüyor
df = pd.DataFrame(portfoy_verileri)

# Kâr-Zarar hesaplamaları
def kar_zarar_hesapla(df):
    print("Kâr-Zarar Takibi Yapılıyor...")
    ilk_degerler = df.iloc[0, 1:]
    son_degerler = df.iloc[-1, 1:]
    kar_zarar = (son_degerler - ilk_degerler) / ilk_degerler * 100
    print("\nKâr-Zarar Oranları (%):")
    print(kar_zarar)

    # Kâr-Zarar raporu Excel'e kaydediliyor
    kar_zarar_df = pd.DataFrame(kar_zarar, columns=['Kâr-Zarar (%)'])
    kar_zarar_df.to_excel('kar_zarar_raporu.xlsx', index=True)
    print("\nKâr-Zarar raporu Excel dosyasına kaydedildi.")

# Performans karşılaştırması
def performans_karsilastirma(df):
    print("Piyasa Performans Karşılaştırması Yapılıyor...")
    ortalama_degerler = df.iloc[:, 1:].mean()
    print("\nVarlıkların Ortalama Performansları:")
    print(ortalama_degerler)

    # Performans raporu Excel'e kaydediliyor
    performans_df = pd.DataFrame(ortalama_degerler, columns=['Ortalama Performans'])
    performans_df.to_excel('performans_karsilastirma.xlsx', index=True)
    print("\nPerformans karşılaştırma raporu Excel dosyasına kaydedildi.")

# Performans takibi fonksiyonu
def performans_takibi(df):
    print("Portföy performans takibi yapılıyor...")

    # Performans raporu
    print("\nPerformans Raporu:")
    print(df.describe())

    # Performans raporu Excel'e kaydediliyor
    df.to_excel('performans_raporu.xlsx', index=False)
    print("\nPerformans raporu Excel dosyasına kaydedildi.")
    
    # Grafiğin oluşturulması
    df.plot(x='Gün', y=['Bitcoin', 'Ethereum', 'Tether', 'BNB', 'Solana'], kind='line', title='Portföy Performansı')
    print("\nPerformans raporu ve grafiği oluşturuldu.")

if __name__ == "__main__":
    # Performans takibini çalıştır
    performans_takibi(df)
    
    # Kâr-Zarar hesaplaması
    kar_zarar_hesapla(df)
    
    # Piyasa performans karşılaştırması
    performans_karsilastirma(df)