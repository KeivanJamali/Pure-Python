import pandas as pd
import numpy as np
from itertools import product

np.random.seed(42)

# ================================================================
# BASE SYSTEM (medical inventory: e.g., blood bags)
# ================================================================
BASE_L = 3
BASE_C = 30
BASE_P = 20
BASE_H = 2.0
BASE_W = 5
BASE_S = 200
BASE_DEMAND = [30, 15, 40, 60, 45, 30, 150, 35, 210, 300, 10, 20, 150, 10]
BASE_T = len(BASE_DEMAND)

runs = []
run_id = 1

# ================================================================
# 1. DEMAND VOLATILITY — MORE DRAMATIC
# ================================================================
# Moderate → Extreme volatility
volatility_levels = [0.05, 0.20, 0.40, 0.70, 1.00]
samples_per_volatility = 500

for sigma in volatility_levels:
    for sample in range(samples_per_volatility):

        # extreme volatility → can be huge spikes → clipped at +300%
        eps = np.random.normal(scale=sigma, size=BASE_T)
        eps = np.clip(eps, -0.99, 3.0)

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
shelf_life_values = [1, 2, 3, 4, 6, 10]
samples_per_shelf = 40

for L in shelf_life_values:
    for _ in range(samples_per_shelf):

        runs.append({
            'run_id': run_id,
            'T': BASE_T,
            'L': L,
            'C': 80,   # high capacity → shelf life truly matters
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
capacity_values = [10, 20, 30, 40, 60, 80, 100, 120]
samples_per_C = 25

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
shortage_penalties = [1, 10, 20, 40, 80, 100, 200]
samples_per_s = 20

for s in shortage_penalties:
    for _ in range(samples_per_s):

        runs.append({
            'run_id': run_id,
            'T': BASE_T,
            'L': BASE_L,
            'C': 50,
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
waste_costs = [-30, -28, -26, -24, -22, 0, -10]
samples_per_w = 20

for w in waste_costs:
    for _ in range(samples_per_w):
        runs.append({
            'run_id': run_id,
            'T': BASE_T,
            'L': 2,
            'C': 500,
            'p': BASE_P,
            'h': 1.0,
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
holding_costs = [0.1, 0.5, 1, 2, 4, 7, 10]
samples_per_h = 20

for h in holding_costs:
    for _ in range(samples_per_h):
        runs.append({
            'run_id': run_id,
            'T': BASE_T,
            'L': 8,
            'C': 120,
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
