import numpy as np
import matplotlib.pyplot as plt

# Fixed requirements (Waterfall)
a, b, c = -0.2, 3, 20

t = np.linspace(0, 24, 50)
T = a*t**2 + b*t + c

plt.plot(t, T)
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.title("Waterfall Weather Model")
plt.show()
