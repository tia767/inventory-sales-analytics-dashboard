import random
import csv
from datetime import datetime, timedelta
base_products = [
    "Paracetamol",
    "Vitamin C",
    "Antiseptic",
    "Hand Sanitizer",
    "Face Mask",
    "Shampoo",
    "Body Lotion",
    "Toothpaste",
    "Baby Powder",
    "Cough Syrup"
]

variants = ["Regular", "Plus", "Extra"]

product_names = []

for product in base_products:
    for variant in variants:
        product_names.append(f"{product} {variant}")

print(len(product_names))
categories = [
    "Medicine",
    "Supplement",
    "Personal Care",
    "Hygiene"
]

products = []

for i, product_name in enumerate(product_names, start=1):
    selling_price = random.randint(10000, 50000)
    cost_price = int(selling_price * random.uniform(0.5, 0.8))
    initial_stock = random.randint(50, 200)
    minimum_stock = random.randint(10, 40)

    product = {
        "Product_ID": f"P{i:03d}",
        "Product_Name": product_name,
        "Category": random.choice(categories),
        "Selling_Price": selling_price,
        "Cost_Price": cost_price,
        "Initial_Stock": initial_stock,
        "Minimum_Stock": minimum_stock
    }

    products.append(product)

print(len(products))
print(products[0])

with open("products.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=products[0].keys())
    writer.writeheader()
    writer.writerows(products)

print("products.csv berhasil dibuat.")

transactions = []

start_date = datetime(2026, 1, 1)

for i in range(1, 301):
    product = random.choice(products)
    transaction_date = start_date + timedelta(days=random.randint(0, 364))
    quantity = random.randint(1, 5)

    transaction = {
        "Date": transaction_date.strftime("%Y-%m-%d"),
        "Transaction_ID": f"TRX{i:03d}",
        "Product_ID": product["Product_ID"],
        "Quantity": quantity
    }

    transactions.append(transaction)

    print(len(transactions))

with open("sales.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=transactions[0].keys())
    writer.writeheader()
    writer.writerows(transactions)

print("sales.csv berhasil dibuat.")

