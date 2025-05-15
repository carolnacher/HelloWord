
import pandas as pd
import matplotlib.pyplot as plt

# For this part, I start with a basic question 
#  Which customer segment buys the most?

# Load the data
df = pd.read_csv('Orders.csv')

# The idea is to group by customer segment sales.
sales_by_segment = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)

# the results are printed on the console
print("🔝 Customer segments with the highest sales:")
print(sales_by_segment)

# build the graph
plt.figure(figsize=(8, 6))
bars = plt.bar(sales_by_segment.index, sales_by_segment.values, color='#2196F3', edgecolor='black')

plt.title('Sales by Customer Segment', fontsize=16, fontweight='bold')
plt.xlabel('Customer Segment', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f"${yval:,.0f}", 
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()