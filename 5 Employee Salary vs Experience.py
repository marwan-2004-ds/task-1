import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

np.random.seed(42)
experience = np.random.uniform(0, 20, 100).reshape(-1, 1)
salary = 40 + 8*experience + np.random.normal(0, 10, 100).reshape(-1, 1)

x = experience
y = salary

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print(f"evaluated with R^2: {model.score(x_test, y_test):.2f}")
