import pandas as pd
import matplotlib.pyplot as plt

# First I need to transforms my Excel files into CVS files.
# This is useful when you have more than one worksheet in your Excel file.

excel_file = 'superstore_data.xls'
xls = pd.ExcelFile(excel_file)

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name)
    df.to_csv(f"{sheet_name}.csv", index=False)
    print(f"sheet '{sheet_name}' save as {sheet_name}.csv")

# Before save the files, the data needs to be cleaned.

for sheet_name in xls.sheet_names:
    df = pd.read_csv(f"{sheet_name}.csv")

    
    print(f"Original data in '{sheet_name}': {df.shape}")

    # Remove duplicates
    df = df.drop_duplicates()

    # Delete empty columns
    df = df.dropna(axis=1, how='all')

    # Delete rows with empty values
    df = df.dropna(axis=0, how='all')

    # Check for missing values
    missing = df.isnull().sum()
    print(f"Missing values ​​in '{sheet_name}':\n{missing[missing > 0]}")

    # And finally save the file, and We are ready to start working with the data
    df.to_csv(f"{sheet_name}_clean.csv", index=False)
    print(f"Clean file saved as {sheet_name}_clean.csv\n")




