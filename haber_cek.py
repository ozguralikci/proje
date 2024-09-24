import requests
from newspaper import Article
from textblob import TextBlob
import logging

# NewsAPI'den haber çekme fonksiyonu
def finansal_haberleri_cek():
    api_key = "7b55fbd96ec346edbc4558f80bf0b7b4"
    url = f"https://newsapi.org/v2/everything?q=finance&language=tr&sortBy=publishedAt&apiKey={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        veriler = response.json()
        return veriler['articles'][:5]  # Son 5 haberi al
    else:
        logging.error(f"{url} haberleri çekilemedi.")
        return None

# Duygu analizi yapan fonksiyon
def haberlerden_duygu_analizi(haber_metin):
    blob = TextBlob(haber_metin)
    olumlu = sum(1 for sent in blob.sentences if sent.sentiment.polarity > 0)
    olumsuz = sum(1 for sent in blob.sentences if sent.sentiment.polarity < 0)
    notr = sum(1 for sent in blob.sentences if sent.sentiment.polarity == 0)
    return olumlu, olumsuz, notr

# Haberlere göre duygu analizini ve etkisini görselleştirme
def haber_analizi_gorsellestir(haberler):
    olumlu_sayilari = []
    olumsuz_sayilari = []
    notr_sayilari = []
    haber_basliklari = []

    for haber in haberler:
        try:
            article = Article(haber['url'])
            article.download()
            article.parse()
            haber_metin = article.text

            olumlu, olumsuz, notr = haberlerden_duygu_analizi(haber_metin)
            olumlu_sayilari.append(olumlu)
            olumsuz_sayilari.append(olumsuz)
            notr_sayilari.append(notr)
            haber_basliklari.append(haber['title'])

            print(f"Haber Başlığı: {haber['title']}")
            print(f"Olumlu: {olumlu}, Olumsuz: {olumsuz}, Nötr: {notr}\n")

        except Exception as e:
            logging.error(f"Haber metni çekilemedi: {haber['url']} - {e}")

    # Grafik oluşturma
    try:
        import matplotlib.pyplot as plt
        x = range(len(haber_basliklari))
        plt.bar(x, olumlu_sayilari, label='Olumlu', color='green', alpha=0.6)
        plt.bar(x, olumsuz_sayilari, bottom=olumlu_sayilari, label='Olumsuz', color='red', alpha=0.6)
        plt.bar(x, notr_sayilari, bottom=[i + j for i, j in zip(olumlu_sayilari, olumsuz_sayilari)], label='Nötr', color='blue', alpha=0.6)
        plt.xticks(x, haber_basliklari, rotation=90)
        plt.legend()
        plt.tight_layout()
        plt.show()
    except ImportError:
        logging.error("Matplotlib yüklü değil, grafik oluşturulamadı.")

# Test etmek için fonksiyon çağrısı
if __name__ == "__main__":
    haberler = finansal_haberleri_cek()
    if haberler:
        haber_analizi_gorsellestir(haberler)