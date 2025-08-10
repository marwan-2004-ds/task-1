import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

months = df['month_number']
plt.bar(months, df['bathingsoap'])

plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Face Cream and Face Wash Sales')
plt.grid(True, linestyle='--')
plt.legend()
plt.savefig('bathingsoap_sales_data.png') 
plt.show()