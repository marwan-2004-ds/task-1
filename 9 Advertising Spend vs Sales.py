import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

np.random.seed(42)
tv_budget = np.random.uniform(1, 100, 100).reshape(-1, 1)
sales = 50 + 8*tv_budget + np.random.normal(0, 30, 100).reshape(-1, 1)

x = tv_budget
y = sales

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(f"Predicted sales for a TV budget of 100: {model.predict([[100]])[0][0]:.2f}")