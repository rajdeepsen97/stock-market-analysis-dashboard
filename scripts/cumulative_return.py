import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("../data/final_processed/clean_stock_data.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Sort dataset
df = df.sort_values(by=['ticker', 'date'])

# Store final returns
performance = []

# Dictionary for cumulative data
cumulative_data = {}

# Group by stock ticker
grouped = df.groupby("ticker")

for ticker, data in grouped:

    # Sort by date
    data = data.sort_values("date")

    # Daily returns
    data['daily_return'] = data['close'].pct_change()

    # Cumulative return
    data['cumulative_return'] = (
        1 + data['daily_return']
    ).cumprod()

    # Final cumulative return
    final_return = data['cumulative_return'].iloc[-1]

    performance.append({
        "ticker": ticker,
        "final_return": final_return
    })

    cumulative_data[ticker] = data

# Create performance dataframe
performance_df = pd.DataFrame(performance)

# Top 5 performing stocks
top_5 = performance_df.sort_values(
    by='final_return',
    ascending=False
).head(5)

print("\nTOP 5 PERFORMING STOCKS")
print(top_5)

# -----------------------------
# LINE CHART
# -----------------------------

plt.figure(figsize=(14,7))

for ticker in top_5['ticker']:

    stock_data = cumulative_data[ticker]

    plt.plot(
        stock_data['date'],
        stock_data['cumulative_return'],
        label=ticker
    )

plt.title("Cumulative Return of Top 5 Performing Stocks")

plt.xlabel("Date")
plt.ylabel("Cumulative Return")

plt.legend()

plt.grid(True)

plt.tight_layout()

# Save chart
plt.savefig("../outputs/cumulative_return_chart.png")

plt.show()

# Save top 5 data
top_5.to_csv(
    "../outputs/top_5_performing_stocks.csv",
    index=False
)

print("\nCumulative return analysis completed successfully")