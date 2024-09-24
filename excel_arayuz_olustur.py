import pandas as pd

def create_excel_file():
    # Ana sayfa verileri
    ana_sayfa_data = {
        'Proje Adı': ['Finansal Analiz ve Yapay Zeka Tabanlı Tahmin Yazılımı'],
        'Açıklama': ['Bu proje, finansal piyasalarda analiz ve tahminler yaparak BTC, altcoinler, döviz, BIST hisse senetleri ve emtia gibi varlıkların fiyat hareketlerini öngörmeyi hedefleyen bir yazılımdır.']
    }
    
    # Veri sayfası verileri
    veri_sayfasi_data = {
        'Varlık Adı': [],
        'Güncel Fiyat': [],
        'Geçmiş Fiyat': [],
        'Değişim Oranı': []
    }
    
    # Tahmin sayfası verileri
    tahmin_sayfasi_data = {
        'Gün': [],
        'Tahmin Edilen Fiyat': []
    }
    
    # Haber analizi sayfası verileri
    haber_sayfasi_data = {
        'Başlık': [],
        'Özet': [],
        'Olumlu': [],
        'Olumsuz': []
    }
    
    # Portföy yönetimi sayfası verileri
    portfoy_sayfasi_data = {
        'Coin Adı': [],
        'Miktar': [],
        'Değer': [],
        'Risk Skoru': []
    }
    
    # DataFrame'ler oluşturma
    ana_sayfa_df = pd.DataFrame(ana_sayfa_data)
    veri_sayfasi_df = pd.DataFrame(veri_sayfasi_data)
    tahmin_sayfasi_df = pd.DataFrame(tahmin_sayfasi_data)
    haber_sayfasi_df = pd.DataFrame(haber_sayfasi_data)
    portfoy_sayfasi_df = pd.DataFrame(portfoy_sayfasi_data)
    
    # Excel dosyasına yazma
    with pd.ExcelWriter('finansal_analiz_projesi.xlsx') as writer:
        ana_sayfa_df.to_excel(writer, sheet_name='Ana Sayfa', index=False)
        veri_sayfasi_df.to_excel(writer, sheet_name='Veri', index=False)
        tahmin_sayfasi_df.to_excel(writer, sheet_name='Tahmin', index=False)
        haber_sayfasi_df.to_excel(writer, sheet_name='Haber Analizi', index=False)
        portfoy_sayfasi_df.to_excel(writer, sheet_name='Portföy', index=False)

    print("Excel dosyası başarıyla oluşturuldu!")

# Fonksiyonu çağır
create_excel_file()