import tkinter as tk
from tkinter import ttk
import importlib

class AnaKontrolPaneli:
    def __init__(self, master):
        self.master = master
        master.title("Finansal Analiz ve Portföy Yönetimi Sistemi")
        
        # Ana çerçeve
        main_frame = ttk.Frame(master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Modül butonları
        self.create_module_button(main_frame, "Portföy Analizi", "portfoy_analiz_modulu")
        self.create_module_button(main_frame, "Risk Yönetimi", "risk_yonetimi_modulu")
        self.create_module_button(main_frame, "Fiyat Tahmini", "fiyat_tahmin_modulu")
        self.create_module_button(main_frame, "Haber Analizi", "haber_analizi")
        self.create_module_button(main_frame, "Teknik Analiz", "teknik_analiz_modulu")
        self.create_module_button(main_frame, "Veri Güncelleme", "otomatik_guncelleme_modulu")
        
    def create_module_button(self, parent, text, module_name):
        button = ttk.Button(parent, text=text, command=lambda: self.run_module(module_name))
        button.pack(pady=5, fill=tk.X)
        
    def run_module(self, module_name):
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, 'main'):
                module.main()
            else:
                print(f"{module_name} modülünde 'main' fonksiyonu bulunamadı.")
        except ImportError:
            print(f"{module_name} modülü yüklenemedi.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnaKontrolPaneli(root)
    root.mainloop()
