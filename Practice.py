#PROJECT 3

import pandas as pd
import os

df = pd.read_excel('customers.xlsx')

for index, row in df.iterrows(): 
    name = row["Costumer_Name"]  
    total_purchases = row["Total_Purchases"]
    number_of_orders = row["Number_of_Orders"]
    
    if total_purchases > 10000:
        status = "VIP Customers"
    elif total_purchases > 5000 < 1000:
        status = "Regular Customers"
    else :
        status = "New Customers"
    print()

