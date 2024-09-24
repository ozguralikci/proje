import importlib
import logging
from functools import wraps

# Hata yönetimi ve loglama ayarları
logging.basicConfig(filename='finansal_analiz.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def hata_yonetimi(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"{func._name_} fonksiyonunda hata: {str(e)}")
            raise
    return wrapper

def load_module(module_name):
    return importlib.import_module(module_name)

class FinansalAnalizSistemi:
    def _init_(self):
        self.veri_modulu = load_module('Veri_cek')
        self.analiz_modulu = load_module('Teknik_analiz_modulu')
        self.portfoy_modulu = load_module('Portfoy_yonetimi_modulu')
        self.risk_modulu = load_module('Risk_yonetimi_modulu')
        self.strateji_modulu = load_module('Yatirim_stratejisi_modulu')
        self.tahmin_modulu = load_module('Tahmin_modulu')
        self.haber_modulu = load_module('Haber_cek')
        self.performans_modulu = load_module('Performans_takibi_modulu')
        self.alarm_modulu = load_module('Alarm_sistemi')
        self.excel_modulu = load_module('Excel_arayuz_olustur')

    @hata_yonetimi
    def veri_topla(self):
        print("Veri toplama işlemi başlatılıyor...")
        return self.veri_modulu.btc_altcoin_veri_cek()

    @hata_yonetimi
    def teknik_analiz(self, veri):
        print("Teknik analiz yapılıyor...")
        return self.analiz_modulu.teknik_analiz_yap(veri)

    @hata_yonetimi
    def risk_degerlendirmesi(self, portfoy):
        print("Risk değerlendirmesi yapılıyor...")
        return self.risk_modulu.risk_degerlendir(portfoy)

    @hata_yonetimi
    def portfoy_olustur(self, risk_degerlendirmesi):
        print("Portföy oluşturuluyor...")
        return self.portfoy_modulu.portfoy_olustur(risk_degerlendirmesi)

    @hata_yonetimi
    def strateji_olustur(self):
        print("Yatırım stratejisi oluşturuluyor...")
        return self.strateji_modulu.yatirim_stratejisi_olustur()

    @hata_yonetimi
    def fiyat_tahmini(self, veri):
        print("Fiyat tahmini yapılıyor...")
        return self.tahmin_modulu.fiyat_tahmin_et(veri)

    @hata_yonetimi
    def haber_analizi(self):
        print("Haber analizi yapılıyor...")
        haberler = self.haber_modulu.finansal_haberleri_cek()
        return self.haber_modulu.haberlerden_duygu_analizi(haberler)

    @hata_yonetimi
    def performans_takibi(self, portfoy):
        print("Performans takibi yapılıyor...")
        return self.performans_modulu.performans_hesapla(portfoy)

    @hata_yonetimi
    def alarm_kur(self, kosullar):
        print("Alarm sistemi kuruluyor...")
        return self.alarm_modulu.alarm_kur(kosullar)

    @hata_yonetimi
    def excel_rapor_olustur(self, veriler):
        print("Excel raporu oluşturuluyor...")
        return self.excel_modulu.excel_rapor_olustur(veriler)

    @hata_yonetimi
    def run(self):
        veri = self.veri_topla()
        analiz_sonuclari = self.teknik_analiz(veri)
        portfoy = self.portfoy_olustur(analiz_sonuclari)
        risk_degerlendirmesi = self.risk_degerlendirmesi(portfoy)
        strateji = self.strateji_olustur()
        tahmin = self.fiyat_tahmini(veri)
        haber_analizi = self.haber_analizi()
        performans = self.performans_takibi(portfoy)
        
        # Alarm kurulumu (örnek)
        self.alarm_kur({'BTC': {'üst_limit': 50000, 'alt_limit': 30000}})
        
        # Tüm sonuçları Excel'e kaydet
        rapor_verileri = {
            'Analiz Sonuçları': analiz_sonuclari,
            'Portföy': portfoy,
            'Risk Değerlendirmesi': risk_degerlendirmesi,
            'Strateji': strateji,
            'Fiyat Tahmini': tahmin,
            'Haber Analizi': haber_analizi,
            'Performans': performans
        }
        self.excel_rapor_olustur(rapor_verileri)
        
        print("Finansal analiz tamamlandı. Sonuçlar Excel raporunda detaylı olarak sunulmuştur.")
        return strateji

if _name_ == "_main_":
    sistem = FinansalAnalizSistemi()
    sonuc = sistem.run()
    print("Önerilen Yatırım Stratejisi:", sonuc)