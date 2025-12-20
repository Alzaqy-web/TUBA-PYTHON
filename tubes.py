import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('1. aapl.csv', parse_dates=['Date'])

df['MA20'] = df['Adj Close'].rolling(20).mean()
df['MA100'] = df['Adj Close'].rolling(100).mean()


# Analisis Time Series
plt.figure(figsize=(10,4))
plt.plot(df['Date'], df['Adj Close'])
plt.title('Time Series Harga AAPL')
plt.xlabel('Waktu')
plt.ylabel('Harga')
plt.show()

# Analisis Teknikal Indikator
plt.plot(df['Date'], df['Adj Close'], alpha=0.5, label='Harga')
plt.plot(df['Date'], df['MA20'], label='MA 20')
plt.plot(df['Date'], df['MA100'], label='MA 100')
plt.legend()
plt.title('Trend Harga AAPL')
plt.show()

# Analisis Volatilitas
plt.plot(df['Date'], df['Adj Close'].pct_change().rolling(window=20).std() * 100)
plt.title('Volatilitas Harian AAPL')
plt.xlabel('Waktu')
plt.grid(True)
plt.ylabel('Volatilitas (%)')
plt.show()

# Analisis Tren
plt.plot(df['Date'], df['Close'], label='Harga Penutupan (Close Price)', color='blue')
plt.title('Tren Harga Saham', fontsize=16) # Menambahkan judul
plt.xlabel('Tanggal', fontsize=14) # Menambahkan label sumbu X
plt.ylabel('Harga (USD)', fontsize=14) # Menambahkan label sumbu Y
plt.grid(True, linestyle='-.', linewidth=0.5) # Menambahkan grid
plt.legend() # Menampilkan legenda
plt.show()



# analisis 
# 1. time series
# 2. indikator teknikal
# 3. volatilitas
# 4. tren