# Product Analysis
# This script will generate a report on the most profitable
# and least profitable products in the dataset.

import pandas as pd
import matplotlib.pyplot as plt

# Read the orders CSV file
df = pd.read_csv('Orders.csv')

# Group products by name and calculate the total profit for each product
# Sort the results in descending order
profit_by_product = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False)

print(" 🔼 📈 Top 10 most profitable products:")
print(profit_by_product.head(10))


# Extracting the top 10 most profitable products
top_10 = profit_by_product.head(10)
plt.figure(figsize=(10, 6))
top_10.plot(kind='bar', color='green')
plt.title('Most profitable products')
plt.ylabel('Total profit')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Show the top 10 products with the most profit
print("\n🔻📉 Top 10 products with the most loss:")
print(profit_by_product.tail(10))


bottom_10 = profit_by_product.tail(10)
plt.figure(figsize=(10, 6))
bottom_10.plot(kind='bar', color='red')
plt.title('Products with the most loss')
plt.ylabel('Total profit')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

