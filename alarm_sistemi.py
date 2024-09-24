import tkinter as tk
import time
import pygame  # Sesli uyarı için pygame modülü

class AlarmSistemi:
    def __init__(self, root):
        self.root = root
        self.alarm_acik = False
        self.root.title("Alarm Sistemi Kontrol Paneli")

        # Açma/Kapatma butonu
        self.button = tk.Button(root, text="Alarmı Aç", command=self.alarmi_ac_kapat)
        self.button.pack(pady=20)

        # Durum etiketi
        self.durum_label = tk.Label(root, text="Alarm Kapalı", fg="red")
        self.durum_label.pack(pady=10)

        # Fiyat tahmini ve risk yönetimi butonları
        self.fiyat_tahmini_button = tk.Button(root, text="Fiyat Tahmini Yap", command=self.fiyat_tahmini)
        self.fiyat_tahmini_button.pack(pady=10)
        
        self.risk_yonetimi_button = tk.Button(root, text="Risk Yönetimi", command=self.risk_yonetimi)
        self.risk_yonetimi_button.pack(pady=10)

    def alarmi_ac_kapat(self):
        if self.alarm_acik:
            self.alarmi_kapat()
        else:
            self.alarmi_ac()

    def alarmi_ac(self):
        self.alarm_acik = True
        self.durum_label.config(text="Alarm Açık", fg="green")
        self.button.config(text="Alarmı Kapat")
        self.alarm_sistemi()

    def alarmi_kapat(self):
        self.alarm_acik = False
        self.durum_label.config(text="Alarm Kapalı", fg="red")
        self.button.config(text="Alarmı Aç")
        pygame.mixer.music.stop()  # Alarmı kapatınca müziği durdur

    def alarm_sistemi(self):
        print("Alarm sistemi başlatılıyor...")

        varliklar = {
            'BTC-USD': 0.05,
            'ETH-USD': 0.03,
            'BNB-USD': 0.08,
            'SOL-USD': 0.04
        }

        risk_limiti = 0.07

        for varlik, risk in varliklar.items():
            if risk > risk_limiti and self.alarm_acik:
                print(f"Uyarı! {varlik} için risk seviyesi yüksek: {risk}.")
                pygame.mixer.init()  # Pygame ses modülünü başlat
                pygame.mixer.music.load("/Users/ozguralikci/Desktop/Finans_Proje/alarm.mp3")
                pygame.mixer.music.play()

        print("Alarm sistemi tamamlandı. Terminale geri dönülüyor.")
        time.sleep(2)

    def fiyat_tahmini(self):
        print("Fiyat tahmini modülü çalışıyor...")
        # Buraya fiyat tahmin modülünden çağrılacak kodu ekleyeceğiz.

    def risk_yonetimi(self):
        print("Risk yönetimi modülü çalışıyor...")
        # Buraya risk yönetimi modülünden çağrılacak kodu ekleyeceğiz.

if __name__ == "__main__":
    root = tk.Tk()
    alarm = AlarmSistemi(root)
    root.mainloop()