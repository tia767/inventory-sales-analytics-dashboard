import csv

with open("products.csv", "r", encoding="utf-8-sig") as file:
    products = list(csv.DictReader(file))

print("Jumlah produk:", len(products))

product_ids = [product["Product_ID"] for product in products]

print("Jumlah ID unik:", len(set(product_ids)))

empty_data = []

for product in products:
    for column, value in product.items():
        if value == "":
            empty_data.append((product["Product_ID"], column))

print("Jumlah data kosong:", len(empty_data))

with open("products.csv", "r", encoding="utf-8-sig") as file:
    products = list(csv.DictReader(file))

print("Jumlah produk:", len(products))

product_ids = [product["Product_ID"] for product in products]

print("Jumlah ID unik:", len(set(product_ids)))

empty_data = []

for product in products:
    for column, value in product.items():
        if value == "":
            empty_data.append((product["Product_ID"], column))

print("Jumlah data kosong:", len(empty_data))

invalid_price = []

for product in products:
    selling_price = int(product["Selling_Price"])
    cost_price = int(product["Cost_Price"])

    if selling_price <= 0 or cost_price <= 0:
        invalid_price.append(product["Product_ID"])

    if selling_price <= cost_price:
        invalid_price.append(product["Product_ID"])

print("Jumlah produk dengan harga tidak valid:", len(invalid_price))


invalid_stock = []

for product in products:
    initial_stock = int(product["Initial_Stock"])
    minimum_stock = int(product["Minimum_Stock"])

    if initial_stock < 0 or minimum_stock < 0:
        invalid_stock.append(product["Product_ID"])

    if minimum_stock > initial_stock:
        invalid_stock.append(product["Product_ID"])

print("Jumlah produk dengan stok tidak valid:", len(invalid_stock))