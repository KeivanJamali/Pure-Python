import matplotlib.pyplot as plt
import numpy as np

c = 0.8
V = 500
LD = 26.29
w0 = 330000
w1 = 180000

x = np.linspace(0, 9963.2, 100)
W = w0 * np.exp(- (c * x) / (V * LD))

plt.figure(figsize=(8,5))
plt.plot(x, W, 'b-', linewidth=2)
plt.title("Weight of Plane vs Distance Flown")
plt.xlabel("Distance (miles)")
plt.ylabel("Weight (lbs)")
plt.grid(True)
plt.savefig('/Users/keivanjamali/Projects/Pure-Python/P6/03-AirP/HW2/weight_vs_distance.png')
