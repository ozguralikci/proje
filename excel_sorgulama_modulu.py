import pandas as pd

def excel_sorgula():
    # Excel dosyasını yükle
    try:
        df_veri = pd.read_excel('finansal_analiz_projesi.xlsx', sheet_name='Veri')
    except FileNotFoundError:
        print("Excel dosyası bulunamadı!")
        return

    # Kullanıcıdan minimum değişim oranını al
    try:
        min_degisim = float(input("En az ne kadar değişim gösteren varlıkları listelemek istersiniz? (Örnek: %10): "))
    except ValueError:
        print("Geçersiz değer girdiniz. Lütfen sayı girin.")
        return

    # Zaman dilimini kullanıcıdan al
    zaman_birimi = input("Zaman birimi seçin (dakika, saat, gün, ay, yıl): ").strip().lower()
    try:
        zaman_degeri = int(input(f"Son kaç {zaman_birimi} içinde değişim gösteren varlıkları listelemek istersiniz?: "))
    except ValueError:
        print("Geçersiz değer girdiniz. Lütfen geçerli bir sayı girin.")
        return

    # Varlıkları filtrele
    filtrelenmis_varliklar = df_veri[df_veri['Değişim Oranı'] >= min_degisim]

    if filtrelenmis_varliklar.empty:
        print(f"{min_degisim}% artış gösteren varlık bulunamadı.")
    else:
        print(f"{min_degisim}% artış gösteren varlıklar:")
        print(filtrelenmis_varliklar)

# Fonksiyonu çağır
excel_sorgula()

import pandas as pd

# Excel dosyasından veri okuma
def veri_cek():
    try:
        df = pd.read_excel('finansal_analiz_projesi.xlsx', sheet_name='Veri')
        return df
    except FileNotFoundError:
        print("Excel dosyası bulunamadı!")
        return None

# Sorgulama fonksiyonu
def varliklari_sorgula(min_degisim, sure, zaman_turu):
    df = veri_cek()
    
    if df is None:
        return
    
    if zaman_turu == 'dakika':
        # Dakika bazlı veri sorgulama (örnek, son 10 dakika)
        df_filtered = df[df['Değişim Oranı'] >= min_degisim]
        print(f"{min_degisim}% artış gösteren varlıklar son {sure} dakika içinde:")
    elif zaman_turu == 'saat':
        # Saat bazlı veri sorgulama (örnek, son 2 saat)
        df_filtered = df[df['Değişim Oranı'] >= min_degisim]
        print(f"{min_degisim}% artış gösteren varlıklar son {sure} saat içinde:")
    elif zaman_turu == 'gün':
        # Gün bazlı veri sorgulama (örnek, son 7 gün)
        df_filtered = df[df['Değişim Oranı'] >= min_degisim]
        print(f"{min_degisim}% artış gösteren varlıklar son {sure} gün içinde:")
    elif zaman_turu == 'ay':
        # Ay bazlı veri sorgulama (örnek, son 3 ay)
        df_filtered = df[df['Değişim Oranı'] >= min_degisim]
        print(f"{min_degisim}% artış gösteren varlıklar son {sure} ay içinde:")
    elif zaman_turu == 'yıl':
        # Yıl bazlı veri sorgulama (örnek, son 1 yıl)
        df_filtered = df[df['Değişim Oranı'] >= min_degisim]
        print(f"{min_degisim}% artış gösteren varlıklar son {sure} yıl içinde:")
    else:
        print("Geçersiz zaman türü!")
        return

    if df_filtered.empty:
        print(f"{min_degisim}% artış gösteren varlık bulunamadı.")
    else:
        print(df_filtered[['Varlık Adı', 'Güncel Fiyat', 'Geçmiş Fiyat', 'Değişim Oranı']])

# Kullanıcıdan giriş alma ve sorgulama başlatma
def veri_al_ve_sorgula():
    min_degisim = float(input("En az ne kadar değişim gösteren varlıkları listelemek istersiniz? (Örnek: %10): "))
    zaman_turu = input("Değişim süresi için hangi zaman birimini kullanmak istersiniz? (dakika, saat, gün, ay, yıl): ")
    sure = int(input(f"Son kaç {zaman_turu} içinde değişim gösteren varlıkları listelemek istersiniz? (Örnek: 10 {zaman_turu}): "))
    
    varliklari_sorgula(min_degisim, sure, zaman_turu)

# Fonksiyonu çalıştır
veri_al_ve_sorgula()