import pandas as pd

def portfoy_dengele(portfoy, risk_seviyeleri):
    print("Portföy dengeleme stratejisi oluşturuluyor...\n")

    dengelenmis_portfoy = {}
    toplam_risk = sum(risk_seviyeleri.values())
    
    for varlik, miktar in portfoy.items():
        risk_orani = risk_seviyeleri[varlik] / toplam_risk
        dengelenmis_miktar = miktar * (1 - risk_orani)  # Risk oranına göre azaltıyoruz
        dengelenmis_portfoy[varlik] = dengelenmis_miktar
    
    dengeleme_df = pd.DataFrame(list(dengelenmis_portfoy.items()), columns=['Varlık', 'Dengelenmiş Değer'])
    
    print("\nPortföy Dengeleme Raporu:")
    print(dengeleme_df)
    
    # Raporu Excel'e kaydetme
    dengeleme_df.to_excel('portfoy_dengeleme_raporu.xlsx', index=False)
    print("\nPortföy dengeleme raporu Excel dosyasına kaydedildi.")

if __name__ == "__main__":
    portfoy = {
        'Bitcoin': 50000,
        'Ethereum': 30000,
        'Tether': 10000,
        'BNB': 15000,
        'Solana': 5000
    }
    
    risk_seviyeleri = {
        'Bitcoin': 0.08,
        'Ethereum': 0.07,
        'Tether': 0.02,
        'BNB': 0.09,
        'Solana': 0.12
    }

    portfoy_dengele(portfoy, risk_seviyeleri)