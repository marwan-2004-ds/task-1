import pandas as pd
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

print(df.head())

X = diabetes.data[:, [2]]
y = diabetes.target

model = LinearRegression()
model.fit(X, y)

predicted = model.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', alpha=0.6, label='Data')
plt.plot(X, predicted, color='blue', label='Actual Data')
plt.xlabel('BMI')
plt.ylabel('Diabetes Progression')
plt.title('Diabetes Progression vs BMI')
plt.legend()
plt.show()