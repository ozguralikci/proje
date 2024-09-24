import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def fiyat_tahmin_et(veri):
    try:
        # Zaman serisi verisini hazırlama
        df = pd.DataFrame(veri, columns=['Tarih', 'Açılış Fiyatı', 'Kapanış Fiyatı'])
        df['Tarih'] = pd.to_datetime(df['Tarih'])  # Tarih kolonunu datetime formatına çevir
        df['Gün'] = (df['Tarih'] - df['Tarih'].min()).dt.days  # Günleri hesapla
        
        # X ve y verilerini ayır
        X = df['Gün'].values.reshape(-1, 1)  # Gün kolonu özellik olarak kullanılıyor
        y = df['Kapanış Fiyatı'].values  # Hedef değer kapanış fiyatları
        
        # Modeli oluştur ve eğit
        model = LinearRegression()
        model.fit(X, y)
        
        # 30 günlük tahmin
        gelecekteki_gunler = np.arange(df['Gün'].max() + 1, df['Gün'].max() + 31).reshape(-1, 1)
        tahminler = model.predict(gelecekteki_gunler)
        
        # Tahmin sonuçlarını bir DataFrame'e çevir ve kaydet
        tahmin_df = pd.DataFrame({
            'Gün': gelecekteki_gunler.flatten(),
            'Tahmin Edilen Fiyat': tahminler
        })
        tahmin_df.to_excel('fiyat_tahminleri.xlsx', index=False)
        print("30 günlük fiyat tahmini başarıyla kaydedildi!")
    
    except Exception as e:
        print(f"Fiyat tahmini yapılırken hata oluştu: {e}")

def tahmin_modulu():
    print("Tahmin modülü başlatılıyor...")
    try:
        # Excel dosyasından veri yükleme
        df = pd.read_excel('finansal_analiz_projesi.xlsx', sheet_name='Veri')
        fiyat_tahmin_et(df)
    except FileNotFoundError:
        print("Excel dosyası bulunamadı!")
    except Exception as e:
        print(f"Excel dosyasından veri yüklenirken hata: {e}")

if __name__ == "__main__":
    tahmin_modulu()