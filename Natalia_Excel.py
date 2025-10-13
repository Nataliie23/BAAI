#
# Natalia, 2025/20/08
# File: Natalia_Excel.py
# Calculate sum of column in Excel file
#
 

# 1. Input
import pandas as pd
import os

# 2. Process
folder = r"C:\Users\natal\OneDrive\Escritorio\Python\New folder\BAAI"
files = sorted([f for f in os.listdir(folder)
                if f.endswith(".xlsx") and not f.startswith("~$")])

for i, filename in enumerate(files):
    path = os.path.join(folder, filename)
    df = pd.read_excel(path) 

# 3. Output
    print(f" leyendo {i+1} / {len(files)} -> {filename}")
   
    if i == len(files) - 1:
        print("This is the LAST file!")