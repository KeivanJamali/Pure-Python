import pandas as pd
import numpy as np
from itertools import product

np.random.seed(42)

# ================================================================
# BASE SYSTEM (medical inventory: e.g., blood bags)
# ================================================================
BASE_L = 8
BASE_C = 150
BASE_P = 45
BASE_H = 5.5
BASE_W = 18
BASE_S = 950
BASE_DEMAND = [85, 120, 25, 180, 95, 200, 60, 145, 320, 75, 140, 260, 50, 190]
BASE_T = len(BASE_DEMAND)

runs = []
run_id = 1

# ================================================================
# 1. DEMAND VOLATILITY — MORE DRAMATIC
# ================================================================
# Moderate → Extreme volatility
volatility_levels = [0.02, 0.15, 0.35, 0.65, 1.25]
samples_per_volatility = 350

for sigma in volatility_levels:
    for sample in range(samples_per_volatility):

        # extreme volatility → can be huge spikes → clipped at +450%
        eps = np.random.normal(scale=sigma, size=BASE_T)
        eps = np.clip(eps, -0.95, 4.5)

        demand = [int(d * (1 + e)) for d, e in zip(BASE_DEMAND, eps)]
        demand = [max(0, d) for d in demand]

        runs.append({
            'run_id': run_id,
            'T': BASE_T,
            'L': BASE_L,
            'C': BASE_C,
            'p': BASE_P,
            'h': BASE_H,
            'w': BASE_W,
            's': BASE_S,
            **{f'demand_t{i+1}': demand[i] for i in range(BASE_T)},
            'scenario_type': 'volatility',
            'scenario_param': f'sigma_{sigma:.2f}'
        })
        run_id += 1

# ================================================================
# 2. SHELF-LIFE (ULTRA SHORT → LONG LIFE MEDS)
# ================================================================
shelf_life_values = [2, 4, 5, 7, 9, 14]
samples_per_shelf = 55

for L in shelf_life_values:
    for _ in range(samples_per_shelf):

        runs.append({
            'run_id': run_id,
            'T': BASE_T,
            'L': L,
            'C': 200,   # high capacity → shelf life truly matters
            'p': BASE_P,
            'h': BASE_H,
            'w': BASE_W,
            's': BASE_S,
            **{f'demand_t{i+1}': BASE_DEMAND[i] for i in range(BASE_T)},
            'scenario_type': 'shelf_life',
            'scenario_param': f'L_{L}'
        })
        run_id += 1

# ================================================================
# 3. CAPACITY STRESS (SEVERE BOTTLENECKS)
# ================================================================
capacity_values = [25, 50, 75, 110, 160, 220, 300, 400]
samples_per_C = 40

for C in capacity_values:
    for _ in range(samples_per_C):

        runs.append({
            'run_id': run_id,
            'T': BASE_T,
            'L': BASE_L,
            'C': C,
            'p': BASE_P,
            'h': BASE_H,
            'w': BASE_W,
            's': BASE_S,
            **{f'demand_t{i+1}': BASE_DEMAND[i] for i in range(BASE_T)},
            'scenario_type': 'capacity',
            'scenario_param': f'C_{C}'
        })
        run_id += 1

# ================================================================
# 6. SHORTAGE PENALTY (LOG SCALE)
# ================================================================
shortage_penalties = [5, 25, 50, 120, 250, 500, 1000]
samples_per_s = 35

for s in shortage_penalties:
    for _ in range(samples_per_s):

        runs.append({
            'run_id': run_id,
            'T': BASE_T,
            'L': BASE_L,
            'C': 175,
            'p': BASE_P,
            'h': BASE_H,
            'w': BASE_W,
            's': s,
            **{f'demand_t{i+1}': BASE_DEMAND[i] for i in range(BASE_T)},
            'scenario_type': 'cost_sensitivity',
            'scenario_param': f's_{s}'
        })
        run_id += 1

# ================================================================
# 7. WASTE COST (DRAMATIC RANGE)
# ================================================================
waste_costs = [-85, -70, -55, -40, -20, 5, -12]
samples_per_w = 30

for w in waste_costs:
    for _ in range(samples_per_w):
        runs.append({
            'run_id': run_id,
            'T': BASE_T,
            'L': 5,
            'C': 850,
            'p': BASE_P,
            'h': 3.5,
            'w': w,
            's': BASE_S,
            **{f'demand_t{i+1}': BASE_DEMAND[i] for i in range(BASE_T)},
            'scenario_type': 'cost_sensitivity',
            'scenario_param': f'w_{w}'
        })
        run_id += 1

# ================================================================
# 8. HOLDING COST (STRONG VARIATION)
# ================================================================
holding_costs = [0.3, 1.2, 2.8, 5.5, 9.5, 15.2, 22.0]
samples_per_h = 32

for h in holding_costs:
    for _ in range(samples_per_h):
        runs.append({
            'run_id': run_id,
            'T': BASE_T,
            'L': 10,
            'C': 280,
            'p': BASE_P,
            'h': h,
            'w': BASE_W,
            's': BASE_S,
            **{f'demand_t{i+1}': BASE_DEMAND[i] for i in range(BASE_T)},
            'scenario_type': 'cost_sensitivity',
            'scenario_param': f'h_{h:.1f}'
        })
        run_id += 1

# ================================================================
# WRITE OUTPUT
# ================================================================
df = pd.DataFrame(runs)
df.to_csv("/mnt/Data1/Python_Projects/Pure-Python/P5/06-Pyomo/Project_1/sensitivity_parameters.csv", index=False)

print(f"Generated {len(df)} dramatic scenarios!")
print(df['scenario_type'].value_counts())
