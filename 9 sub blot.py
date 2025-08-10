import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

months = df['month_number']

plt.subplot(2, 1, 1)
plt.plot(months, df['bathingsoap'], color='black', marker='o')
plt.title('Sales data of a Bathingsoap')

plt.subplot(2, 1, 2)
plt.plot(months, df['facewash'], color='red', marker='o')
plt.title('Sales data of a facewash')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')

plt.tight_layout()
plt.show()
