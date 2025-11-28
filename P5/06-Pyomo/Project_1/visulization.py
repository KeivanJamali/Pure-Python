"""
Visualization Module for Blood-Bank Inventory Optimization

This module provides comprehensive visualization capabilities for analyzing
optimization results across multiple scenarios and sensitivity analyses.

Author: Keivan Jamali
Date: November 16, 2025
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
from matplotlib.figure import Figure
from matplotlib.axes import Axes


class BloodBankVisualizer:
    """
    Comprehensive visualization toolkit for blood bank optimization analysis.
    
    This class provides methods to create various plots for analyzing:
    - Single optimization run results
    - Demand volatility analysis
    - Shelf-life sensitivity
    - Capacity analysis
    - Cost parameter sensitivity
    - Comparative scenario analysis
    """
    
    def __init__(self, style: str = 'seaborn-v0_8-darkgrid', figsize_default: Tuple[int, int] = (12, 6)):
        """
        Initialize the visualizer with plotting preferences.
        
        Args:
            style: Matplotlib style to use
            figsize_default: Default figure size (width, height)
        """
        # Set style
        try:
            plt.style.use(style)
        except:
            plt.style.use('default')
        
        self.figsize_default = figsize_default
        self.colors = {
            'collection': '#2E86AB',
            'holding': '#A23B72',
            'shortage': '#F18F01',
            'waste': '#C73E1D',
            'demand': '#6A994E',
            'inventory': '#BC4B51',
            'total_cost': '#1F77B4',
        }
        
        # Set seaborn style
        sns.set_palette("husl")
    
    def plot_single_run_summary(
        self,
        results: Dict,
        demand: List[float],
        save_path: Optional[str] = None,
        show: bool = True
    ) -> Figure:
        """
        Create a comprehensive 4-panel plot for a single optimization run.
        
        Args:
            results: Results dictionary from BloodBankOptimizer
            demand: Demand list
            save_path: Path to save figure (optional)
            show: Whether to display the plot
            
        Returns:
            Matplotlib Figure object
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Blood Bank Optimization - Single Run Analysis', fontsize=16, fontweight='bold')
        
        periods = list(range(1, len(demand) + 1))
        
        # Panel 1: Collection Schedule vs Demand
        ax1 = axes[0, 0]
        ax1.plot(periods, demand, 'o-', color=self.colors['demand'], 
                linewidth=2, markersize=8, label='Demand')
        ax1.plot(periods, results['collection_schedule'], 's-', 
                color=self.colors['collection'], linewidth=2, markersize=8, label='Collection')
        ax1.fill_between(periods, 0, results['collection_schedule'], 
                         alpha=0.3, color=self.colors['collection'])
        ax1.set_xlabel('Period', fontsize=12)
        ax1.set_ylabel('Units', fontsize=12)
        ax1.set_title('Collection Schedule vs Demand', fontsize=14, fontweight='bold')
        ax1.legend(loc='best', fontsize=10)
        ax1.grid(True, alpha=0.3)
        
        # Panel 2: Shortage and Waste over Time
        ax2 = axes[0, 1]
        x = np.arange(len(periods))
        width = 0.35
        ax2.bar(x - width/2, results['shortages'], width, label='Shortage', 
               color=self.colors['shortage'], alpha=0.8)
        ax2.bar(x + width/2, results['waste'], width, label='Waste', 
               color=self.colors['waste'], alpha=0.8)
        ax2.set_xlabel('Period', fontsize=12)
        ax2.set_ylabel('Units', fontsize=12)
        ax2.set_title('Shortage and Waste by Period', fontsize=14, fontweight='bold')
        ax2.set_xticks(x)
        ax2.set_xticklabels(periods)
        ax2.legend(loc='best', fontsize=10)
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Panel 3: Cost Breakdown (Pie Chart)
        ax3 = axes[1, 0]
        cost_data = [
            results['collection_cost'],
            results['holding_cost'],
            results['shortage_cost'],
            results['waste_cost']
        ]
        cost_labels = ['Collection', 'Holding', 'Shortage', 'Waste']
        colors_pie = [self.colors['collection'], self.colors['holding'], 
                     self.colors['shortage'], self.colors['waste']]
        
        wedges, texts, autotexts = ax3.pie(
            cost_data, labels=cost_labels, autopct='%1.1f%%',
            colors=colors_pie, startangle=90, textprops={'fontsize': 10}
        )
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        ax3.set_title(f'Cost Breakdown\nTotal: ${results["optimal_cost"]:,.2f}', 
                     fontsize=14, fontweight='bold')
        
        # Panel 4: Inventory by Age (Stacked Area)
        ax4 = axes[1, 1]
        
        # Prepare inventory data by age
        T = len(periods)
        L = max([a for (t, a) in results['inventory'].keys()])
        inventory_by_age = {a: [] for a in range(1, L + 1)}
        
        for t in range(1, T + 1):
            for a in range(1, L + 1):
                inventory_by_age[a].append(results['inventory'].get((t, a), 0))
        
        # Create stacked area plot
        ax4.stackplot(
            periods,
            *[inventory_by_age[a] for a in range(1, L + 1)],
            labels=[f'Age {a}' for a in range(1, L + 1)],
            alpha=0.7
        )
        ax4.set_xlabel('Period', fontsize=12)
        ax4.set_ylabel('Inventory Units', fontsize=12)
        ax4.set_title('Inventory by Age Over Time', fontsize=14, fontweight='bold')
        ax4.legend(loc='upper left', fontsize=10)
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        
        return fig
    
    def plot_volatility_analysis(
        self,
        results_df: pd.DataFrame,
        save_path: Optional[str] = None,
        show: bool = True
    ) -> Figure:
        """
        Plot analysis of demand volatility impact.
        
        Args:
            results_df: DataFrame with columns: scenario_param (volatility), 
                       optimal_cost, total_shortage, total_waste
            save_path: Path to save figure
            show: Whether to display the plot
            
        Returns:
            Matplotlib Figure object
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))
        fig.suptitle('Demand Volatility Analysis', fontsize=16, fontweight='bold')
        
        volatility = results_df['scenario_param'].values
        
        # Panel 1: Total Cost vs Volatility
        ax1 = axes[0]
        ax1.plot(volatility, results_df['optimal_cost'], 'o-', 
                color=self.colors['total_cost'], linewidth=2, markersize=8)
        ax1.fill_between(volatility, results_df['optimal_cost'].min(), 
                        results_df['optimal_cost'], alpha=0.3, color=self.colors['total_cost'])
        ax1.set_xlabel('Demand Volatility (σ)', fontsize=12)
        ax1.set_ylabel('Total Cost ($)', fontsize=12)
        ax1.set_title('Total Cost vs Volatility', fontsize=13, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        # Add percentage change annotation
        cost_change = (results_df['optimal_cost'].iloc[-1] - results_df['optimal_cost'].iloc[0]) / results_df['optimal_cost'].iloc[0] * 100
        ax1.text(0.05, 0.95, f'Cost Change: {cost_change:+.1f}%', 
                transform=ax1.transAxes, fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # Panel 2: Shortage vs Volatility
        ax2 = axes[1]
        ax2.plot(volatility, results_df['total_shortage'], 'o-', 
                color=self.colors['shortage'], linewidth=2, markersize=8)
        ax2.fill_between(volatility, 0, results_df['total_shortage'], 
                        alpha=0.3, color=self.colors['shortage'])
        ax2.set_xlabel('Demand Volatility (σ)', fontsize=12)
        ax2.set_ylabel('Total Shortage (units)', fontsize=12)
        ax2.set_title('Shortage vs Volatility', fontsize=13, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        # Panel 3: Waste vs Volatility
        ax3 = axes[2]
        ax3.plot(volatility, results_df['total_waste'], 'o-', 
                color=self.colors['waste'], linewidth=2, markersize=8)
        ax3.fill_between(volatility, 0, results_df['total_waste'], 
                        alpha=0.3, color=self.colors['waste'])
        ax3.set_xlabel('Demand Volatility (σ)', fontsize=12)
        ax3.set_ylabel('Total Waste (units)', fontsize=12)
        ax3.set_title('Waste vs Volatility', fontsize=13, fontweight='bold')
        ax3.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        
        return fig
    
    def plot_shelf_life_analysis(
        self,
        results_df: pd.DataFrame,
        save_path: Optional[str] = None,
        show: bool = True
    ) -> Figure:
        """
        Plot analysis of shelf life impact.
        
        Args:
            results_df: DataFrame with columns: scenario_param (shelf_life L), 
                       optimal_cost, total_shortage, total_waste, collection_cost, holding_cost
            save_path: Path to save figure
            show: Whether to display the plot
            
        Returns:
            Matplotlib Figure object
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Shelf Life Sensitivity Analysis', fontsize=16, fontweight='bold')
        
        shelf_life = results_df['scenario_param'].values
        
        # Panel 1: Total Cost vs Shelf Life
        ax1 = axes[0, 0]
        ax1.plot(shelf_life, results_df['optimal_cost'], 'o-', 
                color=self.colors['total_cost'], linewidth=2, markersize=10)
        ax1.set_xlabel('Shelf Life (days)', fontsize=12)
        ax1.set_ylabel('Total Cost ($)', fontsize=12)
        ax1.set_title('Total Cost vs Shelf Life', fontsize=13, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.set_xticks(shelf_life)
        
        # Panel 2: Shortage and Waste vs Shelf Life
        ax2 = axes[0, 1]
        ax2.plot(shelf_life, results_df['total_shortage'], 'o-', 
                color=self.colors['shortage'], linewidth=2, markersize=10, label='Shortage')
        ax2.plot(shelf_life, results_df['total_waste'], 's-', 
                color=self.colors['waste'], linewidth=2, markersize=10, label='Waste')
        ax2.set_xlabel('Shelf Life (days)', fontsize=12)
        ax2.set_ylabel('Units', fontsize=12)
        ax2.set_title('Shortage and Waste vs Shelf Life', fontsize=13, fontweight='bold')
        ax2.legend(loc='best', fontsize=11)
        ax2.grid(True, alpha=0.3)
        ax2.set_xticks(shelf_life)
        
        # Panel 3: Cost Components Breakdown
        ax3 = axes[1, 0]
        width = 0.6
        x = np.arange(len(shelf_life))
        
        # Stacked bar chart
        ax3.bar(x, results_df['collection_cost'], width, label='Collection', 
               color=self.colors['collection'], alpha=0.8)
        ax3.bar(x, results_df['holding_cost'], width, bottom=results_df['collection_cost'],
               label='Holding', color=self.colors['holding'], alpha=0.8)
        bottom = results_df['collection_cost'] + results_df['holding_cost']
        ax3.bar(x, results_df['shortage_cost'], width, bottom=bottom,
               label='Shortage', color=self.colors['shortage'], alpha=0.8)
        bottom += results_df['shortage_cost']
        ax3.bar(x, results_df['waste_cost'], width, bottom=bottom,
               label='Waste', color=self.colors['waste'], alpha=0.8)
        
        ax3.set_xlabel('Shelf Life (days)', fontsize=12)
        ax3.set_ylabel('Cost ($)', fontsize=12)
        ax3.set_title('Cost Components Breakdown', fontsize=13, fontweight='bold')
        ax3.set_xticks(x)
        ax3.set_xticklabels(shelf_life.astype(int))
        ax3.legend(loc='best', fontsize=10)
        ax3.grid(True, alpha=0.3, axis='y')
        
        # Panel 4: Marginal Benefit of Increasing Shelf Life
        ax4 = axes[1, 1]
        if len(shelf_life) > 1:
            marginal_benefit = -np.diff(results_df['optimal_cost'].values)
            shelf_life_mid = shelf_life[:-1] + 0.5
            
            colors_mb = ['green' if mb > 0 else 'red' for mb in marginal_benefit]
            ax4.bar(shelf_life_mid, marginal_benefit, width=0.6, color=colors_mb, alpha=0.7)
            ax4.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
            ax4.set_xlabel('Shelf Life Extension (from L to L+1)', fontsize=12)
            ax4.set_ylabel('Cost Reduction ($)', fontsize=12)
            ax4.set_title('Marginal Benefit of Increasing Shelf Life by 1 Day', 
                         fontsize=13, fontweight='bold')
            ax4.grid(True, alpha=0.3, axis='y')
            
            # Add value labels on bars
            for i, (x_pos, mb) in enumerate(zip(shelf_life_mid, marginal_benefit)):
                ax4.text(x_pos, mb, f'${mb:.0f}', ha='center', 
                        va='bottom' if mb > 0 else 'top', fontsize=9)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        
        return fig
    
    def plot_capacity_analysis(
        self,
        results_df: pd.DataFrame,
        save_path: Optional[str] = None,
        show: bool = True
    ) -> Figure:
        """
        Plot analysis of collection capacity impact.
        
        Args:
            results_df: DataFrame with columns: scenario_param (capacity C), 
                       optimal_cost, total_shortage, total_waste, total_collected, avg_inventory
            save_path: Path to save figure
            show: Whether to display the plot
            
        Returns:
            Matplotlib Figure object
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Collection Capacity Analysis', fontsize=16, fontweight='bold')
        
        capacity = results_df['scenario_param'].values
        
        # Panel 1: Total Cost vs Capacity
        ax1 = axes[0, 0]
        ax1.plot(capacity, results_df['optimal_cost'], 'o-', 
                color=self.colors['total_cost'], linewidth=2, markersize=10)
        ax1.fill_between(capacity, results_df['optimal_cost'], 
                        results_df['optimal_cost'].max(), alpha=0.2, color=self.colors['total_cost'])
        ax1.set_xlabel('Collection Capacity (units/day)', fontsize=12)
        ax1.set_ylabel('Total Cost ($)', fontsize=12)
        ax1.set_title('Total Cost vs Capacity', fontsize=13, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        # Panel 2: Shortage and Waste vs Capacity
        ax2 = axes[0, 1]
        ax2.plot(capacity, results_df['total_shortage'], 'o-', 
                color=self.colors['shortage'], linewidth=2, markersize=10, label='Shortage')
        ax2.plot(capacity, results_df['total_waste'], 's-', 
                color=self.colors['waste'], linewidth=2, markersize=10, label='Waste')
        ax2.set_xlabel('Collection Capacity (units/day)', fontsize=12)
        ax2.set_ylabel('Units', fontsize=12)
        ax2.set_title('Shortage and Waste vs Capacity', fontsize=13, fontweight='bold')
        ax2.legend(loc='best', fontsize=11)
        ax2.grid(True, alpha=0.3)
        
        # Panel 3: Collection and Inventory Levels
        ax3 = axes[1, 0]
        ax3.plot(capacity, results_df['total_collected'], 'o-', 
                color=self.colors['collection'], linewidth=2, markersize=10, label='Total Collected')
        ax3.plot(capacity, results_df['avg_inventory'], 's-', 
                color=self.colors['inventory'], linewidth=2, markersize=10, label='Avg Inventory')
        ax3.set_xlabel('Collection Capacity (units/day)', fontsize=12)
        ax3.set_ylabel('Units', fontsize=12)
        ax3.set_title('Collection and Average Inventory vs Capacity', fontsize=13, fontweight='bold')
        ax3.legend(loc='best', fontsize=11)
        ax3.grid(True, alpha=0.3)
        
        # Panel 4: Marginal Cost of Capacity Changes
        ax4 = axes[1, 1]
        if len(capacity) > 1:
            marginal_cost = np.diff(results_df['optimal_cost'].values) / np.diff(capacity)
            capacity_mid = capacity[:-1] + np.diff(capacity) / 2
            
            colors_mc = ['green' if mc < 0 else 'red' for mc in marginal_cost]
            ax4.bar(capacity_mid, marginal_cost, width=np.diff(capacity)[0] * 0.8, 
                   color=colors_mc, alpha=0.7)
            ax4.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
            ax4.set_xlabel('Collection Capacity (units/day)', fontsize=12)
            ax4.set_ylabel('Marginal Cost ($/unit capacity)', fontsize=12)
            ax4.set_title('Marginal Cost of Capacity Change', fontsize=13, fontweight='bold')
            ax4.grid(True, alpha=0.3, axis='y')
            
            # Add value labels on bars
            for x_pos, mc in zip(capacity_mid, marginal_cost):
                ax4.text(x_pos, mc, f'${mc:.1f}', ha='center', 
                        va='bottom' if mc > 0 else 'top', fontsize=9)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        
        return fig
    
    def plot_cost_sensitivity_analysis(
        self,
        results_dict: Dict[str, pd.DataFrame],
        save_path: Optional[str] = None,
        show: bool = True
    ) -> Figure:
        """
        Plot cost parameter sensitivity analysis.
        
        Args:
            results_dict: Dictionary with keys as cost parameter names ('shortage_cost', 'waste_cost', 'holding_cost')
                         and values as DataFrames with columns: scenario_param, optimal_cost, 
                         total_shortage, total_waste
            save_path: Path to save figure
            show: Whether to display the plot
            
        Returns:
            Matplotlib Figure object
        """
        n_params = len(results_dict)
        fig, axes = plt.subplots(n_params, 3, figsize=(18, 5 * n_params))
        fig.suptitle('Cost Parameter Sensitivity Analysis', fontsize=16, fontweight='bold')
        
        if n_params == 1:
            axes = axes.reshape(1, -1)
        
        param_labels = {
            'shortage_cost': 'Shortage Penalty (s)',
            'waste_cost': 'Disposal Cost (w)',
            'holding_cost': 'Holding Cost (h)',
            'collection_cost': 'Collection Cost (p)'
        }
        
        for idx, (param_name, df) in enumerate(results_dict.items()):
            param_values = df['scenario_param'].values
            param_label = param_labels.get(param_name, param_name)
            
            # Panel 1: Total Cost vs Parameter
            ax1 = axes[idx, 0]
            ax1.plot(param_values, df['optimal_cost'], 'o-', 
                    color=self.colors['total_cost'], linewidth=2, markersize=8)
            ax1.set_xlabel(param_label, fontsize=11)
            ax1.set_ylabel('Total Cost ($)', fontsize=11)
            ax1.set_title(f'Total Cost vs {param_label}', fontsize=12, fontweight='bold')
            ax1.grid(True, alpha=0.3)
            
            # Calculate elasticity
            if len(param_values) > 1:
                cost_change_pct = (df['optimal_cost'].iloc[-1] - df['optimal_cost'].iloc[0]) / df['optimal_cost'].iloc[0] * 100
                param_change_pct = (param_values[-1] - param_values[0]) / param_values[0] * 100
                elasticity = cost_change_pct / param_change_pct if param_change_pct != 0 else 0
                
                ax1.text(0.05, 0.95, f'Elasticity: {elasticity:.2f}', 
                        transform=ax1.transAxes, fontsize=9, verticalalignment='top',
                        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
            
            # Panel 2: Shortage vs Parameter
            ax2 = axes[idx, 1]
            ax2.plot(param_values, df['total_shortage'], 'o-', 
                    color=self.colors['shortage'], linewidth=2, markersize=8)
            ax2.set_xlabel(param_label, fontsize=11)
            ax2.set_ylabel('Total Shortage (units)', fontsize=11)
            ax2.set_title(f'Shortage vs {param_label}', fontsize=12, fontweight='bold')
            ax2.grid(True, alpha=0.3)
            
            # Panel 3: Waste vs Parameter
            ax3 = axes[idx, 2]
            ax3.plot(param_values, df['total_waste'], 'o-', 
                    color=self.colors['waste'], linewidth=2, markersize=8)
            ax3.set_xlabel(param_label, fontsize=11)
            ax3.set_ylabel('Total Waste (units)', fontsize=11)
            ax3.set_title(f'Waste vs {param_label}', fontsize=12, fontweight='bold')
            ax3.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        
        return fig
    
    def plot_comparative_summary(
        self,
        scenario_summaries: Dict[str, Dict],
        save_path: Optional[str] = None,
        show: bool = True
    ) -> Figure:
        """
        Create a comparative summary across all scenario types.
        
        Args:
            scenario_summaries: Dictionary with scenario types as keys and summary stats as values
                               Each summary should have: mean_cost, mean_shortage, mean_waste
            save_path: Path to save figure
            show: Whether to display the plot
            
        Returns:
            Matplotlib Figure object
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))
        fig.suptitle('Comparative Summary Across All Scenarios', fontsize=16, fontweight='bold')
        
        scenario_names = list(scenario_summaries.keys())
        n_scenarios = len(scenario_names)
        x = np.arange(n_scenarios)
        
        # Extract data
        mean_costs = [scenario_summaries[s]['mean_cost'] for s in scenario_names]
        mean_shortages = [scenario_summaries[s]['mean_shortage'] for s in scenario_names]
        mean_wastes = [scenario_summaries[s]['mean_waste'] for s in scenario_names]
        
        # Panel 1: Mean Total Cost
        ax1 = axes[0]
        bars1 = ax1.bar(x, mean_costs, color=self.colors['total_cost'], alpha=0.7)
        ax1.set_xlabel('Scenario Type', fontsize=12)
        ax1.set_ylabel('Mean Total Cost ($)', fontsize=12)
        ax1.set_title('Average Total Cost by Scenario Type', fontsize=13, fontweight='bold')
        ax1.set_xticks(x)
        ax1.set_xticklabels(scenario_names, rotation=45, ha='right')
        ax1.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for bar in bars1:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height:,.0f}', ha='center', va='bottom', fontsize=9)
        
        # Panel 2: Mean Shortage
        ax2 = axes[1]
        bars2 = ax2.bar(x, mean_shortages, color=self.colors['shortage'], alpha=0.7)
        ax2.set_xlabel('Scenario Type', fontsize=12)
        ax2.set_ylabel('Mean Total Shortage (units)', fontsize=12)
        ax2.set_title('Average Shortage by Scenario Type', fontsize=13, fontweight='bold')
        ax2.set_xticks(x)
        ax2.set_xticklabels(scenario_names, rotation=45, ha='right')
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for bar in bars2:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}', ha='center', va='bottom', fontsize=9)
        
        # Panel 3: Mean Waste
        ax3 = axes[2]
        bars3 = ax3.bar(x, mean_wastes, color=self.colors['waste'], alpha=0.7)
        ax3.set_xlabel('Scenario Type', fontsize=12)
        ax3.set_ylabel('Mean Total Waste (units)', fontsize=12)
        ax3.set_title('Average Waste by Scenario Type', fontsize=13, fontweight='bold')
        ax3.set_xticks(x)
        ax3.set_xticklabels(scenario_names, rotation=45, ha='right')
        ax3.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for bar in bars3:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}', ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        
        return fig
    
    def plot_heatmap_analysis(
        self,
        results_df: pd.DataFrame,
        x_param: str,
        y_param: str,
        value_param: str,
        save_path: Optional[str] = None,
        show: bool = True
    ) -> Figure:
        """
        Create a heatmap showing the relationship between two parameters and a result metric.
        
        Args:
            results_df: DataFrame with optimization results
            x_param: Column name for x-axis parameter
            y_param: Column name for y-axis parameter
            value_param: Column name for the value to plot (e.g., 'optimal_cost')
            save_path: Path to save figure
            show: Whether to display the plot
            
        Returns:
            Matplotlib Figure object
        """
        # Pivot the data for heatmap
        heatmap_data = results_df.pivot_table(
            values=value_param,
            index=y_param,
            columns=x_param,
            aggfunc='mean'
        )
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        sns.heatmap(
            heatmap_data,
            annot=True,
            fmt='.1f',
            cmap='YlOrRd',
            cbar_kws={'label': value_param},
            ax=ax
        )
        
        ax.set_title(f'Heatmap: {value_param} vs {x_param} and {y_param}', 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel(x_param, fontsize=12)
        ax.set_ylabel(y_param, fontsize=12)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        
        return fig


def main():
    """Example usage of the BloodBankVisualizer class."""
    
    print("\n" + "="*70)
    print(" BLOOD BANK VISUALIZATION - EXAMPLE ".center(70))
    print("="*70 + "\n")
    
    # Example: Create dummy results for demonstration
    
    # Single run results
    single_run_results = {
        'optimal_cost': 10500.0,
        'collection_cost': 6000.0,
        'holding_cost': 150.0,
        'shortage_cost': 4000.0,
        'waste_cost': 350.0,
        'collection_schedule': [40, 40, 40, 40, 35, 30, 35, 30],
        'shortages': [0, 0, 10, 20, 0, 0, 0, 0],
        'waste': [0, 10, 5, 10, 15, 0, 5, 0],
        'inventory': {
            (1, 1): 10, (1, 2): 0, (1, 3): 0,
            (2, 1): 5, (2, 2): 10, (2, 3): 0,
            (3, 1): 0, (3, 2): 5, (3, 3): 10,
            (4, 1): 0, (4, 2): 0, (4, 3): 5,
            (5, 1): 5, (5, 2): 0, (5, 3): 0,
            (6, 1): 5, (6, 2): 5, (6, 3): 0,
            (7, 1): 0, (7, 2): 5, (7, 3): 5,
            (8, 1): 0, (8, 2): 0, (8, 3): 5,
        }
    }
    demand = [30, 35, 50, 60, 45, 30, 40, 35]
    
    # Create visualizer
    visualizer = BloodBankVisualizer()
    
    # Plot single run
    print("Creating single run visualization...")
    visualizer.plot_single_run_summary(single_run_results, demand, show=True)
    print("✓ Single run plot created\n")
    
    # Example: Volatility analysis
    volatility_df = pd.DataFrame({
        'scenario_param': [0, 5, 10, 15, 20],
        'optimal_cost': [10000, 10500, 11500, 13000, 15000],
        'total_shortage': [0, 5, 15, 30, 50],
        'total_waste': [10, 15, 20, 25, 30]
    })
    
    print("Creating volatility analysis plot...")
    visualizer.plot_volatility_analysis(volatility_df, show=True)
    print("✓ Volatility analysis plot created\n")
    
    # Example: Shelf life analysis
    shelf_life_df = pd.DataFrame({
        'scenario_param': [2, 3, 4, 5],
        'optimal_cost': [15000, 10500, 9000, 8500],
        'total_shortage': [40, 20, 5, 0],
        'total_waste': [5, 10, 15, 20],
        'collection_cost': [6000, 6000, 6000, 6000],
        'holding_cost': [100, 150, 200, 250],
        'shortage_cost': [8000, 4000, 800, 0],
        'waste_cost': [50, 100, 150, 200]
    })
    
    print("Creating shelf life analysis plot...")
    visualizer.plot_shelf_life_analysis(shelf_life_df, show=True)
    print("✓ Shelf life analysis plot created\n")
    
    # Example: Capacity analysis
    capacity_df = pd.DataFrame({
        'scenario_param': [30, 35, 40, 45, 50],
        'optimal_cost': [18000, 13000, 10500, 10000, 9900],
        'total_shortage': [80, 40, 20, 5, 0],
        'total_waste': [0, 5, 10, 15, 20],
        'total_collected': [250, 280, 305, 320, 330],
        'avg_inventory': [10, 15, 20, 25, 30]
    })
    
    print("Creating capacity analysis plot...")
    visualizer.plot_capacity_analysis(capacity_df, show=True)
    print("✓ Capacity analysis plot created\n")
    
    # Example: Cost sensitivity analysis
    cost_sensitivity_dict = {
        'shortage_cost': pd.DataFrame({
            'scenario_param': [100, 150, 200, 250, 300],
            'optimal_cost': [9000, 9500, 10500, 11500, 12500],
            'total_shortage': [50, 35, 20, 10, 5],
            'total_waste': [10, 10, 10, 10, 10]
        }),
        'waste_cost': pd.DataFrame({
            'scenario_param': [5, 10, 15, 20, 25],
            'optimal_cost': [10200, 10500, 10800, 11100, 11400],
            'total_shortage': [20, 20, 20, 20, 20],
            'total_waste': [35, 30, 25, 20, 15]
        })
    }
    
    print("Creating cost sensitivity analysis plot...")
    visualizer.plot_cost_sensitivity_analysis(cost_sensitivity_dict, show=True)
    print("✓ Cost sensitivity analysis plot created\n")
    
    print("All example plots created successfully!")
    
if __name__ == "__main__":
    main()
