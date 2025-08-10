import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

plt.scatter(df['month_number'], df['toothpaste'], label='Tooth paste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.title('Tooth paste Sales data')
plt.grid(True, linestyle='--')
plt.legend()
plt.show()
