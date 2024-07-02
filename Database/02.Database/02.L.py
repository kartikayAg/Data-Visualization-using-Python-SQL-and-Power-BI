import mysql.connector as ms
import csv

# Connect

db = ms.connect(
    host="localhost",user="ADMIN", passwd="Password" # Change to connect to a different user or follow my new user instructions
)

mycursor = db.cursor()

# Create and Use Database

mycursor.execute("CREATE DATABASE ADMIN_TEST")
mycursor.execute("USE ADMIN_TEST")

# Create and Load Customers Table

mycursor.execute("""
CREATE TABLE IF NOT EXISTS ADMIN_TEST.Customers (
    CustomerID VARCHAR(255) PRIMARY KEY NOT NULL,
    CustomerName VARCHAR(255) NOT NULL,
    Segment VARCHAR(255) NOT NULL
)
""")
File_path = r"C:02.Database\Customers.csv"

data = []
with open(File_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=",")
    i = 0
    for row in csv_reader:
        if i == 0:
            i+=1
            continue
        else:
            CustomerID = row[0]
            CustomerName = row[1]
            Segment = row[2]
            mycursor.execute('''
            INSERT INTO Customers (CustomerID, CustomerName, Segment)
            VALUES (%s, %s, %s)
            ''', (CustomerID, CustomerName, Segment))

# Create and Load Ship_Modes Table

mycursor.execute("""
CREATE TABLE IF NOT EXISTS ADMIN_TEST.Ship_Modes (
    ID VARCHAR(5) PRIMARY KEY NOT NULL,
    ShipMode VARCHAR(255) NOT NULL
)
""")

File_path = r"C:02.Database\Ship_Modes.csv"

data = []
with open(File_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=",")
    i = 0
    for row in csv_reader:
        if i == 0:
            i+=1
            continue
        else:
            ID = row[0]
            ShipMode = row[1]
            mycursor.execute('''
            INSERT INTO Ship_Modes (ID, ShipMode)
            VALUES (%s, %s)
            ''', (ID, ShipMode))

# Create and Load Products Table

mycursor.execute("""
CREATE TABLE IF NOT EXISTS ADMIN_TEST.Products (
    ProductID VARCHAR(255) PRIMARY KEY NOT NULL,
    ProductName VARCHAR(255) NOT NULL,
    Category VARCHAR(255) NOT NULL,
    SubCategory VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL
)
""")

File_path = r"C:02.Database\Products.csv"

data = []
with open(File_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=",")
    i = 0
    for row in csv_reader:
        if i == 0:
            i+=1
            continue
        else:
            ProductID = row[0]
            ProductName = row[1]
            Category = row[2]
            SubCategory = row[3]
            Price = row[4]
            mycursor.execute('''
            INSERT INTO Products (ProductID, ProductName, Category, SubCategory, Price)
            VALUES (%s, %s, %s, %s, %s)
            ''', (ProductID, ProductName, Category, SubCategory, Price))

# Create and Load Orders Table

mycursor.execute("""
CREATE TABLE IF NOT EXISTS ADMIN_TEST.Orders (
    OrderID VARCHAR(255) PRIMARY KEY NOT NULL,
    OrderDate DATE NOT NULL,
    ShipDate DATE NOT NULL,
    Address VARCHAR(255) NOT NULL,
    State VARCHAR(255) NOT NULL,
    ShipModeID VARCHAR(5),
    CustomerID VARCHAR(255),
    FOREIGN KEY (ShipModeID)
    REFERENCES Ship_Modes(ID)
    ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (CustomerID)
    REFERENCES Customers(CustomerID)
    ON UPDATE CASCADE ON DELETE SET NULL
)
""")

File_path = r"C:02.Database\Orders.csv"

data = []
with open(File_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=",")
    i = 0
    for row in csv_reader:
        if i == 0:
            i+=1
            continue
        else:
            OrderID = row[0]
            OrderDate = row[1]
            ShipDate = row[2]
            Address = row[3]
            State = row[4]
            ShipModeID = row[5]
            CustomerID = row[6]
            mycursor.execute('''
            INSERT INTO Orders (OrderID,OrderDate,ShipDate,Address,State,ShipModeID,CustomerID)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (OrderID,OrderDate,ShipDate,Address,State,ShipModeID,CustomerID))

# Create and Load Orders Table

mycursor.execute("""
CREATE TABLE IF NOT EXISTS ADMIN_TEST.Order_Details (
    OrderID VARCHAR(255),
    ProductID VARCHAR(255),
    Quantity INT NOT NULL,
    Total DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID)
    REFERENCES Orders(OrderID)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ProductID)
    REFERENCES Products(ProductID)
    ON UPDATE CASCADE ON DELETE CASCADE
)
""")

File_path = r"C:02.Database\Order_Details.csv"

data = []
with open(File_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=",")
    i = 0
    for row in csv_reader:
        if i == 0:
            i+=1
            continue
        else:
            OrderID = row[0]
            ProductID = row[1]
            Quantity = row[2]
            Total = row[3]
            mycursor.execute('''
            INSERT INTO Order_Details (OrderID,ProductID,Quantity,Total)
            VALUES (%s, %s, %s, %s)
            ''', (OrderID,ProductID,Quantity,Total))


db.commit()
# Close cursor and connection
mycursor.close()
db.close()