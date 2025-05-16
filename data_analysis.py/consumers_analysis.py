# This code will calculate the total sales for each customer segment
# and display the results in a bar chart.

import pandas as pd
import matplotlib.pyplot as plt

# Read the Orders CSV file
df = pd.read_csv('Orders.csv')

# Group the data by customer segment and calculate total sales
sales_by_segment = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)

# Print the results
print("Customer segments with the highest sales:")
print(sales_by_segment)

# Create a bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(sales_by_segment.index, sales_by_segment.values, color='#2196F3', edgecolor='black')

# Customize the chart
plt.title('Sales by Customer Segment', fontsize=16, fontweight='bold')
plt.xlabel('Customer Segment', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add data labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f"${yval:,.0f}", 
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# Show the chart
plt.tight_layout()
plt.show()
