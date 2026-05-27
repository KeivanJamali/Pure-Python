import math

# Constants
rho_0 = 0.0024
rho_36000 = 0.00072
c = 0.8
S = 3000
CL_max = 1.5
St = 900
b = 150
g = 32.2

# Part 4-11 context
V4_mph = 500
v4 = V4_mph * 88 / 60
h4 = 36000
rho4 = rho_36000
W4 = 275000
T4 = 16000  # 4 * 4000
f = 0.02
AR = b ** 2 / S

# part 4
CL4 = W4 / ((rho4 / 2) * (v4 ** 2) * S)
print(f"Part 4: C_L = {CL4:.4f}")

# part 5
CD_P = 0.0055 + 0.01 * (900 / 3000)
CD_I = (CL4 ** 2) / (math.pi * AR)
CD4 = CD_P + CD_I
print(f"Part 5: C_D = {CD4:.5f}")

# part 6
D4 = CD4 * (rho4 / 2) * (v4 ** 2) * S
print(f"Part 6: D = {D4:.2f} lbs")

# part 7
# C'' fuel consumption lb/mile. Total fuel flow = c * Thrust = c * D (in level flight). C'' = c * D / V
C_double_prime = c * D4 / V4_mph
print(f"Part 7: C'' = {C_double_prime:.4f} lbs/mile")

# part 8
a_max = (T4 - D4) / (W4 / g)
print(f"Part 8: a_max = {a_max:.4f} ft/s^2")

# part 9
A = CD_P
B = -T4
C_coeff = (W4 ** 2) / (math.pi * AR)
disc = B**2 - 4*A*C_coeff
qS1 = (-B + math.sqrt(disc)) / (2*A)
v_max = math.sqrt(qS1 / (0.5 * rho4 * S))
V_max = v_max * 60 / 88
print(f"Part 9: V_max = {V_max:.2f} mph")

# part 10
W_empty = 150000
W_initial = W4 # Wait, max range AT given condition?
# w0 = wg = 330000, w1 = wg - wf = 180000
w0 = 330000
w1 = 180000
LD = CL4 / CD4
R_max = 2.3 * (V4_mph / c) * LD * math.log10(w0 / w1)
print(f"Part 10: R = {R_max:.2f} miles")

# part 11
# G = glide distance = h * L/D
G = h4 * LD
print(f"Part 11: G = {G:.2f} ft, or {G/5280:.2f} miles")

# part 12
# S_TO for takeoff with W=330000, h=0, slope +0.2%, V=0 to V_TO
W12 = 330000
v12_TO = math.sqrt(W12 / (CL_max * 0.5 * rho_0 * S))
# Acceleration: Thrust - D - F_friction - F_slope
T12 = 60000
# Mean velocity ~ 0.7 v_TO, but simpler: approx a_avg
qS_avg = 0.5 * rho_0 * (0.7 * v12_TO)**2 * S
# CD in ground roll approx CD_P (no lift induced drag, or small): CD_roll ~ 0.0085
# Actually mostly just T - mu W
a_avg = (T12 - 0.02 * W12 - 0.002 * W12) / (W12 / g)
S_TO = v12_TO**2 / (2 * a_avg)
print(f"Part 12: S_TO = {S_TO:.2f} ft")

