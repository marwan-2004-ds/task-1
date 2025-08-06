import numpy as np

centigrade = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = centigrade * 9/5 + 32
centigrade_back = (fahrenheit - 32) * 5/9

print(centigrade)
print(fahrenheit)
print(centigrade_back)
print(centigrade_back * 9/5 + 32)
