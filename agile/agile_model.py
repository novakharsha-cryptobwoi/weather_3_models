import numpy as np
import matplotlib.pyplot as plt

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

t = np.linspace(0, 24, 100)
T = a*t**2 + b*t + c

max_temp = max(T)
max_time = t[np.argmax(T)]

plt.plot(t, T)
plt.scatter(max_time, max_temp)
plt.text(max_time, max_temp, f"Max Temp: {max_temp:.2f}")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Agile Weather Model")
plt.show()
