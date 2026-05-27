import math

# Constants
W_takeoff = 330000.0
W_empty = 150000.0
W_fuel = 150000.0
W_reserve = 15000.0

# Part 10 - Range max
V_cruise = 500.0 # mph
c_sfc = 0.8 # lbs/(lb hr)
L_D_max = 26.29 # From part 11 max L/D
W_1_actual = W_takeoff - (W_fuel - W_reserve) # 195000.0
R_max = (V_cruise / c_sfc) * L_D_max * math.log(W_takeoff / W_1_actual)

print("Part 10 - W_1:", W_1_actual)
print("Part 10 - R_max (miles):", R_max)

# Part 11 - Glide distance MAX
# (L/D)max happens when CD0 = Cdi
# CD0 = 0.0085 as per student (I will not modify part 5 CD0 arbitrarily since no CD formula was given)
CDP = 0.0085
k = 1.0 / (math.pi * 7.5)
LD_opt = 0.5 / math.sqrt(CDP * k)
h_ft = 36000.0
G_ft = h_ft * LD_opt
G_miles = G_ft / 5280.0

print("Part 11 - LD_max (optimal):", LD_opt)
print("Part 11 - G_ft:", G_ft)
print("Part 11 - G_miles:", G_miles)


# Part 12 - STO using average v = 0.7 V_TO
v_TO = 247.21
v_avg = 0.7 * v_TO
rho0 = 0.0024
S = 3000.0
q = 0.5 * rho0 * v_avg**2 * S
CD_ground = 0.0085 + k * (1.5)**2  # roughly with flaps? Without flaps CL is smaller. Just keep simple F_resist is based on W.
# Let's use the average lift instead. CL_avg = W / qS? No, lift is L_avg = 0.5 * rho * (0.7 V_TO)^2 * S * CL. 
L_avg = q * 1.5/2 # Not sure of CL during roll, assume 0 for simple, or 1.0. Let's just say L_avg = q * 1.5 maybe?
# Normally L = 0.5 W approx.
# simpler version: F_resist = W(f+i) was student's. But with Lift: F_resist = D + (W-L)(f+i)
L_avg = q * 1.5 
D_avg = q * CD_ground
F_fric = (W_takeoff - L_avg) * (0.02 + 0.002) if (W_takeoff - L_avg) > 0 else 0
F_total_resist = D_avg + F_fric
a_avg = 32.2 * (60000 - F_total_resist) / W_takeoff
S_TO = v_TO**2 / (2 * a_avg)

print("Part 12 - v_avg (ft/s):", v_avg)
print("Part 12 - a_avg (ft/s^2):", a_avg)
print("Part 12 - S_TO (ft):", S_TO)
