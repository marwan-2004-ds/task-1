import matplotlib.pyplot as plt


data = {
    'days': ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'temperature': [32, 30, 29, 31, 33, 35, 34]
}

plt.figure(figsize=(6,6))
plt.plot(data['days'], data['temperature'], marker='o', linestyle='-', color='blue', label='Temp (°C)')

plt.title('Temperature Over the Week (°C)')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.xticks(rotation=45)
plt.show()