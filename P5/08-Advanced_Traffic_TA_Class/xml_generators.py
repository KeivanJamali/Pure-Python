#!/usr/bin/env python3
"""
Convert network data to SUMO .net.xml format
This script converts network topology and coordinates from dictionaries
and generates a SUMO-compatible network XML file with optional traffic lights.
"""

import math
import pandas as pd
from datetime import datetime

class SUMONetworkGenerator:
    """
    Generate SUMO .net.xml files with network topology and traffic lights.
    
    This class creates a complete SUMO network file that includes:
    - Nodes/Junctions
    - Edges/Lanes
    - Connections
    - Traffic lights (optional, can be added after network creation)
    
    Example usage:
        # Define nodes and edges
        nodes = {
            '1': {'x': 0.0, 'y': 0.0},
            '2': {'x': 100.0, 'y': 0.0},
            '3': {'x': 100.0, 'y': 100.0}
        }
        edges = [
            {'from': '1', 'to': '2', 'length': 100.0, 'speed': 13.89},  # speed in m/s
            {'from': '2', 'to': '3', 'length': 100.0, 'speed': 20.0},
            {'from': '3', 'to': '1', 'length': 141.4}  # uses default_speed
        ]
        
        # Create network generator (default_speed=13.89 m/s = 50 km/h)
        generator = SUMONetworkGenerator(nodes, edges, default_speed=13.89)
        
        # Save network without traffic lights
        generator.save_xml('network.net.xml')
        
        # Or add traffic lights first
        generator.add_traffic_light('2', green_time=30, yellow_time=5)
        generator.add_traffic_lights_auto(['2', '3'])  # Auto-generate for multiple junctions
        generator.save_xml('network_with_tls.net.xml')
    
    Note:
        The node coordinates (x, y) are used ONLY for visualization/shape in SUMO GUI.
        The actual lane lengths come from the 'length' field in edges data.
        This allows using schematic layouts while maintaining accurate travel times.
    """
    
    def __init__(self, nodes: dict, edges: list[dict], default_speed: float = 13.89):
        """
        Initialize the generator with network data
        
        Args:
            nodes: Dictionary with node data (used for visualization only)
                   Format: {node_id: {'x': float, 'y': float}, ...}
                   Example: {'1': {'x': 0.0, 'y': 0.0}, '2': {'x': 100.0, 'y': 0.0}}
            
            edges: List of dictionaries with edge data
                   Format: [{'from': str, 'to': str, 'length': float, 'speed': float (optional)}, ...]
                   Example: [{'from': '1', 'to': '2', 'length': 100.0, 'speed': 13.89}]
                   - length: Actual edge length in METERS (used for simulation)
                   - speed: Edge speed in m/s (optional, defaults to default_speed)
                   
            default_speed: Default speed in m/s for edges without explicit speed (default: 13.89 m/s = 50 km/h)
        """
        self.default_speed = default_speed
        self.nodes = {str(k): v for k, v in nodes.items()}
        self.edges = [
            {
                'from': str(e['from']),
                'to': str(e['to']),
                'length': float(e['length']),
                'speed': float(e.get('speed', default_speed))
            }
            for e in edges
        ]
        
        self.traffic_lights = {}
        
        self._build_junction_map()
        
        self._validate_data()
    
    def _build_junction_map(self):
        """Build a map of junction IDs to their incoming edges"""
        self.junction_incoming = {}  # {junction_id: [list of (from_node, edge_id)]}
        
        for edge in self.edges:
            to_node = edge['to']
            from_node = edge['from']
            edge_id = f"E{from_node}_{to_node}"
            
            if to_node not in self.junction_incoming:
                self.junction_incoming[to_node] = []
            self.junction_incoming[to_node].append({
                'from_node': from_node,
                'edge_id': edge_id,
                'lane_id': f"{edge_id}_0"
            })
        
    def _validate_data(self):
        """Validate that all edges reference existing nodes"""
        for edge in self.edges:
            if edge['from'] not in self.nodes:
                raise ValueError(f"Edge references non-existent node: {edge['from']}")
            if edge['to'] not in self.nodes:
                raise ValueError(f"Edge references non-existent node: {edge['to']}")
        print(f"Validated {len(self.nodes)} nodes and {len(self.edges)} edges")
    
    def add_traffic_light(
        self,
        junction_id: str,
        phases: list[dict] = None,
        green_time: int = 30,
        yellow_time: int = 5,
        program_id: str = '0',
        offset: int = 0,
        tl_type: str = 'static'
    ):
        """
        Add a traffic light to a specific junction.
        
        Args:
            junction_id: The junction ID (e.g., '2' or 'J2')
            phases: Optional list of phase dictionaries. If not provided,
                   phases will be auto-generated based on incoming edges.
                   Format: [{'duration': int, 'state': str}, ...]
            green_time: Duration of green phase (used if phases not provided)
            yellow_time: Duration of yellow phase (used if phases not provided)
            program_id: Traffic light program ID (default: '0')
            offset: Time offset in seconds (default: 0)
            tl_type: Traffic light type: 'static' or 'actuated' (default: 'static')
            
        Example:
            # Auto-generate phases
            generator.add_traffic_light('2', green_time=30, yellow_time=5)
            
            # Custom phases
            generator.add_traffic_light('2', phases=[
                {'duration': 30, 'state': 'GGrr'},
                {'duration': 5, 'state': 'yyrr'},
                {'duration': 30, 'state': 'rrGG'},
                {'duration': 5, 'state': 'rryy'}
            ])
        """
        if junction_id.startswith('J'):
            junction_id = junction_id[1:]
        
        if junction_id not in self.junction_incoming:
            raise ValueError(f"Junction '{junction_id}' not found in network")
        
        if phases is None:
            phases = self._generate_phases_for_junction(junction_id, green_time, yellow_time)
        
        self._validate_phases(junction_id, phases)
        
        self.traffic_lights[junction_id] = {
            'junction_id': f'J{junction_id}',
            'program_id': program_id,
            'offset': offset,
            'type': tl_type,
            'phases': phases
        }
        
        print(f"Added traffic light to junction J{junction_id} with {len(phases)} phases")
    
    def add_traffic_lights_auto(
        self,
        junction_ids: list[str] = None,
        green_time: int = 30,
        yellow_time: int = 5
    ):
        """
        Automatically add traffic lights to multiple junctions.
        
        Args:
            junction_ids: List of junction IDs to add traffic lights to.
                         If None, adds to all junctions with 2+ incoming edges.
            green_time: Duration of green phase for each direction
            yellow_time: Duration of yellow transition phase
            
        Example:
            # Add to specific junctions
            generator.add_traffic_lights_auto(['2', '3', '5'])
            
            # Add to all eligible junctions
            generator.add_traffic_lights_auto()
        """
        if junction_ids is None:
            junction_ids = [
                jid for jid, incoming in self.junction_incoming.items()
                if len(incoming) >= 2
            ]
        
        for jid in junction_ids:
            if jid.startswith('J'):
                jid = jid[1:]
            self.add_traffic_light(jid, green_time=green_time, yellow_time=yellow_time)
        
        print(f"Added traffic lights to {len(junction_ids)} junctions")
    
    def remove_traffic_light(self, junction_id: str):
        """Remove a traffic light from a junction."""
        if junction_id.startswith('J'):
            junction_id = junction_id[1:]
        
        if junction_id in self.traffic_lights:
            del self.traffic_lights[junction_id]
            print(f"Removed traffic light from junction J{junction_id}")
        else:
            print(f"No traffic light found at junction J{junction_id}")
    
    def clear_traffic_lights(self):
        """Remove all traffic lights."""
        count = len(self.traffic_lights)
        self.traffic_lights.clear()
        print(f"Removed {count} traffic lights")
    
    def _count_junction_connections(self, junction_id: str) -> tuple[int, list[tuple]]:
        """
        Count total connections at a junction and group them by incoming edge.
        
        Returns:
            Tuple of (total_connections, list of (from_node, num_outgoing) tuples)
        """
        incoming = self.junction_incoming.get(junction_id, [])
        
        outgoing_edges = [e for e in self.edges if e['from'] == junction_id]
        num_outgoing = len(outgoing_edges)
        
        connection_groups = []
        total_connections = 0
        
        for inc in incoming:
            from_node = inc['from_node']
            conn_count = num_outgoing
            connection_groups.append((from_node, conn_count))
            total_connections += conn_count
        
        return total_connections, connection_groups
    
    def _generate_phases_for_junction(self, junction_id: str, green_time: int, yellow_time: int) -> list[dict]:
        """
        Generate traffic light phases for a junction based on connections.
        
        The state string length must match the total number of connections at the junction.
        Each connection gets one character in the state string.
        Connections are grouped by incoming edge - all connections from one incoming edge
        get green together.
        """
        total_connections, connection_groups = self._count_junction_connections(junction_id)
        
        if total_connections == 0:
            raise ValueError(f"Junction {junction_id} has no connections")
        
        num_incoming = len(connection_groups)
        
        if num_incoming == 1:
            # Only one incoming direction - always green for all connections
            return [{'duration': green_time + yellow_time, 'state': 'G' * total_connections}]
        
        # Multiple incoming directions - rotate green by incoming edge groups
        phases = []
        
        for i in range(num_incoming):
            # Build state string: green for connections from direction i, red for others
            green_state = ''
            yellow_state = ''
            
            for j, (from_node, conn_count) in enumerate(connection_groups):
                if j == i:
                    # This group gets green
                    green_state += 'G' * conn_count
                    yellow_state += 'y' * conn_count
                else:
                    # This group is red
                    green_state += 'r' * conn_count
                    yellow_state += 'r' * conn_count
            
            phases.append({'duration': green_time, 'state': green_state})
            phases.append({'duration': yellow_time, 'state': yellow_state})
        
        return phases
    
    def _validate_phases(self, junction_id: str, phases: list[dict]):
        """Validate traffic light phases against total connection count."""
        if not phases:
            raise ValueError(f"Traffic light for junction {junction_id} has no phases")
        
        total_connections, _ = self._count_junction_connections(junction_id)
        
        valid_chars = set('GgyrRoOus')
        
        for i, phase in enumerate(phases):
            if 'duration' not in phase:
                raise ValueError(f"Phase {i} of junction {junction_id} missing 'duration'")
            if 'state' not in phase:
                raise ValueError(f"Phase {i} of junction {junction_id} missing 'state'")
            
            # Check state length matches total number of connections
            if len(phase['state']) != total_connections:
                raise ValueError(
                    f"Phase {i} of junction {junction_id}: state length {len(phase['state'])} "
                    f"doesn't match {total_connections} connections"
                )
            
            # Validate state characters
            invalid_chars = set(phase['state']) - valid_chars
            if invalid_chars:
                raise ValueError(f"Invalid state characters {invalid_chars} in phase {i} of junction {junction_id}")
    
    def get_junction_info(self) -> pd.DataFrame:
        """
        Get information about each junction's connections.
        Useful for understanding the traffic light state string order.
        
        Returns:
            DataFrame with junction info including connections count and state length
        """
        data = []
        for node_id in sorted(self.junction_incoming.keys(), key=lambda x: int(x)):
            incoming = self.junction_incoming[node_id]
            has_tl = node_id in self.traffic_lights
            
            total_connections, connection_groups = self._count_junction_connections(node_id)
            
            data.append({
                'junction_id': f"J{node_id}",
                'num_incoming': len(incoming),
                'incoming_from_nodes': ', '.join([inc['from_node'] for inc in incoming]),
                'total_connections': total_connections,
                'state_length': total_connections,
                'has_traffic_light': has_tl
            })
        
        return pd.DataFrame(data)
    
    def _calculate_bounds(self):
        """Calculate network boundaries"""
        x_coords = [node['x'] for node in self.nodes.values()]
        y_coords = [node['y'] for node in self.nodes.values()]
        
        min_x = min(x_coords)
        max_x = max(x_coords)
        min_y = min(y_coords)
        max_y = max(y_coords)
        
        return min_x, min_y, max_x, max_y
    
    def _calculate_edge_shape(self, from_node, to_node):
        """
        Calculate lane shape based on node positions
        Returns coordinates for the lane
        """
        x1, y1 = self.nodes[from_node]['x'], self.nodes[from_node]['y']
        x2, y2 = self.nodes[to_node]['x'], self.nodes[to_node]['y']
        
        # Calculate angle and offset for right-hand lanes
        dx = x2 - x1
        dy = y2 - y1
        length = math.sqrt(dx**2 + dy**2)
        
        if length == 0:
            return x1, y1, x2, y2
        
        # Perpendicular offset for right-hand traffic (1.6m from center)
        offset = 1.6
        px = -dy / length * offset
        py = dx / length * offset
        
        return x1 + px, y1 + py, x2 + px, y2 + py
    
    def _create_dataframes(self):
        """Create DataFrames for different XML elements"""
        min_x, min_y, max_x, max_y = self._calculate_bounds()
        
        # Location DataFrame
        location_df = pd.DataFrame([{
            'netOffset': '0.00,0.00',
            'convBoundary': f'{min_x:.2f},{min_y:.2f},{max_x:.2f},{max_y:.2f}',
            'origBoundary': '10000000000.00,10000000000.00,-10000000000.00,-10000000000.00',
            'projParameter': '!'
        }])
        
        # Create edges and lanes
        edge_map = {}
        edges_data = []
        lanes_data = []
        
        for edge_data in self.edges:
            edge_id = f"E{edge_data['from']}_{edge_data['to']}"
            edge_map[(edge_data['from'], edge_data['to'])] = edge_id
            
            edges_data.append({
                'id': edge_id,
                'from': f"J{edge_data['from']}",
                'to': f"J{edge_data['to']}",
                'priority': '-1'
            })
            
            # Calculate lane shape (visual only - uses node coordinates)
            x1, y1, x2, y2 = self._calculate_edge_shape(edge_data['from'], edge_data['to'])
            
            # Use actual edge length from input data (in meters), not calculated from coordinates
            lanes_data.append({
                'edge_id': edge_id,
                'id': f"{edge_id}_0",
                'index': '0',
                'speed': f"{edge_data['speed']:.2f}",
                'length': f"{edge_data['length']:.2f}",  # Actual length in meters from edge data
                'shape': f"{x1:.2f},{y1:.2f} {x2:.2f},{y2:.2f}"  # Visual shape from node coordinates
            })
        
        edges_df = pd.DataFrame(edges_data)
        lanes_df = pd.DataFrame(lanes_data)
        
        # Create junctions
        junctions_data = []
        for node_id, coords in sorted(self.nodes.items(), key=lambda x: int(x[0])):
            # Find incoming lanes
            inc_lanes = []
            for edge_data in self.edges:
                if edge_data['to'] == node_id:
                    edge_id = edge_map[(edge_data['from'], edge_data['to'])]
                    inc_lanes.append(f"{edge_id}_0")
            
            # Simple shape (square around junction)
            shape_coords = [
                f"{coords['x']-2:.2f},{coords['y']-2:.2f}",
                f"{coords['x']+2:.2f},{coords['y']-2:.2f}",
                f"{coords['x']+2:.2f},{coords['y']+2:.2f}",
                f"{coords['x']-2:.2f},{coords['y']+2:.2f}"
            ]
            
            # Set junction type based on whether it has a traffic light
            junction_type = 'traffic_light' if node_id in self.traffic_lights else 'priority'
            
            junctions_data.append({
                'id': f"J{node_id}",
                'type': junction_type,
                'x': f"{coords['x']:.2f}",
                'y': f"{coords['y']:.2f}",
                'incLanes': ' '.join(inc_lanes),
                'intLanes': '',
                'shape': ' '.join(shape_coords)
            })
        
        junctions_df = pd.DataFrame(junctions_data)
        
        # Create connections with traffic light links
        connections_data = []
        tl_link_index = {}  # Track link indices for each traffic light
        
        for edge_data in self.edges:
            from_edge_id = edge_map[(edge_data['from'], edge_data['to'])]
            to_node = edge_data['to']
            
            # Find outgoing edges from the 'to' node
            for next_edge in self.edges:
                if next_edge['from'] == to_node:
                    to_edge_id = edge_map[(next_edge['from'], next_edge['to'])]
                    
                    connection = {
                        'from': from_edge_id,
                        'to': to_edge_id,
                        'fromLane': '0',
                        'toLane': '0',
                        'dir': 's',
                        'state': 'M'
                    }
                    
                    # Add traffic light attributes if this node has a traffic light
                    if to_node in self.traffic_lights:
                        tl_id = f"J{to_node}"
                        if tl_id not in tl_link_index:
                            tl_link_index[tl_id] = 0
                        
                        connection['tl'] = tl_id
                        connection['linkIndex'] = str(tl_link_index[tl_id])
                        tl_link_index[tl_id] += 1
                    
                    connections_data.append(connection)
        
        connections_df = pd.DataFrame(connections_data) if connections_data else pd.DataFrame()
        
        return location_df, edges_df, lanes_df, junctions_df, connections_df, edge_map
    
    def _generate_traffic_lights_xml(self) -> str:
        """Generate XML for traffic light logic elements."""
        if not self.traffic_lights:
            return ""
        
        tls_xml = "    <!-- Traffic Light Logic -->\n"
        
        for node_id in sorted(self.traffic_lights.keys(), key=lambda x: int(x)):
            tl = self.traffic_lights[node_id]
            
            tls_xml += f'    <tlLogic id="{tl["junction_id"]}" type="{tl["type"]}" programID="{tl["program_id"]}" offset="{tl["offset"]}">\n'
            
            for phase in tl['phases']:
                phase_attrs = f'duration="{phase["duration"]}" state="{phase["state"]}"'
                if 'minDur' in phase and phase['minDur']:
                    phase_attrs += f' minDur="{phase["minDur"]}"'
                if 'maxDur' in phase and phase['maxDur']:
                    phase_attrs += f' maxDur="{phase["maxDur"]}"'
                tls_xml += f'        <phase {phase_attrs}/>\n'
            
            tls_xml += '    </tlLogic>\n'
        
        return tls_xml + '\n'
        
    def save_xml(self, output_file):
        """
        Save the network as SUMO .net.xml file.
        
        This includes:
        - Network topology (nodes, edges, lanes)
        - Connections between edges
        - Traffic light logic (if any traffic lights have been added)
        
        Args:
            output_file: Path to the output .net.xml file
        """
        location_df, edges_df, lanes_df, junctions_df, connections_df, edge_map = self._create_dataframes()
        
        # Header
        header = '<?xml version="1.0" encoding="UTF-8"?>\n'
        header += f'<!-- generated on {datetime.now().strftime("%Y-%m-%dT%H:%M:%S")} by SUMONetworkGenerator -->\n\n'
        header += '<net version="1.20" junctionCornerDetail="5" limitTurnSpeed="5.50" '
        header += 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        header += 'xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/net_file.xsd">\n\n'
        
        # Location - using to_xml with attr_cols (all columns as attributes)
        location_xml = location_df.to_xml(
            root_name=None,
            row_name='location',
            attr_cols=location_df.columns.tolist(),
            index=False,
            xml_declaration=False
        )
        # Extract just the <location .../> element
        location_xml = location_xml.split('\n')[1].strip() + '\n\n'
        
        # Edges with nested lanes - need custom handling for nesting
        edges_xml = ""
        for _, edge in edges_df.iterrows():
            edge_lanes = lanes_df[lanes_df['edge_id'] == edge['id']].drop(columns=['edge_id'])
            
            # Create lanes XML using to_xml
            lanes_xml = edge_lanes.to_xml(
                root_name=None,
                row_name='lane',
                attr_cols=edge_lanes.columns.tolist(),
                index=False,
                xml_declaration=False
            )
            # Extract lane elements and indent
            lane_lines = [f"        {line.strip()}" for line in lanes_xml.split('\n')[1:-1] if line.strip()]
            
            edges_xml += f'    <edge id="{edge["id"]}" from="{edge["from"]}" to="{edge["to"]}" priority="{edge["priority"]}">\n'
            edges_xml += '\n'.join(lane_lines) + '\n'
            edges_xml += '    </edge>\n'
        
        # Traffic Light Logic (before junctions)
        tls_xml = self._generate_traffic_lights_xml()
        
        # Junctions - using to_xml with attr_cols
        junctions_xml = junctions_df.to_xml(
            root_name=None,
            row_name='junction',
            attr_cols=junctions_df.columns.tolist(),
            index=False,
            xml_declaration=False
        )
        # Extract junction elements and add proper indentation
        junction_lines = [f"    {line.strip()}" for line in junctions_xml.split('\n')[1:-1] if line.strip()]
        junctions_xml = '\n'.join(junction_lines) + '\n'
        
        # Connections - using to_xml with attr_cols
        connections_xml = ""
        if not connections_df.empty:
            connections_xml = connections_df.to_xml(
                root_name=None,
                row_name='connection',
                attr_cols=connections_df.columns.tolist(),
                index=False,
                xml_declaration=False
            )
            # Extract connection elements and add proper indentation
            conn_lines = [f"    {line.strip()}" for line in connections_xml.split('\n')[1:-1] if line.strip()]
            connections_xml = '\n'.join(conn_lines) + '\n'
        
        # Footer
        footer = '\n</net>\n'
        
        # Combine all parts
        full_xml = header + location_xml + edges_xml + '\n' + tls_xml + junctions_xml + '\n' + connections_xml + footer
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_xml)
        
        tl_count = len(self.traffic_lights)
        print(f"Network saved to {output_file} ({len(self.nodes)} nodes, {len(self.edges)} edges, {tl_count} traffic lights)")
        print(f"WARNING: This manually generated network may have issues with traffic lights.")
        print(f"         Consider using save_with_netconvert() for fully valid networks.")
    
    def save_with_netconvert(
        self, 
        output_file: str, 
        cleanup: bool = True,
        green_time: int = 30,
        yellow_time: int = 5
    ):
        """
        Save the network using SUMO's netconvert for proper network generation.
        
        This method creates plain XML files and uses netconvert to generate
        a fully valid SUMO network with proper internal junctions and traffic lights.
        
        IMPORTANT: Edge lengths are taken from the input edge data, NOT calculated
        from node coordinates. This allows using schematic/visual node positions
        while maintaining accurate edge lengths for simulation.
        
        Args:
            output_file: Path to the output .net.xml file
            cleanup: If True, remove temporary plain XML files after conversion
            green_time: Green phase duration for traffic lights (default: 30s)
            yellow_time: Yellow phase duration for traffic lights (default: 5s)
        
        Note:
            - Requires SUMO to be installed and netconvert to be in PATH.
            - Node coordinates are used for visualization only.
            - Edge lengths come from the 'length' field in edges data (in meters).
        """
        import subprocess
        import os
        
        base_path = output_file.rsplit('.', 1)[0]
        nodes_file = f"{base_path}.nod.xml"
        edges_file = f"{base_path}.edg.xml"
        
        # Generate nodes XML
        nodes_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        nodes_xml += '<nodes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        nodes_xml += 'xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/nodes_file.xsd">\n'
        
        for node_id, coords in self.nodes.items():
            node_type = 'traffic_light' if node_id in self.traffic_lights else 'priority'
            nodes_xml += f'    <node id="J{node_id}" x="{coords["x"]}" y="{coords["y"]}" type="{node_type}"/>\n'
        
        nodes_xml += '</nodes>\n'
        
        with open(nodes_file, 'w', encoding='utf-8') as f:
            f.write(nodes_xml)
        
        # Generate edges XML with explicit lengths
        # Note: We specify 'length' attribute to override netconvert's calculation from coordinates
        # This allows using schematic/visual coordinates while maintaining accurate edge lengths
        edges_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        edges_xml += '<edges xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        edges_xml += 'xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/edges_file.xsd">\n'
        
        for edge in self.edges:
            from_node = edge['from']
            to_node = edge['to']
            edge_id = f"E{from_node}_{to_node}"
            speed = edge.get('speed', self.default_speed)
            length = edge['length']  # Use actual length from input data (in meters)
            edges_xml += f'    <edge id="{edge_id}" from="J{from_node}" to="J{to_node}" numLanes="1" speed="{speed:.2f}" length="{length:.2f}"/>\n'
        
        edges_xml += '</edges>\n'
        
        with open(edges_file, 'w', encoding='utf-8') as f:
            f.write(edges_xml)
        
        # Build netconvert command - let netconvert generate traffic light phases
        cmd = [
            'netconvert', 
            '-n', nodes_file, 
            '-e', edges_file, 
            '-o', output_file,
            '--tls.green.time', str(green_time),
            '--tls.yellow.time', str(yellow_time),
        ]
        
        # Run netconvert
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"netconvert error:\n{result.stderr}")
                raise RuntimeError(f"netconvert failed: {result.stderr}")
            
            print(f"Network generated successfully: {output_file}")
            print(f"  Nodes: {len(self.nodes)}")
            print(f"  Edges: {len(self.edges)}")
            print(f"  Traffic lights: {len(self.traffic_lights)}")
            
        except FileNotFoundError:
            raise RuntimeError("netconvert not found. Please ensure SUMO is installed and in PATH.")
        
        finally:
            # Cleanup temporary files
            if cleanup:
                for f in [nodes_file, edges_file]:
                    if f and os.path.exists(f):
                        os.remove(f)


class SUMORouteGenerator:
    """
    Generate SUMO route files (.rou.xml) with vehicle types, routes, and flows.
    
    This class supports two routing modes:
    
    1. STATIC ROUTES (add_route):
       - Define exact edge sequences that vehicles must follow
       - Vehicles will NOT reroute based on traffic conditions
       - Use when you want deterministic paths
    
    2. DYNAMIC ROUTING (add_routes_from_od / add_trip):
       - Define origin-destination pairs (trips)
       - SUMO/duarouter computes shortest path
       - Can be combined with rerouting devices for dynamic updates
       - Use for traffic assignment and realistic routing
    
    Example usage:
        route_gen = SUMORouteGenerator()
        
        # Static route - fixed path
        route_gen.add_route('route_1', ['E1_2', 'E2_3', 'E3_4'], flow=500)
        
        # Dynamic routing from OD matrix - SUMO finds shortest path
        od_matrix = {('1', '5'): 500, ('2', '4'): 300}
        route_gen.add_routes_from_od(od_matrix)
        
        route_gen.save_xml('routes.rou.xml')
    """
    
    def __init__(self):
        """Initialize the route generator."""
        self.vehicle_types = {}
        self.routes = {}       # Static routes with explicit edge sequences
        self.trips = []        # Dynamic trips (from/to) for shortest path routing
        self.flows = []        # Flows attached to routes
        self.vehicles = []     # Individual vehicles
        
        # Add default vehicle type
        self.add_vehicle_type(
            type_id='default',
            accel=2.6,
            decel=4.5,
            sigma=0.5,
            length=5.0,
            min_gap=2.5,
            max_speed=55.56,  # 200 km/h
            color='yellow'
        )
    
    def add_vehicle_type(
        self,
        type_id: str,
        accel: float = 2.6,
        decel: float = 4.5,
        sigma: float = 0.5,
        length: float = 5.0,
        min_gap: float = 2.5,
        max_speed: float = 55.56,
        color: str = None,
        vclass: str = 'passenger',
        gui_shape: str = None
    ):
        """
        Add a vehicle type definition.
        
        Args:
            type_id: Unique identifier for the vehicle type
            accel: Maximum acceleration (m/s²)
            decel: Maximum deceleration (m/s²)
            sigma: Driver imperfection (0=perfect, 1=maximum)
            length: Vehicle length (m)
            min_gap: Minimum gap to leading vehicle (m)
            max_speed: Maximum vehicle speed (m/s)
            color: Vehicle color (e.g., 'red', 'blue', '1,0,0' for RGB)
            vclass: Vehicle class (passenger, truck, bus, bicycle, etc.)
            gui_shape: GUI shape (passenger, truck, bus, motorcycle, etc.)
        """
        self.vehicle_types[type_id] = {
            'id': type_id,
            'accel': accel,
            'decel': decel,
            'sigma': sigma,
            'length': length,
            'minGap': min_gap,
            'maxSpeed': max_speed,
            'color': color,
            'vClass': vclass,
            'guiShape': gui_shape
        }
        print(f"Added vehicle type '{type_id}'")
    
    def add_route(
        self,
        route_id: str,
        edges: list[str],
        flow: float = None,
        vtype: str = 'default',
        begin: float = 0,
        end: float = 3600,
        color: str = None
    ):
        """
        Add a STATIC route with explicit edge sequence.
        
        Vehicles using this route will follow the exact edge sequence
        and will NOT reroute based on traffic conditions.
        
        Args:
            route_id: Unique identifier for the route
            edges: List of edge IDs that form the route (exact path)
            flow: Vehicles per hour (optional, creates a flow if provided)
            vtype: Vehicle type to use for the flow
            begin: Start time for the flow (seconds)
            end: End time for the flow (seconds)
            color: Route color for visualization
            
        Example:
            # Static route - vehicles follow exactly E1_2 -> E2_3 -> E3_4
            route_gen.add_route('main_route', ['E1_2', 'E2_3', 'E3_4'], flow=600)
        """
        # Store route
        self.routes[route_id] = {
            'id': route_id,
            'edges': edges,
            'color': color
        }
        
        # Create flow if flow rate is provided
        if flow is not None:
            flow_data = {
                'id': f"flow_{route_id}",
                'route': route_id,
                'type': vtype,
                'begin': begin,
                'end': end,
                'vehsPerHour': flow
            }
            if color:
                flow_data['color'] = color
            self.flows.append(flow_data)
        
        print(f"Added STATIC route '{route_id}' with {len(edges)} edges" + 
              (f" and flow {flow} veh/h" if flow else ""))
    
    def add_trip(
        self,
        trip_id: str,
        from_edge: str,
        to_edge: str,
        depart: float = 0,
        vtype: str = 'default',
        color: str = None
    ):
        """
        Add a single trip for DYNAMIC routing.
        
        SUMO will compute the shortest path from from_edge to to_edge.
        Can be rerouted during simulation with TraCI or rerouting device.
        
        Args:
            trip_id: Unique trip identifier
            from_edge: Starting edge ID
            to_edge: Destination edge ID
            depart: Departure time in seconds
            vtype: Vehicle type
            color: Vehicle color
        """
        trip = {
            'id': trip_id,
            'from': from_edge,
            'to': to_edge,
            'depart': depart,
            'type': vtype
        }
        if color:
            trip['color'] = color
        
        self.trips.append(trip)
        print(f"Added trip '{trip_id}' from {from_edge} to {to_edge} (dynamic routing)")
    
    def add_routes_from_od(
        self,
        od_matrix: dict,
        vtype: str = 'default',
        begin: float = 0,
        end: float = 3600,
        color: str = None
    ):
        """
        Add trips/flows from an Origin-Destination matrix for DYNAMIC routing.
        
        This creates flows with 'from' and 'to' attributes instead of explicit routes.
        SUMO will compute shortest paths for these vehicles.
        
        For dynamic rerouting during simulation, enable rerouting device:
            sumo --device.rerouting.probability 1.0 --device.rerouting.period 60
        
        Or use duarouter for iterative traffic assignment:
            duarouter -n network.net.xml -r routes.rou.xml -o routes_assigned.rou.xml
        
        Args:
            od_matrix: Dictionary mapping (origin_node, dest_node) to flow (veh/hour)
                      Example: {('1', '5'): 500, ('2', '4'): 300}
            vtype: Vehicle type for all flows
            begin: Start time for all flows (seconds)
            end: End time for all flows (seconds)
            color: Vehicle color
            
        Example:
            od_matrix = {
                ('1', '5'): 500,  # 500 veh/hour from node 1 to node 5
                ('2', '4'): 300,
                ('3', '1'): 200,
            }
            route_gen.add_routes_from_od(od_matrix)
        """
        count = 0
        for (origin, dest), flow in od_matrix.items():
            origin = str(origin)
            dest = str(dest)
            
            if flow <= 0:
                continue
            
            # Create a flow with from/to (not route) - SUMO computes path
            flow_id = f"flow_{origin}_to_{dest}"
            
            # Find first outgoing edge from origin and last incoming edge to dest
            # User should provide edge IDs, but we support node IDs too
            from_edge = f"E{origin}_"  # Will be filled by user or matched
            to_edge = f"_E{dest}"
            
            flow_data = {
                'id': flow_id,
                'from_node': origin,  # We'll convert to edges
                'to_node': dest,
                'type': vtype,
                'begin': begin,
                'end': end,
                'vehsPerHour': flow,
                'is_trip': True  # Mark as trip-based flow
            }
            if color:
                flow_data['color'] = color
            
            self.flows.append(flow_data)
            count += 1
        
        print(f"Added {count} OD flows for DYNAMIC routing (shortest path)")
        print("  → Use 'duarouter' or '--device.rerouting.probability 1.0' for dynamic assignment")
    
    def save_xml(self, output_file: str, begin: float = 0, end: float = 3600):
        """
        Save routes to a SUMO .rou.xml file.
        
        For OD-based flows, you may need to run duarouter first:
            duarouter -n network.net.xml -r routes.rou.xml -o routes_computed.rou.xml
        
        Args:
            output_file: Path to the output file
            begin: Simulation begin time (for header comment)
            end: Simulation end time (for header comment)
        """
        # Header
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n\n'
        xml += '<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        xml += 'xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">\n\n'
        
        # Vehicle types
        for vtype in self.vehicle_types.values():
            attrs = [f'id="{vtype["id"]}"']
            attrs.append(f'accel="{vtype["accel"]}"')
            attrs.append(f'decel="{vtype["decel"]}"')
            attrs.append(f'sigma="{vtype["sigma"]}"')
            attrs.append(f'length="{vtype["length"]}"')
            attrs.append(f'minGap="{vtype["minGap"]}"')
            attrs.append(f'maxSpeed="{vtype["maxSpeed"]}"')
            if vtype.get('color'):
                attrs.append(f'color="{vtype["color"]}"')
            if vtype.get('vClass'):
                attrs.append(f'vClass="{vtype["vClass"]}"')
            if vtype.get('guiShape'):
                attrs.append(f'guiShape="{vtype["guiShape"]}"')
            
            xml += f'    <vType {" ".join(attrs)}/>\n'
        xml += '\n'
        
        # Static Routes
        if self.routes:
            for route in self.routes.values():
                edges_str = ' '.join(route['edges'])
                attrs = [f'id="{route["id"]}"', f'edges="{edges_str}"']
                if route.get('color'):
                    attrs.append(f'color="{route["color"]}"')
                xml += f'    <route {" ".join(attrs)}/>\n'
            xml += '\n'
        
        # Trips (for dynamic routing - single vehicles)
        if self.trips:
            sorted_trips = sorted(self.trips, key=lambda t: t['depart'])
            for trip in sorted_trips:
                attrs = [
                    f'id="{trip["id"]}"',
                    f'depart="{trip["depart"]}"',
                    f'from="{trip["from"]}"',
                    f'to="{trip["to"]}"',
                    f'type="{trip["type"]}"'
                ]
                if trip.get('color'):
                    attrs.append(f'color="{trip["color"]}"')
                xml += f'    <trip {" ".join(attrs)}/>\n'
            xml += '\n'
        
        # Flows
        static_flows = [f for f in self.flows if not f.get('is_trip')]
        dynamic_flows = [f for f in self.flows if f.get('is_trip')]
        
        if static_flows:
            for flow in static_flows:
                attrs = [
                    f'id="{flow["id"]}"',
                    f'route="{flow["route"]}"',
                    f'type="{flow["type"]}"',
                    f'begin="{flow["begin"]}"',
                    f'end="{flow["end"]}"',
                    f'vehsPerHour="{flow["vehsPerHour"]}"'
                ]
                if flow.get('color'):
                    attrs.append(f'color="{flow["color"]}"')
                xml += f'    <flow {" ".join(attrs)}/>\n'
            xml += '\n'
        
        if dynamic_flows:
            for flow in dynamic_flows:
                from_node = flow['from_node']
                to_node = flow['to_node']
                
                attrs = [
                    f'id="{flow["id"]}"',
                    f'type="{flow["type"]}"',
                    f'begin="{flow["begin"]}"',
                    f'end="{flow["end"]}"',
                    f'vehsPerHour="{flow["vehsPerHour"]}"',
                    f'fromJunction="J{from_node}"',
                    f'toJunction="J{to_node}"'
                ]
                if flow.get('color'):
                    attrs.append(f'color="{flow["color"]}"')
                xml += f'    <flow {" ".join(attrs)}/>\n'
            xml += '\n'
        
        # Individual vehicles
        if self.vehicles:
            sorted_vehicles = sorted(self.vehicles, key=lambda v: v['depart'])
            for veh in sorted_vehicles:
                attrs = [
                    f'id="{veh["id"]}"',
                    f'route="{veh["route"]}"',
                    f'depart="{veh["depart"]}"',
                    f'type="{veh["type"]}"'
                ]
                if veh.get('departLane'):
                    attrs.append(f'departLane="{veh["departLane"]}"')
                if veh.get('departSpeed'):
                    attrs.append(f'departSpeed="{veh["departSpeed"]}"')
                if veh.get('color'):
                    attrs.append(f'color="{veh["color"]}"')
                xml += f'    <vehicle {" ".join(attrs)}/>\n'
            xml += '\n'
        
        # Footer
        xml += '</routes>\n'
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml)
        
        static_count = len(self.routes) + len(static_flows)
        dynamic_count = len(self.trips) + len(dynamic_flows)
        
        print(f"Routes saved to {output_file}")
        print(f"  - {len(self.vehicle_types)} vehicle types")
        print(f"  - {len(self.routes)} static routes, {len(static_flows)} static flows")
        print(f"  - {len(self.trips)} dynamic trips, {len(dynamic_flows)} dynamic flows (OD-based)")
        
        if dynamic_count > 0:
            print(f"\n  ⚠️  For dynamic routing, run:")
            print(f"      duarouter -n network.net.xml -r {output_file} -o routes_computed.rou.xml")
            print(f"      OR use: sumo --device.rerouting.probability 1.0 --device.rerouting.period 60")
    
    def clear(self):
        """Clear all routes, trips, flows, and vehicles (keeps vehicle types)."""
        self.routes.clear()
        self.trips.clear()
        self.flows.clear()
        self.vehicles.clear()
        print("Cleared all routes, trips, flows, and vehicles")
    
    def get_summary(self) -> pd.DataFrame:
        """
        Get a summary of all routes and flows.
        
        Returns:
            DataFrame with route/flow information
        """
        data = []
        
        # Static routes
        for route_id, route in self.routes.items():
            flow_info = next((f for f in self.flows if f.get('route') == route_id), None)
            data.append({
                'id': route_id,
                'type': 'STATIC',
                'path': ' → '.join(route['edges'][:3]) + ('...' if len(route['edges']) > 3 else ''),
                'flow_veh_h': flow_info.get('vehsPerHour') if flow_info else None,
                'begin': flow_info.get('begin') if flow_info else None,
                'end': flow_info.get('end') if flow_info else None
            })
        
        # Dynamic OD flows
        for flow in self.flows:
            if flow.get('is_trip'):
                data.append({
                    'id': flow['id'],
                    'type': 'DYNAMIC (OD)',
                    'path': f"J{flow['from_node']} → J{flow['to_node']} (shortest path)",
                    'flow_veh_h': flow.get('vehsPerHour'),
                    'begin': flow.get('begin'),
                    'end': flow.get('end')
                })
        
        return pd.DataFrame(data)


class SUMOConfigGenerator:
    """
    Generate SUMO configuration files (.sumocfg) and additional files.
    
    This class creates:
    - Main configuration file (.sumocfg)
    - Optional additional files (.add.xml) for detectors
    - Output specifications for simulation results
    
    Example usage:
        config = SUMOConfigGenerator()
        
        # Set input files
        config.set_network('network.net.xml')
        config.set_routes('routes.rou.xml')
        
        # Set simulation time
        config.set_time(begin=0, end=3600, step_length=0.1)
        
        # Add outputs
        config.add_output('tripinfo', 'tripinfo.xml')
        config.add_output('summary', 'summary.xml')
        
        # Enable dynamic routing
        config.enable_rerouting(probability=1.0, period=60)
        
        # Add detectors
        config.add_induction_loop('loop1', 'E1_2', pos=50)
        
        # Save all files
        config.save('simulation.sumocfg')
    """
    
    def __init__(self):
        """Initialize the configuration generator."""
        # Input files
        self.network_file = None
        self.route_files = []
        self.additional_files = []
        
        # Time settings
        self.begin = 0
        self.end = 3600
        self.step_length = 1.0
        
        # Processing options
        self.options = {
            'time-to-teleport': -1,  # Disable teleporting (vehicles wait)
            'waiting-time-memory': 100,
            'junction-taz': 'true',  # Allow fromJunction/toJunction in routes
        }
        
        # Routing options (for dynamic routing)
        self.routing_options = {}
        
        # Output specifications
        self.outputs = {}
        
        # Detectors and additional elements
        self.induction_loops = []
        self.lane_area_detectors = []
        self.multi_entry_exit_detectors = []
        
        # GUI settings
        self.gui_settings = {
            'start': True,  # Start simulation immediately
            'quit-on-end': False,
        }
    
    def set_network(self, network_file: str):
        """
        Set the network file.
        
        Args:
            network_file: Path to the .net.xml file
        """
        self.network_file = network_file
        print(f"Set network file: {network_file}")
    
    def set_routes(self, route_file: str):
        """
        Set or add a route file.
        
        Args:
            route_file: Path to the .rou.xml file
        """
        if route_file not in self.route_files:
            self.route_files.append(route_file)
        print(f"Added route file: {route_file}")
    
    def add_additional_file(self, additional_file: str):
        """
        Add an additional file (detectors, etc.).
        
        Args:
            additional_file: Path to the .add.xml file
        """
        if additional_file not in self.additional_files:
            self.additional_files.append(additional_file)
        print(f"Added additional file: {additional_file}")
    
    def set_time(
        self,
        begin: float = 0,
        end: float = 3600,
        step_length: float = 1.0
    ):
        """
        Set simulation time parameters.
        
        Args:
            begin: Simulation start time (seconds)
            end: Simulation end time (seconds)
            step_length: Simulation step length (seconds, default: 1.0)
        """
        self.begin = begin
        self.end = end
        self.step_length = step_length
        print(f"Set simulation time: {begin}s to {end}s (step: {step_length}s)")
    
    def set_option(self, option: str, value):
        """
        Set a general SUMO option.
        
        Args:
            option: Option name (e.g., 'time-to-teleport', 'seed')
            value: Option value
        """
        self.options[option] = value
        print(f"Set option: {option} = {value}")
    
    def enable_rerouting(
        self,
        probability: float = 1.0,
        period: float = 60,
        adaptation_interval: float = 1,
        adaptation_weight: float = 0.5
    ):
        """
        Enable automatic rerouting for dynamic traffic assignment.
        
        Vehicles will periodically recalculate their routes based on
        current travel times in the network.
        
        Args:
            probability: Probability that a vehicle has rerouting device (0-1)
            period: How often vehicles check for better routes (seconds)
            adaptation_interval: How often edge weights are updated (seconds)
            adaptation_weight: Weight for new travel time info (0-1)
        """
        self.routing_options = {
            'device.rerouting.probability': probability,
            'device.rerouting.period': period,
            'device.rerouting.adaptation-interval': adaptation_interval,
            'device.rerouting.adaptation-weight': adaptation_weight,
        }
        print(f"Enabled rerouting: probability={probability}, period={period}s")
    
    def disable_rerouting(self):
        """Disable automatic rerouting."""
        self.routing_options = {}
        print("Disabled rerouting")
    
    def add_output(self, output_type: str, filename: str, **kwargs):
        """
        Add an output file specification.
        
        Args:
            output_type: Type of output. Supported types:
                - 'tripinfo': Per-vehicle trip information
                - 'summary': Aggregated simulation statistics
                - 'edgedata': Edge-based statistics
                - 'lanedata': Lane-based statistics
                - 'queue': Queue lengths at junctions
                - 'emission': Vehicle emissions
                - 'fcd': Floating car data (trajectories)
                - 'full': Full vehicle state output
                - 'vtk': VTK format for visualization
                - 'netstate': Complete network state
            filename: Output file path
            **kwargs: Additional options (e.g., period for periodic outputs)
        """
        self.outputs[output_type] = {
            'file': filename,
            **kwargs
        }
        print(f"Added output: {output_type} → {filename}")
    
    def add_induction_loop(
        self,
        detector_id: str,
        edge_id: str,
        pos: float,
        lane: int = 0,
        freq: float = 60,
        output_file: str = None
    ):
        """
        Add an induction loop detector.
        
        Induction loops count vehicles passing a point on a lane.
        
        Args:
            detector_id: Unique detector ID
            edge_id: Edge where detector is placed
            pos: Position on the lane (meters from start)
            lane: Lane index (default: 0)
            freq: Output frequency in seconds
            output_file: Output file (default: detector_id.xml)
        """
        self.induction_loops.append({
            'id': detector_id,
            'lane': f"{edge_id}_{lane}",
            'pos': pos,
            'freq': freq,
            'file': output_file or f"{detector_id}.xml"
        })
        print(f"Added induction loop '{detector_id}' on {edge_id} at {pos}m")
    
    def add_lane_area_detector(
        self,
        detector_id: str,
        edge_id: str,
        pos: float,
        end_pos: float = None,
        lane: int = 0,
        freq: float = 60,
        output_file: str = None
    ):
        """
        Add a lane area detector (E2 detector).
        
        Lane area detectors measure traffic over a section of lane.
        
        Args:
            detector_id: Unique detector ID
            edge_id: Edge where detector is placed
            pos: Start position on the lane (meters)
            end_pos: End position (default: end of lane)
            lane: Lane index (default: 0)
            freq: Output frequency in seconds
            output_file: Output file (default: detector_id.xml)
        """
        detector = {
            'id': detector_id,
            'lane': f"{edge_id}_{lane}",
            'pos': pos,
            'freq': freq,
            'file': output_file or f"{detector_id}.xml"
        }
        if end_pos is not None:
            detector['endPos'] = end_pos
        
        self.lane_area_detectors.append(detector)
        print(f"Added lane area detector '{detector_id}' on {edge_id}")
    
    def set_gui_option(self, option: str, value):
        """
        Set a GUI option.
        
        Args:
            option: Option name (e.g., 'start', 'quit-on-end')
            value: Option value
        """
        self.gui_settings[option] = value
    
    def set_seed(self, seed: int):
        """
        Set random seed for reproducibility.
        
        Args:
            seed: Random seed value
        """
        self.options['seed'] = seed
        print(f"Set random seed: {seed}")
    
    def _generate_additional_xml(self) -> str:
        """Generate additional file content (detectors)."""
        if not (self.induction_loops or self.lane_area_detectors or 
                self.multi_entry_exit_detectors):
            return None
        
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n\n'
        xml += '<additional xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        xml += 'xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/additional_file.xsd">\n\n'
        
        # Induction loops (E1 detectors)
        if self.induction_loops:
            for loop in self.induction_loops:
                attrs = [
                    f'id="{loop["id"]}"',
                    f'lane="{loop["lane"]}"',
                    f'pos="{loop["pos"]}"',
                    f'freq="{loop["freq"]}"',
                    f'file="{loop["file"]}"'
                ]
                xml += f'    <inductionLoop {" ".join(attrs)}/>\n'
            xml += '\n'
        
        # Lane area detectors (E2 detectors)
        if self.lane_area_detectors:
            for det in self.lane_area_detectors:
                attrs = [
                    f'id="{det["id"]}"',
                    f'lane="{det["lane"]}"',
                    f'pos="{det["pos"]}"',
                    f'freq="{det["freq"]}"',
                    f'file="{det["file"]}"'
                ]
                if 'endPos' in det:
                    attrs.append(f'endPos="{det["endPos"]}"')
                xml += f'    <laneAreaDetector {" ".join(attrs)}/>\n'
            xml += '\n'
        
        xml += '</additional>\n'
        return xml
    
    def save(self, output_file: str, save_additional: bool = True):
        """
        Save the configuration to a .sumocfg file.
        
        Args:
            output_file: Path to the output .sumocfg file
            save_additional: If True, also save detectors to .add.xml file
        """
        if not self.network_file:
            raise ValueError("Network file not set. Use set_network() first.")
        
        if not self.route_files:
            raise ValueError("No route files set. Use set_routes() first.")
        
        # Generate and save additional file if needed
        additional_xml = self._generate_additional_xml()
        if additional_xml and save_additional:
            add_file = output_file.replace('.sumocfg', '.add.xml')
            with open(add_file, 'w', encoding='utf-8') as f:
                f.write(additional_xml)
            self.add_additional_file(add_file)
            print(f"Saved additional file: {add_file}")
        
        # Build configuration XML
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n\n'
        xml += '<configuration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        xml += 'xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/sumoConfiguration.xsd">\n\n'
        
        # Input section
        xml += '    <input>\n'
        xml += f'        <net-file value="{self.network_file}"/>\n'
        xml += f'        <route-files value="{",".join(self.route_files)}"/>\n'
        if self.additional_files:
            xml += f'        <additional-files value="{",".join(self.additional_files)}"/>\n'
        xml += '    </input>\n\n'
        
        # Time section
        xml += '    <time>\n'
        xml += f'        <begin value="{self.begin}"/>\n'
        xml += f'        <end value="{self.end}"/>\n'
        xml += f'        <step-length value="{self.step_length}"/>\n'
        xml += '    </time>\n\n'
        
        # Processing section
        if self.options:
            xml += '    <processing>\n'
            for opt, val in self.options.items():
                xml += f'        <{opt} value="{val}"/>\n'
            xml += '    </processing>\n\n'
        
        # Routing section (for dynamic routing)
        if self.routing_options:
            xml += '    <routing>\n'
            for opt, val in self.routing_options.items():
                xml += f'        <{opt} value="{val}"/>\n'
            xml += '    </routing>\n\n'
        
        # Output section
        if self.outputs:
            xml += '    <output>\n'
            
            output_mapping = {
                'tripinfo': 'tripinfo-output',
                'summary': 'summary-output',
                'edgedata': 'edgedata-output',
                'lanedata': 'lanedata-output',
                'queue': 'queue-output',
                'emission': 'emission-output',
                'fcd': 'fcd-output',
                'full': 'full-output',
                'vtk': 'vtk-output',
                'netstate': 'netstate-dump',
            }
            
            for out_type, out_config in self.outputs.items():
                tag = output_mapping.get(out_type, f'{out_type}-output')
                xml += f'        <{tag} value="{out_config["file"]}"/>\n'
                
                # Add period if specified
                if 'period' in out_config:
                    xml += f'        <{tag.replace("-output", "")}.period value="{out_config["period"]}"/>\n'
            
            xml += '    </output>\n\n'
        
        # GUI section
        if self.gui_settings:
            xml += '    <gui_only>\n'
            for opt, val in self.gui_settings.items():
                val_str = str(val).lower() if isinstance(val, bool) else str(val)
                xml += f'        <{opt} value="{val_str}"/>\n'
            xml += '    </gui_only>\n\n'
        
        xml += '</configuration>\n'
        
        # Write configuration file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml)
        
        print(f"\nConfiguration saved to {output_file}")
        print(f"  Network: {self.network_file}")
        print(f"  Routes: {', '.join(self.route_files)}")
        print(f"  Time: {self.begin}s to {self.end}s (step: {self.step_length}s)")
        if self.routing_options:
            print(f"  Rerouting: enabled (period={self.routing_options.get('device.rerouting.period')}s)")
        if self.outputs:
            print(f"  Outputs: {', '.join(self.outputs.keys())}")
        
        print(f"\n  To run simulation:")
        print(f"      sumo -c {output_file}")
        print(f"      sumo-gui -c {output_file}  (with GUI)")
    
    def get_sumo_command(self, gui: bool = False) -> list:
        """
        Get the SUMO command to run this configuration.
        
        Args:
            gui: If True, use sumo-gui instead of sumo
            
        Returns:
            List of command arguments
        """
        binary = 'sumo-gui' if gui else 'sumo'
        return [binary, '-c', self.network_file.replace('.net.xml', '.sumocfg')]
    
    def clear_outputs(self):
        """Clear all output specifications."""
        self.outputs.clear()
        print("Cleared all outputs")
    
    def clear_detectors(self):
        """Clear all detector definitions."""
        self.induction_loops.clear()
        self.lane_area_detectors.clear()
        self.multi_entry_exit_detectors.clear()
        print("Cleared all detectors")


