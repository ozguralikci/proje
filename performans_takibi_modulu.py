import pandas as pd
import matplotlib.pyplot as plt

def performans_takibi():
    # Performans verileri
    portfoy = {
        'Bitcoin': 50000,
        'Ethereum': 30000,
        'Tether': 10000,
        'BNB': 15000,
        'Solana': 5000
    }

    # Performans raporu
    df = pd.DataFrame(list(portfoy.items()), columns=['Varlık', 'Değer'])

    # Performans raporunu Excel'e kaydet
    df.to_excel('portfoy_performans_raporu.xlsx', index=False)
    
    # Varlıkların pasta grafiği
    plt.figure(figsize=(6, 6))
    plt.pie(df['Değer'], labels=df['Varlık'], autopct='%1.1f%%', startangle=90, colors=['gold', 'blue', 'green', 'red', 'purple'])
    plt.title("Portföy Dağılımı")
    plt.axis('equal')  # Eşit eksen oranı ile pasta grafiğini dairesel yapar
    plt.savefig('portfoy_dagilimi.png')
    plt.show()

    print("Performans raporu ve grafiği oluşturuldu.")

if __name__ == "__main__":
    performans_takibi()