#!/usr/bin/env python3.8
#!venv/bin/python

"""
This opens a csv file and saves it
out as an Excel xlsx format.
It cleans up the DOIs and URLs for a given prefix output file from 
customer db reports.
First you need to rename the file from xls extension to csv. 
Its really a tab seperated file!

poppy riddle feb 16, 2024
version 1.0
"""

# Run the script
import pandas as pd
from colorama import Fore

file_path = 'DOIs,_URLs_for_prefix_(ORACLE).csv'

df = pd.read_csv(file_path, sep="\t")

# Delete the ABS_URL column
df.drop(columns=["ABS_URL"], inplace=True)

# Rename the FT_URL column
df.rename(columns={"FT_URL": "URL"}, inplace=True)

# Save the changes to an Excel file
file_to_save = "DOIs,_URLs_for_prefix_(ORACLE).xlsx"
df.to_excel(file_to_save, index=False)
print(Fore.MAGENTA + f"saved file:  {file_to_save}")

# Deactivate the virtual environment
#!deactivate

#reset color
print('\033[39m')
print('done')
