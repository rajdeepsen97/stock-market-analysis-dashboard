import pandas as pd

# Load extracted dataset
df = pd.read_csv("../data/final_processed/all_stock_data.csv")

print("INITIAL DATA")
print(df.head())

print("\nDATA INFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Rename columns to lowercase
df.columns = df.columns.str.lower()

# Convert numeric columns
numeric_cols = ['open', 'close', 'high', 'low', 'volume']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remove rows with missing values
df.dropna(inplace=True)

# Sort by ticker and date
df = df.sort_values(by=['ticker', 'date'])

print("\nCLEANED DATA")
print(df.head())

print("\nFINAL SHAPE")
print(df.shape)

# Save cleaned dataset
df.to_csv(
    "../data/final_processed/clean_stock_data.csv",
    index=False
)

print("\nCleaned dataset saved successfully")