import csv
import matplotlib.pyplot as plt

with open("product_summary.csv", "r", encoding="utf-8-sig") as file:
    data = list(csv.DictReader(file))

for row in data:
    row["Total_Sold"] = int(row["Total_Sold"])
    row["Revenue"] = int(row["Revenue"])
    row["Profit"] = int(row["Profit"])

top_sold = sorted(data, key=lambda row: row["Total_Sold"], reverse=True)[:5]

names = [row["Product_Name"] for row in top_sold]
quantities = [row["Total_Sold"] for row in top_sold]

plt.figure(figsize=(10, 6))
plt.barh(names[::-1], quantities[::-1])
plt.xlabel("Units Sold")
plt.ylabel("Product")
plt.title("Top 5 Best-Selling Products")
plt.tight_layout()
plt.show()

top_profit = sorted(
    data,
    key=lambda row: row["Profit"],
    reverse=True
)[:5]

profit_names = [row["Product_Name"] for row in top_profit]
profits = [row["Profit"] for row in top_profit]

plt.figure(figsize=(10, 6))
plt.barh(profit_names[::-1], profits[::-1])
plt.xlabel("Total Profit (Rp)")
plt.ylabel("Product")
plt.title("Top 5 Most Profitable Products")
plt.tight_layout()
plt.show()

stock_risk = sorted(
    data,
    key=lambda row: int(row["Estimated_Stock"]) - int(row["Minimum_Stock"])
)[:5]

stock_names = [row["Product_Name"] for row in stock_risk]
estimated_stock = [int(row["Estimated_Stock"]) for row in stock_risk]
minimum_stock = [int(row["Minimum_Stock"]) for row in stock_risk]

positions = list(range(len(stock_risk)))

plt.figure(figsize=(10, 6))
plt.barh(
    [p - 0.18 for p in positions],
    estimated_stock,
    height=0.35,
    label="Estimated Stock"
)
plt.barh(
    [p + 0.18 for p in positions],
    minimum_stock,
    height=0.35,
    label="Minimum Stock"
)

plt.yticks(positions, stock_names)
plt.xlabel("Units")
plt.title("5 Products Closest to Restock Threshold")
plt.legend()
plt.tight_layout()
plt.show()