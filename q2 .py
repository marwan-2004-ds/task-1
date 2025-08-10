import numpy as np
import matplotlib.pyplot as plt

fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']
sales = np.random.randint(50, 200, size=5)
explode = [0.1 if s == max(sales) else 0 for s in sales]

plt.figure(figsize=(8, 6))
plt.pie(sales, labels=fruits, autopct='%1.1f%%', explode=explode, startangle=140)
plt.title("Fruit Sales Distribution")
plt.axis('equal')  
plt.show()