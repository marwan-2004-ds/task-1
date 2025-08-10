import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('company_sales_data.csv')
print("Data loaded from CSV file." , df.head())

print("=======  first plot  ========")

plt.figure(figsize=(10, 6))
plt.plot(df['month_number'], df['total_profit'], linestyle='-', color='b')
plt.title('company Profit Over Months')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.show()


