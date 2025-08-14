"""#!venv/bin/python
what is the command here to run a virtual env but use the built in python,
not package up python which this seems to do
"""

"""
This opens a csv file and saves it
out as an Excel xlsx format.
poppy riddle feb 14, 2024
version 1.0
"""

import pandas as pd
from colorama import Fore

# Read the CSV file
print(Fore.GREEN + "Enter your CSV filename (without .csv extension): ")
# Remove the .csv extension from the input
csv_filename = input().rstrip('.csv')
data = pd.read_csv(csv_filename + '.csv')

# Save as Excel XLSX file and add the .xlsx extension
excel_filename = f"{csv_filename}.xlsx"
data.to_excel(excel_filename, index=False, sheet_name='Sheet1')

# resets color and prints completion message
print('\033[39m')
print(f"Data has been saved to {excel_filename}")
