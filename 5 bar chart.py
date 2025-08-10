import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

months = df['month_number']
plt.bar(months, df['facecream'], label='Face Cream', width=0.4)
plt.bar(months + 0.4 , df['facewash'], label='Face Wash', width=0.4)

plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Face Cream and Face Wash Sales')
plt.legend()
plt.show()
