import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("../data/final_processed/clean_stock_data.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Sort values
df = df.sort_values(by=['ticker', 'date'])

# Store volatility results
volatility_results = []

# Group by ticker
grouped = df.groupby("ticker")

for ticker, data in grouped:

    # Calculate daily returns
    data['daily_return'] = data['close'].pct_change()

    # Calculate volatility
    volatility = data['daily_return'].std()

    volatility_results.append({
        "ticker": ticker,
        "volatility": volatility
    })

# Create dataframe
volatility_df = pd.DataFrame(volatility_results)

# Top 10 volatile stocks
top_volatile = volatility_df.sort_values(
    by='volatility',
    ascending=False
).head(10)

print("\nTOP 10 MOST VOLATILE STOCKS")
print(top_volatile)

# -----------------------------
# BAR CHART
# -----------------------------

plt.figure(figsize=(12,6))

plt.bar(
    top_volatile['ticker'],
    top_volatile['volatility']
)

plt.title("Top 10 Most Volatile Stocks")
plt.xlabel("Stock Ticker")
plt.ylabel("Volatility")

plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig("../outputs/volatility_chart.png")

plt.show()

# Save data
top_volatile.to_csv(
    "../outputs/top_volatile_stocks.csv",
    index=False
)

print("\nVolatility analysis completed successfully")