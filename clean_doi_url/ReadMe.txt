Author: Poppy Riddle
pnriddle@dal.ca or poppynicolette@gmail.com
2024

This cleans the output file from customer db, which saves as an xls. Its really a tab delimited csv. 
To use:
1. Rename the file as a csv extension. Otherwise, keep the original name. 
2. Save the file to this folder.
3. Open a Terminal from this folder. 
4. type the following: python clean_doi_url.py

The script will automatically set the venv, remove the unneccesary column and rename the URL column, then save out as an .xlsx file. 
The script automatically deactivates the venv. You may close the terminal. 

to test:
[ ] does this work on windows?
[ ] how to use an file upload option instead?
[ ] translate to a collab notebook?