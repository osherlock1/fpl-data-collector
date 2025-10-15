import pandas as pd

# URL of the CSV file (example)
filepath = "/Users/omalleysherlock/Documents/Developer/fpl-data-collector/fpl_training_data/merged_gw.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(filepath)


# Basic info
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

# Summary statistics for numeric columns
print("\nSummary statistics:\n", df.describe())

# Count of unique players
print("\nUnique players:", df['name'].nunique())

# Top 5 players by total points (if 'total_points' exists)
if 'total_points' in df.columns:
    print("\nTop 5 players by total points:\n", df.groupby('name')['total_points'].sum().sort_values(ascending=False).head())