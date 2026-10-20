import csv

with open("products.csv", "r", encoding="utf-8-sig") as file:
    products = list(csv.DictReader(file))

product_lookup = {
    product["Product_ID"]: product
    for product in products
}

with open("sales.csv", "r", encoding="utf-8-sig") as file:
    sales = list(csv.DictReader(file))

analysis = []

for sale in sales:
    product = product_lookup[sale["Product_ID"]]

    quantity = int(sale["Quantity"])
    selling_price = int(product["Selling_Price"])
    cost_price = int(product["Cost_Price"])

    revenue = quantity * selling_price
    cost = quantity * cost_price
    profit = revenue - cost

    row = {
        "Date": sale["Date"],
        "Transaction_ID": sale["Transaction_ID"],
        "Product_ID": sale["Product_ID"],
        "Product_Name": product["Product_Name"],
        "Category": product["Category"],
        "Quantity": quantity,
        "Selling_Price": selling_price,
        "Cost_Price": cost_price,
        "Revenue": revenue,
        "Profit": profit
    }

    analysis.append(row)

total_revenue = sum(row["Revenue"] for row in analysis)
total_profit = sum(row["Profit"] for row in analysis)

print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)

product_sales = {}

for row in analysis:
    product_name = row["Product_Name"]
    quantity = row["Quantity"]

    if product_name not in product_sales:
        product_sales[product_name] = 0

    product_sales[product_name] += quantity

top_products = sorted(
    product_sales.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nTop 5 Produk Terlaris:")

for product_name, quantity in top_products[:5]:
    print(product_name, "-", quantity, "unit")

    product_profit = {}

for row in analysis:
    product_name = row["Product_Name"]
    profit = row["Profit"]

    if product_name not in product_profit:
        product_profit[product_name] = 0

    product_profit[product_name] += profit

top_profit_products = sorted(
    product_profit.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nTop 5 Produk dengan Profit Terbesar:")

for product_name, profit in top_profit_products[:5]:
    print(product_name, "-", profit)

    sales_by_product = {}

for row in analysis:
    product_id = row["Product_ID"]
    quantity = row["Quantity"]

    if product_id not in sales_by_product:
        sales_by_product[product_id] = 0

    sales_by_product[product_id] += quantity


restock_list = []

for product in products:
    product_id = product["Product_ID"]
    initial_stock = int(product["Initial_Stock"])
    minimum_stock = int(product["Minimum_Stock"])
    total_sold = sales_by_product.get(product_id, 0)

    estimated_stock = initial_stock - total_sold

    if estimated_stock <= minimum_stock:
        restock_list.append({
            "Product_ID": product_id,
            "Product_Name": product["Product_Name"],
            "Initial_Stock": initial_stock,
            "Total_Sold": total_sold,
            "Estimated_Stock": estimated_stock,
            "Minimum_Stock": minimum_stock
        })


restock_list = sorted(
    restock_list,
    key=lambda product: product["Estimated_Stock"] - product["Minimum_Stock"]
)

print("\nProduk yang Perlu Direstock:")

for product in restock_list:
    print(
        product["Product_Name"],
        "| Sisa:", product["Estimated_Stock"],
        "| Minimum:", product["Minimum_Stock"]
    )

    product_summary = []

for product in products:
    product_id = product["Product_ID"]

    total_sold = sales_by_product.get(product_id, 0)

    total_revenue = sum(
        row["Revenue"]
        for row in analysis
        if row["Product_ID"] == product_id
    )

    total_profit = sum(
        row["Profit"]
        for row in analysis
        if row["Product_ID"] == product_id
    )

    initial_stock = int(product["Initial_Stock"])
    minimum_stock = int(product["Minimum_Stock"])
    estimated_stock = initial_stock - total_sold

    if estimated_stock <= minimum_stock:
        stock_status = "RESTOCK"
    else:
        stock_status = "OK"

    product_summary.append({
        "Product_ID": product_id,
        "Product_Name": product["Product_Name"],
        "Category": product["Category"],
        "Total_Sold": total_sold,
        "Revenue": total_revenue,
        "Profit": total_profit,
        "Initial_Stock": initial_stock,
        "Estimated_Stock": estimated_stock,
        "Minimum_Stock": minimum_stock,
        "Stock_Status": stock_status
    })

    with open("product_summary.csv", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=product_summary[0].keys())
        writer.writeheader()
        writer.writerows(product_summary)

print("product_summary.csv berhasil dibuat.")

with open("transaction_analysis.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=analysis[0].keys())
    writer.writeheader()
    writer.writerows(analysis)

print("transaction_analysis.csv berhasil dibuat.")