import csv
import matplotlib.pyplot as plt

# Read the product summary dataset
with open("product_summary.csv", "r", encoding="utf-8-sig") as file:
    data = list(csv.DictReader(file))

# Convert numeric columns from text to integers
for row in data:
    row["Total_Sold"] = int(row["Total_Sold"])
    row["Revenue"] = int(row["Revenue"])
    row["Profit"] = int(row["Profit"])
    row["Estimated_Stock"] = int(row["Estimated_Stock"])
    row["Minimum_Stock"] = int(row["Minimum_Stock"])

# Calculate business metrics
total_revenue = sum(row["Revenue"] for row in data)
total_profit = sum(row["Profit"] for row in data)
restock_count = sum(
    1 for row in data if row["Stock_Status"] == "RESTOCK"
)

# Rank products
top_sold = sorted(
    data, key=lambda row: row["Total_Sold"], reverse=True
)[:5]

top_profit = sorted(
    data, key=lambda row: row["Profit"], reverse=True
)[:5]

stock_risk = sorted(
    data,
    key=lambda row: row["Estimated_Stock"] - row["Minimum_Stock"]
)[:5]

# Create one dashboard with four panels
fig, axes = plt.subplots(2, 2, figsize=(13, 7.5))
fig.suptitle(
    "Inventory & Sales Analytics Dashboard",
    fontsize=18,
    fontweight="bold"
)

# Chart 1: Best-selling products
ax = axes[0, 0]
ax.barh(
    [row["Product_Name"] for row in top_sold[::-1]],
    [row["Total_Sold"] for row in top_sold[::-1]]
)
ax.set_title("Top 5 Best-Selling Products")
ax.set_xlabel("Units Sold")
ax.grid(axis="x", alpha=0.2)

# Chart 2: Most profitable products
ax = axes[0, 1]
ax.barh(
    [row["Product_Name"] for row in top_profit[::-1]],
    [row["Profit"] for row in top_profit[::-1]]
)
ax.set_title("Top 5 Most Profitable Products")
ax.set_xlabel("Profit (IDR)")
ax.grid(axis="x", alpha=0.2)

# Chart 3: Stock compared with minimum stock
ax = axes[1, 0]
positions = list(range(len(stock_risk)))

ax.barh(
    [p - 0.18 for p in positions],
    [row["Estimated_Stock"] for row in stock_risk],
    height=0.35,
    label="Estimated Stock"
)
ax.barh(
    [p + 0.18 for p in positions],
    [row["Minimum_Stock"] for row in stock_risk],
    height=0.35,
    label="Minimum Stock"
)
ax.set_yticks(positions)
ax.set_yticklabels([row["Product_Name"] for row in stock_risk])
ax.set_title("Stock vs Restock Threshold")
ax.set_xlabel("Units")
ax.legend()
ax.grid(axis="x", alpha=0.2)

# Panel 4: Business summary
ax = axes[1, 1]
ax.axis("off")
ax.set_title("Business Summary", fontsize=14)

ax.text(
    0.05, 0.78,
    f"Products analyzed: {len(data)}",
    fontsize=13,
    transform=ax.transAxes
)
ax.text(
    0.05, 0.62,
    f"Total revenue: Rp{total_revenue:,.0f}",
    fontsize=13,
    transform=ax.transAxes
)
ax.text(
    0.05, 0.46,
    f"Total profit: Rp{total_profit:,.0f}",
    fontsize=13,
    transform=ax.transAxes
)
ax.text(
    0.05, 0.30,
    f"Products flagged for restock: {restock_count}",
    fontsize=13,
    transform=ax.transAxes
)
ax.text(
    0.05, 0.08,
    "Synthetic dataset. Stock is estimated from initial stock "
    "minus recorded sales; replenishment is not modeled.",
    fontsize=10,
    wrap=True,
    transform=ax.transAxes
)

fig.subplots_adjust(
        left=0.20,
    right=0.98,
    top=0.90,
    bottom=0.09,
    wspace=0.55,
    hspace=0.42
)

fig.savefig(
    "inventory_sales_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

print("Dashboard saved: inventory_sales_dashboard.png")
plt.show()
    