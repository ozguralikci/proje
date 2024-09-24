import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
from openpyxl.drawing.image import Image

# RSI hesaplama
def rsi(data, window=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# MACD hesaplama
def macd(data, short_window=12, long_window=26, signal_window=9):
    short_ema = data.ewm(span=short_window, adjust=False).mean()
    long_ema = data.ewm(span=long_window, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()
    return macd_line, signal_line

# Teknik analiz ve grafik oluşturma
def teknik_analiz_yap(fiyat_data):
    try:
        df = pd.DataFrame(fiyat_data, columns=['Tarih', 'Fiyat'])
        df['RSI'] = rsi(df['Fiyat'])
        df['MACD'], df['Signal'] = macd(df['Fiyat'])
        
        # Grafik oluşturma
        plt.figure(figsize=(12, 6))
        plt.plot(df['Tarih'], df['RSI'], label='RSI')
        plt.plot(df['Tarih'], df['MACD'], label='MACD')
        plt.plot(df['Tarih'], df['Signal'], label='Signal')
        plt.title('RSI ve MACD Teknik Göstergeleri')
        plt.legend()
        plt.savefig('teknik_analiz_grafigi.png')  # Grafik kaydetme
        plt.show()
        
        # Grafiği Excel'e ekleme
        grafik_olustur(df)
        return df
    except Exception as e:
        print(f"Teknik analiz yapılamadı: {e}")

# Grafik ekleme fonksiyonu
def grafik_olustur(df, filename='teknik_analiz_grafigi.png'):
    try:
        wb = openpyxl.load_workbook('finansal_analiz_projesi.xlsx')
        ws = wb.create_sheet('Teknik Analiz')
        img = Image(filename)
        ws.add_image(img, 'A1')
        wb.save('finansal_analiz_projesi.xlsx')
        print("Grafik Excel dosyasına eklendi.")
    except Exception as e:
        print(f"Grafik kaydedilemedi: {e}")

# Örnek test verisi
fiyat_data = {'Tarih': pd.date_range(start='2023-01-01', periods=30, freq='D'), 'Fiyat': np.random.random(30) * 100}
teknik_analiz_yap(fiyat_data)