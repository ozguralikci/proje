import requests
from datetime import datetime

# Canlidoviz API URL'leri
doviz_url = "https://api.canlidoviz.com/web/items?marketId=1&type=0"
altin_url = "https://api.canlidoviz.com/web/items?marketId=1&type=1"
kripto_url = "https://api.canlidoviz.com/web/items?marketId=1&type=2"

# Döviz verilerini çekme
def doviz_veri_cek():
    try:
        response = requests.get(doviz_url)
        if response.status_code == 200:
            doviz_veri = response.json()
            for doviz in doviz_veri:
                print(f"{doviz['name']} son fiyat: {doviz['buying']} {doviz['currency']}")
        else:
            print("Döviz verisi çekilemedi:", response.status_code)
    except Exception as e:
        print(f"Döviz verisi çekilirken hata oluştu: {e}")

# Altın verilerini çekme
def altin_veri_cek():
    try:
        response = requests.get(altin_url)
        if response.status_code == 200:
            altin_veri = response.json()
            for altin in altin_veri:
                print(f"{altin['name']} son fiyat: {altin['buying']} {altin['currency']}")
        else:
            print("Altın verisi çekilemedi:", response.status_code)
    except Exception as e:
        print(f"Altın verisi çekilirken hata oluştu: {e}")

# Kripto para verilerini çekme
def kripto_veri_cek():
    try:
        response = requests.get(kripto_url)
        if response.status_code == 200:
            kripto_veri = response.json()
            for kripto in kripto_veri:
                print(f"{kripto['name']} son fiyat: {kripto['buying']} {kripto['currency']}")
        else:
            print("Kripto verisi çekilemedi:", response.status_code)
    except Exception as e:
        print(f"Kripto verisi çekilirken hata oluştu: {e}")

# Veri güncelleme fonksiyonu
def veri_guncelle():
    print("Otomatik veri güncelleme başlatılıyor...")
    doviz_veri_cek()
    altin_veri_cek()
    kripto_veri_cek()
    print(f"{datetime.now()} - Veriler başarıyla güncellendi!")

if __name__ == "__main__":
    veri_guncelle()