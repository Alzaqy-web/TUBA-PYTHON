import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ASUMSI: Data Anda sudah disimpan dalam file CSV.


# 1. Memuat Data
df = pd.read_csv('1. aapl.csv')

# 2. Mengubah kolom Date menjadi format tanggal
df['Date'] = pd.to_datetime(df['Date'])

# 3. Menetapkan kolom Date sebagai indeks
df = df.set_index('Date')

# 4. Memastikan data terurut berdasarkan tanggal
df = df.sort_index()

print("Data berhasil dimuat. Lima baris pertama:")
print(df.head())

#  Visualisasi Data Harga Penutupan 
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['Close'], label='Harga Penutupan Saham', color='blue')
plt.title('Grafik Deret Waktu (Time Series) Harga Penutupan')
plt.xlabel('Tanggal')
plt.ylabel('Harga (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Hitung Simple Moving Average (SMA) 50 hari
# 'rolling(window=50)' mengambil rata-rata 50 hari sebelumnya untuk setiap titik
df['SMA_50_Hari'] = df['Close'].rolling(window=50).mean()

plt.figure(figsize=(14, 6))
plt.plot(df['Close'], label='Harga Penutupan Harian', color='blue', alpha=0.5)
plt.plot(df['SMA_50_Hari'], label='Tren (SMA 50 Hari)', color='red', linestyle='--')
plt.title('Analisis Tren Menggunakan Moving Average')
plt.xlabel('Tanggal')
plt.ylabel('Harga (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Hitung Daily Return (Persentase perubahan harian)
df['Daily_Return'] = df['Close'].pct_change() * 100

# Hitung Volatilitas 20 hari (Rolling Standard Deviation)
df['Volatilitas_20d'] = df['Daily_Return'].rolling(window=20).std()

# analisis Volatilitas (Standar Deviasi dari Return Harian)
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['Volatilitas_20d'], label='Volatilitas Bergulir (20 hari)', color='orange')
plt.title('Analisis Volatilitas Harian')
plt.xlabel('Tanggal')
plt.ylabel('Standar Deviasi Return Harian (%)')
plt.legend()
plt.grid(True)
plt.show()


# Fungsi bantuan untuk menghitung RSI (ini sedikit lebih kompleks secara rumus)
def calculate_rsi(df, window=14): # def = adalah
    delta = df['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

df = calculate_rsi(df)

plt.figure(figsize=(14, 4))
plt.plot(df.index, df['RSI'], label='RSI 14 Hari', color='purple')
plt.axhline(70, linestyle='--', alpha=0.5, color='red', label='Overbought (70)')
plt.axhline(30, linestyle='--', alpha=0.5, color='green', label='Oversold (30)')
plt.title('Indikator Teknikal: Relative Strength Index (RSI)')
plt.legend()
plt.grid(True)
plt.show()