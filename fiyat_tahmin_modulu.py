import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import requests

# Veri çekme fonksiyonu
def veri_cek(kripto_url):
    response = requests.get(kripto_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Veri çekilemedi, Hata kodu: {response.status_code}")
        return None

# LSTM modelini oluşturma
def lstm_model_olustur(girdi_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(girdi_shape[1], girdi_shape[2])))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Veriyi işleme ve model eğitimi
def fiyat_tahmin_et(kripto_url, epochs=50, batch_size=32):
    # Veri çekme
    veri = veri_cek(kripto_url)
    if veri is None:
        return
    
    fiyatlar = [float(v['usd']) for v in veri.values()]
    df = pd.DataFrame(fiyatlar, columns=["Fiyat"])
    
    # Veriyi normalize etme
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df)
    
    # Eğitim ve test seti oluşturma
    if len(scaled_data) < 60:
        print("Veri seti çok küçük, daha fazla veri gerekli.")
        return
    
    egitim_verisi = scaled_data[:len(scaled_data) - 60]
    test_verisi = scaled_data[-60:]
    
    x_train, y_train = [], []
    for i in range(60, len(egitim_verisi)):
        x_train.append(egitim_verisi[i-60:i])
        y_train.append(egitim_verisi[i])
    
    # Eğer eğitim verisi yetersizse hata verelim
    if len(x_train) == 0:
        print("Eğitim verisi oluşturulamadı. Veri yetersiz.")
        return
    
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    
    # Model oluşturma ve eğitme
    model = lstm_model_olustur(x_train.shape)
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
    
    # Tahmin yapma
    tahminler = model.predict(np.reshape(test_verisi, (1, test_verisi.shape[0], 1)))
    tahmin_fiyat = scaler.inverse_transform(tahminler)
    
    print(f"Tahmin edilen fiyat: {tahmin_fiyat[-1]}")

if __name__ == "__main__":
    kripto_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    fiyat_tahmin_et(kripto_url)