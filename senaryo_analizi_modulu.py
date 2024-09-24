import pandas as pd
import matplotlib.pyplot as plt

class SenaryoAnalizi:
    def __init__(self, portfoy):
        self.portfoy = portfoy

    def senaryo_analizi_yap(self, fiyat_degisim_oranlari):
        print("Senaryo analizi yapılıyor...")

        # Portföyün yeni değerlerini hesapla
        yeni_portfoy = {}
        for varlik, deger in self.portfoy.items():
            yeni_deger = deger * (1 + fiyat_degisim_oranlari.get(varlik, 0))
            yeni_portfoy[varlik] = yeni_deger

        # Yeni portföy toplam değeri
        toplam_yeni_deger = sum(yeni_portfoy.values())
        print(f"Yeni Portföy Toplam Değeri: {toplam_yeni_deger} USD")

        # Yeni portföydeki oranlar
        for varlik, yeni_deger in yeni_portfoy.items():
            oran = (yeni_deger / toplam_yeni_deger) * 100
            print(f"{varlik}: Yeni portföydeki oranı: %{oran:.2f}")

        # Senaryo analizi raporu oluşturma
        senaryo_df = pd.DataFrame(list(yeni_portfoy.items()), columns=['Varlık', 'Yeni Değer'])
        senaryo_df['Yeni Portföy Oranı (%)'] = (senaryo_df['Yeni Değer'] / toplam_yeni_deger) * 100
        print("\nSenaryo Analiz Raporu:")
        print(senaryo_df)

        # Raporu Excel'e kaydetme
        senaryo_df.to_excel('senaryo_analiz_raporu.xlsx', index=False)
        print("\nSenaryo analiz raporu Excel dosyasına kaydedildi.")
        
        # Yeni eklenen: Grafiği oluştur
        self.grafik_olustur(senaryo_df)

    def grafik_olustur(self, senaryo_df):
        plt.figure(figsize=(10, 6))
        plt.bar(senaryo_df['Varlık'], senaryo_df['Yeni Portföy Oranı (%)'])
        plt.title('Portföydeki Varlıkların Oranları (Senaryo Analizi)')
        plt.ylabel('Portföy Oranı (%)')
        plt.xlabel('Varlıklar')
        plt.savefig('senaryo_analizi_grafik.png')
        print("Senaryo analiz grafiği oluşturuldu ve kaydedildi.")

if __name__ == "__main__":
    # Portföy örneği
    portfoy = {
        'Bitcoin': 50000,
        'Ethereum': 30000,
        'Tether': 10000,
        'BNB': 15000,
        'Solana': 5000
    }

    # Fiyat değişim oranları (% olarak)
    fiyat_degisim_oranlari = {
        'Bitcoin': 0.10,  # %10 artış
        'Ethereum': -0.05,  # %5 düşüş
        'Tether': 0.00,  # Sabit
        'BNB': 0.02,  # %2 artış
        'Solana': 0.15  # %15 artış
    }

    # Senaryo analizi objesi
    senaryo_analizi = SenaryoAnalizi(portfoy)
    senaryo_analizi.senaryo_analizi_yap(fiyat_degisim_oranlari)