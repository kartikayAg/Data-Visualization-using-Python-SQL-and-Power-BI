import pandas as pd
import random as rd
from datetime import datetime

# Random Seed

rd.seed(5) # numbes are always the same when runing the code

file_path = r"C:01.Extraxt_Transform_Script\SalesReport.csv"
df = pd.read_csv(file_path)

# Ship mode table

Ship_mode = df.loc[:,["Ship Mode"]]

Ship_mode.drop_duplicates(subset="Ship Mode", keep="first", inplace=True)

desired_order = ["Same Day", "First Class", "Second Class", "Standard Class"]

Ship_mode['Ship Mode'] = Ship_mode['Ship Mode'].astype(pd.CategoricalDtype(categories=desired_order, ordered=True))
Ship_mode.sort_values(by='Ship Mode', inplace=True)

Ship_mode.index = ["S" + str(i) for i in range(len(Ship_mode))]

Ship_mode.rename_axis("ID",inplace=True) # no need to specify which axis when renaming index

Ship_mode.to_csv("02.Database/Ship_Modes.csv")

# Customers

Customer = df.loc[:,["Customer ID","Customer Name", "Segment"]]

Customer.drop_duplicates(subset=["Customer ID","Customer Name", "Segment"], keep="first", inplace=True)

Customer.set_index("Customer ID", inplace=True)

Customer.to_csv("02.Database/Customers.csv")

# Products

Products= df.loc[:,["Product ID","Product Name","Category","Sub-Category"]]

Products.drop_duplicates(subset=["Product ID","Product Name","Category","Sub-Category"], keep="first", inplace=True)

Products["Price"] = [round(rd.uniform(25,500),2) for i in range(len(Products["Product Name"]))]

IDS = []

def duplicate_ids(row):
    a = row["Product ID"]
    if a in IDS:
        a += "D"
        IDS.append(a)
        return a
    else:
        IDS.append(a)
        return a
    

Products["Product ID"] = Products.apply(duplicate_ids, axis=1)

Products.set_index("Product ID", inplace=True)

Products.to_csv("02.Database/Products.csv")

# Orders

Orders = df.loc[:, ["Order ID", "Order Date", "Ship Date", "Ship Mode", "Customer ID", "Product ID", "Country", "City", "State", "Postal Code"]]

# funciones importantes de recordar
def direccion(row):
    return f"{row['Country']}, {row['City']}, {row['Postal Code']}"

def SMID(row):
    if row['Ship Mode'] in Ship_mode['Ship Mode'].values:
        # Get the corresponding Ship Mode ID (index)
        return Ship_mode.index[Ship_mode['Ship Mode'] == row['Ship Mode']].tolist()[0]
    else:
        return None 
    
Orders['Address'] = Orders.apply(direccion, axis=1)
Orders['Ship Mode ID'] = Orders.apply(SMID, axis=1)

Orders = Orders.loc[:,["Order ID", "Order Date", "Ship Date", "Address", "State", "Ship Mode ID", "Customer ID", "Product ID"]]

Orders.drop_duplicates(subset=["Order ID", "Order Date", "Ship Date", "Address", "State", "Ship Mode ID", "Customer ID", "Product ID"], keep="first", inplace=True)

Orders["Quantity"] = [rd.randint(1,5) for i in range(len(Orders["Order ID"]))]

Orders2 = Orders.loc[:, ["Order ID", "Order Date", "Ship Date", "Address", "State", "Ship Mode ID", "Customer ID"]]
Orders2.drop_duplicates(subset=["Order ID", "Order Date", "Ship Date", "Address", "State", "Ship Mode ID", "Customer ID"], keep="first", inplace=True)
Orders2['Order Date'] = Orders2['Order Date'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y').strftime('%Y-%m-%d'))
Orders2['Ship Date'] = Orders2['Ship Date'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y').strftime('%Y-%m-%d'))

Orders2.to_csv("02.Database/Orders.csv", index=False)

# Orders details

O_details = Orders.loc[:, ["Order ID", "Product ID", "Quantity"]]

def Total(row):
    try:
        ID = row["Product ID"]
        price = Products.loc[ ID, "Price"]
        total = price * row["Quantity"]
        return round(total,2)
    except:
        return None
       
O_details["Total"] = O_details.apply(Total, axis=1)
O_details.drop_duplicates(subset=["Order ID", "Product ID"], keep="first", inplace=True)

O_details.to_csv("02.Database/Order_Details.csv", index=False)