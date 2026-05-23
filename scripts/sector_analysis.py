import pandas as pd
import matplotlib.pyplot as plt




# LOAD STOCK DATA
stock_df = pd.read_csv(
    "../data/final_processed/clean_stock_data.csv"
)




# Convert date column
stock_df['date'] = pd.to_datetime(stock_df['date'])





# LOAD SECTOR DATA
sector_df = pd.read_csv(
    "../data/Sector_data - Sheet1.csv"
)

print("\nSECTOR DATA")
print(sector_df.head())





# CLEAN SYMBOL COLUMN
# Extract ticker after colon
sector_df['ticker'] = sector_df['Symbol'].str.split(":").str[-1]

# Remove spaces
sector_df['ticker'] = sector_df['ticker'].str.strip()

print("\nCLEANED TICKERS")
print(sector_df[['Symbol', 'ticker']].head())






# CALCULATE YEARLY RETURNS
results = []

grouped = stock_df.groupby("ticker")

for ticker, data in grouped:

    data = data.sort_values("date")

    first_close = data.iloc[0]["close"]
    last_close = data.iloc[-1]["close"]

    yearly_return = (
        (last_close - first_close)
        / first_close
    ) * 100

    results.append({
        "ticker": ticker,
        "yearly_return": yearly_return
    })

returns_df = pd.DataFrame(results)








# MERGE WITH SECTOR DATA
merged_df = pd.merge(
    returns_df,
    sector_df,
    on="ticker",
    how="inner"
)

print("\nMERGED DATA")
print(merged_df.head())

# SECTOR-WISE PERFORMANCE


sector_performance = merged_df.groupby(
    "sector"
)["yearly_return"].mean().reset_index()

# Sort values
sector_performance = sector_performance.sort_values(
    by="yearly_return",
    ascending=False
)

print("\nSECTOR PERFORMANCE")
print(sector_performance)







# BAR CHART
plt.figure(figsize=(14,6))

plt.bar(
    sector_performance['sector'],
    sector_performance['yearly_return']
)

plt.title("Average Yearly Return by Sector")

plt.xlabel("Sector")
plt.ylabel("Average Yearly Return (%)")

plt.xticks(rotation=45)

plt.tight_layout()








# Save chart
plt.savefig("../outputs/sector_performance_chart.png")

plt.show()

# Save CSV
sector_performance.to_csv(
    "../outputs/sector_performance.csv",
    index=False
)

print("\nSector analysis completed successfully")