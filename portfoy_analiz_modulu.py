from fiyat_tahmin_modulu import fiyat_tahmini_yap
from risk_yonetimi_modulu import risk_yonetimi

def portfoy_analizi_yap():
    print("Portföy analizi yapılıyor...")
    try:
        portfoy = {
            'Bitcoin': 50000,
            'Ethereum': 30000,
            'Tether': 10000,
            'BNB': 15000,
            'Solana': 5000
        }

        toplam_deger = sum(portfoy.values())
        print(f"Portföy Toplam Değeri: {toplam_deger} USD")

        for varlik, deger in portfoy.items():
            oran = (deger / toplam_deger) * 100
            print(f"{varlik}: Portföydeki oranı: %{oran:.2f}")

        print("\nFiyat tahminleri alınıyor...")
        fiyat_tahmini = fiyat_tahmini_yap(portfoy)
        if fiyat_tahmini:
            print(f"Bir sonraki fiyat tahmini: {fiyat_tahmini}")

        print("\nRisk yönetimi analizi yapılıyor...")
        risk_yonetimi()

    except Exception as e:
        print(f"Portföy analizi sırasında hata oluştu: {e}")

if __name__ == "__main__":
    portfoy_analizi_yap()