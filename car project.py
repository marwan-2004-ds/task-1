import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("car_prediction_data.csv")

print("========= process ==========")
print("Null values per column:")
print(df.isnull().sum())
df = df.dropna()

df = df.drop("Owner", axis=1)
df = pd.get_dummies(df, drop_first=True)


print("\nFull dataset after cleaning:")
print(df)



print('======= split the data =========')
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

print("\n X (features):")
print(X)

print("\ny (Selling Price):")
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nX_train:")
print(X_train)

print("\ny_train:")
print(y_train)

print("\nX_test:")
print(X_test)

print("\ny_test:")
print(y_test)


print('========= train ===========')
model = LinearRegression()
model.fit(X_train, y_train)

print('======= evaluate ==========')
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)*100

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2): {r2}")


print(" ======= visualize data =========")
plt.figure()
plt.scatter(df["Present_Price"], df["Selling_Price"], color="blue", label="Present_Price")
plt.scatter(df["Kms_Driven"], df["Selling_Price"], color="red", label="Kms_Driven")
plt.title("Selling Price Visualization")
plt.xlabel("Feature Value")
plt.ylabel("Selling Price")
plt.legend()
plt.show()
input("Press Enter to close...")


print("===== thank you ===========")

