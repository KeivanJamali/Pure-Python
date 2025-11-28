"""
Main script for Blood Bank Optimization - Sensitivity Analysis

This script:
1. Reads sensitivity_parameters.csv
2. Solves optimization for each scenario
3. Aggregates results by scenario type
4. Generates comprehensive visualizations
5. Saves all plots to the 'plots' folder

Author: Keivan Jamali
Date: November 16, 2025
"""

import os
import sys
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')

# Import local modules
from model import BloodBankOptimizer
from visulization import BloodBankVisualizer


def create_output_folder(base_folder: str = "plots") -> Path:
    """Create output folder for plots if it doesn't exist."""
    output_path = Path(__file__).parent / base_folder
    output_path.mkdir(exist_ok=True)
    return output_path


def load_sensitivity_data(csv_path: str = "sensitivity_parameters.csv") -> pd.DataFrame:
    """Load and validate sensitivity parameters CSV."""
    csv_file = Path(__file__).parent / csv_path
    
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_file}")
    
    df = pd.read_csv(csv_file)
    
    return df


def run_single_optimization(row: pd.Series, run_id: int, total_runs: int) -> Dict:
    """
    Run optimization for a single parameter set.
    
    Args:
        row: Row from sensitivity_parameters DataFrame
        run_id: Current run ID
        total_runs: Total number of runs
        
    Returns:
        Dictionary with optimization results
    """
    # Extract parameters
    T = int(row['T'])
    L = int(row['L'])
    p = float(row['p'])
    h = float(row['h'])
    w = float(row['w'])
    s = float(row['s'])
    
    # Extract demand
    demand_cols = [f'demand_t{i}' for i in range(1, T + 1)]
    D = [float(row[col]) for col in demand_cols]
    
    # Handle capacity - can be constant or time-varying (for capacity_disruption)
    capacity_cols = [f'capacity_t{i}' for i in range(1, T + 1)]
    if pd.notna(row.get('capacity_t1')):
        # Time-varying capacity (capacity_disruption scenario)
        # For now, use average capacity for the model (since model doesn't support time-varying C)
        capacities = [float(row[col]) for col in capacity_cols if pd.notna(row.get(col))]
        C = np.mean(capacities) if capacities else float(row['C'])
        has_time_varying_capacity = True
    else:
        C = float(row['C'])
        has_time_varying_capacity = False
    
    # Progress indicator
    if run_id % 100 == 0 or run_id == 1:
        print(f"  [{run_id}/{total_runs}] Running: {row['scenario_type']} - {row['scenario_param']}")
    
    # Create optimizer
    optimizer = BloodBankOptimizer(
        T=T, L=L, D=D, C=C,
        p=p, h=h, s=s, w=w,
        solver_name='glpk'
    )
    
    # Solve
    success = optimizer.solve(verbose=False, tee=False)
    
    if not success:
        print(f"    WARNING: Optimization failed for run_id {row['run_id']}")
        return None
    
    # Extract results
    results = optimizer.results
    
    # Calculate demand volatility (std dev of demand pattern)
    demand_volatility = np.std(D)
    
    return {
        'run_id': int(row['run_id']),
        'scenario_type': row['scenario_type'],
        'scenario_param': row['scenario_param'],
        'T': T,
        'L': L,
        'C': C,
        'p': p,
        'h': h,
        'w': w,
        's': s,
        'demand_volatility': demand_volatility,
        'optimal_cost': results['optimal_cost'],
        'collection_cost': results['collection_cost'],
        'holding_cost': results['holding_cost'],
        'shortage_cost': results['shortage_cost'],
        'waste_cost': results['waste_cost'],
        'total_collected': results['total_collected'],
        'total_shortage': results['total_shortage'],
        'total_waste': results['total_waste'],
        'total_demand': results['total_demand'],
        'service_level': results['service_level'],
        'shortage_frequency': results['shortage_frequency'],
        'avg_inventory': results['avg_inventory'],
    }


def run_all_optimizations(sensitivity_df: pd.DataFrame) -> pd.DataFrame:
    """
    Run optimizations for all scenarios in the CSV.
    
    Args:
        sensitivity_df: DataFrame with sensitivity parameters
        
    Returns:
        DataFrame with all results
    """
    print(f"\n{'='*70}")
    print(f" RUNNING OPTIMIZATIONS ".center(70))
    print(f"{'='*70}\n")
    
    results_list = []
    total_runs = len(sensitivity_df)
    
    for idx, row in sensitivity_df.iterrows():
        result = run_single_optimization(row, idx + 1, total_runs)
        if result is not None:
            results_list.append(result)
    
    results_df = pd.DataFrame(results_list)
    
    print(f"\n{'='*70}")
    print(f"  ✓ Completed {len(results_df)}/{total_runs} optimizations successfully")
    print(f"{'='*70}\n")
    
    return results_df


def extract_numeric_param(scenario_param: str) -> float:
    """Extract numeric value from scenario_param string."""
    # Examples: 'sigma_0.00', 'L_3', 'C_40', 'h_0.5'
    try:
        parts = scenario_param.split('_')
        if len(parts) >= 2:
            return float(parts[-1])
        return float(scenario_param)
    except:
        return 0.0


def analyze_volatility(results_df: pd.DataFrame, visualizer: BloodBankVisualizer, output_path: Path):
    """Analyze demand volatility scenarios."""
    print("\n" + "="*70)
    print(" ANALYZING DEMAND VOLATILITY ".center(70))
    print("="*70)
    
    vol_df = results_df[results_df['scenario_type'] == 'volatility'].copy()
    
    if len(vol_df) == 0:
        print("  No volatility scenarios found.")
        return
    
    # Extract sigma value from scenario_param (e.g., 'sigma_0.05' -> 0.05)
    vol_df['sigma'] = vol_df['scenario_param'].apply(extract_numeric_param)
    
    # Group by sigma level and compute statistics
    grouped = vol_df.groupby('sigma').agg({
        'optimal_cost': ['mean', 'std'],
        'total_shortage': ['mean', 'std'],
        'total_waste': ['mean', 'std'],
        'service_level': 'mean',
        'shortage_frequency': 'mean',
        'demand_volatility': 'mean'  # Average actual demand std dev
    }).reset_index()
    
    # Prepare data for plotting
    plot_df = pd.DataFrame({
        'scenario_param': grouped['sigma'],
        'optimal_cost': grouped['optimal_cost']['mean'],
        'total_shortage': grouped['total_shortage']['mean'],
        'total_waste': grouped['total_waste']['mean']
    })
    
    print(f"\n  Volatility Levels Analyzed: {len(plot_df)}")
    print(f"  Runs per level: {len(vol_df) // max(len(plot_df), 1)}")
    print("\n  Summary Statistics:")
    summary_table = pd.DataFrame({
        'Sigma': grouped['sigma'],
        'Avg_Demand_StdDev': grouped['demand_volatility']['mean'],
        'Mean_Cost': grouped['optimal_cost']['mean'],
        'StdDev_Cost': grouped['optimal_cost']['std'],
        'Mean_Shortage': grouped['total_shortage']['mean'],
        'Mean_Waste': grouped['total_waste']['mean']
    })
    print(summary_table.to_string(index=False))
    
    # Generate plot
    print("\n  Generating volatility analysis plot...")
    visualizer.plot_volatility_analysis(
        plot_df,
        save_path=output_path / "01_volatility_analysis.png",
        show=False
    )
    print("  ✓ Saved: 01_volatility_analysis.png")


def analyze_shelf_life(results_df: pd.DataFrame, visualizer: BloodBankVisualizer, output_path: Path):
    """Analyze shelf life scenarios."""
    print("\n" + "="*70)
    print(" ANALYZING SHELF LIFE SENSITIVITY ".center(70))
    print("="*70)
    
    shelf_df = results_df[results_df['scenario_type'] == 'shelf_life'].copy()
    
    if len(shelf_df) == 0:
        print("  No shelf_life scenarios found.")
        return
    
    # Extract numeric shelf life values
    shelf_df['shelf_life_val'] = shelf_df['L']
    
    # Group by shelf life and compute statistics
    grouped = shelf_df.groupby('shelf_life_val').agg({
        'optimal_cost': 'mean',
        'collection_cost': 'mean',
        'holding_cost': 'mean',
        'shortage_cost': 'mean',
        'waste_cost': 'mean',
        'total_shortage': 'mean',
        'total_waste': 'mean',
    }).reset_index()
    
    # Prepare data for plotting
    plot_df = pd.DataFrame({
        'scenario_param': grouped['shelf_life_val'],
        'optimal_cost': grouped['optimal_cost'],
        'collection_cost': grouped['collection_cost'],
        'holding_cost': grouped['holding_cost'],
        'shortage_cost': grouped['shortage_cost'],
        'waste_cost': grouped['waste_cost'],
        'total_shortage': grouped['total_shortage'],
        'total_waste': grouped['total_waste']
    })
    
    print(f"\n  Shelf Life Levels Analyzed: {len(plot_df)}")
    print(f"  Range: {plot_df['scenario_param'].min():.0f} - {plot_df['scenario_param'].max():.0f} days")
    print("\n  Summary Statistics:")
    print(plot_df.to_string(index=False))
    
    # Generate plot
    print("\n  Generating shelf life analysis plot...")
    visualizer.plot_shelf_life_analysis(
        plot_df,
        save_path=output_path / "02_shelf_life_analysis.png",
        show=False
    )
    print("  ✓ Saved: 02_shelf_life_analysis.png")


def analyze_capacity(results_df: pd.DataFrame, visualizer: BloodBankVisualizer, output_path: Path):
    """Analyze capacity scenarios."""
    print("\n" + "="*70)
    print(" ANALYZING CAPACITY SENSITIVITY ".center(70))
    print("="*70)
    
    cap_df = results_df[results_df['scenario_type'] == 'capacity'].copy()
    
    if len(cap_df) == 0:
        print("  No capacity scenarios found.")
        return
    
    # Use capacity from C column
    cap_df['capacity_val'] = cap_df['C']
    
    # Group by capacity and compute statistics
    grouped = cap_df.groupby('capacity_val').agg({
        'optimal_cost': 'mean',
        'total_shortage': 'mean',
        'total_waste': 'mean',
        'total_collected': 'mean',
        'avg_inventory': 'mean',
    }).reset_index()
    
    # Prepare data for plotting
    plot_df = pd.DataFrame({
        'scenario_param': grouped['capacity_val'],
        'optimal_cost': grouped['optimal_cost'],
        'total_shortage': grouped['total_shortage'],
        'total_waste': grouped['total_waste'],
        'total_collected': grouped['total_collected'],
        'avg_inventory': grouped['avg_inventory']
    })
    
    print(f"\n  Capacity Levels Analyzed: {len(plot_df)}")
    print(f"  Range: {plot_df['scenario_param'].min():.0f} - {plot_df['scenario_param'].max():.0f} units/day")
    print("\n  Summary Statistics:")
    print(plot_df.to_string(index=False))
    
    # Generate plot
    print("\n  Generating capacity analysis plot...")
    visualizer.plot_capacity_analysis(
        plot_df,
        save_path=output_path / "03_capacity_analysis.png",
        show=False
    )
    print("  ✓ Saved: 03_capacity_analysis.png")


def analyze_cost_sensitivity(results_df: pd.DataFrame, visualizer: BloodBankVisualizer, output_path: Path):
    """Analyze cost parameter sensitivity scenarios."""
    print("\n" + "="*70)
    print(" ANALYZING COST PARAMETER SENSITIVITY ".center(70))
    print("="*70)
    
    cost_df = results_df[results_df['scenario_type'] == 'cost_sensitivity'].copy()
    
    if len(cost_df) == 0:
        print("  No cost_sensitivity scenarios found.")
        return
    
    # Identify which cost parameter is being varied
    cost_params_dict = {}
    
    # Check for shortage cost variations
    shortage_variations = cost_df[cost_df['scenario_param'].str.contains('s_', na=False)]
    if len(shortage_variations) > 0:
        shortage_df = shortage_variations.copy()
        shortage_df['param_value'] = shortage_df['s']
        grouped = shortage_df.groupby('param_value').agg({
            'optimal_cost': 'mean',
            'total_shortage': 'mean',
            'total_waste': 'mean',
        }).reset_index()
        cost_params_dict['shortage_cost'] = pd.DataFrame({
            'scenario_param': grouped['param_value'],
            'optimal_cost': grouped['optimal_cost'],
            'total_shortage': grouped['total_shortage'],
            'total_waste': grouped['total_waste']
        })
    
    # Check for waste cost variations
    waste_variations = cost_df[cost_df['scenario_param'].str.contains('w_', na=False)]
    if len(waste_variations) > 0:
        waste_df = waste_variations.copy()
        waste_df['param_value'] = waste_df['w']
        grouped = waste_df.groupby('param_value').agg({
            'optimal_cost': 'mean',
            'total_shortage': 'mean',
            'total_waste': 'mean',
        }).reset_index()
        cost_params_dict['waste_cost'] = pd.DataFrame({
            'scenario_param': grouped['param_value'],
            'optimal_cost': grouped['optimal_cost'],
            'total_shortage': grouped['total_shortage'],
            'total_waste': grouped['total_waste']
        })
    
    # Check for holding cost variations
    holding_variations = cost_df[cost_df['scenario_param'].str.contains('h_', na=False)]
    if len(holding_variations) > 0:
        holding_df = holding_variations.copy()
        holding_df['param_value'] = holding_df['h']
        grouped = holding_df.groupby('param_value').agg({
            'optimal_cost': 'mean',
            'total_shortage': 'mean',
            'total_waste': 'mean',
        }).reset_index()
        cost_params_dict['holding_cost'] = pd.DataFrame({
            'scenario_param': grouped['param_value'],
            'optimal_cost': grouped['optimal_cost'],
            'total_shortage': grouped['total_shortage'],
            'total_waste': grouped['total_waste']
        })
    
    # Check for collection cost variations
    collection_variations = cost_df[cost_df['scenario_param'].str.contains('p_', na=False)]
    if len(collection_variations) > 0:
        collection_df = collection_variations.copy()
        collection_df['param_value'] = collection_df['p']
        grouped = collection_df.groupby('param_value').agg({
            'optimal_cost': 'mean',
            'total_shortage': 'mean',
            'total_waste': 'mean',
        }).reset_index()
        cost_params_dict['collection_cost'] = pd.DataFrame({
            'scenario_param': grouped['param_value'],
            'optimal_cost': grouped['optimal_cost'],
            'total_shortage': grouped['total_shortage'],
            'total_waste': grouped['total_waste']
        })
    
    if len(cost_params_dict) == 0:
        print("  No cost parameter variations found.")
        return
    
    print(f"\n  Cost Parameters Analyzed: {list(cost_params_dict.keys())}")
    for param, df in cost_params_dict.items():
        print(f"\n  {param}:")
        print(f"    Levels: {len(df)}")
        print(f"    Range: {df['scenario_param'].min():.2f} - {df['scenario_param'].max():.2f}")
    
    # Generate plot
    print("\n  Generating cost sensitivity analysis plot...")
    visualizer.plot_cost_sensitivity_analysis(
        cost_params_dict,
        save_path=output_path / "04_cost_sensitivity_analysis.png",
        show=False
    )
    print("  ✓ Saved: 04_cost_sensitivity_analysis.png")


def generate_comparative_summary(results_df: pd.DataFrame, visualizer: BloodBankVisualizer, output_path: Path):
    """Generate comparative summary across all scenario types."""
    print("\n" + "="*70)
    print(" GENERATING COMPARATIVE SUMMARY ".center(70))
    print("="*70)
    
    # Compute summary statistics for each scenario type
    # Exclude capacity_disruption as it's a special case
    scenario_types_to_plot = [st for st in results_df['scenario_type'].unique() 
                              if st != 'capacity_disruption']
    
    scenario_summaries = {}
    
    for scenario_type in scenario_types_to_plot:
        scenario_data = results_df[results_df['scenario_type'] == scenario_type]
        
        scenario_summaries[scenario_type] = {
            'mean_cost': scenario_data['optimal_cost'].mean(),
            'mean_shortage': scenario_data['total_shortage'].mean(),
            'mean_waste': scenario_data['total_waste'].mean(),
            'std_cost': scenario_data['optimal_cost'].std(),
        }
    
    print("\n  Scenario Type Summaries:")
    for scenario, summary in scenario_summaries.items():
        print(f"\n  {scenario}:")
        print(f"    Mean Cost: ${summary['mean_cost']:,.2f} (±${summary['std_cost']:.2f})")
        print(f"    Mean Shortage: {summary['mean_shortage']:.2f} units")
        print(f"    Mean Waste: {summary['mean_waste']:.2f} units")
    
    # Also print capacity_disruption separately if it exists
    if 'capacity_disruption' in results_df['scenario_type'].unique():
        cap_disrupt_data = results_df[results_df['scenario_type'] == 'capacity_disruption']
        print(f"\n  capacity_disruption (not plotted):")
        print(f"    Mean Cost: ${cap_disrupt_data['optimal_cost'].mean():,.2f} (±${cap_disrupt_data['optimal_cost'].std():.2f})")
        print(f"    Mean Shortage: {cap_disrupt_data['total_shortage'].mean():.2f} units")
        print(f"    Mean Waste: {cap_disrupt_data['total_waste'].mean():.2f} units")
    
    # Generate plot
    print("\n  Generating comparative summary plot...")
    visualizer.plot_comparative_summary(
        scenario_summaries,
        save_path=output_path / "05_comparative_summary.png",
        show=False
    )
    print("  ✓ Saved: 05_comparative_summary.png")


def save_results_to_csv(results_df: pd.DataFrame, output_path: Path):
    """Save aggregated results to CSV."""
    print("\n" + "="*70)
    print(" SAVING RESULTS ".center(70))
    print("="*70)
    
    csv_path = output_path / "aggregated_results.csv"
    results_df.to_csv(csv_path, index=False)
    print(f"  ✓ Saved: aggregated_results.csv ({len(results_df)} rows)")
    
    # Save summary statistics
    summary_stats = []
    for scenario_type in results_df['scenario_type'].unique():
        scenario_data = results_df[results_df['scenario_type'] == scenario_type]
        summary_stats.append({
            'scenario_type': scenario_type,
            'num_runs': len(scenario_data),
            'mean_cost': scenario_data['optimal_cost'].mean(),
            'std_cost': scenario_data['optimal_cost'].std(),
            'min_cost': scenario_data['optimal_cost'].min(),
            'max_cost': scenario_data['optimal_cost'].max(),
            'mean_shortage': scenario_data['total_shortage'].mean(),
            'mean_waste': scenario_data['total_waste'].mean(),
            'mean_service_level': scenario_data['service_level'].mean(),
        })
    
    summary_df = pd.DataFrame(summary_stats)
    summary_path = output_path / "summary_statistics.csv"
    summary_df.to_csv(summary_path, index=False)
    print(f"  ✓ Saved: summary_statistics.csv")


def run_base_case_example(visualizer: BloodBankVisualizer, output_path: Path):
    """Run and visualize the base case example."""
    print("\n" + "="*70)
    print(" RUNNING BASE CASE EXAMPLE ".center(70))
    print("="*70)
    
    # Base parameters
    T = 10
    L = 3
    D = [30, 15, 20, 60, 45, 30, 100, 35, 10, 10]
    C = 40
    p = 20
    h = 0.5
    w = 5
    s = 200
    
    print(f"\n  Parameters:")
    print(f"    T={T}, L={L}, C={C}, p={p}, h={h}, w={w}, s={s}")
    print(f"    Demand: {D}")
    
    # Create and solve
    optimizer = BloodBankOptimizer(
        T=T, L=L, D=D, C=C,
        p=p, h=h, s=s, w=w,
        solver_name='glpk'
    )
    
    print("\n  Solving base case...")
    success = optimizer.solve(verbose=False)
    
    if success:
        print("  ✓ Optimization successful!")
        optimizer.print_summary()
        
        # Generate visualization
        print("\n  Generating base case visualization...")
        visualizer.plot_single_run_summary(
            optimizer.results,
            D,
            save_path=output_path / "00_base_case_analysis.png",
            show=False
        )
        print("  ✓ Saved: 00_base_case_analysis.png")
    else:
        print("  ✗ Optimization failed!")


def main():
    """Main execution function."""
    print("\n" + "="*70)
    print(" BLOOD BANK OPTIMIZATION - SENSITIVITY ANALYSIS ".center(70))
    print("="*70)
    print(f"  Author: Keivan Jamali")
    print(f"  Date: November 16, 2025")
    print("="*70)
    
    # Create output folder
    output_path = create_output_folder("./plots")
    print(f"\n✓ Output folder created: {output_path}")
    
    # Initialize visualizer
    visualizer = BloodBankVisualizer()
    print("✓ Visualizer initialized")
    
    # Run base case
    run_base_case_example(visualizer, output_path)
    
    # Load sensitivity data
    sensitivity_df = load_sensitivity_data()
    
    # Run all optimizations
    results_df = run_all_optimizations(sensitivity_df)
    
    # Perform analyses
    analyze_volatility(results_df, visualizer, output_path)
    analyze_shelf_life(results_df, visualizer, output_path)
    analyze_capacity(results_df, visualizer, output_path)
    analyze_cost_sensitivity(results_df, visualizer, output_path)
    
    # Generate comparative summary
    generate_comparative_summary(results_df, visualizer, output_path)
    
    # Save results
    save_results_to_csv(results_df, output_path)

if __name__ == "__main__":
    main()
