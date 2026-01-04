import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 24, 50)

models = [
    (-0.1, 2, 18),   # Iteration 1
    (-0.2, 3, 20)    # Iteration 2
]

for i, (a, b, c) in enumerate(models):
    T = a*t**2 + b*t + c
    plt.plot(t, T, label=f"Iteration {i+1}")

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Iterative Weather Model")
plt.legend()
plt.show()
