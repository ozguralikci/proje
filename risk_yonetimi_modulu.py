import pandas as pd

class RiskYonetimi:
    def __init__(self, portfoy):
        self.portfoy = portfoy

    def risk_degerlendir(self, risk_faktoru):
        print("Risk yönetimi analizi yapılıyor...")
        risk_seviyeleri = {}
        for varlik, deger in self.portfoy.items():
            risk_seviyesi = deger * risk_faktoru.get(varlik, 0)
            if risk_seviyesi > 0.07:
                risk_seviyeleri[varlik] = "Yüksek Riskli"
            else:
                risk_seviyeleri[varlik] = "Düşük Riskli"
        
        # Risk analiz raporu
        print("\nRisk Seviyeleri:")
        for varlik, seviye in risk_seviyeleri.items():
            print(f"{varlik}: {seviye}")

        # Raporu Excel'e kaydetme
        df = pd.DataFrame(list(risk_seviyeleri.items()), columns=['Varlık', 'Risk Seviyesi'])
        df.to_excel('risk_analiz_raporu.xlsx', index=False)
        print("\nRisk analiz raporu Excel dosyasına kaydedildi.")

if __name__ == "__main__":
    portfoy = {
        'Bitcoin': 50000,
        'Ethereum': 30000,
        'Tether': 10000,
        'BNB': 15000,
        'Solana': 5000
    }
    
    risk_faktoru = {
        'Bitcoin': 0.09,
        'Ethereum': 0.05,
        'Tether': 0.02,
        'BNB': 0.08,
        'Solana': 0.03
    }

    risk_yonetimi = RiskYonetimi(portfoy)
    risk_yonetimi.risk_degerlendir(risk_faktoru)