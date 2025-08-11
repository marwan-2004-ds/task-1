import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

np.random.seed(42)
height = np.random.uniform(150, 200, 100).reshape(-1, 1)
weight = 0.8*height - 70 + np.random.normal(0, 5, 100).reshape(-1, 1)

x = height
y = weight

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(f"Predicted weight for a height of 180 cm: {model.predict([[180]])[0][0]:.2f}")

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

