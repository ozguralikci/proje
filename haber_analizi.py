import requests
from textblob import TextBlob
import pandas as pd

# NewsAPI'den haber çekme fonksiyonu
def finansal_haberleri_cek(api_key, sorgu="finance", dil="tr"):
    url = f"https://newsapi.org/v2/everything?q={sorgu}&language={dil}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        haberler = response.json().get('articles', [])
        return haberler
    else:
        print(f"Veri çekilemedi, hata kodu: {response.status_code}")
        return None

# Duygu analizi fonksiyonu
def duygu_analizi(haber_metni):
    blob = TextBlob(haber_metni)
    olumlu = sum(1 for cümle in blob.sentences if cümle.sentiment.polarity > 0)
    olumsuz = sum(1 for cümle in blob.sentences if cümle.sentiment.polarity < 0)
    return olumlu, olumsuz

# Haber sonuçlarını kaydetme
def haber_sonuclari_kaydet(haberler, sonuclar):
    df = pd.DataFrame(sonuclar)
    with pd.ExcelWriter('finansal_analiz_projesi.xlsx', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='Haber Analizi', index=False)
    print("Haber analizi sonuçları başarıyla kaydedildi!")

# Haber Analizi Modülü
if __name__ == "__main__":
    api_key = "YOUR_NEWSAPI_KEY"
    
    # Haberleri çek
    haberler = finansal_haberleri_cek(api_key)
    
    if haberler:
        sonuclar = []
        for haber in haberler:
            try:
                haber_metni = haber['content'] if haber['content'] else ""
                olumlu, olumsuz = duygu_analizi(haber_metni)
                sonuclar.append({
                    'Başlık': haber['title'],
                    'Yayınlanma Tarihi': haber['publishedAt'],
                    'Olumlu Cümle Sayısı': olumlu,
                    'Olumsuz Cümle Sayısı': olumsuz
                })
            except Exception as e:
                print(f"Haber analiz edilirken hata oluştu: {e}")
        
        # Sonuçları kaydet
        haber_sonuclari_kaydet(haberler, sonuclar)