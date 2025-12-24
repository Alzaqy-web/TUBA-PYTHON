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