import os
import yaml
import pandas as pd

# Input folder containing monthly YAML folders
DATA_FOLDER = "../data/raw_yaml"

# Output CSV file
OUTPUT_FILE = "../data/final_processed/all_stock_data.csv"

all_data = []

# Traverse all folders and files
for root, dirs, files in os.walk(DATA_FOLDER):

    for file in files:

        # Check YAML files
        if file.endswith(".yaml") or file.endswith(".yml"):

            file_path = os.path.join(root, file)

            print(f"Reading: {file}")

            try:
                with open(file_path, "r", encoding="utf-8") as f:

                    data = yaml.safe_load(f)

                    # If YAML contains list
                    if isinstance(data, list):

                        for row in data:
                            all_data.append(row)

                    # If YAML contains dictionary
                    elif isinstance(data, dict):

                        all_data.append(data)

            except Exception as e:
                print(f"Error reading {file}: {e}")

# Convert to DataFrame
df = pd.json_normalize(all_data)

# Show first 5 rows
print("\nFIRST 5 ROWS:")
print(df.head())

# Save CSV
df.to_csv(OUTPUT_FILE, index=False)

print("\nCSV file created successfully")
print(f"Total records: {len(df)}")