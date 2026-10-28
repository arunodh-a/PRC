import pandas as pd
import os

if not os.path.exists("students.csv"):
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Score': [85, 92, 78, 90, 88]}
    pd.DataFrame(data).to_csv("students.csv", index=False)
    print("Created sample 'students.csv' file.\n")

file_path = "students.csv"

try:
    df = pd.read_csv(file_path)
    print("CSV file loaded successfully!\n")
except FileNotFoundError:
    print("Error: File not found. Please check that 'students.csv' exists.")
    exit()

print("First 5 rows of the DataFrame:")
print(df.head())

if 'Score' in df.columns:
    if pd.api.types.is_numeric_dtype(df['Score']):
        score_mean = df['Score'].mean()
        print(f"\nMean of the 'Score' column: {score_mean}")
    else:
        print("\n'Score' column is not numeric. Cannot calculate mean.")
else:
    print("\n'Score' column not found in the DataFrame.")