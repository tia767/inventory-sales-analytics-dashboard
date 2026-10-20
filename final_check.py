
import csv


def load_csv(filename):
    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


products = load_csv("products.csv")
sales = load_csv("sales.csv")
transaction_analysis = load_csv("transaction_analysis.csv")
product_summary = load_csv("product_summary.csv")

product_ids = [row["Product_ID"] for row in products]
product_id_set = set(product_ids)

transaction_ids = [row["Transaction_ID"] for row in sales]

unknown_product_ids = [
    row["Product_ID"]
    for row in sales
    if row["Product_ID"] not in product_id_set
]

total_sales_units = sum(int(row["Quantity"]) for row in sales)
analysis_units = sum(int(row["Quantity"]) for row in transaction_analysis)
summary_units = sum(int(row["Total_Sold"]) for row in product_summary)

transaction_revenue = sum(int(row["Revenue"]) for row in transaction_analysis)
summary_revenue = sum(int(row["Revenue"]) for row in product_summary)

transaction_profit = sum(int(row["Profit"]) for row in transaction_analysis)
summary_profit = sum(int(row["Profit"]) for row in product_summary)

checks = [
    ("Jumlah produk adalah 30", len(products) == 30),
    ("Jumlah transaksi adalah 300", len(sales) == 300),
    ("Product ID unik", len(product_ids) == len(set(product_ids))),
    ("Transaction ID unik", len(transaction_ids) == len(set(transaction_ids))),
    ("Semua transaksi memiliki Product ID valid", len(unknown_product_ids) == 0),
    ("Jumlah baris analisis cocok", len(transaction_analysis) == len(sales)),
    ("Jumlah baris ringkasan cocok", len(product_summary) == len(products)),
    ("Total unit terjual konsisten", total_sales_units == analysis_units == summary_units),
    ("Total revenue konsisten", transaction_revenue == summary_revenue),
    ("Total profit konsisten", transaction_profit == summary_profit),
]

print("=== FINAL PROJECT AUDIT ===")

for label, passed in checks:
    result = "LULUS" if passed else "PERIKSA"
    print(f"[{result}] {label}")

if all(passed for _, passed in checks):
    print("\nAUDIT AKHIR: LULUS")
else:
    print("\nAUDIT AKHIR: PERLU DIPERIKSA")
