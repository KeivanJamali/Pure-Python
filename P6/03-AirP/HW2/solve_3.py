v_initial = 177.78
g = 32.2
fb = 0.15
slope = 0.002
a = g * (fb + slope)
d = (v_initial ** 2) / (2 * a)
print(f"Braking distance d = {d:.2f} ft")
