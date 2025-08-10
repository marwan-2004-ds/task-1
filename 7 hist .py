import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

plt.hist( df['total_profit'], bins=10, color='b', label='Profit Data')

plt.xlabel('Profit range in dollars')
plt.ylabel('actual profit in dollar')
plt.title('Profit Data')
plt.legend()
plt.grid(True, linestyle='--')
plt.tight_layout()
plt.show()
