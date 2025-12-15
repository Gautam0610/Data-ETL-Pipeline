import pandas as pd

# Read the CSV file
df = pd.read_csv("data/input.csv")

# Drop rows with any null values
df = df.dropna()

# Save the cleaned data to a JSON file
df.to_json("data/output.json", orient="records")

print("ETL process complete. Output saved to data/output.json")