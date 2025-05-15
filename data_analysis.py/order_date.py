import pandas as pd
import matplotlib.pyplot as plt

# The second question was: How do sales vary depending on the time of year?

# This line of code Load the data
df = pd.read_csv('Orders.csv')

# Here I proceed to obtain the data, sort it and group it and then..

df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month Name'] = df['Order Date'].dt.strftime('%B')
df['Quarter'] = df['Order Date'].dt.quarter

monthly_sales = df.groupby(['Year', 'Month Name'])['Sales'].sum().reset_index()

month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
monthly_sales['Month Name'] = pd.Categorical(monthly_sales['Month Name'], categories=month_order, ordered=True)
monthly_sales = monthly_sales.sort_values(['Year', 'Month Name'])

# create a simple line graph for de year sales and then for the quarter sales.
plt.figure(figsize=(14, 6))
for year in monthly_sales['Year'].unique():
    year_data = monthly_sales[monthly_sales['Year'] == year]
    plt.plot(year_data['Month Name'], year_data['Sales'], marker='o', label=str(year))

plt.title('Monthly Sales per Year', fontsize=16, fontweight='bold')
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Total Sales($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend(title='Year')
plt.tight_layout()
plt.show()



quarterly_sales = df.groupby(['Year', 'Quarter'])['Sales'].sum().reset_index()


plt.figure(figsize=(10, 6))
for year in quarterly_sales['Year'].unique():
    q_data = quarterly_sales[quarterly_sales['Year'] == year]
    plt.plot(q_data['Quarter'], q_data['Sales'], marker='o', label=str(year))

plt.title('Sales by Quarter', fontsize=16, fontweight='bold')
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Total sales ($)', fontsize=12)
plt.xticks([1, 2, 3, 4])
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend(title='Year')
plt.tight_layout()
plt.show()

# the results are printed
print("Year sales:")
print(quarterly_sales)
print("Quarter sales:")
print(q_data)

