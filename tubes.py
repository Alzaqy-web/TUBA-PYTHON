import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('1. aapl.csv', parse_dates=['Date'])

df['MA20'] = df['Adj Close'].rolling(20).mean()
df['MA100'] = df['Adj Close'].rolling(100).mean()

# Analisis Time Series
def visualisasi_timeseries (df):
    plt.figure(figsize=(10,4))
    plt.plot(df['Date'], df['Adj Close'])
    plt.title('Time Series Harga AAPL')
    plt.xlabel('Waktu')
    plt.ylabel('Harga')
    plt.show()

# Analisis Teknikal Indikator
def visulisasi_Teknilal_Indikator(df):
    plt.plot(df['Date'], df['Adj Close'], alpha=0.5, label='Harga')
    plt.plot(df['Date'], df['MA20'], label='MA 20 Hari')
    plt.plot(df['Date'], df['MA100'], label='MA 100 Hari')
    plt.legend()
    plt.title('Trend Harga AAPL')
    plt.show()

# Analisis Volatilitas
def visualisasi_volatilitas(df):
    plt.plot(df['Date'], df['Adj Close'].pct_change().rolling(window=20).std() * 100)
    plt.title('Volatilitas Harian AAPL')
    plt.xlabel('Waktu')
    plt.grid(True)
    plt.ylabel('Volatilitas (%)')
    plt.show()

# Analisis Tren
def analisis_tren(df):
    plt.plot(df['Date'], df['Close'], label='Harga Penutupan (Close Price)', color='blue')
    plt.title('Tren Harga Saham', fontsize=16) # Menambahkan judul
    plt.xlabel('Tanggal', fontsize=14) # Menambahkan label sumbu X
    plt.ylabel('Harga (USD)', fontsize=14) # Menambahkan label sumbu Y
    plt.grid(True, linestyle='-.', linewidth=0.5) # Menambahkan grid
    plt.legend() # Menampilkan legenda
    plt.show()
    
#Menampilkan 5 Column
def nampilincolum(df):
    while True:
        print("A. data terbesar")
        print("B. data terendah")
        sub = input("Pilih Data yang mau di tampilkan (A/B): ")
        
        if sub == "a":
            high = df.sort_values(by="High", ascending=False).head(5)
            print('\nTop data AAPL\n',high[["Date","Open", "High","Volume"]])
        elif sub == "b":
            Low = df.sort_values(by="Low",ascending=True).head(5)
            print("\nLowest Data AAPL\n",Low[["Date","Open","Low","Volume"]])
            break
        else:
            print("Salah input data")

#Fungsi Machine Learning
def machine_learning_prediksi(df):
    # Fitur dan target
    X = df[['Open', 'High', 'Low', 'Volume']]
    y = df['Close']

    # Split data train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Model Linear Regression
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Prediksi
    y_pred = model.predict(X_test)

    # Evaluasi
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.2f}")

    # Visualisasi hasil prediksi vs aktual
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'].iloc[-len(y_test):], y_test, label='Actual Close', color='blue')
    plt.plot(df['Date'].iloc[-len(y_test):], y_pred, label='Predicted Close', color='red', linestyle='--')
    plt.title('Prediksi Harga Saham AAPL (Linear Regression)')
    plt.xlabel('Tanggal')
    plt.grid(True, which='both', axis='both', linestyle='-', linewidth=1, color='gray')
    plt.ylabel('Harga (USD)')
    plt.legend()
    plt.show()
    
#Relative Strength Index mengetahui berlebihan beli/jual
def perkiraan_RSI(df, periode=14):
    delta = df['Adj Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    
    avg_gain = gain.rolling(window=periode).mean()
    avg_loss = loss.rolling(window=periode).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    df['RSI'] = rsi
    
    # Visual RSI
    plt.figure(figsize=(10,4))
    plt.plot(df['Date'], df["RSI"], label='RSI 14 Hari', color='blue')
    
    plt.axhline(70, color='red', linestyle='--', label='Overbought')
    plt.axhline(30, color='green', linestyle='--', label='Oversold')
    
    plt.title('Relative Strength Index')
    plt.xlabel('Waktu')
    plt.ylabel('RSI')
    plt.grid(True, which='both', axis='both', linestyle='-', linewidth=1, color='gray')
    plt.legend(loc='upper right')
    plt.show()

def candle(df):
    # Convert Date & jadikan index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Ambil kolom yang dibutuhkan
    df_candle = df[['Open', 'High', 'Low', 'Close', 'Volume']]

    # Plot candlestick
    mpf.plot(
        df_candle.tail(60),
        type='candle',
        volume=True,
        style='yahoo',
        title='Candlestick AAPL'
    )
    
        
while True:
    print("\n=== MENU ANALISIS SAHAM AAPL ===")
    print("1. Time Series")
    print("2. Indikator")
    print("3. Volatilitas")
    print("4. Tren")
    print("5. Memunculkan colum")
    print("6. Relative Strength Index (RSI)")
    print("7. Machine Learning")
    print("8. Candle Chart")
    print("Keluar")
    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        visualisasi_timeseries(df)
    elif pilihan == "2":
        visulisasi_Teknilal_Indikator(df)
    elif pilihan == "3":
        visualisasi_volatilitas(df)
    elif pilihan == "4":
        analisis_tren(df)
    elif pilihan == "5":
        nampilincolum(df)
    elif pilihan == "6":
        perkiraan_RSI(df)
    elif pilihan == "7":
        machine_learning_prediksi(df)
    elif pilihan == "8":
        candle(df)
    elif pilihan == "Keluar":
        print("Anda sudah keluar dari program")
        break
    else:
        print("Menu belum ditentukan")