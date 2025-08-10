import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

sales = [
    df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(), df['bathingsoap'].sum(), df['shampoo'].sum(),
    df['moisturizer'].sum()
]

labels = ['FaceCream', 'FaceWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']

plt.pie(sales, labels=labels)
plt.title('Sales data')
plt.legend(loc='best')
plt.show()
