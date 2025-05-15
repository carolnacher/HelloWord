
import pandas as pd
import matplotlib.pyplot as plt

# Finally the last question was - Which products generate more (or less) profit?

df = pd.read_csv('Orders.csv')

# Here I proceed to obtain the data and according to the profit sort it and group it and then..
profit_by_product = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False)

print(" 🔼 📈 Top 10 most profitable products:")
print(profit_by_product.head(10))

# creating a graph with the top 10 profitables product.
top_10 = profit_by_product.head(10)
plt.figure(figsize=(10, 6)) 
top_10.plot(kind='bar', color='green')
plt.title('Most profitable products')
plt.ylabel('Total profit')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# and the Top 10 products with least profit.
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

