import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns







# LOAD DATA
df = pd.read_csv(
    "../data/final_processed/clean_stock_data.csv"
)







# Convert date column
df['date'] = pd.to_datetime(df['date'])







# CREATE PIVOT TABLE
pivot_df = df.pivot_table(
    index='date',
    columns='ticker',
    values='close'
)

print("\nPIVOT TABLE")
print(pivot_df.head())








# CORRELATION MATRIX
correlation_matrix = pivot_df.corr()

print("\nCORRELATION MATRIX")
print(correlation_matrix.head())








# HEATMAP
plt.figure(figsize=(18,12))

sns.heatmap(
    correlation_matrix,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Stock Correlation Heatmap")

plt.tight_layout()







# Save chart
plt.savefig("../outputs/correlation_heatmap.png")

plt.show()

print("\nCorrelation heatmap created successfully")