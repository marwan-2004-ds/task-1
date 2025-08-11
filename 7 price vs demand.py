import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

np.random.seed(42)
price = np.random.uniform(10, 50, 50).reshape(-1, 1)
demand = 300 - 6*price + np.random.normal(0, 15, 50).reshape(-1, 1)

x = price
y = demand

model = LinearRegression()
model.fit(x, y)
predicted_demand = model.predict(x)
print(f"Predicted demand for a price of $20: {model.predict([[20]])[0][0]:.2f}")

