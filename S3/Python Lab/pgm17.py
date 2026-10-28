import pandas as pd
import os

if not os.path.exists("students.csv"):
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Score': [85, 90, 78, 92, 88]
    }
    pd.DataFrame(data).to_csv("students.csv", index=False)
    print("Created sample 'students.csv' file.\n")

file_path = "students.csv"

try:
    df = pd.read_csv(file_path)
    print("CSV file loaded successfully.\n")
except FileNotFoundError:
    print("File not found. Please make sure 'students.csv' is in the correct directory.")
    exit()

print("First 5 rows of the dataset:")
print(df.head())

column_name = 'Score'

if column_name in df.columns:
    if pd.api.types.is_numeric_dtype(df[column_name]):
        col_sum = df[column_name].sum()
        col_mean = df[column_name].mean()
        col_std = df[column_name].std()

        print(f"\nData Analysis for column '{column_name}':")
        print(f"Sum: {col_sum}")
        print(f"Mean: {col_mean}")
        print(f"Standard Deviation: {col_std:.2f}")
    else:
        print(f"Column '{column_name}' is not numeric.")
else:
    print(f"Column '{column_name}' not found in the dataset.")