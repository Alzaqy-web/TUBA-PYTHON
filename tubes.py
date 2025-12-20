import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('1. aapl.csv')

df['MA20'] = df['Adj Close'].rolling(20).mean()
df['MA100'] = df['Adj Close'].rolling(100).mean()
df['Return'] = df['Adj Close'].pct_change()



# plt.figure(figsize=(10,4))
# plt.plot(df['Date'], df['Adj Close'])
# plt.title('Time Series Harga AAPL')
# plt.xlabel('Waktu')
# plt.ylabel('Harga')
# plt.show()

plt.plot(df['Date'], df['Adj Close'], alpha=0.5, label='Harga')
plt.plot(df['Date'], df['MA20'], label='MA 20')
plt.plot(df['Date'], df['MA100'], label='MA 100')
plt.legend()
plt.title('Trend Harga AAPL')
plt.show()

# plt.plot(df['Date'], df['Return'])
# plt.title('Return Harian AAPL')
# plt.show()


