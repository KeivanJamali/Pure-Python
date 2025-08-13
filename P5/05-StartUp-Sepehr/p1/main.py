from drawV1 import *

writer = CodeWriter(r"/mnt/Data1/Python_Projects/Pure-Python/P5/05-StartUp-Sepehr/p1/generated_drawing.py")
page = Page(writer, file_name="output.dwg")

wall = Wall(writer, x=0, y=0, length=10, width=0.2, color=1)
line = Line(writer, x=0, y=0, length=5, angle_deg=45, color=2)
circle = Circle(writer, x=3, y=3, radius=1.5, color=2)
polyline = Polyline(writer, start=(0, 0), lengths=[5, 3, 4], angles=[90, -45], color=2, layer="PolylineLayer")
polywall = PolyWall(writer, start=(0, 0), lengths=[5, 4, 6], angles=[90, -45], width=0.3, color=1, layer="Walls")
box_wall = BoxWall(writer, x=0, y=0, length=10, width=6, wall_thickness=0.3, color=1, layer="Walls")

wall.draw()
line.draw()
circle.draw()
polyline.draw()
polywall.draw()
box_wall.draw()

page.finalize()
writer.save()

