"""
Multi-Period Blood-Bank Inventory Optimization using Pyomo

This module provides a class to solve blood inventory optimization problems
considering collection costs, storage costs, shortage penalties, and waste costs.

Author: Keivan Jamali
Date: November 16, 2025
"""

import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import numpy as np
from typing import Dict, List, Optional, Tuple
import pandas as pd


class BloodBankOptimizer:
    """
    Optimize blood collection and inventory management decisions across multiple periods.
    
    This class formulates and solves an LP model to minimize total costs while balancing:
    - Collection costs from procuring blood units
    - Storage costs from maintaining inventory
    - Shortage costs from unmet demand (patient risk)
    - Waste costs from expired blood units
    
    Attributes:
        T (int): Number of planning periods
        L (int): Shelf life of blood (in periods)
        D (list): Demand for blood in each period
        C (float): Maximum collection capacity per period
        p (float): Unit cost of collecting blood
        h (float): Unit cost of holding inventory per period
        s (float): Unit cost of shortage (high penalty for unmet demand)
        w (float): Unit cost of wasting expired blood
        model (ConcreteModel): Pyomo optimization model
        results (dict): Optimization results and KPIs
    """
    
    def __init__(
        self,
        T: int,
        L: int,
        D: List[float],
        C: float,
        p: float,
        h: float,
        s: float,
        w: float,
        initial_inventory: Optional[Dict[int, float]] = None,
        solver_name: str = 'glpk'
    ):
        """
        Initialize the Blood Bank Optimizer.
        
        Args:
            T: Number of planning periods
            L: Shelf life of blood (in periods)
            D: List of demand values for each period (length should be T)
            C: Maximum collection capacity per period
            p: Unit cost of collecting blood
            h: Unit cost of holding inventory per period
            s: Unit cost of shortage (penalty for unmet demand)
            w: Unit cost of wasting expired blood
            initial_inventory: Dict mapping age to initial inventory (default: all zeros)
            solver_name: Name of the solver to use (default: 'glpk')
        """
        # Validate inputs
        if len(D) != T:
            raise ValueError(f"Demand list length ({len(D)}) must equal planning horizon T ({T})")
        if L < 1:
            raise ValueError(f"Shelf life L must be at least 1, got {L}")
        if C < 0:
            raise ValueError(f"Capacity C must be non-negative, got {C}")
        
        # Store parameters
        self.T = T
        self.L = L
        self.D = D
        self.C = C
        self.p = p
        self.h = h
        self.s = s
        self.w = w
        self.solver_name = solver_name
        
        # Initial inventory (default: all zeros)
        if initial_inventory is None:
            self.initial_inventory = {a: 0.0 for a in range(1, L + 1)}
        else:
            self.initial_inventory = initial_inventory
        
        # Model and results
        self.model = None
        self.results = None
        self.solver_status = None
    
    def build_model(self) -> pyo.ConcreteModel:
        """
        Build the Pyomo optimization model.
        
        Returns:
            ConcreteModel: The formulated Pyomo model
        """
        model = pyo.ConcreteModel(name="Blood_Bank_Inventory_Optimization")
        
        # Sets
        model.T_set = pyo.RangeSet(1, self.T)  # Time periods
        model.A_set = pyo.RangeSet(1, self.L)  # Age of blood (1 = fresh, L = oldest)
        
        # Decision Variables
        model.x = pyo.Var(model.T_set, domain=pyo.NonNegativeReals, doc="Blood units collected in period t")
        model.I = pyo.Var(model.T_set, model.A_set, domain=pyo.NonNegativeReals, 
                         doc="Inventory of blood age a at end of period t")
        model.use = pyo.Var(model.T_set, model.A_set, domain=pyo.NonNegativeReals,
                           doc="Blood units of age a used in period t")
        model.shortage = pyo.Var(model.T_set, domain=pyo.NonNegativeReals,
                                doc="Unmet demand in period t")
        model.waste = pyo.Var(model.T_set, domain=pyo.NonNegativeReals,
                             doc="Expired blood units in period t")
        
        # Objective Function: Minimize total cost
        def objective_rule(m):
            collection_cost = sum(self.p * m.x[t] for t in m.T_set)
            holding_cost = sum(self.h * m.I[t, a] for t in m.T_set for a in m.A_set)
            shortage_cost = sum(self.s * m.shortage[t] for t in m.T_set)
            waste_cost = sum(self.w * m.waste[t] for t in m.T_set)
            return collection_cost + holding_cost + shortage_cost + waste_cost
        
        model.objective = pyo.Objective(rule=objective_rule, sense=pyo.minimize)
        
        # Constraints
        
        # 1. Collection capacity constraint
        def collection_capacity_rule(m, t):
            return m.x[t] <= self.C
        model.collection_capacity = pyo.Constraint(model.T_set, rule=collection_capacity_rule)
        
        # 2. Demand satisfaction constraint
        def demand_satisfaction_rule(m, t):
            return sum(m.use[t, a] for a in m.A_set) + m.shortage[t] == self.D[t - 1]
        model.demand_satisfaction = pyo.Constraint(model.T_set, rule=demand_satisfaction_rule)
        
        # 3. Inventory balance by age (for age >= 2)
        def inventory_balance_rule(m, t, a):
            if a == 1:
                return pyo.Constraint.Skip
            if t == 1:
                # Initial inventory
                return m.I[t, a] == self.initial_inventory.get(a - 1, 0) - m.use[t, a]
            else:
                return m.I[t, a] == m.I[t - 1, a - 1] - m.use[t, a]
        model.inventory_balance = pyo.Constraint(model.T_set, model.A_set, rule=inventory_balance_rule)
        
        # 4. New inventory (age = 1)
        def new_inventory_rule(m, t):
            return m.I[t, 1] == m.x[t] - m.use[t, 1]
        model.new_inventory = pyo.Constraint(model.T_set, rule=new_inventory_rule)
        
        # 5. Waste (expired blood)
        def waste_rule(m, t):
            if t == 1:
                # Waste from initial inventory of oldest age
                return m.waste[t] == self.initial_inventory.get(self.L, 0)
            else:
                return m.waste[t] == m.I[t - 1, self.L]
        model.waste_constraint = pyo.Constraint(model.T_set, rule=waste_rule)
        
        self.model = model
        return model
    
    def solve(self, verbose: bool = False, tee: bool = False) -> bool:
        """
        Solve the optimization model.
        
        Args:
            verbose: If True, print solver output
            tee: If True, display solver output stream
            
        Returns:
            bool: True if solved successfully, False otherwise
        """
        if self.model is None:
            self.build_model()
        
        # Create solver
        solver = SolverFactory(self.solver_name)
        
        if not solver.available():
            raise RuntimeError(f"Solver '{self.solver_name}' is not available. "
                             f"Please install it or specify a different solver.")
        
        # Solve
        self.solver_status = solver.solve(self.model, tee=tee)
        
        # Check if solved successfully
        if (self.solver_status.solver.status == pyo.SolverStatus.ok and
            self.solver_status.solver.termination_condition == pyo.TerminationCondition.optimal):
            
            if verbose:
                print("✓ Optimization solved successfully!")
                print(f"Optimal Total Cost: ${pyo.value(self.model.objective):.2f}")
            
            self._extract_results()
            return True
        else:
            if verbose:
                print("✗ Optimization failed or did not find optimal solution.")
                print(f"Status: {self.solver_status.solver.status}")
                print(f"Termination: {self.solver_status.solver.termination_condition}")
            return False
    
    def _extract_results(self):
        """Extract and store optimization results."""
        m = self.model
        
        # Extract decision variables
        x_schedule = [pyo.value(m.x[t]) for t in m.T_set]
        inventory = {(t, a): pyo.value(m.I[t, a]) for t in m.T_set for a in m.A_set}
        usage = {(t, a): pyo.value(m.use[t, a]) for t in m.T_set for a in m.A_set}
        shortages = [pyo.value(m.shortage[t]) for t in m.T_set]
        waste = [pyo.value(m.waste[t]) for t in m.T_set]
        
        # Calculate costs
        total_cost = pyo.value(m.objective)
        collection_cost = sum(self.p * pyo.value(m.x[t]) for t in m.T_set)
        holding_cost = sum(self.h * pyo.value(m.I[t, a]) for t in m.T_set for a in m.A_set)
        shortage_cost = sum(self.s * pyo.value(m.shortage[t]) for t in m.T_set)
        waste_cost = sum(self.w * pyo.value(m.waste[t]) for t in m.T_set)
        
        # Calculate KPIs
        total_collected = sum(x_schedule)
        total_shortage = sum(shortages)
        total_waste = sum(waste)
        total_demand = sum(self.D)
        shortage_frequency = sum(1 for s in shortages if s > 0.01) / self.T
        service_level = (total_demand - total_shortage) / total_demand if total_demand > 0 else 1.0
        avg_inventory = sum(sum(pyo.value(m.I[t, a]) for a in m.A_set) for t in m.T_set) / self.T
        
        # Store results
        self.results = {
            'optimal_cost': total_cost,
            'collection_cost': collection_cost,
            'holding_cost': holding_cost,
            'shortage_cost': shortage_cost,
            'waste_cost': waste_cost,
            'collection_schedule': x_schedule,
            'inventory': inventory,
            'usage': usage,
            'shortages': shortages,
            'waste': waste,
            'total_collected': total_collected,
            'total_shortage': total_shortage,
            'total_waste': total_waste,
            'total_demand': total_demand,
            'shortage_frequency': shortage_frequency,
            'service_level': service_level,
            'avg_inventory': avg_inventory,
        }
    
    def get_results_summary(self) -> Dict:
        """
        Get a summary of the optimization results.
        
        Returns:
            Dictionary containing key results and KPIs
        """
        if self.results is None:
            raise RuntimeError("Model has not been solved yet. Call solve() first.")
        
        return {
            'optimal_total_cost': self.results['optimal_cost'],
            'cost_breakdown': {
                'collection': self.results['collection_cost'],
                'holding': self.results['holding_cost'],
                'shortage': self.results['shortage_cost'],
                'waste': self.results['waste_cost'],
            },
            'operations': {
                'total_collected': self.results['total_collected'],
                'total_shortage': self.results['total_shortage'],
                'total_waste': self.results['total_waste'],
                'total_demand': self.results['total_demand'],
            },
            'kpis': {
                'service_level': self.results['service_level'],
                'shortage_frequency': self.results['shortage_frequency'],
                'avg_inventory': self.results['avg_inventory'],
            }
        }
    
    def print_summary(self):
        """Print a formatted summary of the optimization results."""
        if self.results is None:
            raise RuntimeError("Model has not been solved yet. Call solve() first.")
        
        print("\n" + "="*70)
        print(" BLOOD BANK OPTIMIZATION RESULTS ".center(70))
        print("="*70)
        
        print(f"\n{'COST BREAKDOWN':^70}")
        print("-"*70)
        print(f"  Total Cost:              ${self.results['optimal_cost']:>12,.2f}")
        print(f"    ├─ Collection Cost:    ${self.results['collection_cost']:>12,.2f}  ({self.results['collection_cost']/self.results['optimal_cost']*100:>5.1f}%)")
        print(f"    ├─ Holding Cost:       ${self.results['holding_cost']:>12,.2f}  ({self.results['holding_cost']/self.results['optimal_cost']*100:>5.1f}%)")
        print(f"    ├─ Shortage Cost:      ${self.results['shortage_cost']:>12,.2f}  ({self.results['shortage_cost']/self.results['optimal_cost']*100:>5.1f}%)")
        print(f"    └─ Waste Cost:         ${self.results['waste_cost']:>12,.2f}  ({self.results['waste_cost']/self.results['optimal_cost']*100:>5.1f}%)")
        
        print(f"\n{'OPERATIONAL METRICS':^70}")
        print("-"*70)
        print(f"  Total Demand:            {self.results['total_demand']:>12,.1f} units")
        print(f"  Total Collected:         {self.results['total_collected']:>12,.1f} units")
        print(f"  Total Shortage:          {self.results['total_shortage']:>12,.1f} units")
        print(f"  Total Waste:             {self.results['total_waste']:>12,.1f} units")
        print(f"  Average Inventory:       {self.results['avg_inventory']:>12,.1f} units")
        
        print(f"\n{'KEY PERFORMANCE INDICATORS':^70}")
        print("-"*70)
        print(f"  Service Level:           {self.results['service_level']*100:>12,.1f}%")
        print(f"  Shortage Frequency:      {self.results['shortage_frequency']*100:>12,.1f}%")
        
        print(f"\n{'COLLECTION SCHEDULE':^70}")
        print("-"*70)
        for t, amount in enumerate(self.results['collection_schedule'], 1):
            print(f"  Period {t}:  {amount:>8,.1f} units  (Demand: {self.D[t-1]:>6,.1f}, Shortage: {self.results['shortages'][t-1]:>6,.1f})")
        
        print("\n" + "="*70 + "\n")
    
    def get_inventory_dataframe(self) -> pd.DataFrame:
        """
        Get inventory data as a pandas DataFrame.
        
        Returns:
            DataFrame with columns: Period, Age, Inventory
        """
        if self.results is None:
            raise RuntimeError("Model has not been solved yet. Call solve() first.")
        
        data = []
        for (t, a), value in self.results['inventory'].items():
            data.append({'Period': t, 'Age': a, 'Inventory': value})
        
        return pd.DataFrame(data)
    
    def get_schedule_dataframe(self) -> pd.DataFrame:
        """
        Get collection schedule and key metrics as a pandas DataFrame.
        
        Returns:
            DataFrame with columns: Period, Demand, Collection, Shortage, Waste, Total_Inventory
        """
        if self.results is None:
            raise RuntimeError("Model has not been solved yet. Call solve() first.")
        
        data = []
        for t in range(1, self.T + 1):
            total_inv = sum(self.results['inventory'][(t, a)] for a in range(1, self.L + 1))
            data.append({
                'Period': t,
                'Demand': self.D[t - 1],
                'Collection': self.results['collection_schedule'][t - 1],
                'Shortage': self.results['shortages'][t - 1],
                'Waste': self.results['waste'][t - 1],
                'Total_Inventory': total_inv
            })
        
        return pd.DataFrame(data)
    
    def get_dual_values(self) -> Dict[str, Dict]:
        """
        Extract dual values (shadow prices) from the optimization model.
        
        Returns:
            Dictionary containing dual values for each constraint
        """
        if self.model is None or self.results is None:
            raise RuntimeError("Model has not been solved yet. Call solve() first.")
        
        dual_values = {}
        
        # Load dual values (shadow prices)
        self.model.dual = pyo.Suffix(direction=pyo.Suffix.IMPORT)
        
        try:
            # Collection capacity duals
            dual_values['collection_capacity'] = {
                t: self.model.dual[self.model.collection_capacity[t]]
                for t in self.model.T_set
            }
            
            # Demand satisfaction duals
            dual_values['demand_satisfaction'] = {
                t: self.model.dual[self.model.demand_satisfaction[t]]
                for t in self.model.T_set
            }
        except KeyError:
            print("Warning: Dual values not available. Some solvers don't provide dual information.")
            return {}
        
        return dual_values


def main():
    """Example usage of the BloodBankOptimizer class."""
    
    print("\n" + "="*70)
    print(" BLOOD BANK OPTIMIZATION - BASE CASE ".center(70))
    print("="*70 + "\n")
    
    # Base parameters (Part A)
    T = 8  # Planning horizon (days)
    L = 3  # Shelf life (days)
    D = [30, 35, 50, 60, 45, 30, 40, 35]  # Demand (units/day)
    C = 40  # Collection capacity (units/day)
    p = 20  # Collection cost ($/unit)
    h = 0.5  # Holding cost ($/unit/day)
    w = 10  # Disposal cost ($/expired unit)
    s = 200  # Shortage penalty ($/unit)
    
    print("Parameters:")
    print(f"  Planning Horizon (T):     {T} days")
    print(f"  Shelf Life (L):           {L} days")
    print(f"  Collection Capacity (C):  {C} units/day")
    print(f"  Collection Cost (p):      ${p}/unit")
    print(f"  Holding Cost (h):         ${h}/unit/day")
    print(f"  Disposal Cost (w):        ${w}/expired unit")
    print(f"  Shortage Penalty (s):     ${s}/unit")
    print(f"  Demand Pattern:           {D}")
    
    # Create optimizer instance
    optimizer = BloodBankOptimizer(
        T=T, L=L, D=D, C=C,
        p=p, h=h, s=s, w=w,
        solver_name='glpk'
    )
    
    # Build and solve model
    print("\nBuilding optimization model...")
    optimizer.build_model()
    
    print("Solving...")
    success = optimizer.solve(verbose=True)
    
    if success:
        # Print detailed summary
        optimizer.print_summary()
        
        # Get dataframes
        schedule_df = optimizer.get_schedule_dataframe()
        print("\nSchedule DataFrame:")
        print(schedule_df.to_string(index=False))
        
        inventory_df = optimizer.get_inventory_dataframe()
        print("\nInventory by Age (first 10 rows):")
        print(inventory_df.head(10).to_string(index=False))
        
        # Get summary dictionary
        summary = optimizer.get_results_summary()
        print("\nResults Summary Dictionary:")
        print(f"  Optimal Cost: ${summary['optimal_total_cost']:.2f}")
        print(f"  Service Level: {summary['kpis']['service_level']*100:.1f}%")
    else:
        print("\n✗ Optimization failed!")


if __name__ == "__main__":
    main()
