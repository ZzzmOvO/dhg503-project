import yfinance as yf

ticker = "0038.HK"
data = yf.download(ticker, start="2024-01-01", end="2024-12-31")

date_close_only = data["Close"].reset_index()
date_close_only.columns = ["Date", "Close"]
print(date_close_only)

mean_price = date_close_only["Close"].mean()
median_price = date_close_only["Close"].median()
std_deviation = date_close_only["Close"].std()

print("Mean:", mean_price)
print("Median:", median_price)
print("Standard Deviation:", std_deviation)


target_price = mean_price + 1.96 * std_deviation
matched_dates = date_close_only[date_close_only["Close"] == target_price]

if matched_dates.empty:
    print("None")
else:
    sorted_dates = matched_dates.sort_values("Date", ascending=False)
    if len(sorted_dates) >= 3:
        third_highest_date = sorted_dates.iloc[2]["Date"].strftime("%Y-%m-%d")
        print(third_highest_date)
    else:
        print("None")
