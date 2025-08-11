import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

np.random.seed(42)
house_size = np.random.randint(1000, 5000, 100).reshape(-1, 1)  
price = np.random.randint(100, 500, 100) 


model = LinearRegression()
model.fit(house_size, price)


predicted_price = model.predict([[3200]])
print(f"Predicted price for a 3,200 sq. ft. house: ${predicted_price[0]:,.2f}")
