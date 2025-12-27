"""
Traffic Flow Analysis: Triangular Fundamental Diagram and Trajectory Plotting
==============================================================================
This module provides tools for visualizing traffic flow using:
- Triangular Fundamental Diagram (q-k relationship with two linear branches)
- Time-Space (x-t) Trajectory Diagrams with shockwave analysis

The Triangular FD consists of:
1. Free-flow branch: q = v_f * k  (for k <= k_c)
2. Congested branch: q = w * (k - k_j)  (for k > k_c), where w < 0

Author: Traffic Analysis Tool
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Dict
from enum import Enum


# =============================================================================
# UNIT SYSTEM
# =============================================================================

class SpeedUnit(Enum):
    KMH = "km/h"
    MPH = "mph"
    MS = "m/s"


class DistanceUnit(Enum):
    KM = "km"
    MILES = "miles"
    METERS = "m"


class TimeUnit(Enum):
    HOURS = "h"
    MINUTES = "min"
    SECONDS = "s"


class DensityUnit(Enum):
    VEH_PER_KM = "veh/km"
    VEH_PER_MILE = "veh/mile"
    VEH_PER_M = "veh/m"


class FlowUnit(Enum):
    VEH_PER_HOUR = "veh/h"
    VEH_PER_MIN = "veh/min"
    VEH_PER_SEC = "veh/s"


@dataclass
class UnitSystem:
    """Define the unit system for the analysis."""
    speed: SpeedUnit = SpeedUnit.KMH
    distance: DistanceUnit = DistanceUnit.KM
    time: TimeUnit = TimeUnit.HOURS
    density: DensityUnit = DensityUnit.VEH_PER_KM
    flow: FlowUnit = FlowUnit.VEH_PER_HOUR
    
    def get_labels(self) -> Dict[str, str]:
        """Return axis labels based on unit system."""
        return {
            "speed": f"Speed ({self.speed.value})",
            "distance": f"Distance ({self.distance.value})",
            "time": f"Time ({self.time.value})",
            "density": f"Density ({self.density.value})",
            "flow": f"Flow ({self.flow.value})"
        }


# =============================================================================
# TRIANGULAR FUNDAMENTAL DIAGRAM
# =============================================================================

@dataclass
class TriangularFD:
    """
    Triangular Fundamental Diagram.
    
    The Triangular FD has two linear branches:
    
    1. Free-flow branch (k <= k_c):
       q = v_f * k
       v = v_f (constant free-flow speed)
       
    2. Congested branch (k > k_c):
       q = q_max + w * (k - k_c)  OR  q = w * (k - k_j)
       v = q / k
       
    Where:
        v_f = free flow speed
        k_j = jam density (density when q=0, v=0)
        k_c = critical density (density at maximum flow)
        q_max = maximum flow (capacity)
        w = backward wave speed (negative) = -q_max / (k_j - k_c)
    
    Parameters
    ----------
    v_free : float
        Free flow speed
    k_jam : float
        Jam density (maximum density, where flow = 0)
    k_critical : float
        Critical density (density at maximum flow)
    units : UnitSystem
        Unit system for the analysis
    """
    v_free: float
    k_jam: float
    k_critical: float
    units: UnitSystem = field(default_factory=UnitSystem)
    
    def __post_init__(self):
        """Calculate derived parameters."""
        if self.k_critical >= self.k_jam:
            raise ValueError("k_critical must be less than k_jam")
        if self.k_critical <= 0:
            raise ValueError("k_critical must be positive")
            
        # Maximum flow (capacity) - at critical density
        self.q_max = self.v_free * self.k_critical
        
        # Backward wave speed (congested branch slope) - negative value
        self.w = -self.q_max / (self.k_jam - self.k_critical)
        
        # Speed at critical density
        self.v_critical = self.v_free  # In triangular FD, speed is v_f until k_c
    
    def speed_from_density(self, k: float) -> float:
        """
        Calculate speed from density using Triangular FD.
        
        - Free-flow (k <= k_c): v = v_f
        - Congested (k > k_c): v = q / k where q = w * (k - k_j)
        """
        if k < 0 or k > self.k_jam:
            raise ValueError(f"Density must be between 0 and {self.k_jam}")
        
        if k <= self.k_critical:
            # Free-flow regime: constant speed
            return self.v_free
        else:
            # Congested regime: v = q / k
            q = self.flow_from_density(k)
            return q / k if k > 0 else 0
    
    def flow_from_density(self, k: float) -> float:
        """
        Calculate flow from density using Triangular FD.
        
        - Free-flow (k <= k_c): q = v_f * k
        - Congested (k > k_c): q = w * (k - k_j)
        """
        if k < 0 or k > self.k_jam:
            raise ValueError(f"Density must be between 0 and {self.k_jam}")
        
        if k <= self.k_critical:
            # Free-flow branch
            return self.v_free * k
        else:
            # Congested branch: q = w * (k - k_j)
            return self.w * (k - self.k_jam)
    
    def density_from_flow(self, q: float, congested: bool = False) -> float:
        """
        Calculate density from flow.
        
        Parameters
        ----------
        q : float
            Flow rate
        congested : bool
            If True, return density on congested branch; otherwise free-flow branch
        """
        if q < 0 or q > self.q_max:
            raise ValueError(f"Flow must be between 0 and {self.q_max}")
        
        if not congested:
            # Free-flow branch: k = q / v_f
            return q / self.v_free
        else:
            # Congested branch: k = k_j + q / w
            return self.k_jam + q / self.w
    
    def is_congested(self, k: float) -> bool:
        """Check if the given density is in congested regime."""
        return k > self.k_critical
    
    def shockwave_speed(self, k1: float, k2: float) -> float:
        """
        Calculate shockwave speed between two regions.
        
        w = (q2 - q1) / (k2 - k1)
        
        For Triangular FD:
        - If both in free-flow: w = v_f (vehicles just travel at free-flow speed)
        - If both in congested: w = w (backward wave speed)
        - If one in each regime: w = (q2 - q1) / (k2 - k1)
        
        Parameters
        ----------
        k1, k2 : float
            Densities of the two regions
            
        Returns
        -------
        float
            Shockwave speed (positive = moves in direction of traffic,
                           negative = moves against traffic)
        """
        if k1 == k2:
            return self.speed_from_density(k1)
        
        q1 = self.flow_from_density(k1)
        q2 = self.flow_from_density(k2)
        return (q2 - q1) / (k2 - k1)
    
    def get_fd_curve(self) -> Tuple[np.ndarray, np.ndarray]:
        """Get the triangular fundamental diagram curve (k, q) for plotting."""
        # Three points: origin, capacity point, jam point
        k = np.array([0, self.k_critical, self.k_jam])
        q = np.array([0, self.q_max, 0])
        return k, q
    
    def get_speed_density_curve(self, n_points: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        """Get the speed-density curve (k, v) for plotting."""
        k = np.linspace(0, self.k_jam, n_points)
        v = np.array([self.speed_from_density(ki) for ki in k])
        return k, v


# =============================================================================
# REGION DEFINITION
# =============================================================================

@dataclass
class Region:
    """
    Define a region in the time-space diagram.
    
    Parameters
    ----------
    name : str
        Name/label for the region (e.g., "A", "B", "C")
    x_range : Tuple[float, float]
        (x_min, x_max) spatial extent of the region
    t_range : Tuple[float, float]
        (t_min, t_max) temporal extent of the region
    k : float
        Density in this region
    """
    name: str
    x_range: Tuple[float, float]
    t_range: Tuple[float, float]
    k: float
    
    # Calculated properties (set after initialization with FD)
    v: float = field(init=False, default=0.0)
    q: float = field(init=False, default=0.0)
    is_congested: bool = field(init=False, default=False)
    
    def set_from_fd(self, fd: TriangularFD):
        """Calculate v and q from the fundamental diagram."""
        self.v = fd.speed_from_density(self.k)
        self.q = fd.flow_from_density(self.k)
        self.is_congested = fd.is_congested(self.k)
    
    def contains_point(self, x: float, t: float) -> bool:
        """Check if a point (x, t) is within this region."""
        return (self.x_range[0] <= x <= self.x_range[1] and 
                self.t_range[0] <= t <= self.t_range[1])


# =============================================================================
# SHOCKWAVE CALCULATION
# =============================================================================

@dataclass
class Shockwave:
    """
    Represents a shockwave between two regions.
    
    Parameters
    ----------
    region1 : Region
        First region (upstream or earlier)
    region2 : Region
        Second region (downstream or later)
    speed : float
        Shockwave propagation speed (dx/dt)
    start_point : Tuple[float, float]
        (x, t) starting point of the shockwave
    """
    region1: Region
    region2: Region
    speed: float
    start_point: Tuple[float, float]
    
    def get_trajectory(self, t_max: float, x_max: float) -> Tuple[np.ndarray, np.ndarray]:
        """
        Get the shockwave trajectory for plotting.
        
        The shockwave moves with speed w = dx/dt, so:
        x(t) = x0 + w * (t - t0)
        
        Returns (x_array, t_array) for plotting.
        """
        x0, t0 = self.start_point
        
        # Generate trajectory points
        t_points = [t0]
        x_points = [x0]
        
        # Calculate where the shockwave ends (hits a boundary)
        if abs(self.speed) > 1e-10:
            # Time to reach x=0 or x=x_max
            if self.speed > 0:
                # Moving forward (downstream) - will hit x_max
                dt_to_x_boundary = (x_max - x0) / self.speed
            else:
                # Moving backward (upstream) - will hit x=0
                dt_to_x_boundary = (0 - x0) / self.speed  # This is positive since speed < 0
            
            # Time available until t_max
            dt_to_t_boundary = t_max - t0
            
            # Take the minimum
            dt = min(dt_to_x_boundary, dt_to_t_boundary)
            
            if dt > 0:
                t_end = t0 + dt
                x_end = x0 + self.speed * dt
                
                # Clamp to boundaries
                x_end = max(0, min(x_max, x_end))
                t_end = min(t_max, t_end)
                
                t_points.append(t_end)
                x_points.append(x_end)
        else:
            # Stationary shockwave - vertical line at x0
            t_points.append(t_max)
            x_points.append(x0)
        
        return np.array(x_points), np.array(t_points)


# =============================================================================
# TRAJECTORY PLOTTER
# =============================================================================

class TrajectoryPlotter:
    """
    Main class for plotting traffic trajectories and fundamental diagrams.
    
    Parameters
    ----------
    fd : TriangularFD
        Fundamental diagram parameters
    x_max : float
        Maximum distance (road length)
    t_max : float
        Maximum time
    regions : List[Region]
        List of regions with their densities
    vehicles_per_line : int
        Number of vehicles represented by each trajectory line (0 = auto)
    """
    
    def __init__(
        self,
        fd: TriangularFD,
        x_max: float,
        t_max: float,
        regions: List[Region],
        vehicles_per_line: int = 0
    ):
        self.fd = fd
        self.x_max = x_max
        self.t_max = t_max
        self.regions = regions
        self.vehicles_per_line = vehicles_per_line
        
        # Initialize regions with FD data
        for region in self.regions:
            region.set_from_fd(fd)
        
        # Calculate shockwaves between adjacent regions
        self.shockwaves = self._calculate_shockwaves()
        
        # Color scheme for regions
        self.colors = plt.cm.Set1(np.linspace(0, 1, max(len(regions), 9)))
    
    def _calculate_shockwaves(self) -> List[Shockwave]:
        """Calculate shockwaves between adjacent regions."""
        shockwaves = []
        
        for i, r1 in enumerate(self.regions):
            for j, r2 in enumerate(self.regions):
                if i >= j:
                    continue
                
                # Skip if same density (no shockwave)
                if abs(r1.k - r2.k) < 1e-6:
                    continue
                
                # Check for spatial adjacency (regions touch in space)
                time_overlap = (r1.t_range[0] < r2.t_range[1] and r2.t_range[0] < r1.t_range[1])
                
                if time_overlap:
                    # Check if r1 is upstream of r2 (r1.x_max == r2.x_min)
                    if abs(r1.x_range[1] - r2.x_range[0]) < 1e-6:
                        speed = self.fd.shockwave_speed(r1.k, r2.k)
                        start_x = r1.x_range[1]
                        start_t = max(r1.t_range[0], r2.t_range[0])
                        shockwaves.append(Shockwave(r1, r2, speed, (start_x, start_t)))
                    
                    # Check if r2 is upstream of r1 (r2.x_max == r1.x_min)
                    elif abs(r2.x_range[1] - r1.x_range[0]) < 1e-6:
                        speed = self.fd.shockwave_speed(r2.k, r1.k)
                        start_x = r2.x_range[1]
                        start_t = max(r1.t_range[0], r2.t_range[0])
                        shockwaves.append(Shockwave(r2, r1, speed, (start_x, start_t)))
                
                # Check for temporal adjacency (regions touch in time)
                space_overlap = (r1.x_range[0] < r2.x_range[1] and r2.x_range[0] < r1.x_range[1])
                
                if space_overlap:
                    # Check if r1 ends when r2 starts
                    if abs(r1.t_range[1] - r2.t_range[0]) < 1e-6:
                        speed = self.fd.shockwave_speed(r1.k, r2.k)
                        # Shockwave starts at the boundary
                        start_x = max(r1.x_range[0], r2.x_range[0])
                        start_t = r1.t_range[1]
                        shockwaves.append(Shockwave(r1, r2, speed, (start_x, start_t)))
                    
                    # Check if r2 ends when r1 starts
                    elif abs(r2.t_range[1] - r1.t_range[0]) < 1e-6:
                        speed = self.fd.shockwave_speed(r2.k, r1.k)
                        start_x = max(r1.x_range[0], r2.x_range[0])
                        start_t = r2.t_range[1]
                        shockwaves.append(Shockwave(r2, r1, speed, (start_x, start_t)))
        
        return shockwaves
    
    def _get_region_at_point(self, x: float, t: float) -> Optional[Region]:
        """Find which region contains the point (x, t)."""
        for region in self.regions:
            if region.contains_point(x, t):
                return region
        return None
    
    def _calculate_adaptive_vehicles_per_line(self) -> int:
        """
        Calculate an appropriate number of vehicles per line based on
        the flow rates and plot dimensions.
        """
        max_q = max(r.q for r in self.regions)
        min_q_nonzero = min((r.q for r in self.regions if r.q > 0), default=max_q)
        
        if max_q <= 0:
            return 1
        
        # Aim for approximately 25-40 lines in the highest flow region
        target_lines_max = 35
        
        # Calculate based on highest flow rate and time duration
        total_vehicles_max_region = max_q * self.t_max
        vehicles_per_line = max(1, int(total_vehicles_max_region / target_lines_max))
        
        # Ensure we can distinguish between different flow rates
        if min_q_nonzero > 0 and min_q_nonzero < max_q:
            min_lines = total_vehicles_max_region / vehicles_per_line * (min_q_nonzero / max_q)
            if min_lines < 5:  # Ensure at least 5 lines in lowest flow region
                vehicles_per_line = max(1, int(total_vehicles_max_region * min_q_nonzero / max_q / 5))
        
        return vehicles_per_line
    
    def _generate_trajectories(self) -> List[List[Tuple[float, float]]]:
        """
        Generate vehicle trajectories considering all regions and shockwaves.
        
        Returns a list of trajectories, where each trajectory is a list of (x, t) points.
        """
        trajectories = []
        
        # Auto-calculate vehicles per line if not set
        if self.vehicles_per_line <= 0:
            self.vehicles_per_line = self._calculate_adaptive_vehicles_per_line()
        
        # Find all regions that can generate vehicles (at x=0 or with flow > 0)
        entry_regions = sorted(
            [r for r in self.regions if r.x_range[0] == 0 and r.q > 0],
            key=lambda r: r.t_range[0]
        )
        
        if not entry_regions:
            # Use all regions with flow > 0
            entry_regions = sorted(
                [r for r in self.regions if r.q > 0],
                key=lambda r: r.t_range[0]
            )
        
        # Generate vehicles for each entry region
        for region in entry_regions:
            t_start = region.t_range[0]
            t_end = min(region.t_range[1], self.t_max)
            
            if region.q <= 0:
                continue
            
            # Time headway between vehicles (in time units)
            headway = self.vehicles_per_line / region.q
            
            # Generate vehicles
            t = t_start
            while t < t_end:
                x_start = region.x_range[0]
                trajectory = self._trace_vehicle_with_queue(x_start, t, trajectories)
                if len(trajectory) > 1:
                    trajectories.append(trajectory)
                t += headway
        
        return trajectories
    
    def _trace_vehicle_with_queue(self, x_start: float, t_start: float, 
                                   existing_trajectories: List[List[Tuple[float, float]]]) -> List[Tuple[float, float]]:
        """
        Trace a single vehicle's trajectory, respecting the vehicle ahead.
        
        This ensures trajectories don't cross - if we catch up to the vehicle ahead,
        we follow it at the same speed.
        """
        trajectory = [(x_start, t_start)]
        x, t = x_start, t_start
        
        # Time step for simulation
        dt = 0.002 * self.t_max
        max_iterations = int(2 * self.t_max / dt) + 1000
        iteration = 0
        
        # Minimum spacing between vehicles (based on jam density)
        min_spacing = 1.0 / self.fd.k_jam if self.fd.k_jam > 0 else 0.001
        
        while t < self.t_max and x < self.x_max and iteration < max_iterations:
            iteration += 1
            
            # Find which region the vehicle is ACTUALLY in (considering shockwaves)
            region = self._get_dynamic_region_at_point(x, t)
            
            if region is None:
                break
            
            v = region.v
            
            if v <= 0:
                # Vehicle is stopped
                t += dt
                trajectory.append((x, t))
                continue
            
            # Check position of vehicle ahead (last trajectory in the list)
            v_actual = v
            if existing_trajectories:
                x_ahead = self._get_vehicle_ahead_position(t, existing_trajectories[-1])
                if x_ahead is not None:
                    gap = x_ahead - x
                    if gap < min_spacing * 2:
                        # Too close - match speed of vehicle ahead or stop
                        v_actual = max(0, min(v, (gap - min_spacing) / dt))
            
            # Calculate next position
            x_new = x + v_actual * dt
            t_new = t + dt
            
            # Check for shockwave crossing
            for sw in self.shockwaves:
                crossing = self._check_shockwave_crossing(x, t, x_new, t_new, sw)
                if crossing:
                    x_cross, t_cross = crossing
                    # Add crossing point
                    if t_cross > t + 1e-10:
                        trajectory.append((x_cross, t_cross))
                    x, t = x_cross, t_cross
                    break
            else:
                # No shockwave crossing
                if x_new >= self.x_max:
                    t_at_xmax = t + (self.x_max - x) / v_actual if v_actual > 0 else t
                    trajectory.append((self.x_max, t_at_xmax))
                    break
                
                trajectory.append((x_new, t_new))
                x, t = x_new, t_new
        
        return trajectory
    
    def _get_vehicle_ahead_position(self, t: float, ahead_trajectory: List[Tuple[float, float]]) -> Optional[float]:
        """Get the position of the vehicle ahead at time t."""
        if not ahead_trajectory:
            return None
        
        # Find the segment in the trajectory that contains time t
        for i in range(len(ahead_trajectory) - 1):
            x1, t1 = ahead_trajectory[i]
            x2, t2 = ahead_trajectory[i + 1]
            
            if t1 <= t <= t2:
                # Interpolate position
                if abs(t2 - t1) < 1e-10:
                    return x1
                alpha = (t - t1) / (t2 - t1)
                return x1 + alpha * (x2 - x1)
        
        # If t is after the trajectory ends, return last position
        if t >= ahead_trajectory[-1][1]:
            return ahead_trajectory[-1][0]
        
        return None
    
    def _check_shockwave_crossing(self, x1: float, t1: float, x2: float, t2: float, 
                                   sw: Shockwave) -> Optional[Tuple[float, float]]:
        """
        Check if the vehicle segment from (x1,t1) to (x2,t2) crosses the shockwave.
        Returns crossing point (x, t) if it does, None otherwise.
        """
        x_sw0, t_sw0 = sw.start_point
        w = sw.speed
        
        # Shockwave position at t1 and t2
        x_sw1 = x_sw0 + w * (t1 - t_sw0)
        x_sw2 = x_sw0 + w * (t2 - t_sw0)
        
        # Check if vehicle crosses shockwave
        # At t1: vehicle at x1, shockwave at x_sw1
        # At t2: vehicle at x2, shockwave at x_sw2
        
        side1 = x1 - x_sw1  # positive if vehicle is downstream of shockwave
        side2 = x2 - x_sw2
        
        if side1 * side2 < 0:
            # Crossing occurred - find exact point
            # Vehicle: x = x1 + v*(t - t1) where v = (x2-x1)/(t2-t1)
            # Shockwave: x = x_sw0 + w*(t - t_sw0)
            # Solve: x1 + v*(t - t1) = x_sw0 + w*(t - t_sw0)
            
            v_veh = (x2 - x1) / (t2 - t1) if abs(t2 - t1) > 1e-10 else 0
            
            if abs(v_veh - w) < 1e-10:
                return None  # Parallel, no crossing
            
            # t = (x_sw0 - w*t_sw0 - x1 + v_veh*t1) / (v_veh - w)
            t_cross = (x_sw0 - w * t_sw0 - x1 + v_veh * t1) / (v_veh - w)
            
            if t1 < t_cross < t2:
                x_cross = x1 + v_veh * (t_cross - t1)
                return (x_cross, t_cross)
        
        return None
    
    def _get_dynamic_region_at_point(self, x: float, t: float) -> Optional[Region]:
        """
        Find which region contains the point (x, t) considering shockwave boundaries.
        
        The shockwave creates a dynamic boundary: at time t, the shockwave is at
        position x_sw(t) = x_sw(0) + w * t
        
        For a backward shockwave (w < 0) between regions A (upstream) and B (downstream):
        - If x < x_sw(t): point is in region A (upstream side of shockwave)
        - If x >= x_sw(t): point is in region B (downstream side, congested)
        """
        # Check each shockwave to see if it affects this point
        for sw in self.shockwaves:
            # Calculate shockwave position at time t
            x_sw_at_t = sw.start_point[0] + sw.speed * (t - sw.start_point[1])
            
            r1, r2 = sw.region1, sw.region2  # r1 is upstream, r2 is downstream
            
            # Check if this point is in the time range of these regions
            t_min = min(r1.t_range[0], r2.t_range[0])
            t_max = max(r1.t_range[1], r2.t_range[1])
            if not (t_min <= t <= t_max):
                continue
            
            # Check if this point is in the combined x range affected by shockwave
            x_min = min(r1.x_range[0], r2.x_range[0])
            x_max = max(r1.x_range[1], r2.x_range[1])
            
            # For backward shockwave, the shockwave moves from original boundary into r1's space
            if sw.speed < 0:
                # Shockwave boundary at time t
                # Region r2 (congested) has expanded from x_sw_at_t to r2.x_range[1]
                # Region r1 (free-flow) is from r1.x_range[0] to x_sw_at_t
                
                if x_min <= x <= x_max:
                    if x < x_sw_at_t:
                        # Upstream of shockwave - in region r1 (free-flow)
                        return r1
                    else:
                        # At or downstream of shockwave - in region r2 (congested)
                        return r2
            else:
                # Forward shockwave
                if x_min <= x <= x_max:
                    if x <= x_sw_at_t:
                        return r1
                    else:
                        return r2
        
        # No shockwave affects this point - use static region boundaries
        for region in self.regions:
            if (region.x_range[0] <= x <= region.x_range[1] and
                region.t_range[0] <= t <= region.t_range[1]):
                return region
        
        return None
    
    def _draw_dynamic_regions(self, ax):
        """
        Draw regions as polygons with boundaries defined by shockwaves.
        
        When two regions are separated by a shockwave, the shockwave line
        becomes the dynamic boundary between them instead of a static line.
        """
        from matplotlib.patches import Polygon
        
        for i, region in enumerate(self.regions):
            # Find shockwaves that affect this region
            affecting_shockwaves = []
            for sw in self.shockwaves:
                if sw.region1 == region or sw.region2 == region:
                    affecting_shockwaves.append(sw)
            
            if not affecting_shockwaves:
                # No shockwaves - draw as simple rectangle
                rect = plt.Rectangle(
                    (region.t_range[0], region.x_range[0]),
                    region.t_range[1] - region.t_range[0],
                    region.x_range[1] - region.x_range[0],
                    facecolor=self.colors[i], alpha=0.15, edgecolor=self.colors[i],
                    linewidth=2.5, linestyle='--'
                )
                ax.add_patch(rect)
            else:
                # Draw polygon with shockwave as boundary
                polygon_points = self._get_region_polygon(region, affecting_shockwaves)
                if polygon_points:
                    # Points are in (t, x) format for plotting
                    poly = Polygon(polygon_points, facecolor=self.colors[i], alpha=0.15,
                                  edgecolor=self.colors[i], linewidth=2.5, linestyle='--')
                    ax.add_patch(poly)
            
            # Calculate centroid for label placement
            if affecting_shockwaves:
                polygon_points = self._get_region_polygon(region, affecting_shockwaves)
                if polygon_points:
                    center_t = sum(p[0] for p in polygon_points) / len(polygon_points)
                    center_x = sum(p[1] for p in polygon_points) / len(polygon_points)
                else:
                    center_t = (region.t_range[0] + region.t_range[1]) / 2
                    center_x = (region.x_range[0] + region.x_range[1]) / 2
            else:
                center_t = (region.t_range[0] + region.t_range[1]) / 2
                center_x = (region.x_range[0] + region.x_range[1]) / 2
            
            # Region label with flow info
            regime = "Congested" if region.is_congested else "Free-flow"
            label_text = f"{region.name}\n(k={region.k:.0f}, q={region.q:.0f})\n{regime}"
            ax.text(center_t, center_x, label_text, fontsize=10, 
                   fontweight='bold', ha='center', va='center',
                   color=self.colors[i], alpha=0.9,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                            alpha=0.7, edgecolor=self.colors[i]))
    
    def _get_region_polygon(self, region: Region, shockwaves: List[Shockwave]) -> List[Tuple[float, float]]:
        """
        Get polygon vertices for a region considering shockwave boundaries.
        
        Returns list of (t, x) points forming the polygon.
        """
        # For each shockwave, determine if this region is upstream or downstream
        for sw in shockwaves:
            x_sw, t_sw = sw.get_trajectory(self.t_max, self.x_max)
            
            # Shockwave starts at (x_sw[0], t_sw[0]) and ends at (x_sw[1], t_sw[1])
            sw_start_x, sw_start_t = x_sw[0], t_sw[0]
            sw_end_x, sw_end_t = x_sw[1], t_sw[1]
            
            if sw.region1 == region:
                # This region is upstream of the shockwave
                # The shockwave moves into this region (if speed < 0) or away (if speed > 0)
                if sw.speed < 0:
                    # Backward shockwave - region shrinks from downstream side
                    # Polygon: bottom-left, top of shockwave, bottom of shockwave, bottom-right... 
                    # Actually for upstream region with backward wave:
                    # The region is bounded by: left edge, top edge, shockwave line, bottom edge
                    points = [
                        (region.t_range[0], region.x_range[0]),  # bottom-left
                        (region.t_range[0], region.x_range[1]),  # top-left (at x=5)
                        (sw_start_t, sw_start_x),                 # shockwave start (t=0, x=5)
                        (sw_end_t, sw_end_x),                     # shockwave end (t=0.5, x=1.43)
                        (region.t_range[1], region.x_range[0]),  # bottom-right
                    ]
                    return points
                else:
                    # Forward shockwave - region expands
                    points = [
                        (region.t_range[0], region.x_range[0]),
                        (region.t_range[0], region.x_range[1]),
                        (sw_end_t, sw_end_x),
                        (sw_start_t, sw_start_x),
                        (region.t_range[1], region.x_range[0]),
                    ]
                    return points
                    
            elif sw.region2 == region:
                # This region is downstream of the shockwave
                if sw.speed < 0:
                    # Backward shockwave - this region expands upstream
                    # Polygon bounded by: shockwave line, top edge, right edge, bottom to shockwave
                    points = [
                        (sw_start_t, sw_start_x),                 # shockwave start (t=0, x=5)
                        (region.t_range[0], region.x_range[1]),  # top-left (t=0, x=10)
                        (region.t_range[1], region.x_range[1]),  # top-right (t=0.5, x=10)
                        (region.t_range[1], sw_end_x),           # right edge at shockwave height
                        (sw_end_t, sw_end_x),                     # shockwave end
                    ]
                    return points
                else:
                    # Forward shockwave
                    points = [
                        (sw_start_t, sw_start_x),
                        (sw_end_t, sw_end_x),
                        (region.t_range[1], region.x_range[1]),
                        (region.t_range[0], region.x_range[1]),
                    ]
                    return points
        
        return []
    
    def plot(self, figsize: Tuple[int, int] = (14, 6), save_path: Optional[str] = None):
        """
        Create the combined plot with Fundamental Diagram and Trajectory Diagram.
        
        Parameters
        ----------
        figsize : Tuple[int, int]
            Figure size (width, height)
        save_path : Optional[str]
            If provided, save the figure to this path
        """
        fig, (ax_fd, ax_traj) = plt.subplots(1, 2, figsize=figsize)
        
        labels = self.fd.units.get_labels()
        
        # =====================================================================
        # PLOT 1: Triangular Fundamental Diagram
        # =====================================================================
        k_curve, q_curve = self.fd.get_fd_curve()
        
        # Plot the two branches of the triangular FD
        ax_fd.plot(k_curve[:2], q_curve[:2], 'b-', linewidth=2.5, 
                   label=f'Free-flow branch (slope = v_f = {self.fd.v_free:.0f})')
        ax_fd.plot(k_curve[1:], q_curve[1:], 'b-', linewidth=2.5,
                   label=f'Congested branch (slope = w = {self.fd.w:.1f})')
        
        # Mark critical point (q_max)
        ax_fd.plot(self.fd.k_critical, self.fd.q_max, 'ro', markersize=12, 
                   label=f'Capacity: (k_c={self.fd.k_critical:.0f}, q_max={self.fd.q_max:.0f})', zorder=5)
        
        # Mark jam density
        ax_fd.plot(self.fd.k_jam, 0, 'ks', markersize=10, 
                   label=f'Jam: k_j={self.fd.k_jam:.0f}', zorder=5)
        
        # Dashed lines for capacity
        ax_fd.axhline(y=self.fd.q_max, color='r', linestyle='--', alpha=0.3)
        ax_fd.axvline(x=self.fd.k_critical, color='r', linestyle='--', alpha=0.3)
        
        # Plot each region's operating point
        for i, region in enumerate(self.regions):
            marker = 's' if region.is_congested else 'o'
            ax_fd.plot(region.k, region.q, marker, color=self.colors[i], 
                      markersize=14, markeredgecolor='black', markeredgewidth=2, zorder=10)
            
            # Add label with offset
            offset_x = 3 if region.k < self.fd.k_jam * 0.8 else -15
            offset_y = 8
            ax_fd.annotate(region.name, (region.k, region.q), 
                          xytext=(offset_x, offset_y), textcoords='offset points',
                          fontsize=14, fontweight='bold', color=self.colors[i])
        
        ax_fd.set_xlabel(labels['density'], fontsize=12)
        ax_fd.set_ylabel(labels['flow'], fontsize=12)
        ax_fd.set_title('Triangular Fundamental Diagram', fontsize=14, fontweight='bold')
        ax_fd.legend(loc='upper right', fontsize=9)
        ax_fd.grid(True, alpha=0.3)
        ax_fd.set_xlim(0, self.fd.k_jam * 1.05)
        ax_fd.set_ylim(0, self.fd.q_max * 1.15)
        
        # =====================================================================
        # PLOT 2: Time-Space Trajectory Diagram
        # =====================================================================
        
        # Draw dynamic region boundaries considering shockwaves
        # For regions that are separated by a shockwave, draw polygons instead of rectangles
        self._draw_dynamic_regions(ax_traj)
        
        # Draw shockwaves
        for sw in self.shockwaves:
            x_sw, t_sw = sw.get_trajectory(self.t_max, self.x_max)
            direction = "→" if sw.speed > 0 else "←" if sw.speed < 0 else "•"
            ax_traj.plot(t_sw, x_sw, 'r-', linewidth=3,
                        label=f'Shockwave {sw.region1.name}{direction}{sw.region2.name}: w={sw.speed:.1f}',
                        zorder=5)
            
            # Mark shockwave start point
            ax_traj.plot(t_sw[0], x_sw[0], 'r^', markersize=8, zorder=6)
        
        # Draw vehicle trajectories
        trajectories = self._generate_trajectories()
        for traj in trajectories:
            if len(traj) > 1:
                x_vals = [p[0] for p in traj]
                t_vals = [p[1] for p in traj]
                ax_traj.plot(t_vals, x_vals, 'k-', linewidth=0.7, alpha=0.6)
        
        ax_traj.set_xlabel(labels['time'], fontsize=12)
        ax_traj.set_ylabel(labels['distance'], fontsize=12)
        ax_traj.set_title('Time-Space Trajectory Diagram', fontsize=14, fontweight='bold')
        ax_traj.set_xlim(0, self.t_max)
        ax_traj.set_ylim(0, self.x_max)
        ax_traj.grid(True, alpha=0.3)
        
        # Add legend for shockwaves if any exist
        if self.shockwaves:
            ax_traj.legend(loc='upper left', fontsize=9)
        
        # =====================================================================
        # Add info box
        # =====================================================================
        info_text = (f"Triangular FD Parameters:\n"
                    f"v_f = {self.fd.v_free:.1f} {self.fd.units.speed.value}\n"
                    f"k_j = {self.fd.k_jam:.1f} {self.fd.units.density.value}\n"
                    f"k_c = {self.fd.k_critical:.1f} {self.fd.units.density.value}\n"
                    f"q_max = {self.fd.q_max:.1f} {self.fd.units.flow.value}\n"
                    f"w = {self.fd.w:.1f} {self.fd.units.speed.value}")
        
        ax_fd.text(0.98, 0.02, info_text, transform=ax_fd.transAxes,
                  fontsize=9, verticalalignment='bottom', horizontalalignment='right',
                  bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Figure saved to: {save_path}")
        
        plt.show()
        
        return fig, (ax_fd, ax_traj)
    
    def print_summary(self):
        """Print a summary of the analysis."""
        print("=" * 70)
        print("TRAFFIC FLOW ANALYSIS SUMMARY - TRIANGULAR FUNDAMENTAL DIAGRAM")
        print("=" * 70)
        print(f"\nFundamental Diagram Parameters:")
        print(f"  Free flow speed (v_f):     {self.fd.v_free:.2f} {self.fd.units.speed.value}")
        print(f"  Jam density (k_j):         {self.fd.k_jam:.2f} {self.fd.units.density.value}")
        print(f"  Critical density (k_c):    {self.fd.k_critical:.2f} {self.fd.units.density.value}")
        print(f"  Maximum flow (q_max):      {self.fd.q_max:.2f} {self.fd.units.flow.value}")
        print(f"  Backward wave speed (w):   {self.fd.w:.2f} {self.fd.units.speed.value}")
        
        print(f"\nRegions:")
        print("-" * 70)
        for region in self.regions:
            regime = "CONGESTED" if region.is_congested else "FREE-FLOW"
            print(f"\n  Region {region.name} [{regime}]:")
            print(f"    Space: [{region.x_range[0]:.2f}, {region.x_range[1]:.2f}] {self.fd.units.distance.value}")
            print(f"    Time:  [{region.t_range[0]:.2f}, {region.t_range[1]:.2f}] {self.fd.units.time.value}")
            print(f"    Density (k): {region.k:.2f} {self.fd.units.density.value}")
            print(f"    Speed (v):   {region.v:.2f} {self.fd.units.speed.value}")
            print(f"    Flow (q):    {region.q:.2f} {self.fd.units.flow.value}")
        
        if self.shockwaves:
            print(f"\nShockwaves:")
            print("-" * 70)
            for sw in self.shockwaves:
                direction = "Forward (downstream)" if sw.speed > 0 else "Backward (upstream)" if sw.speed < 0 else "Stationary"
                print(f"\n  {sw.region1.name} → {sw.region2.name}:")
                print(f"    Shockwave speed: {sw.speed:.2f} {self.fd.units.speed.value}")
                print(f"    Start point: (x={sw.start_point[0]:.2f}, t={sw.start_point[1]:.2f})")
                print(f"    Direction: {direction}")
        
        print("\n" + "=" * 70)


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

def example_basic():
    """Basic example with two regions - one free-flow, one congested."""
    print("\n" + "=" * 70)
    print("EXAMPLE: Basic Two-Region Scenario (Free-flow meets Congestion)")
    print("=" * 70)
    
    # Define unit system
    units = UnitSystem(
        speed=SpeedUnit.KMH,
        distance=DistanceUnit.KM,
        time=TimeUnit.HOURS,
        density=DensityUnit.VEH_PER_KM,
        flow=FlowUnit.VEH_PER_HOUR
    )
    
    # Create triangular fundamental diagram
    fd = TriangularFD(
        v_free=100,      # km/h - free flow speed
        k_jam=150,       # veh/km - jam density
        k_critical=50,   # veh/km - critical density (at capacity)
        units=units
    )
    # This gives: q_max = 100 * 50 = 5000 veh/h
    #             w = -5000 / (150-50) = -50 km/h
    
    # Define regions
    regions = [
        Region(name="A", x_range=(0, 5), t_range=(0, 0.5), k=30),   # Free flow (k < k_c)
        Region(name="B", x_range=(5, 10), t_range=(0, 0.5), k=100), # Congested (k > k_c)
    ]
    
    # Create plotter
    plotter = TrajectoryPlotter(
        fd=fd,
        x_max=10,   # km
        t_max=0.5,  # hours (30 minutes)
        regions=regions
    )
    
    # Print summary and plot
    plotter.print_summary()
    plotter.plot()


def example_bottleneck():
    """Example simulating a bottleneck scenario with queue formation."""
    print("\n" + "=" * 70)
    print("EXAMPLE: Bottleneck Scenario")
    print("=" * 70)
    
    units = UnitSystem(
        speed=SpeedUnit.KMH,
        distance=DistanceUnit.KM,
        time=TimeUnit.HOURS,
        density=DensityUnit.VEH_PER_KM,
        flow=FlowUnit.VEH_PER_HOUR
    )
    
    fd = TriangularFD(v_free=120, k_jam=200, k_critical=40, units=units)
    # q_max = 120 * 40 = 4800 veh/h
    # w = -4800 / (200-40) = -30 km/h
    
    regions = [
        # Upstream - approaching traffic (free flow)
        Region(name="A", x_range=(0, 3), t_range=(0, 0.3), k=30),
        # Bottleneck area - congested (queue)
        Region(name="B", x_range=(3, 5), t_range=(0, 0.3), k=120),
        # Downstream - free flow after bottleneck
        Region(name="C", x_range=(5, 10), t_range=(0, 0.3), k=25),
    ]
    
    plotter = TrajectoryPlotter(fd=fd, x_max=10, t_max=0.3, regions=regions)
    plotter.print_summary()
    plotter.plot()


def example_at_capacity():
    """Example with region exactly at maximum capacity."""
    print("\n" + "=" * 70)
    print("EXAMPLE: Operating at Capacity (q_max)")
    print("=" * 70)
    
    units = UnitSystem(
        speed=SpeedUnit.KMH,
        distance=DistanceUnit.KM,
        time=TimeUnit.HOURS,
        density=DensityUnit.VEH_PER_KM,
        flow=FlowUnit.VEH_PER_HOUR
    )
    
    fd = TriangularFD(v_free=100, k_jam=150, k_critical=50, units=units)
    
    regions = [
        Region(name="Free", x_range=(0, 5), t_range=(0, 0.5), k=30),     # Free flow
        Region(name="Cap", x_range=(5, 10), t_range=(0, 0.5), k=50),    # Exactly at capacity
    ]
    
    plotter = TrajectoryPlotter(fd=fd, x_max=10, t_max=0.5, regions=regions)
    plotter.print_summary()
    plotter.plot()


def example_queue_discharge():
    """Example showing queue formation and discharge."""
    print("\n" + "=" * 70)
    print("EXAMPLE: Queue Formation and Discharge")
    print("=" * 70)
    
    units = UnitSystem(
        speed=SpeedUnit.KMH,
        distance=DistanceUnit.KM,
        time=TimeUnit.MINUTES,
        density=DensityUnit.VEH_PER_KM,
        flow=FlowUnit.VEH_PER_HOUR
    )
    
    fd = TriangularFD(v_free=60, k_jam=180, k_critical=45, units=units)
    
    regions = [
        # Initial free flow
        Region(name="A", x_range=(0, 1), t_range=(0, 5), k=30),
        # Queue builds up
        Region(name="B", x_range=(1, 2), t_range=(0, 5), k=140),
        # Downstream clearing
        Region(name="C", x_range=(2, 4), t_range=(0, 5), k=20),
    ]
    
    plotter = TrajectoryPlotter(fd=fd, x_max=4, t_max=5, regions=regions)
    plotter.print_summary()
    plotter.plot()


def example_three_regimes():
    """Example with three different traffic regimes."""
    print("\n" + "=" * 70)
    print("EXAMPLE: Three Traffic Regimes")
    print("=" * 70)
    
    units = UnitSystem(
        speed=SpeedUnit.KMH,
        distance=DistanceUnit.KM,
        time=TimeUnit.HOURS,
        density=DensityUnit.VEH_PER_KM,
        flow=FlowUnit.VEH_PER_HOUR
    )
    
    fd = TriangularFD(v_free=80, k_jam=160, k_critical=40, units=units)
    # q_max = 80 * 40 = 3200 veh/h
    
    regions = [
        # Light traffic
        Region(name="Light", x_range=(0, 3), t_range=(0, 0.4), k=20),
        # Moderate (near capacity)
        Region(name="Moderate", x_range=(3, 6), t_range=(0, 0.4), k=38),
        # Heavy congestion
        Region(name="Heavy", x_range=(6, 10), t_range=(0, 0.4), k=120),
    ]
    
    plotter = TrajectoryPlotter(fd=fd, x_max=10, t_max=0.4, regions=regions)
    plotter.print_summary()
    plotter.plot()


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    # Run the basic example by default
    example_basic()
    
    # Uncomment to run other examples:
    # example_bottleneck()
    # example_at_capacity()
    # example_queue_discharge()
    # example_three_regimes()
