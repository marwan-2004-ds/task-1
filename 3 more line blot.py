import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')
months = df['month_number']

plt.plot(months, df['facecream'], label='Face cream Sales Data', marker='o')
plt.plot(months, df['facewash'], label='Face Wash Sales Data', marker='o')
plt.plot(months, df['toothpaste'], label='ToothPaste Sales Data', marker='o')
plt.plot(months, df['bathingsoap'], label='Bathing Soap Sales Data', marker='o')
plt.plot(months, df['shampoo'], label='Shampoo Sales Data', marker='o')
plt.plot(months, df['moisturizer'], label='Moisturizer Sales Data', marker='o')

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Sales data')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
