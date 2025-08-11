import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

np.random.seed(42)
study_hours = np.random.uniform(1, 10, 50).reshape(-1, 1)
exam_score = 50 + 5 * study_hours + np.random.normal(0, 8, 50).reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(study_hours, exam_score, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
