import os
file_path = os.path.join(os.getcwd(), 'output.dwg')
from pyautocad import Autocad, APoint, aDouble
acad = Autocad(create_if_not_exists=True)
acad.app.Documents.Add()
acad.app.Visible = True

# Create or activate layer 'Walls'
try:
    layer = acad.doc.Layers.Item('Walls')
except:
    layer = acad.doc.Layers.Add('Walls')
acad.doc.ActiveLayer = layer
# Wall on layer 'Walls' at (0,0), length=10, width=0.2
p1 = APoint(0, 0)
p2 = APoint(10, 0)
p3 = APoint(10, 0.2)
p4 = APoint(0, 0.2)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
entity = acad.model.AddLine(p2, p3)
entity.Layer = 'Walls'
entity.Color = 1
entity = acad.model.AddLine(p3, p4)
entity.Layer = 'Walls'
entity.Color = 1
entity = acad.model.AddLine(p4, p1)
entity.Layer = 'Walls'
entity.Color = 1
# Create or activate layer 'Lines'
try:
    layer = acad.doc.Layers.Item('Lines')
except:
    layer = acad.doc.Layers.Add('Lines')
acad.doc.ActiveLayer = layer
# Line on layer 'Lines'
start = APoint(0, 0)
end = APoint(3.5355339059327378, 3.5355339059327373)
entity = acad.model.AddLine(start, end)
entity.Layer = 'Lines'
entity.Color = 2
# Create or activate layer 'Circles'
try:
    layer = acad.doc.Layers.Item('Circles')
except:
    layer = acad.doc.Layers.Add('Circles')
acad.doc.ActiveLayer = layer
# Circle on layer 'Circles' at (3, 3)
center = APoint(3, 3)
entity = acad.model.AddCircle(center, 1.5)
entity.Layer = 'Circles'
entity.Color = 4
# Create or activate layer 'PolylineLayer'
try:
    layer = acad.doc.Layers.Item('PolylineLayer')
except:
    layer = acad.doc.Layers.Add('PolylineLayer')
acad.doc.ActiveLayer = layer
# Polyline on layer 'PolylineLayer' from (0, 0)
p1 = APoint(0, 0)
p2 = APoint(3.061616997868383e-16, 5.0)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'PolylineLayer'
entity.Color = 2
p1 = APoint(3.061616997868383e-16, 5.0)
p2 = APoint(2.1213203435596433, 7.121320343559642)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'PolylineLayer'
entity.Color = 2
p1 = APoint(2.1213203435596433, 7.121320343559642)
p2 = APoint(4.949747468305834, 9.949747468305832)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'PolylineLayer'
entity.Color = 2
# PolyWall on layer 'Walls' with width 0.3
p1 = APoint(-0.15, 1.8369701987210297e-17)
p2 = APoint(-0.1385819298766927, 5.057402514854764)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(-0.1385819298766927, 5.057402514854764)
p2 = APoint(2.722361107568209, 7.934493141924172)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(2.722361107568209, 7.934493141924172)
p2 = APoint(6.9650017946874945, 12.177133829043457)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(0.15, -1.8369701987210297e-17)
p2 = APoint(0.13858192987669332, 4.942597485145236)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(0.13858192987669332, 4.942597485145236)
p2 = APoint(2.9344931419241727, 7.722361107568208)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(2.9344931419241727, 7.722361107568208)
p2 = APoint(7.177133829043458, 11.965001794687494)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(-0.15, 1.8369701987210297e-17)
p2 = APoint(0.15, -1.8369701987210297e-17)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(6.9650017946874945, 12.177133829043457)
p2 = APoint(7.177133829043458, 11.965001794687494)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
# Drawing outer rectangle of BoxWall on layer 'Walls'
p1 = APoint(0, 0)
p2 = APoint(10, 0)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(10, 0)
p2 = APoint(10, 6)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(10, 6)
p2 = APoint(0, 6)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(0, 6)
p2 = APoint(0, 0)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
# Drawing inner rectangle (offset) of BoxWall on layer 'Walls'
p1 = APoint(0.3, 0.3)
p2 = APoint(9.7, 0.3)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(9.7, 0.3)
p2 = APoint(9.7, 5.7)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(9.7, 5.7)
p2 = APoint(0.3, 5.7)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(0.3, 5.7)
p2 = APoint(0.3, 0.3)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(0, 0)
p2 = APoint(0.3, 0.3)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(10, 0)
p2 = APoint(9.7, 0.3)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(10, 6)
p2 = APoint(9.7, 5.7)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
p1 = APoint(0, 6)
p2 = APoint(0.3, 5.7)
entity = acad.model.AddLine(p1, p2)
entity.Layer = 'Walls'
entity.Color = 1
try:
    acad_doc = acad.app.ActiveDocument
    acad_doc.SaveAs(file_path)
    print(f'Drawing saved successfully at {file_path}')
except Exception as e:
    print(f'Error saving drawing: {e}')