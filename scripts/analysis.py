import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/final_processed/clean_stock_data.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Group by ticker
grouped = df.groupby("ticker")

results = []

# Calculate yearly return
for ticker, data in grouped:

    # Sort by date
    data = data.sort_values("date")

    # First and last closing price
    first_close = data.iloc[0]["close"]
    last_close = data.iloc[-1]["close"]

    # Yearly return %
    yearly_return = ((last_close - first_close) / first_close) * 100

    # Average metrics
    avg_price = data["close"].mean()
    avg_volume = data["volume"].mean()

    results.append({
        "ticker": ticker,
        "yearly_return": yearly_return,
        "avg_price": avg_price,
        "avg_volume": avg_volume
    })

# Create DataFrame
result_df = pd.DataFrame(results)

# -------------------------
# TOP 10 GREEN STOCKS
# -------------------------

top_10_green = result_df.sort_values(
    by="yearly_return",
    ascending=False
).head(10)

print("\nTOP 10 GREEN STOCKS")
print(top_10_green)

# -------------------------
# TOP 10 RED STOCKS
# -------------------------

top_10_red = result_df.sort_values(
    by="yearly_return",
    ascending=True
).head(10)

print("\nTOP 10 RED STOCKS")
print(top_10_red)

# -------------------------
# MARKET SUMMARY
# -------------------------

green_stocks = result_df[result_df["yearly_return"] > 0].shape[0]

red_stocks = result_df[result_df["yearly_return"] < 0].shape[0]

overall_avg_price = result_df["avg_price"].mean()

overall_avg_volume = result_df["avg_volume"].mean()

print("\nMARKET SUMMARY")
print(f"Green Stocks: {green_stocks}")
print(f"Red Stocks: {red_stocks}")
print(f"Average Stock Price: {overall_avg_price:.2f}")
print(f"Average Volume: {overall_avg_volume:.2f}")

# Save summary
result_df.to_csv(
    "../outputs/stock_performance_summary.csv",
    index=False
)

print("\nStock performance analysis completed successfully")