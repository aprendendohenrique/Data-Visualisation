from turtledemo.chaos import plot

import matplotlib.pyplot as plt


x_values = range(1, 5001)
y_values = [x**2 for x in x_values]

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Greens)

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cube Numbers", fontsize=14)

plt.show()