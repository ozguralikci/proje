import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_currency_rates():
    url = 'https://www.tcmb.gov.tr/kurlar/today.xml'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')

    currency_data = []
    for currency in soup.find_all('Currency'):
        code = currency['CurrencyCode']
        name = currency.find('CurrencyName').text
        forex_buying = currency.find('ForexBuying').text
        forex_selling = currency.find('ForexSelling').text
        currency_data.append([code, name, forex_buying, forex_selling])

    df = pd.DataFrame(currency_data, columns=['Kod', 'Para Birimi', 'Alış Fiyatı', 'Satış Fiyatı'])
    return df

def update_data():
    logging.info("Veri güncelleniyor...")
    start_time = time.time()
    
    currency_data = get_currency_rates()

    with pd.ExcelWriter('finansal_analiz_projesi.xlsx', mode='a', if_sheet_exists='replace') as writer:
        currency_data.to_excel(writer, sheet_name='Döviz Verileri', index=False)

    logging.info(f"Veriler başarıyla güncellendi! Güncelleme tamamlandı. Geçen süre: {round(time.time() - start_time, 2)} saniye.")

if __name__ == "__main__":
    update_data()