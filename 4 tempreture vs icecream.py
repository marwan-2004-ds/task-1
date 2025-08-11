import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


np.random.seed(42)
temperature = np.random.uniform(15, 35, 50).reshape(-1, 1)
sales = 20 + 5*temperature + np.random.normal(0, 10, 50).reshape(-1, 1)

x = temperature
y = sales

model = LinearRegression()
model.fit(x, y)
predicted_sales = model.predict(x)

mse =mean_squared_error(sales, predicted_sales)
print(f"MSE: {mse:.2f}")

