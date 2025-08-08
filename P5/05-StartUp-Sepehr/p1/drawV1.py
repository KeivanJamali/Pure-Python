from pathlib import Path
import math

class CodeWriter:
    def __init__(self, file_path):
        self.filepath = Path(file_path)
        self.lines = []
        self.created_layers = set()

    def write_line(self, line):
        self.lines.append(line)

    def ensure_layer(self, layer_name):
        if layer_name not in self.created_layers:
            self.write_line(f"# Create or activate layer '{layer_name}'")
            self.write_line(f"try:")
            self.write_line(f"    layer = acad.doc.Layers.Item('{layer_name}')")
            self.write_line(f"except:")
            self.write_line(f"    layer = acad.doc.Layers.Add('{layer_name}')")
            self.write_line(f"acad.doc.ActiveLayer = layer")
            self.created_layers.add(layer_name)

    def save(self):
        with open(self.filepath, "w") as f:
            f.write("\n".join(self.lines))

class Page:
    def __init__(self, writer: CodeWriter, file_name):
        self.writer = writer
        self.writer.write_line("import os")
        self.writer.write_line(f"file_path = os.path.join(os.getcwd(), '{file_name}')")
        self.writer.write_line("from pyautocad import Autocad, APoint, aDouble")
        self.writer.write_line("acad = Autocad(create_if_not_exists=True)")
        self.writer.write_line("acad.app.Documents.Add()")
        self.writer.write_line("acad.app.Visible = True")
        self.writer.write_line("")

    def finalize(self):
        self.writer.write_line("try:")
        self.writer.write_line("    acad_doc = acad.app.ActiveDocument")
        self.writer.write_line("    acad_doc.SaveAs(file_path)")
        self.writer.write_line("    print(f'Drawing saved successfully at {file_path}')")
        self.writer.write_line("except Exception as e:")
        self.writer.write_line("    print(f'Error saving drawing: {e}')")


class Wall:
    def __init__(self, writer, x, y, length, width, color=1, layer="Walls"):
        self.writer = writer
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.color = color
        self.layer = layer

    def draw(self):
        self.writer.ensure_layer(self.layer)

        x, y, l, w, c = self.x, self.y, self.length, self.width, self.color
        self.writer.write_line(f"# Wall on layer '{self.layer}' at ({x},{y}), length={l}, width={w}")
        self.writer.write_line(f"p1 = APoint({x}, {y})")
        self.writer.write_line(f"p2 = APoint({x + l}, {y})")
        self.writer.write_line(f"p3 = APoint({x + l}, {y + w})")
        self.writer.write_line(f"p4 = APoint({x}, {y + w})")
        for i in range(1, 5):
            self.writer.write_line(f"entity = acad.model.AddLine(p{i}, p{(i % 4) + 1})")
            self.writer.write_line(f"entity.Layer = '{self.layer}'")
            self.writer.write_line(f"entity.Color = {c}")


class Line:
    def __init__(self, writer, x, y, length, angle_deg=0, color=2, layer="Lines"):
        self.writer = writer
        self.x = x
        self.y = y
        self.length = length
        self.angle_deg = angle_deg
        self.color = color
        self.layer = layer

    def draw(self):
        from math import cos, sin, radians
        self.writer.ensure_layer(self.layer)

        angle = radians(self.angle_deg)
        dx = self.length * cos(angle)
        dy = self.length * sin(angle)

        x1, y1 = self.x, self.y
        x2, y2 = x1 + dx, y1 + dy

        self.writer.write_line(f"# Line on layer '{self.layer}'")
        self.writer.write_line(f"start = APoint({x1}, {y1})")
        self.writer.write_line(f"end = APoint({x2}, {y2})")
        self.writer.write_line("entity = acad.model.AddLine(start, end)")
        self.writer.write_line(f"entity.Layer = '{self.layer}'")
        self.writer.write_line(f"entity.Color = {self.color}")


class Circle:
    def __init__(self, writer, x, y, radius, color=4, layer="Circles"):
        self.writer = writer
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.layer = layer

    def draw(self):
        self.writer.ensure_layer(self.layer)

        self.writer.write_line(f"# Circle on layer '{self.layer}' at ({self.x}, {self.y})")
        self.writer.write_line(f"center = APoint({self.x}, {self.y})")
        self.writer.write_line(f"entity = acad.model.AddCircle(center, {self.radius})")
        self.writer.write_line(f"entity.Layer = '{self.layer}'")
        self.writer.write_line(f"entity.Color = {self.color}")


class Polyline:
    def __init__(self, writer, start, lengths, angles, color=1, layer="Polylines"):
        """
        :param writer: CodeWriter object
        :param start: (x, y) tuple for starting point
        :param lengths: list of segment lengths
        :param angles: list of relative turning angles in degrees
        :param color: AutoCAD color
        :param layer: layer name
        """
        self.writer = writer
        self.start = start
        self.lengths = lengths
        self.angles = angles
        self.color = color
        self.layer = layer

    def _compute_points(self):
        points = [self.start]
        current_angle = 0
        current_point = self.start

        for i, length in enumerate(self.lengths):
            if i < len(self.angles):
                current_angle += self.angles[i]

            rad = math.radians(current_angle)
            x_new = current_point[0] + length * math.cos(rad)
            y_new = current_point[1] + length * math.sin(rad)
            current_point = (x_new, y_new)
            points.append(current_point)

        return points

    def draw(self):
        self.writer.ensure_layer(self.layer)

        points = self._compute_points()

        self.writer.write_line(f"# Polyline on layer '{self.layer}' from ({self.start[0]}, {self.start[1]})")
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            self.writer.write_line(f"p1 = APoint({x1}, {y1})")
            self.writer.write_line(f"p2 = APoint({x2}, {y2})")
            self.writer.write_line(f"entity = acad.model.AddLine(p1, p2)")
            self.writer.write_line(f"entity.Layer = '{self.layer}'")
            self.writer.write_line(f"entity.Color = {self.color}")

import math

class PolyWall:
    def __init__(self, writer, start, lengths, angles, width, color=1, layer="PolyWalls"):
        """
        :param writer: CodeWriter instance
        :param start: tuple (x, y) start point
        :param lengths: list of segment lengths
        :param angles: list of relative turning angles in degrees
        :param width: wall thickness (total width)
        :param color: AutoCAD color
        :param layer: layer name
        """
        self.writer = writer
        self.start = start
        self.lengths = lengths
        self.angles = angles
        self.width = width
        self.color = color
        self.layer = layer

    def draw(self):
        self.writer.ensure_layer(self.layer)

        center_points = self._compute_points()
        half_w = self.width / 2.0

        # Calculate offset points for each center point (left and right)
        offsets_left = []
        offsets_right = []

        # Calculate directions (angles) for each segment (needed for offsets)
        directions = self._compute_segment_angles(center_points)

        # For the first point, use direction of first segment
        # For the last point, use direction of last segment
        # For intermediate points, average direction of incoming and outgoing segment

        n = len(center_points)

        for i in range(n):
            if i == 0:
                angle = directions[0]
            elif i == n - 1:
                angle = directions[-1]
            else:
                # Average of previous and next segment angles
                angle = (directions[i - 1] + directions[i]) / 2

            # Offset vector perpendicular to angle (to left and right)
            perp_angle = angle + 90  # degrees
            rad = math.radians(perp_angle)

            cx, cy = center_points[i]
            dx = half_w * math.cos(rad)
            dy = half_w * math.sin(rad)

            offsets_left.append( (cx + dx, cy + dy) )
            offsets_right.append( (cx - dx, cy - dy) )

        # Draw wall as pairs of offset lines connected by polylines
        # Connect left offset points and right offset points

        self.writer.write_line(f"# PolyWall on layer '{self.layer}' with width {self.width}")
        # Draw left side polyline
        for i in range(n - 1):
            x1, y1 = offsets_left[i]
            x2, y2 = offsets_left[i + 1]
            self.writer.write_line(f"p1 = APoint({x1}, {y1})")
            self.writer.write_line(f"p2 = APoint({x2}, {y2})")
            self.writer.write_line(f"entity = acad.model.AddLine(p1, p2)")
            self.writer.write_line(f"entity.Layer = '{self.layer}'")
            self.writer.write_line(f"entity.Color = {self.color}")

        # Draw right side polyline
        for i in range(n - 1):
            x1, y1 = offsets_right[i]
            x2, y2 = offsets_right[i + 1]
            self.writer.write_line(f"p1 = APoint({x1}, {y1})")
            self.writer.write_line(f"p2 = APoint({x2}, {y2})")
            self.writer.write_line(f"entity = acad.model.AddLine(p1, p2)")
            self.writer.write_line(f"entity.Layer = '{self.layer}'")
            self.writer.write_line(f"entity.Color = {self.color}")

        # Connect ends (start cap)
        x1, y1 = offsets_left[0]
        x2, y2 = offsets_right[0]
        self.writer.write_line(f"p1 = APoint({x1}, {y1})")
        self.writer.write_line(f"p2 = APoint({x2}, {y2})")
        self.writer.write_line(f"entity = acad.model.AddLine(p1, p2)")
        self.writer.write_line(f"entity.Layer = '{self.layer}'")
        self.writer.write_line(f"entity.Color = {self.color}")

        # Connect ends (end cap)
        x1, y1 = offsets_left[-1]
        x2, y2 = offsets_right[-1]
        self.writer.write_line(f"p1 = APoint({x1}, {y1})")
        self.writer.write_line(f"p2 = APoint({x2}, {y2})")
        self.writer.write_line(f"entity = acad.model.AddLine(p1, p2)")
        self.writer.write_line(f"entity.Layer = '{self.layer}'")
        self.writer.write_line(f"entity.Color = {self.color}")

    def _compute_points(self):
        points = [self.start]
        current_angle = 0
        current_point = self.start
        for i, length in enumerate(self.lengths):
            if i < len(self.angles):
                current_angle += self.angles[i]
            rad = math.radians(current_angle)
            x_new = current_point[0] + length * math.cos(rad)
            y_new = current_point[1] + length * math.sin(rad)
            current_point = (x_new, y_new)
            points.append(current_point)
        return points

    def _compute_segment_angles(self, points):
        """Compute angle (deg) of each segment from point i to i+1."""
        angles = []
        for i in range(len(points)-1):
            dx = points[i+1][0] - points[i][0]
            dy = points[i+1][1] - points[i][1]
            angle = math.degrees(math.atan2(dy, dx))
            angles.append(angle)
        return angles


class BoxWall:
    def __init__(self, writer, x, y, length, width, wall_thickness, color=1, layer="BoxWalls"):
        """
        :param writer: CodeWriter instance
        :param x, y: bottom-left corner of outer rectangle
        :param length: outer rectangle length (X direction)
        :param width: outer rectangle width (Y direction)
        :param wall_thickness: thickness of the wall (offset inward)
        :param color: AutoCAD color number
        :param layer: layer name
        """
        self.writer = writer
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.wall_thickness = wall_thickness
        self.color = color
        self.layer = layer

    def draw(self):
        self.writer.ensure_layer(self.layer)
        
        ox, oy = self.x, self.y
        l, w = self.length, self.width
        t = self.wall_thickness
        
        # Outer rectangle points (clockwise)
        outer_pts = [
            (ox, oy),
            (ox + l, oy),
            (ox + l, oy + w),
            (ox, oy + w)
        ]
        
        # Inner rectangle points (offset inward by wall_thickness)
        inner_pts = [
            (ox + t, oy + t),
            (ox + l - t, oy + t),
            (ox + l - t, oy + w - t),
            (ox + t, oy + w - t)
        ]
        
        # Helper to draw polyline from points list (closed)
        def draw_polyline(points):
            n = len(points)
            for i in range(n):
                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % n]
                self.writer.write_line(f"p1 = APoint({x1}, {y1})")
                self.writer.write_line(f"p2 = APoint({x2}, {y2})")
                self.writer.write_line(f"entity = acad.model.AddLine(p1, p2)")
                self.writer.write_line(f"entity.Layer = '{self.layer}'")
                self.writer.write_line(f"entity.Color = {self.color}")
        
        self.writer.write_line(f"# Drawing outer rectangle of BoxWall on layer '{self.layer}'")
        draw_polyline(outer_pts)
        
        self.writer.write_line(f"# Drawing inner rectangle (offset) of BoxWall on layer '{self.layer}'")
        draw_polyline(inner_pts)
        
        # Draw connecting lines between outer and inner rectangles at corners to form the thick walls
        for i in range(4):
            x_out, y_out = outer_pts[i]
            x_in, y_in = inner_pts[i]
            self.writer.write_line(f"p1 = APoint({x_out}, {y_out})")
            self.writer.write_line(f"p2 = APoint({x_in}, {y_in})")
            self.writer.write_line(f"entity = acad.model.AddLine(p1, p2)")
            self.writer.write_line(f"entity.Layer = '{self.layer}'")
            self.writer.write_line(f"entity.Color = {self.color}")
