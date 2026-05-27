import math

# Constants
rho_0 = 0.0024
rho_36000 = 0.00072
c = 0.8
S = 3000
CL_max = 1.5

# Part 1: Takeoff speed at h=0, W=330000
W1 = 330000
v1_sq = W1 / (CL_max * (rho_0 / 2) * S)
v1 = math.sqrt(v1_sq)
V1 = v1 * 60 / 88
print(f"Part 1: v = {v1:.2f} ft/s, V = {V1:.2f} mph")

