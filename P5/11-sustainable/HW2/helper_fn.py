from pathlib import Path
import pandas as pd
import numpy as np
import geopandas as gpd
from typing import Optional


class DataLoader:
    """Load and prepare all datasets for accessibility analysis."""
    
    def __init__(self, traveltime_path: Path, geojson_path: Path, jobs_path: Path):
        """
        Initialize DataLoader with paths to all required data files.
        
        Args:
            traveltime_path: Path to O-D travel time matrix CSV
            geojson_path: Path to GeoJSON file with zone geometries
            jobs_path: Path to Excel file with jobs and population data
        """
        self.traveltime = pd.read_csv(traveltime_path)
        self.jobs_pop = pd.read_excel(jobs_path)
        self.geo_data = gpd.read_file(geojson_path)
        
        # Convert id to int for consistent merging
        self.geo_data['id'] = self.geo_data['id'].astype(int)
        self.jobs_pop['id'] = self.jobs_pop['id'].astype(int)
        
    def get_travel_time_matrix(self) -> pd.DataFrame:
        """
        Convert long-format travel time data to a square matrix.
        
        Returns:
            DataFrame with from_id as index, to_id as columns, travel_time as values
        """
        return self.traveltime.pivot(
            index='from_id', 
            columns='to_id', 
            values='travel_time'
        )
    
    def get_jobs_by_zone(self) -> pd.Series:
        """
        Get jobs indexed by zone id.
        
        Returns:
            Series with zone id as index and jobs as values
        """
        return self.jobs_pop.set_index('id')['jobs']
    
    def get_population_by_zone(self) -> pd.Series:
        """
        Get population indexed by zone id.
        
        Returns:
            Series with zone id as index and population as values
        """
        return self.jobs_pop.set_index('id')['pop']
    
    def get_zone_to_mantagheh_mapping(self) -> pd.Series:
        """
        Get mapping from zone id to Mantagheh (district).
        
        Returns:
            Series with zone id as index and Mantagheh name as values
        """
        return self.geo_data.set_index('id')['Mantagheh']
    
    def get_merged_geodata(self) -> gpd.GeoDataFrame:
        """
        Merge geographic data with jobs and population data.
        
        Returns:
            GeoDataFrame with all zone information
        """
        return self.geo_data.merge(self.jobs_pop[['id', 'jobs', 'pop']], on='id', how='left')


class AccessibilityCalculator:
    """Calculate accessibility indicators using different methods."""
    
    def __init__(self, data_loader: DataLoader, beta: float = 0.1068):
        """
        Initialize calculator with data and parameters.
        
        Args:
            data_loader: DataLoader instance with all data
            beta: Decay parameter for gravity model (default: 0.1068)
        """
        self.data_loader = data_loader
        self.beta = beta
        
        # Prepare data for calculations
        self.tt_matrix = data_loader.get_travel_time_matrix()
        self.jobs = data_loader.get_jobs_by_zone()
        
    def gravity_accessibility(self) -> pd.Series:
        """
        Calculate gravity-based accessibility for all zones.
        
        Formula: A_i = Σ_j (O_j * exp(-β * t_ij))
        
        Returns:
            Series with zone id as index and gravity accessibility as values
        """
        # Ensure jobs are aligned with travel time columns
        jobs_aligned = self.jobs.reindex(self.tt_matrix.columns).fillna(0)
        
        # Calculate impedance: exp(-β * t_ij)
        impedance = np.exp(-self.beta * self.tt_matrix)
        
        # Calculate accessibility: sum of (jobs * impedance) for each origin
        accessibility = impedance.multiply(jobs_aligned, axis=1).sum(axis=1)
        
        accessibility.name = 'jobs_grav'
        return accessibility
    
    def cumulative_accessibility(self, threshold: int = 30) -> pd.Series:
        """
        Calculate cumulative opportunities accessibility for all zones.
        
        Formula: A_i = Σ_j O_j where t_ij <= threshold
        
        Args:
            threshold: Maximum travel time in minutes (default: 30)
            
        Returns:
            Series with zone id as index and cumulative accessibility as values
        """
        # Ensure jobs are aligned with travel time columns
        jobs_aligned = self.jobs.reindex(self.tt_matrix.columns).fillna(0)
        
        # Create binary mask: 1 if travel time <= threshold, 0 otherwise
        within_threshold = (self.tt_matrix <= threshold).astype(int)
        
        # Calculate accessibility: sum of jobs within threshold for each origin
        accessibility = within_threshold.multiply(jobs_aligned, axis=1).sum(axis=1)
        
        accessibility.name = 'jobs_cumul30'
        return accessibility
    
    def calculate_all(self, threshold: int = 30) -> pd.DataFrame:
        """
        Calculate both accessibility indicators for all zones.
        
        Args:
            threshold: Threshold for cumulative method (default: 30 minutes)
            
        Returns:
            DataFrame with zone id as index and both accessibility indicators
        """
        grav = self.gravity_accessibility()
        cumul = self.cumulative_accessibility(threshold)
        
        result = pd.DataFrame({
            'jobs_grav': grav,
            'jobs_cumul30': cumul
        })
        result.index.name = 'id'
        return result


class AccessibilityAnalyzer:
    """Aggregate and analyze accessibility results."""
    
    def __init__(self, data_loader: DataLoader, accessibility_df: pd.DataFrame):
        """
        Initialize analyzer with data and accessibility results.
        
        Args:
            data_loader: DataLoader instance
            accessibility_df: DataFrame with accessibility indicators by zone
        """
        self.data_loader = data_loader
        self.accessibility = accessibility_df
        self.zone_to_mantagheh = data_loader.get_zone_to_mantagheh_mapping()
        
    def aggregate_by_mantagheh(self, method: str = 'mean') -> pd.DataFrame:
        """
        Aggregate accessibility indicators by Mantagheh (district).
        
        Args:
            method: Aggregation method ('mean', 'sum', 'median')
            
        Returns:
            DataFrame with Mantagheh as index and aggregated accessibility
        """
        # Add Mantagheh to accessibility data
        df = self.accessibility.copy()
        df['Mantagheh'] = self.zone_to_mantagheh.reindex(df.index)
        
        # Aggregate by Mantagheh
        if method == 'mean':
            return df.groupby('Mantagheh').mean()
        elif method == 'sum':
            return df.groupby('Mantagheh').sum()
        elif method == 'median':
            return df.groupby('Mantagheh').median()
        else:
            raise ValueError(f"Unknown method: {method}")
    
    def get_zone_results_with_info(self) -> pd.DataFrame:
        """
        Get accessibility results with zone information.
        
        Returns:
            DataFrame with zone info and accessibility indicators
        """
        jobs_pop = self.data_loader.jobs_pop.set_index('id')
        
        result = self.accessibility.copy()
        result['name'] = jobs_pop['name'].reindex(result.index)
        result['Mantagheh'] = self.zone_to_mantagheh.reindex(result.index)
        result['jobs'] = jobs_pop['jobs'].reindex(result.index)
        result['pop'] = jobs_pop['pop'].reindex(result.index)
        
        # Reorder columns
        cols = ['name', 'Mantagheh', 'jobs', 'pop', 'jobs_grav', 'jobs_cumul30']
        return result[cols]
    
    def summary_statistics(self) -> pd.DataFrame:
        """
        Calculate summary statistics for accessibility indicators.
        
        Returns:
            DataFrame with statistics for each indicator
        """
        return self.accessibility.describe()


class AccessibilityVisualizer:
    """Create maps and visualizations for accessibility analysis."""
    
    def __init__(self, data_loader: DataLoader, accessibility_df: pd.DataFrame):
        """
        Initialize visualizer with data and accessibility results.
        
        Args:
            data_loader: DataLoader instance
            accessibility_df: DataFrame with accessibility indicators by zone
        """
        self.data_loader = data_loader
        self.accessibility = accessibility_df
        self.geo_data = data_loader.get_merged_geodata()
        
        # Merge accessibility with geodata
        self.geo_with_access = self.geo_data.merge(
            accessibility_df.reset_index(), 
            on='id', 
            how='left'
        )
    
    def plot_accessibility_map(
        self, 
        indicator: str = 'jobs_grav',
        cmap: str = 'RdYlGn',
        figsize: tuple = (12, 10),
        title: Optional[str] = None,
        ax = None
    ):
        """
        Create a choropleth map of accessibility indicator.
        
        Args:
            indicator: Column name to plot ('jobs_grav' or 'jobs_cumul30')
            cmap: Colormap name
            figsize: Figure size tuple
            title: Map title (auto-generated if None)
            ax: Matplotlib axes (creates new figure if None)
            
        Returns:
            Matplotlib axes object
        """
        import matplotlib.pyplot as plt
        
        if ax is None:
            fig, ax = plt.subplots(1, 1, figsize=figsize)
        
        if title is None:
            if indicator == 'jobs_grav':
                title = 'Gravity-Based Job Accessibility'
            elif indicator == 'jobs_cumul30':
                title = 'Cumulative Job Accessibility (30-min threshold)'
            else:
                title = f'Accessibility: {indicator}'
        
        self.geo_with_access.plot(
            column=indicator,
            cmap=cmap,
            legend=True,
            legend_kwds={'label': indicator, 'shrink': 0.8},
            ax=ax,
            edgecolor='black',
            linewidth=0.5
        )
        
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_axis_off()
        
        return ax
    
    def plot_both_maps(self, figsize: tuple = (16, 8), cmap: str = 'RdYlGn'):
        """
        Create side-by-side maps of both accessibility indicators.
        
        Args:
            figsize: Figure size tuple
            cmap: Colormap name
            
        Returns:
            Figure and axes objects
        """
        import matplotlib.pyplot as plt
        
        fig, axes = plt.subplots(1, 2, figsize=figsize)
        
        self.plot_accessibility_map('jobs_grav', cmap=cmap, ax=axes[0])
        self.plot_accessibility_map('jobs_cumul30', cmap=cmap, ax=axes[1])
        
        plt.tight_layout()
        return fig, axes
    
    def create_folium_map(
        self, 
        indicator: str = 'jobs_grav',
        tiles: str = 'CartoDB positron'
    ):
        """
        Create an interactive Folium map.
        
        Args:
            indicator: Column name to plot
            tiles: Tile layer style
            
        Returns:
            Folium Map object
        """
        import folium
        
        # Get centroid for map center
        centroid = self.geo_with_access.geometry.centroid.unary_union.centroid
        
        m = folium.Map(
            location=[centroid.y, centroid.x],
            zoom_start=12,
            tiles=tiles
        )
        
        # Add choropleth
        folium.Choropleth(
            geo_data=self.geo_with_access.__geo_interface__,
            data=self.geo_with_access,
            columns=['id', indicator],
            key_on='feature.properties.id',
            fill_color='RdYlGn',
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name=indicator
        ).add_to(m)
        
        # Add tooltips
        style_function = lambda x: {
            'fillColor': '#ffffff',
            'color': '#000000',
            'fillOpacity': 0.1,
            'weight': 0.1
        }
        
        highlight_function = lambda x: {
            'fillColor': '#000000',
            'color': '#000000',
            'fillOpacity': 0.50,
            'weight': 0.1
        }
        
        tooltip = folium.features.GeoJsonTooltip(
            fields=['name', 'Mantagheh', indicator],
            aliases=['Zone:', 'District:', f'{indicator}:'],
            style="background-color: white; color: #333333; font-size: 12px;"
        )
        
        folium.features.GeoJson(
            self.geo_with_access,
            style_function=style_function,
            highlight_function=highlight_function,
            tooltip=tooltip
        ).add_to(m)
        
        return m