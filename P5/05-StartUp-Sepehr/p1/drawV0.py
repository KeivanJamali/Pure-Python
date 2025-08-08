from pathlib import Path

class CodeWriter:
    def __init__(self, file_path):
        self.filepath = Path(file_path)
        self.lines = []

    def write_line(self, line):
        self.lines.append(line)

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            for line in self.lines:
                f.write(line + '\n')

class Page:
    def __init__(self, writer: CodeWriter, file_path_dwg):
        self.writer = writer
        self.writer.write_line(f"file_path = r'{file_path_dwg}'")
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

class Rectangular:
    def __init__(self, writer: CodeWriter, x, y, width, height, color=1):
        self.writer = writer
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.color = color

    def draw(self):
        x, y, w, h, c = self.x, self.y, self.w, self.h, self.color
        self.writer.write_line(f"# Drawing rectangle at ({x},{y}) w={w} h={h}")
        self.writer.write_line(f"p1 = APoint({x}, {y})")
        self.writer.write_line(f"p2 = APoint({x + w}, {y})")
        self.writer.write_line(f"p3 = APoint({x + w}, {y + h})")
        self.writer.write_line(f"p4 = APoint({x}, {y + h})")
        self.writer.write_line("entity = acad.model.AddLine(p1, p2)")
        self.writer.write_line(f"entity.Color = {c}")
        self.writer.write_line("entity = acad.model.AddLine(p2, p3)")
        self.writer.write_line(f"entity.Color = {c}")
        self.writer.write_line("entity = acad.model.AddLine(p3, p4)")
        self.writer.write_line(f"entity.Color = {c}")
        self.writer.write_line("entity = acad.model.AddLine(p4, p1)")
        self.writer.write_line(f"entity.Color = {c}")
        self.writer.write_line("")

class Wall:
    def __init__(self, writer, x, y, length, width, color=1):
        self.writer = writer
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.color = color

    def draw(self):
        x, y, l, w, c = self.x, self.y, self.length, self.width, self.color
        self.writer.write_line(f"# Wall at ({x},{y}), length={l}, width={w}")
        self.writer.write_line(f"p1 = APoint({x}, {y})")
        self.writer.write_line(f"p2 = APoint({x + l}, {y})")
        self.writer.write_line(f"p3 = APoint({x + l}, {y + w})")
        self.writer.write_line(f"p4 = APoint({x}, {y + w})")
        self.writer.write_line("entity = acad.model.AddLine(p1, p2)")
        self.writer.write_line(f"entity.Color = {c}")
        self.writer.write_line("entity = acad.model.AddLine(p2, p3)")
        self.writer.write_line(f"entity.Color = {c}")
        self.writer.write_line("entity = acad.model.AddLine(p3, p4)")
        self.writer.write_line(f"entity.Color = {c}")
        self.writer.write_line("entity = acad.model.AddLine(p4, p1)")
        self.writer.write_line(f"entity.Color = {c}")
        self.writer.write_line("")

class Line:
    def __init__(self, writer, x, y, length, angle_deg=0, color=2):
        self.writer = writer
        self.x = x
        self.y = y
        self.length = length
        self.angle_deg = angle_deg
        self.color = color

    def draw(self):
        from math import cos, sin, radians
        angle = radians(self.angle_deg)
        dx = self.length * cos(angle)
        dy = self.length * sin(angle)

        x1, y1 = self.x, self.y
        x2, y2 = x1 + dx, y1 + dy

        self.writer.write_line(f"# Line from ({x1},{y1}) to ({x2},{y2}), color={self.color}")
        self.writer.write_line(f"start = APoint({x1}, {y1})")
        self.writer.write_line(f"end = APoint({x2}, {y2})")
        self.writer.write_line("entity = acad.model.AddLine(start, end)")
        self.writer.write_line(f"entity.Color = {self.color}")
        self.writer.write_line("")

class Circle:
    def __init__(self, writer, x, y, radius, color=4):
        self.writer = writer
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        self.writer.write_line(f"# Circle at ({self.x},{self.y}), radius={self.radius}")
        self.writer.write_line(f"center = APoint({self.x}, {self.y})")
        self.writer.write_line(f"entity = acad.model.AddCircle(center, {self.radius})")
        self.writer.write_line(f"entity.Color = {self.color}")
        self.writer.write_line("")
