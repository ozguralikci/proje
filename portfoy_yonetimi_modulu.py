import pandas as pd

# Portföy yönetimi sınıfı
class PortfoyYonetimi:
    def __init__(self, portfoy):
        self.portfoy = portfoy

    def risk_analizi(self):
        print("Portföy risk analizi yapılıyor...")
        
        # Varlık risk analizlerini saklayacağız
        risk_degerlendirmeleri = {}

        for varlik, miktar in self.portfoy.items():
            # Örnek risk oranı, her varlık için farklı olabilir
            risk_orani = self.get_risk_orani(varlik)

            if risk_orani > 0.07:
                risk_degerlendirmeleri[varlik] = f"Yüksek riskli, kısa vadeli yatırım önerilir."
            else:
                risk_degerlendirmeleri[varlik] = f"Güvenli seviyede, uzun vadeli yatırım uygun olabilir."

        return risk_degerlendirmeleri

    def get_risk_orani(self, varlik):
        # Basit bir risk oranı belirleme işlevi (örnek değerler)
        risk_oranlari = {
            'Bitcoin': 0.09,
            'Ethereum': 0.05,
            'Tether': 0.02,
            'BNB': 0.08,
            'Solana': 0.04
        }
        return risk_oranlari.get(varlik, 0.05)

    def dengeleme_onerisi(self):
        print("Portföy dengeleme önerisi hesaplanıyor...")

        toplam_deger = sum(self.portfoy.values())
        dengeleme_onerileri = {}

        for varlik, miktar in self.portfoy.items():
            pay = (miktar / toplam_deger) * 100
            dengeleme_onerileri[varlik] = f"{pay:.2f}%"

        return dengeleme_onerileri

# Portföy örneği (kripto para portföyü)
portfoy = {
    'Bitcoin': 50000,
    'Ethereum': 30000,
    'Tether': 10000,
    'BNB': 15000,
    'Solana': 5000
}

# Portföy yönetimi objesi
portfoy_yonetimi = PortfoyYonetimi(portfoy)

# Risk analizini çalıştır
risk_degerlendirmeleri = portfoy_yonetimi.risk_analizi()
for varlik, degerlendirme in risk_degerlendirmeleri.items():
    print(f"{varlik}: {degerlendirme}")

# Dengeleme önerilerini çalıştır
dengeleme_onerileri = portfoy_yonetimi.dengeleme_onerisi()
print("\nPortföy Dengeleme Önerileri:")
for varlik, pay in dengeleme_onerileri.items():
    print(f"{varlik}: {pay}")

print("Portföy yönetimi tamamlandı. Terminale geri dönülüyor.")