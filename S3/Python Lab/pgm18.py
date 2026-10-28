import pandas as pd
import os

if not os.path.exists("students.csv"):
    data = {
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
        'Score': [85, 90, 85, 78, 90]
    }
    pd.DataFrame(data).to_csv("students.csv", index=False)
    print("Created sample 'students.csv' with duplicate entries.\n")

file_path = "students.csv"

try:
    df = pd.read_csv(file_path)
    print("Original DataFrame:")
    print(df)
except FileNotFoundError:
    print("File not found. Please make sure the CSV file exists.")
    exit()

df_cleaned = df.drop_duplicates()

print("\nCleaned DataFrame (duplicates removed):")
print(df_cleaned)