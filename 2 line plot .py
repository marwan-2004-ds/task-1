import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('company_sales_data.csv')
print("Data loaded from CSV file." , df.head())

print("=======  second plot  ========")

plt.figure(figsize=(10, 6))
plt.plot(df['month_number'], df['total_profit'], marker='o' , linestyle='--', color='red')
plt.title('company sales data of last year ')
plt.xlabel('Month Number')
plt.ylabel('sold units Profit')
plt.legend('profit data of last year')
plt.show()