import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


np.random.seed(42)
rainfall = np.random.uniform(300, 900, 50).reshape(-1, 1)
crop_yield = 2 + 0.007*rainfall + np.random.normal(0, 0.5, 50).reshape(-1, 1)

x = rainfall
y = crop_yield

model = LinearRegression()
model.fit(x, y)
predicted_yield = model.predict(x)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Actual Crop Yield')
plt.plot(x, predicted_yield, '-', label='Data points')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Crop Yield (tons/ha)')
plt.title('Crop Yield vs Rainfall')
plt.legend()
plt.show()