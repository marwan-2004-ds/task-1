import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
data = pd.read_csv(url)

print(data.head())

x = data['displacement']
y = data['mpg']

model = LinearRegression()
model.fit(x.values.reshape(-1, 1), y)
predicted = model.predict(x.values.reshape(-1, 1))

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', alpha=0.6, label='Data')
plt.plot(x, predicted, color='red', label='Regression Line')
plt.xlabel('Displacement')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('MPG vs Displacement')
plt.legend()
plt.show()