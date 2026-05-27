import math

rho_0 = 0.0024
S = 3000
CL_max = 1.5

W2 = 200000
v2_air_sq = W2 / (CL_max * (rho_0 / 2) * S)
v2_air = math.sqrt(v2_air_sq)

V2_air = v2_air * 60 / 88
print(f"Air speed v = {v2_air:.2f} ft/s, V = {V2_air:.2f} mph")

V_wind_mph = 10
v_wind_ft_s = 10 * 88 / 60

v2_ground = v2_air - v_wind_ft_s
V2_ground = V2_air - V_wind_mph

print(f"Ground speed v = {v2_ground:.2f} ft/s, V = {V2_ground:.2f} mph")
