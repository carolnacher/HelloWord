

import pandas as pd
import matplotlib.pyplot as plt

# This script will transform Excel files into CSV files and clean the data.
# It will remove duplicate rows, columns with all NaN values, and rows with all NaN values.
# It will also print the number of missing values in each column.

excel_file = 'superstore_data.xls'
xls = pd.ExcelFile(excel_file)

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name)
    df.to_csv(f"{sheet_name}.csv", index=False)
    print(f"sheet '{sheet_name}' save as {sheet_name}.csv")



for sheet_name in xls.sheet_names:
    df = pd.read_csv(f"{sheet_name}.csv")

    
    print(f"Original data in '{sheet_name}': {df.shape}")

    
    df = df.drop_duplicates()

   
    df = df.dropna(axis=1, how='all')

    
    df = df.dropna(axis=0, how='all')

    
    missing = df.isnull().sum()
    print(f"Missing values ​​in '{sheet_name}':\n{missing[missing > 0]}")

    
    df.to_csv(f"{sheet_name}_clean.csv", index=False)
    print(f"Clean file saved as {sheet_name}_clean.csv\n")
