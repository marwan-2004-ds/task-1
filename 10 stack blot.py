import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('company_sales_data.csv')

months = df['month_number']
data = df[['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']]

plt.figure(figsize=(8,5))
plt.stackplot( months, data ,  labels=['face Cream','Face wash','Tooth paste','Bathing soap','Shampoo','Moisturizer'])
plt.title('All product sales data using stack plot')
plt.xlabel('Month Number')
plt.ylabel('Sales units in Number')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
