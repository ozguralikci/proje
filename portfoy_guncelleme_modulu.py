import pandas as pd
import requests
from datetime import datetime

# Güncel kripto para fiyatlarını almak için CoinGecko API'yi kullanıyoruz
def get_current_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether,binancecoin,solana&vs_currencies=usd"
    response = requests.get(url)
    return response.json()

# Portföy güncelleme işlemi
def update_portfolio():
    print("Portföy güncelleniyor...")
    
    current_prices = get_current_prices()

    # Portföydeki varlıklar ve oranları
    portfolio = {
        'Bitcoin': 50000,
        'Ethereum': 30000,
        'Tether': 10000,
        'BNB': 15000,
        'Solana': 5000
    }
    
    # Her bir varlığın güncel fiyatlarını alıyoruz
    for varlik in portfolio.keys():
        api_key = varlik.lower()
        if api_key == 'bnb':
            api_key = 'binancecoin'  # Binance Coin için doğru anahtar
        portfolio[varlik] = current_prices[api_key]['usd'] * portfolio[varlik] / 1000

    # Güncellenmiş portföy verilerini Excel'e kaydediyoruz
    df = pd.DataFrame(list(portfolio.items()), columns=['Varlık', 'Değer'])
    df.to_excel('guncellenmis_portfoy.xlsx', index=False)
    
    print(f"Portföy başarıyla güncellendi: {datetime.now()}")

if __name__ == "__main__":
    update_portfolio()