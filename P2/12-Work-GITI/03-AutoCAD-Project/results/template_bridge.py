file_path = r'D:\All Python\Pure-Python\P2\12-Work-GITI\03-AutoCAD-Project\results\bridge.dwg'
from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)
acad.app.Visible = True

entity = acad.model.AddLine(APoint(48.57301469314007, 263.4562252688308, 0.0), APoint(90.54474411659521, 263.4562252688308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.59253581200028, 263.4562252688308, 0.0), APoint(105.07301469314325, 263.4562252688308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 261.9562252688308, 0.0), APoint(90.54474411659521, 261.9562252688308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.59253581200119, 261.95622526883074, 0.0), APoint(106.57301469314007, 261.95622526883074, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 259.95622526883096, 0.0), APoint(90.54474411659521, 259.95622526883096, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.59253581200028, 259.9562252688311, 0.0), APoint(106.57301469313916, 259.95622526883096, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 237.9562252688308, 0.0), APoint(90.54474411659521, 237.95622526883074, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.59253581200028, 237.9562252688308, 0.0), APoint(106.57301469313916, 237.9562252688308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.07301469314325, 260.82225067261277, 0.0), APoint(105.07301469314325, 237.09019986504836, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.82301469314143, 259.8118877015322, 0.0), APoint(106.82301469314325, 238.10056283613028, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 259.95622526883096, 0.0), APoint(106.57301469313916, 237.9562252688308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 234.45622526883056, 0.0), APoint(90.54474411659521, 234.45622526883056, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.59253581200028, 234.45622526883056, 0.0), APoint(105.07301469314325, 234.45622526883056, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 235.95622526883056, 0.0), APoint(90.54474411659521, 235.95622526883056, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.59253581200028, 235.95622526883056, 0.0), APoint(106.57301469313916, 235.95622526883056, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313734, 263.4562252688308, 0.0), APoint(105.07301469314325, 263.4562252688308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 234.45622526883056, 0.0), APoint(105.07301469314325, 234.45622526883056, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.82301469314325, 259.81188770153204, 0.0), APoint(136.8230146931419, 277.1323957772193, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 259.9562252688317, 0.0), APoint(136.69801469314143, 277.34890212816845, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.07301469314325, 260.82225067261277, 0.0), APoint(136.8230146931419, 279.1531217193817, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 269.31220714904, 0.0), APoint(136.8230146931419, 281.75119793073543, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313825, 262.5543014801787, 0.0), APoint(136.8230146931419, 280.0191471231685, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(136.8230146931419, 277.1323957772193, 0.0), APoint(136.8230146931419, 281.75119793073543, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313825, 263.4562252688308, 0.0), APoint(106.57301469313916, 269.31220714904, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.82301469314325, 238.10056283613028, 0.0), APoint(136.8230146931419, 220.78005476044302, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 237.9562252688308, 0.0), APoint(136.69801469314143, 220.56354840949382, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.07301469314325, 237.09019986504836, 0.0), APoint(136.8230146931419, 218.7593288182792, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 228.60024338862246, 0.0), APoint(136.8230146931419, 216.16125260692718, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 235.3581490574844, 0.0), APoint(136.8230146931419, 217.89330341449397, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(136.8230146931419, 220.78005476044302, 0.0), APoint(136.8230146931419, 216.16125260692718, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.07301469313916, 260.82225067261606, 0.0), APoint(50.07301469313916, 237.0901998650453, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.32301469313916, 259.81188770153506, 0.0), APoint(48.32301469313916, 238.10056283612835, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 259.9562252688317, 0.0), APoint(48.57301469313916, 237.9562252688297, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 259.9562252688317, 0.0), APoint(18.323014693139157, 277.42107091181833, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.07301469313916, 260.82225067261606, 0.0), APoint(18.323014693139157, 279.1531217193868, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.32301469313916, 259.81188770153506, 0.0), APoint(18.323014693139157, 277.1323957772245, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 269.60088228363895, 0.0), APoint(18.323014693139157, 282.0398730653344, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469314325, 262.8429766147778, 0.0), APoint(18.323014693139157, 280.30782225776755, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(18.323014693139157, 277.1323957772245, 0.0), APoint(18.323014693139157, 282.0398730653344, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 261.6882760764006, 0.0), APoint(48.57301469313916, 269.60088228363895, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 237.9562252688297, 0.0), APoint(18.323014693139157, 220.4913796258429, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.07301469313916, 237.0901998650453, 0.0), APoint(18.323014693139157, 218.75932881827396, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.32301469313916, 238.10056283612835, 0.0), APoint(18.323014693139157, 220.78005476043882, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 228.3115682540224, 0.0), APoint(18.323014693139157, 215.87257747232707, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469314325, 235.0694739228838, 0.0), APoint(18.323014693139157, 217.60462827989386, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(18.323014693139157, 220.78005476043882, 0.0), APoint(18.323014693139157, 215.87257747232707, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.5151660952879, 187.5319763098174, 0.0), APoint(206.76516609528153, 187.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.76516609528153, 187.5319763098174, 0.0), APoint(206.76516609528153, 184.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.22685953151813, 187.5319763098174, 0.0), APoint(207.22685953151813, 184.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.76516609528153, 184.5319763098174, 0.0), APoint(209.7651660952879, 184.5319763098174, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253149082, 160.15697630981742, 0.0), APoint(216.76816253148354, 160.15697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253148354, 152.65697630981742, 0.0), APoint(216.76816253148354, 152.65697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 184.5319763098174, 0.0), APoint(209.7651660952879, 182.28197630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 182.28197630981742, 0.0), APoint(204.5151660952879, 182.28197630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.5151660952879, 182.28197630981742, 0.0), APoint(204.5151660952879, 187.53197630981757, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 182.28197630981742, 0.0), APoint(209.7651660952879, 160.15697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.76816253149082, 160.15697630981742, 0.0), APoint(216.76816253148354, 152.65697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253149082, 160.15697630981742, 0.0), APoint(194.26816253148354, 152.65697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.5151660952879, 182.28197630981742, 0.0), APoint(196.26516609529153, 160.15697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.01516609527698, 187.5319763098174, 0.0), APoint(242.76516609528426, 187.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.76516609528426, 187.5319763098174, 0.0), APoint(242.76516609528426, 184.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.76516609528426, 184.5319763098174, 0.0), APoint(239.7651660952797, 184.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.7651660952797, 184.5319763098174, 0.0), APoint(239.7651660952797, 182.28197630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.7651660952797, 182.28197630981742, 0.0), APoint(245.01516609527698, 182.28197630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.01516609527698, 182.28197630981742, 0.0), APoint(245.01516609527698, 187.53197630981757, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.76516609528426, 184.5319763098174, 0.0), APoint(242.76516609528426, 187.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.91516609528662, 184.5319763098174, 0.0), APoint(242.76516609528426, 184.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.22685953151813, 187.5319763098174, 0.0), APoint(242.30347265904948, 187.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.22685953151813, 187.5319763098174, 0.0), APoint(242.30347265904948, 187.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.76516609528426, 187.5319763098174, 0.0), APoint(242.76516609528426, 184.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.76516609528426, 184.5319763098174, 0.0), APoint(206.91516609528662, 184.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.22685953151813, 184.5319763098174, 0.0), APoint(207.22685953151813, 187.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 78.25226789047554, 0.0), APoint(89.70644040441721, 78.80815197294567, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 78.81862988989963, 0.0), APoint(121.1180321574152, 79.12226789047577, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 85.75264288110077, 0.0), APoint(89.70644040441721, 86.30852696357101, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 86.31900488052497, 0.0), APoint(121.11803215741656, 86.62264288110111, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157408834, 110.12886160063374, 0.0), APoint(89.70644040441721, 110.68474568310398, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 110.69522360005806, 0.0), APoint(121.1180321574152, 110.99886160063397, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.368032157416565, 113.15151159688412, 0.0), APoint(89.70644040441721, 113.6848956793541, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 113.69537359630817, 0.0), APoint(118.8680321574152, 113.97651159688405, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(119.01803215741347, 115.87401159688386, 0.0), APoint(121.34303215741375, 115.87401159688409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.4930321574193, 115.72401159688468, 0.0), APoint(121.4930321574193, 113.99901159688386, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.4930321574193, 113.99901159688386, 0.0), APoint(121.3838214781963, 113.99901159688386, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.22724283664729, 113.99901159688386, 0.0), APoint(121.1180321574152, 113.99901159688386, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(119.01803215741984, 115.87401159688386, 0.0), APoint(118.8680321574152, 115.72401159688377, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.34303215741375, 115.87401159688386, 0.0), APoint(121.4930321574193, 115.72401159688377, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(121.3055321574193, 113.99901159688386, 0.0), 0.0782893207747293, 0.0, 3.141592653589793)


entity = acad.model.AddLine(APoint(118.8680321574152, 115.72401159688377, 0.0), APoint(118.8680321574152, 113.97651159688405, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 110.12886160063374, 0.0), APoint(89.70644040441721, 110.68474568310387, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 110.69522360005806, 0.0), APoint(121.1180321574152, 110.99886160063386, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.11803215741656, 86.62264288110111, 0.0), APoint(121.1180321574152, 110.99886160063386, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.21803215741829, 114.97401159688354, 0.0), APoint(33.89303215741802, 114.97401159688377, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.74303215741338, 114.82401159688436, 0.0), APoint(33.74303215741338, 113.09901159688354, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.74303215741338, 113.09901159688354, 0.0), APoint(33.85224283663638, 113.09901159688354, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.00882147818538, 113.09901159688354, 0.0), APoint(34.118032157416565, 113.09901159688354, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.21803215741147, 114.97401159688354, 0.0), APoint(36.368032157416565, 114.82401159688368, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.89303215741802, 114.97401159688354, 0.0), APoint(33.74303215741338, 114.82401159688368, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(33.93053215741338, 113.09901159688354, 0.0), 0.0782893207747293, 0.0, 3.141592653589793)


entity = acad.model.AddLine(APoint(36.368032157416565, 114.82401159688368, 0.0), APoint(36.368032157416565, 113.15151159688412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 85.75264288110066, 0.0), APoint(34.118032157416565, 110.12886160063374, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 108.71971684538187, 0.0), APoint(90.75423209982318, 108.42587361901803, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.70644040441721, 108.4157336993851, 0.0), APoint(34.118032157416565, 107.87778136151076, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193883, 271.07613347407926, 0.0), APoint(220.7914799918599, 271.07613347407937, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 267.82613347407926, 0.0), APoint(198.74147999193156, 266.32613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 266.32613347407926, 0.0), APoint(198.74147999193156, 251.2277000613184, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 256.57613347407926, 0.0), APoint(183.24147999193428, 251.57613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 267.82613347407926, 0.0), APoint(220.74147999192974, 267.82613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 269.82613347407926, 0.0), APoint(220.74147999192974, 269.82613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 269.82613347407926, 0.0), APoint(220.74147999192974, 269.82613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 267.82613347407926, 0.0), APoint(198.74147999193156, 267.82613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 251.57613347407926, 0.0), APoint(178.24147999193428, 251.57613347407926, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 256.57613347407926, 0.0), APoint(181.7792158409893, 256.57613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 271.07613347407926, 0.0), APoint(183.24147999193428, 257.82613347408153, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.7792158409893, 256.57613347407926, 0.0), APoint(178.24147999193428, 251.57613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 256.57613347407926, 0.0), APoint(183.24147999193428, 257.8261334740811, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 257.8261334740814, 0.0), APoint(181.7792158409893, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.7792158409893, 256.57613347407926, 0.0), APoint(181.7792158409893, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 267.82613347407926, 0.0), APoint(198.74147999193156, 271.07613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(197.27921584098476, 271.07613347407926, 0.0), APoint(181.7792158409893, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(197.27921584098476, 271.07613347407926, 0.0), APoint(198.74147999193156, 271.07613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(178.24147999193428, 251.57613347407926, 0.0), APoint(172.9335499324834, 252.0113579716691, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 251.57613347407926, 0.0), APoint(189.44101312293787, 251.0539502832964, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(189.44101312293787, 251.0539502832964, 0.0), APoint(200.64822693209408, 251.26332159110427, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.64822693209408, 251.26332159110427, 0.0), APoint(211.42529451850987, 250.90293511902672, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(211.42529451850987, 250.90293511902672, 0.0), APoint(216.04158886143887, 251.6893309586859, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.04158886143887, 251.6893309586859, 0.0), APoint(225.291479991929, 251.57613347407926, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.291479991929, 251.57613347407926, 0.0), APoint(232.56690786543004, 251.26241485750245, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 267.82613347407937, 0.0), APoint(220.7914799918617, 266.32613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 266.32613347407926, 0.0), APoint(220.7914799918617, 251.2277000613185, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.29147999186353, 256.57613347407937, 0.0), APoint(236.29147999186353, 251.57613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.29147999186353, 251.57613347407926, 0.0), APoint(241.2914799918617, 251.57613347407926, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.29147999186353, 256.57613347407937, 0.0), APoint(237.7537441428085, 256.57613347407937, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 271.07613347407937, 0.0), APoint(236.29147999186353, 257.82613347408153, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.7537441428085, 256.57613347407937, 0.0), APoint(241.2914799918617, 251.57613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.29147999186353, 256.57613347407937, 0.0), APoint(236.29147999186353, 257.8261334740812, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.29147999186353, 257.8261334740814, 0.0), APoint(237.7537441428085, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.7537441428085, 256.57613347407937, 0.0), APoint(237.7537441428085, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 267.82613347407937, 0.0), APoint(220.7914799918617, 271.07613347407937, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.25374414281123, 271.07613347407937, 0.0), APoint(237.7537441428085, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.25374414281123, 271.07613347407937, 0.0), APoint(220.7914799918617, 271.07613347407937, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(241.2914799918617, 251.57613347407926, 0.0), APoint(244.93365816394817, 251.94849062386737, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.29147999186353, 251.57613347407926, 0.0), APoint(232.56690786543004, 251.26241485750245, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(314.64631940552044, 167.20713884488202, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(322.796013843059, 157.32354167787787, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(322.796013843059, 153.25304271766697, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(310.80319464512104, 167.20713884488202, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(310.75537976149553, 153.26025861831738, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(314.7388572787886, 153.22469161923607, 0.0), 0.2400000000008731)


entity = acad.model.AddLine(APoint(321.2636823923194, 155.33439162244179, 0.0), APoint(312.7261675199061, 155.33439162244156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(312.7355260958093, 165.90492344512825, 0.0), APoint(312.7261675199061, 155.33439162244156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(316.1013226850464, 155.33439162244156, 0.0), APoint(314.7388572787886, 153.22469161923607, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.75537976149553, 153.26025861831738, 0.0), APoint(312.7261675199061, 155.33439162244156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.75537976149553, 157.40852462656574, 0.0), APoint(312.7261675199061, 155.33439162244156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.64631940552044, 167.20713884488202, 0.0), APoint(312.7355260958093, 165.9194381904282, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.8031946451365, 167.20713884487998, 0.0), APoint(312.7355260958093, 165.90492344512825, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.834470150754, 153.2141591936478, 0.0), APoint(321.2636823923194, 155.33439162244179, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.834470150754, 157.3624252018966, 0.0), APoint(321.2636823923194, 155.33439162244179, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.7320544214044, 157.35339904307227, 0.0), APoint(316.1013226850464, 155.33439162244156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.7150066166423, 167.35530916141272, 0.0), APoint(354.7150066166423, 170.68733661708382, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.11500661664286, 167.35530916141272, 0.0), APoint(367.11500661664286, 170.68733661708382, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.11500661664286, 170.68733661708518, 0.0), APoint(354.7150066166423, 170.68733661708382, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(354.7150066166423, 166.7897244155348, 0.0), 0.5655847458779121)
entity.Color = 8

entity = acad.model.AddCircle(APoint(367.11500661664286, 166.7897244155348, 0.0), 0.5655847458779121)
entity.Color = 8

entity = acad.model.AddLine(APoint(360.91500661664304, 167.35530916141272, 0.0), APoint(360.91500661664304, 170.68733661708382, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(360.91500661664304, 166.7897244155348, 0.0), 0.5655847458779121)
entity.Color = 8

entity = acad.model.AddLine(APoint(403.4582339857425, 158.26864768713415, 0.0), APoint(395.6582339857541, 158.26864768713415, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.02616751966616, 161.26864768713403, 0.0), APoint(317.02616751966616, 166.66864768713413, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(317.6261675196665, 166.66864768713413, 0.0), 0.6, 1.5707963267948966, 3.141592653589793)


entity = acad.model.AddLine(APoint(317.6261675196665, 167.26864768713403, 0.0), APoint(324.1261675197011, 167.26864768713403, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(324.1261675197011, 167.26864768713403, 0.0), APoint(332.1261675197002, 159.26864768713403, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(332.1261675197002, 159.26864768713403, 0.0), APoint(377.74293745552313, 159.26864768713403, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.28893645538756, 159.26864768713403, 0.0), APoint(401.8582339857139, 159.26864768713403, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(401.8582339857139, 159.86864768713417, 0.0), 0.6, 4.71238898038469, 0.0)


entity = acad.model.AddLine(APoint(402.4582339857143, 159.86864768713417, 0.0), APoint(402.4582339857143, 165.2686476871337, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2587412368357, 161.2544124097535, 0.0), APoint(402.2587412368357, 166.6544124097536, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.65874123683625, 167.2544124097535, 0.0), APoint(395.1587412368008, 167.2544124097535, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(401.65874123683625, 166.6544124097536, 0.0), 0.6, 0.0, 1.5707963267948966)


entity = acad.model.AddLine(APoint(395.1587412368008, 167.2544124097535, 0.0), APoint(387.1587412368008, 159.2544124097535, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(387.1587412368008, 159.2544124097535, 0.0), APoint(379.0894437064517, 159.2544124097535, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(340.9073363251282, 159.26864768713403, 0.0), APoint(318.33803879480365, 159.26864768713403, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(318.33803879480365, 159.86864768713417, 0.0), 0.6, 3.141592653589793, 4.71238898038469)


entity = acad.model.AddLine(APoint(317.73803879480056, 159.86864768713417, 0.0), APoint(317.73803879480056, 165.2686476871337, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.658233985715, 163.86864768713406, 0.0), APoint(402.65823398576595, 166.668647687124, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(402.0582339857656, 166.66864768713492, 0.0), 0.5999999999994543, 6.283185307161396, 1.5707963267935323)


entity = acad.model.AddLine(APoint(402.0582339857674, 167.26864768713403, 0.0), APoint(379.4889364553883, 167.26864768713403, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 167.26864768713403, 0.0), APoint(317.6261675196665, 167.26864768713403, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(317.6261675196647, 166.66864768713492, 0.0), 0.599999999999227, 1.5707963267962606, 3.14159265359093)


entity = acad.model.AddLine(APoint(317.02616751966616, 166.66864768713413, 0.0), APoint(317.02616751966616, 163.86864768713406, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(317.6261675196665, 166.66864768713413, 0.0), 0.6, 1.5707963267948966, 3.141592653589793)


entity = acad.model.AddCircle(APoint(310.75537976149553, 157.40852462656574, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(317.5150066166425, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(317.5150066166425, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(323.7150066166414, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(323.7150066166414, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(329.91500661664213, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(329.91500661664213, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(336.1150066166447, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(336.1150066166447, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(342.31500661664086, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(342.31500661664086, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(348.5150066166416, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(348.5150066166416, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(354.7150066166423, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(354.7150066166423, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(360.91500661664304, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(360.91500661664304, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(367.11500661664286, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(367.11500661664286, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(373.31500661663995, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(373.31500661663995, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(382.2856780686916, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(382.2856780686916, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(388.4856780686923, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(388.4856780686923, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(394.6856780686885, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(395.37856458876377, 166.7897244155348, 0.0), 0.2400000000008731)
entity.Color = 6

# Entity type AcDbHatch not supported
entity = acad.model.AddCircle(APoint(401.7838163513725, 159.03761135205525, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(401.7838163513725, 166.7897244155348, 0.0), 0.2400000000008731)


entity = acad.model.AddLine(APoint(354.7140853435503, 158.47202735650228, 0.0), APoint(354.70865785056776, 155.14000432121804, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.11406889326736, 158.45182916969645, 0.0), APoint(367.1086414002848, 155.11980613441222, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.1086414002848, 155.11980613441074, 0.0), APoint(354.70865785056776, 155.14000432121804, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(354.7150066166423, 159.03761135205525, 0.0), 0.565584745877912)
entity.Color = 8

entity = acad.model.AddCircle(APoint(367.11499016636117, 159.0174131652493, 0.0), 0.565584745877912)
entity.Color = 8

entity = acad.model.AddLine(APoint(360.9140771184093, 158.46192826309925, 0.0), APoint(360.9086496254258, 155.12990522781513, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(360.9149983915004, 159.02751225865222, 0.0), 0.565584745877912)
entity.Color = 8

entity = acad.model.AddCircle(APoint(314.7285135327602, 157.39616150064285, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(314.7416946106432, 172.3563675280767, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(407.0766872945851, 172.85741139590584, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(331.607455822691, 175.96047677108743, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(377.0420859249216, 176.77828219111314, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(377.12076349070503, 151.0357257410517, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(335.9973867618246, 146.66930720233722, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(339.0616685778068, 151.57548915728933, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddText('جزئیات الف', APoint(367.00271501205725, 86.06149801674223, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(365.2774942144706, 84.91000833305111, 0.0), APoint(381.04577019479893, 84.91000833305111, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(365.2774942144706, 84.33930054784616, 0.0), APoint(381.04577019479893, 84.33930054784616, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(375.95850206621253, 104.94896588874394, 0.0), APoint(384.64768482943873, 105.0358577163762, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9585020662089, 97.35859089811856, 0.0), APoint(384.7226810797192, 97.53623268825356, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9585020662107, 97.35859089811856, 0.0), APoint(366.9585020662107, 104.85896588874402, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(368.4585020662107, 98.01290488447819, 0.0), APoint(368.4585020662107, 104.01942365151842, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(368.05850206621017, 104.01942365151842, 0.0), 0.4, 0.0, 0.6959394611362612)


entity = acad.model.AddLine(APoint(365.4585020662107, 104.85896588874402, 0.0), APoint(365.4585020662107, 111.75896588874241, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9585020662107, 106.10521716137089, 0.0), APoint(366.9585020662107, 110.45896588874393, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(367.3585020662131, 110.45896588874393, 0.0), 0.4, 1.5707963267948966, 3.141592653589793)


entity = acad.model.AddLine(APoint(375.95850206621253, 104.94896588874394, 0.0), APoint(375.95850206621253, 111.75896588874343, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(374.4585020662107, 98.16791901740726, 0.0), APoint(374.4585020662107, 110.45896588874393, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(374.05850206621017, 110.45896588874393, 0.0), 0.4, 0.0, 1.5707963267948966)


entity = acad.model.AddLine(APoint(366.0585020662138, 112.35896588874402, 0.0), APoint(375.35850206620944, 112.35896588874402, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.3585020662131, 110.85896588874402, 0.0), APoint(374.05850206621017, 110.85896588874402, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(365.4585020662107, 104.85896588874402, 0.0), APoint(365.94789833114464, 104.85896588874402, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.46910580127496, 104.85896588874402, 0.0), APoint(366.9585020662107, 104.85896588874402, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(366.2085020662107, 104.85896588874402, 0.0), 0.2606037350650894, 0.0, 3.141592653589793)


entity = acad.model.AddLine(APoint(365.4585020662107, 111.75896588874377, 0.0), APoint(366.05850206621017, 112.35896588874402, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(375.95850206621253, 111.75896588874377, 0.0), APoint(375.35850206620944, 112.35896588874402, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(384.64768482943873, 106.32982817505865, 0.0), APoint(384.64768482943873, 101.5024366066317, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(384.64768482943873, 99.4142676326145, 0.0), APoint(384.64768482943873, 95.83815506042617, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(384.6638488495955, 100.880704796813, 0.0), 0.6219418934983878, 0.0, 3.141592653589793)
entity.Color = 7

entity = acad.model.AddLine(APoint(384.04190695609395, 100.880704796813, 0.0), APoint(385.2857907430898, 100.03599944243342, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(384.66668960935294, 100.02838945928693, 0.0), 0.6219418934983878, 3.1415926535897474, 4.5698335692637634e-14)
entity.Color = 7

entity = acad.model.AddLine(APoint(367.0515213679273, 105.8487744759982, 0.0), APoint(368.36548276449685, 104.27586633689077, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(367.3585020662131, 106.10521716137089, 0.0), 0.4, 3.1415926535895657, 3.837532114726054)


# Entity type AcDbHatch not supported
entity = acad.model.AddCircle(APoint(373.99940696184785, 110.37726563290869, 0.0), 0.408)


# Entity type AcDbHatch not supported
entity = acad.model.AddCircle(APoint(367.43556086302306, 110.34181237625353, 0.0), 0.408)


# Entity type AcDbHatch not supported
entity = acad.model.AddCircle(APoint(367.3968245929773, 106.16412324782596, 0.0), 0.408)


entity = acad.model.AddCircle(APoint(357.5211036223309, 93.30570029709827, 0.0), 1.875)
entity.Color = 8

entity = acad.model.AddLine(APoint(373.99940696184785, 110.37726563290869, 0.0), APoint(367.3968245929773, 106.16412324782596, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.43556086302306, 110.34181237625353, 0.0), APoint(370.69811577741166, 108.27069444036727, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(370.69811577741166, 108.27069444036727, 0.0), APoint(384.5608158476234, 108.27069444036727, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(385.8733158476234, 108.27069444036727, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddLine(APoint(172.93354993248067, 274.38323435707656, 0.0), APoint(220.7914799918617, 274.38323435707673, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 274.3832343570768, 0.0), APoint(244.93365816394817, 274.38323435707684, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(208.1980407607016, 272.2636986119407, 0.0), APoint(208.1980407607016, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.26666169488726, 273.32346648450846, 0.0), APoint(209.26666169488908, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(210.3352826290784, 272.2636986119407, 0.0), APoint(210.3352826290784, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(211.4039035632686, 273.32346648450846, 0.0), APoint(211.40390356326589, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(212.4725244974543, 272.2636986119407, 0.0), APoint(212.4725244974543, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(213.5411454316427, 273.32346648450846, 0.0), APoint(213.5411454316427, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(214.6097663658329, 272.2636986119407, 0.0), APoint(214.6097663658329, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(215.67838730002313, 273.32346648450846, 0.0), APoint(215.67838730001858, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.7470082342088, 272.2636986119407, 0.0), APoint(216.7470082342088, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(217.8156291683963, 273.32346648450846, 0.0), APoint(217.8156291683963, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.8842501025856, 272.2636986119407, 0.0), APoint(218.8842501025856, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.1294198265159, 273.32346648450846, 0.0), APoint(207.12941982651137, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.06079889232387, 272.2636986119407, 0.0), APoint(206.06079889232387, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.99217795813274, 273.32346648450846, 0.0), APoint(204.99217795813547, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.92355702394798, 272.2636986119407, 0.0), APoint(203.92355702394798, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(202.85493608975867, 273.32346648450846, 0.0), APoint(202.85493608975867, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(201.78631515557026, 272.2636986119407, 0.0), APoint(201.78631515557026, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.71769422137913, 273.32346648450846, 0.0), APoint(200.71769422138277, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(199.64907328719437, 272.2636986119407, 0.0), APoint(199.64907328719437, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.58045235300506, 273.32346648450846, 0.0), APoint(198.58045235300506, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(197.51183141881756, 272.2636986119407, 0.0), APoint(197.51183141881756, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.44321048462643, 273.32346648450846, 0.0), APoint(196.44321048462734, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(195.3745895504362, 269.44798519344937, 0.0), APoint(195.37458955043985, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.3059686162551, 272.26664830269203, 0.0), APoint(194.30596861625145, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(193.2373476820767, 267.62098811243084, 0.0), APoint(193.23734768206305, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.16872674787373, 271.20983012087345, 0.0), APoint(192.16872674787373, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.1001058136726, 265.7939910313764, 0.0), APoint(191.10010581368624, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(190.0314848794951, 270.1530119390542, 0.0), APoint(190.03148487949784, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(188.96286394531217, 263.9669939503592, 0.0), APoint(188.96286394531035, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(187.89424301112467, 269.0961937572363, 0.0), APoint(187.89424301112103, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(186.82562207691353, 262.13999686930845, 0.0), APoint(186.82562207693263, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(185.7570011427424, 268.0393755754184, 0.0), APoint(185.75700114274332, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(184.68838020855674, 260.31299978829287, 0.0), APoint(184.68838020855674, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.61975927437106, 267.5109664845086, 0.0), APoint(183.61975927436742, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.55113834015447, 258.48600270723887, 0.0), APoint(182.55113834017902, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.4825174059897, 267.5109664845086, 0.0), APoint(181.4825174059897, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(180.41389647180222, 254.64648209896177, 0.0), APoint(180.41389647180222, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(180.4138964718304, 254.64648209900008, 0.0), APoint(180.41389647180222, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(179.3452755376111, 267.5109664845086, 0.0), APoint(179.34527553761382, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(178.27665460339085, 251.6258469249379, 0.0), APoint(178.27665460342632, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.20803366923792, 267.5109664845086, 0.0), APoint(177.20803366923792, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(176.13941273504406, 251.74849278468298, 0.0), APoint(176.13941273504952, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(175.0707918008593, 267.5109664845086, 0.0), APoint(175.0707918008593, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(174.00217086663451, 250.89405655819996, 0.0), APoint(174.0021708666727, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.9335499324834, 272.2636986119407, 0.0), APoint(172.9335499324834, 275.6006963773462, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.9335499324834, 275.6006963773462, 0.0), APoint(172.93354993248067, 263.8661142614273, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.93354993248067, 262.29998753091434, 0.0), APoint(172.9335499324834, 249.88684807843526, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(172.92142691736535, 263.3998154040632, 0.0), 0.4664564201237909, 0.0, 3.141592653589793)
entity.Color = 7

entity = acad.model.AddLine(APoint(173.38788333749017, 263.3998154040632, 0.0), APoint(172.45497049724236, 262.76628638827844, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(172.92142691736535, 262.76628638827844, 0.0), 0.4664564201237909, 3.141592653589793, 0.0)
entity.Color = 7

entity = acad.model.AddLine(APoint(172.9335499324834, 263.8661142614273, 0.0), APoint(172.9335499324834, 264.7798375281452, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.9443238630838, 262.30039227825847, 0.0), APoint(172.9443238630838, 261.54115175190327, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.93365816394817, 275.53782902954447, 0.0), APoint(244.93365816394635, 263.80324691362557, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.93365816394635, 262.2371201831127, 0.0), APoint(244.93365816394817, 249.8239807306336, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(244.92153514883012, 263.33694805626146, 0.0), 0.4664564201237909, 0.0, 3.141592653589793)
entity.Color = 7

entity = acad.model.AddLine(APoint(245.38799156895402, 263.33694805626146, 0.0), APoint(244.4550787287062, 262.7034190404768, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(244.92153514883012, 262.7034190404768, 0.0), 0.4664564201237909, 3.141592653589793, 0.0)
entity.Color = 7

entity = acad.model.AddLine(APoint(244.93365816394817, 263.80324691362557, 0.0), APoint(244.93365816394817, 264.7169701803435, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.94443209454857, 262.2375249304568, 0.0), APoint(244.94443209454857, 261.47828440410154, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.9528710367731, 273.32346648450846, 0.0), APoint(219.9528710367731, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.95943400937176, 273.32346648450846, 0.0), APoint(222.9594340093745, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.890813075187, 272.2636986119407, 0.0), APoint(221.890813075187, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.82219214099769, 273.32346648450846, 0.0), APoint(220.82219214099769, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.05837043336123, 269.44798519344937, 0.0), APoint(224.05837043335669, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.12699136754236, 272.26664830269203, 0.0), APoint(225.1269913675451, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.19561230172076, 267.62098811243084, 0.0), APoint(226.1956123017335, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(227.26423323592098, 271.20983012087356, 0.0), APoint(227.26423323592098, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.33285417012303, 265.7939910313765, 0.0), APoint(228.3328541701112, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.40147510430234, 270.1530119390543, 0.0), APoint(229.4014751042978, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(230.47009603848437, 263.9669939503592, 0.0), APoint(230.470096038488, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(231.53871697267368, 269.0961937572364, 0.0), APoint(231.5387169726764, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(232.607337906883, 262.13999686930845, 0.0), APoint(232.6073379068639, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(233.67595884105504, 268.0393755754185, 0.0), APoint(233.6759588410523, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(234.7445797752407, 260.31299978829287, 0.0), APoint(234.7445797752407, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(235.81320070942638, 267.5109664845087, 0.0), APoint(235.8132007094291, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.88182164364298, 258.48600270723887, 0.0), APoint(236.88182164361842, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.950442577805, 267.5109664845087, 0.0), APoint(237.950442577805, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.01906351199523, 254.64648209896188, 0.0), APoint(239.01906351199523, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.01906351196794, 254.6464820990002, 0.0), APoint(239.01906351199523, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.08768444618636, 267.5109664845087, 0.0), APoint(240.0876844461818, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(241.1563053804066, 251.6258469249379, 0.0), APoint(241.15630538037203, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.22492631455953, 267.5109664845087, 0.0), APoint(242.22492631455953, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.29354724875247, 251.7484927846831, 0.0), APoint(243.29354724874793, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.36216818293633, 267.5109664845087, 0.0), APoint(244.36216818293633, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(344.93487556371474, 135.03932618240378, 0.0), APoint(375.2157554761552, 135.03932618240367, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(344.93487556371474, 134.46861839719907, 0.0), APoint(375.2157554761552, 134.4686183971993, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('آرماتور بندی دال و شناژ', APoint(346.9620720063167, 136.28559099344807, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('2-2', APoint(356.186264123633, 131.09357855624535, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(216.79688469293342, 139.1331307453936, 0.0), APoint(233.5909769638265, 139.13313074539371, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.7968846929316, 138.77473932461612, 0.0), APoint(233.5909769638265, 138.77473932461612, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('2-2', APoint(217.51730136348306, 140.3853608907582, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(206.83663942200656, 240.36805192973088, 0.0), APoint(216.23639829708463, 240.36805192973088, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.78969117079214, 239.79734414452622, 0.0), APoint(216.23639829708463, 239.79734414452622, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('نما', APoint(209.5361280572788, 240.80873106788772, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(73.35269446354141, 212.3585186245367, 0.0), APoint(83.15876076241375, 212.3585186245367, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.37354065032514, 212.00012720375918, 0.0), APoint(83.15876076241375, 212.00012720375906, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('پلان', APoint(76.58491441876504, 214.101258436862, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('مقطع', APoint(80.48599412692693, 60.63984467739124, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(72.41198738685307, 59.330118032797486, 0.0), APoint(87.7236828390769, 59.330118032797714, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.43552180255438, 58.97172661202012, 0.0), APoint(87.7236828390769, 58.97172661202001, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('1-1', APoint(72.28088762067136, 60.56774999780555, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(77.3949678541303, 274.69918892475994, 0.0), APoint(77.3949678541303, 226.24439172567406, 0.0))
entity.Color = 4


entity = acad.model.AddLine(APoint(90.54474411659521, 267.4900886374305, 0.0), APoint(90.54474411659521, 230.71851182393897, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.59253581200028, 267.27411378776895, 0.0), APoint(91.59253581200028, 230.7462192062548, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('C.L.', APoint(74.58718661841749, 276.0767699626228, 0.0), 2.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(27.56191975748834, 264.215277256224, 0.0), APoint(26.430866001661798, 262.3991541320247, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.835931114548202, 259.8869343157614, 0.0), APoint(25.63339855810318, 261.1430442238922, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.37644064895312, 261.94105003849455, 0.0), APoint(24.835931114548202, 259.8869343157614, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.13291746019877, 282.1045448533092, 0.0), APoint(39.18734281290699, 282.5626489468385, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('3', APoint(23.3675427593339, 261.83477978522797, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddText('3', APoint(36.16797080116203, 281.8856547371109, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(42.04966926937141, 249.19931547928172, 0.0), APoint(39.91021679361029, 249.18117974731354, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.93447060186827, 249.18172901686398, 0.0), APoint(38.42234369773723, 249.18145438208956, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.42261851791909, 250.67033194253167, 0.0), APoint(36.93447060186827, 249.18172901686398, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.61688515200922, 249.1673468958955, 0.0), APoint(110.54829837854004, 249.14981187901498, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.10503306805913, 250.6559498215629, 0.0), APoint(115.59263134374805, 249.16679762634624, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('1', APoint(37.79230129940106, 251.46523352288568, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddText('1', APoint(113.40317748069037, 251.35339779255088, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(60.987484019639396, 231.56350392253597, 0.0), APoint(61.0056197516069, 229.424051446774, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.00507048205691, 226.44830525503238, 0.0), APoint(61.00561975160779, 229.42405144666895, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.516467556389216, 227.9364531710828, 0.0), APoint(61.00507048205691, 226.44830525503238, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.015024072422875, 269.3290301956912, 0.0), APoint(61.03255908930396, 267.2604434222224, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.52642114675609, 270.817178111742, 0.0), APoint(61.01557334197196, 272.3047763874313, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('2', APoint(58.72156597603498, 227.306135952565, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddText('2', APoint(58.828973175768624, 270.1153225243723, 0.0), 1.9756799999999992)
entity.Color = 1

# Entity type AcDbHatch not supported
entity = acad.model.AddLine(APoint(77.72399283695813, 134.9455784482434, 0.0), APoint(77.72399283695813, 72.02445643668318, 0.0))
entity.Color = 4


entity = acad.model.AddLine(APoint(89.70644040441721, 129.51093919296454, 0.0), APoint(89.70644040441721, 70.73665015866573, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 129.55411810967405, 0.0), APoint(90.75423209982318, 70.6970443310355, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('C.L.', APoint(74.91621160124487, 136.24193746297271, 0.0), 2.5)
entity.Color = 1

entity = acad.model.AddText('i-097', APoint(65.96961459937938, 133.01573766214926, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(118.8680321574152, 113.97651159688405, 0.0), APoint(100.89380215333131, 125.27561250566305, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.368032157416565, 113.15151159688412, 0.0), APoint(54.55418352058405, 125.27561250566305, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.55418352058405, 125.27561250566305, 0.0), APoint(77.72399283695813, 125.50731059882673, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.64035642685258, 124.78144798538187, 0.0), APoint(77.72924257447812, 124.98233684685806, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.70644040441994, 124.86245987380823, 0.0), APoint(77.72399283695813, 124.98228434948282, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.89380215333131, 125.27561250566305, 0.0), APoint(90.75423209982318, 125.37700820619807, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.8076292470655, 124.78144798538187, 0.0), APoint(90.74898236230365, 124.8520344542294, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.70644040441812, 125.38748612315203, 0.0), APoint(77.72399283695813, 125.50731059882673, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.81287898458504, 125.30642173735055, 0.0), APoint(97.8076292470655, 124.78144798538187, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.635106689331224, 125.30642173735055, 0.0), APoint(57.64035642684985, 124.78144798538187, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.29487555533024, 119.23205178572516, 0.0), APoint(107.02600710154002, 122.07796408825186, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.02600710154002, 122.07796408825186, 0.0), APoint(111.29487555533024, 122.07796408825186, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.29487555533024, 122.07796408825186, 0.0), APoint(111.29487555533024, 119.23205178572516, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-182', APoint(108.37515465262004, 122.8148757869692, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('1', APoint(111.38367833416987, 119.49476670924173, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(126.58822750588024, 86.65497309898649, 0.0), APoint(126.58822750588024, 90.79824047936665, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(127.93822750587833, 86.65497309898649, 0.0), APoint(125.23822750587942, 86.65497309898649, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.58822750588024, 88.00497309898662, 0.0), APoint(127.93822750587833, 88.00497309898662, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(127.93822750587833, 88.00497309898662, 0.0), APoint(126.58822750588024, 86.65497309898649, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.58822750588024, 86.65497309898649, 0.0), APoint(125.23822750587942, 88.00497309898662, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(125.23822750587942, 88.00497309898662, 0.0), APoint(126.58822750588024, 88.00497309898662, 0.0))
entity.Color = 8


# Entity type AcDbSolid not supported
entity = acad.model.AddLine(APoint(126.58822750588024, 90.79824047936665, 0.0), APoint(134.68822750587833, 90.79824047936665, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(128.21935332337807, 79.11864367203282, 0.0), APoint(125.51935332338007, 79.11864367203282, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.86935332337953, 77.7686436720328, 0.0), APoint(128.21935332337807, 77.7686436720328, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(128.21935332337807, 77.7686436720328, 0.0), APoint(126.86935332337953, 79.11864367203282, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.86935332337953, 79.11864367203282, 0.0), APoint(126.86935332337953, 74.97537629165276, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(125.51935332338007, 77.7686436720328, 0.0), APoint(126.86935332337953, 77.7686436720328, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.86935332337953, 79.11864367203282, 0.0), APoint(125.51935332338007, 77.7686436720328, 0.0))
entity.Color = 8


# Entity type AcDbSolid not supported
entity = acad.model.AddLine(APoint(126.86935332337953, 74.97537629165276, 0.0), APoint(134.96935332337807, 74.97537629165276, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-105', APoint(130.04656825892198, 76.21478786357738, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-104', APoint(128.3737502290519, 91.98447663885179, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(126.58822750588024, 108.39715845366766, 0.0), APoint(126.58822750588024, 112.54042583404782, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(127.93822750587833, 108.39715845366766, 0.0), APoint(125.23822750587942, 108.39715845366766, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.58822750588024, 109.74715845366768, 0.0), APoint(127.93822750587833, 109.74715845366768, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(127.93822750587833, 109.74715845366768, 0.0), APoint(126.58822750588024, 108.39715845366766, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.58822750588024, 108.39715845366766, 0.0), APoint(125.23822750587942, 109.74715845366768, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(125.23822750587942, 109.74715845366768, 0.0), APoint(126.58822750588024, 109.74715845366768, 0.0))
entity.Color = 8


# Entity type AcDbSolid not supported
entity = acad.model.AddLine(APoint(126.58822750588024, 112.54042583404782, 0.0), APoint(134.68822750587833, 112.54042583404782, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-103', APoint(128.3737502290519, 113.72666199353296, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(29.18864683376887, 85.61770296069221, 0.0), APoint(29.18864683376887, 89.76097034107227, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.838646833770326, 85.61770296069221, 0.0), APoint(30.538646833770144, 85.61770296069221, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(29.18864683376887, 86.96770296069224, 0.0), APoint(27.838646833770326, 86.96770296069224, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.838646833770326, 86.96770296069224, 0.0), APoint(29.18864683376887, 85.61770296069221, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(29.18864683376887, 85.61770296069221, 0.0), APoint(30.538646833770144, 86.96770296069224, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(30.538646833770144, 86.96770296069224, 0.0), APoint(29.18864683376887, 86.96770296069224, 0.0))
entity.Color = 8


# Entity type AcDbSolid not supported
entity = acad.model.AddLine(APoint(29.18864683376887, 89.76097034107227, 0.0), APoint(21.088646833771236, 89.76097034107227, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.557521016268765, 78.08137353373843, 0.0), APoint(30.25752101626813, 78.08137353373843, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(28.90752101627004, 76.73137353373852, 0.0), APoint(27.557521016268765, 76.73137353373852, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.557521016268765, 76.73137353373852, 0.0), APoint(28.90752101627004, 78.08137353373843, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(28.90752101627004, 78.08137353373843, 0.0), APoint(28.90752101627004, 73.93810615335838, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(30.25752101626813, 76.73137353373852, 0.0), APoint(28.90752101627004, 76.73137353373852, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(28.90752101627004, 78.08137353373843, 0.0), APoint(30.25752101626813, 76.73137353373852, 0.0))
entity.Color = 8


# Entity type AcDbSolid not supported
entity = acad.model.AddLine(APoint(28.90752101627004, 73.93810615335838, 0.0), APoint(20.80752101627013, 73.93810615335838, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-102', APoint(20.77792512834594, 75.177517725283, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-101', APoint(22.450743158216028, 90.9472065005574, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(29.18864683376887, 107.35988831537327, 0.0), APoint(29.18864683376887, 111.50315569575343, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.838646833770326, 107.35988831537327, 0.0), APoint(30.538646833770144, 107.35988831537327, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(29.18864683376887, 108.70988831537318, 0.0), APoint(27.838646833770326, 108.70988831537318, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.838646833770326, 108.70988831537318, 0.0), APoint(29.18864683376887, 107.35988831537327, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(29.18864683376887, 107.35988831537327, 0.0), APoint(30.538646833770144, 108.70988831537318, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(30.538646833770144, 108.70988831537318, 0.0), APoint(29.18864683376887, 108.70988831537318, 0.0))
entity.Color = 8


# Entity type AcDbSolid not supported
entity = acad.model.AddLine(APoint(29.18864683376887, 111.50315569575343, 0.0), APoint(21.088646833771236, 111.50315569575343, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-100', APoint(22.450743158216028, 112.68939185523857, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(48.57301469313916, 228.3115682540224, 0.0), APoint(48.57301469313916, 236.22417446126076, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 228.60024338862246, 0.0), APoint(106.57301469313916, 235.95622526883056, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(404.8380820999064, 167.20713884488214, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(396.68838766236695, 153.25304271766697, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(408.68120686030215, 167.20713884488214, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(408.72902174392857, 153.26025861831738, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(404.79978053677587, 153.25665066799218, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(408.72902174392857, 157.40852462656574, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(404.7537437271958, 157.35198313584885, 0.0), 0.2400000000008731)


entity = acad.model.AddCircle(APoint(396.68838766236695, 157.30423426600498, 0.0), 0.2400000000008731)


entity = acad.model.AddLine(APoint(121.11803215741656, 86.62264288110111, 0.0), APoint(121.1180321574152, 79.12226789047577, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 85.75264288110077, 0.0), APoint(34.19302840769751, 78.25301785297825, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 113.09901159688354, 0.0), APoint(34.118032157408834, 110.12886160063374, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 113.99901159688386, 0.0), APoint(121.1180321574152, 110.99886160063386, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 259.95622526883096, 0.0), APoint(106.57301469313916, 261.9562252688308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313734, 263.4562252688308, 0.0), APoint(106.57301469314007, 261.95622526883074, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 237.9562252688308, 0.0), APoint(106.57301469313916, 235.95622526883056, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 261.6882760764006, 0.0), APoint(48.57301469313916, 259.9562252688317, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 237.9562252688297, 0.0), APoint(48.57301469313916, 236.22417446126076, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.74147999192974, 269.82613347407926, 0.0), APoint(236.29147999186353, 256.57613347407937, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 269.82613347407926, 0.0), APoint(183.24147999193428, 256.57613347407926, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('جزئیات الف', APoint(19.37597106445628, 120.02304893113558, 0.0), 1.75)
entity.Color = 1

entity = acad.model.AddCircle(APoint(35.4223406081901, 113.53782974353669, 0.0), 2.8560782053764338)
entity.Color = 8

entity = acad.model.AddLine(APoint(255.2621696590786, 160.15697630981742, 0.0), APoint(232.76216965908588, 160.15697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(255.26216965908498, 152.65697630981742, 0.0), APoint(232.76216965908588, 152.65697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.7651660952797, 182.28197630981742, 0.0), APoint(239.7651660952797, 160.15697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(232.7621696590786, 160.15697630981742, 0.0), APoint(232.76216965908588, 152.65697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(255.2621696590786, 160.15697630981742, 0.0), APoint(255.26216965908498, 152.65697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.0151660952797, 182.28197630981742, 0.0), APoint(253.26516609527607, 160.15697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.30347265904948, 184.5319763098174, 0.0), APoint(242.30347265904948, 187.5319763098174, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(168.1712378626189, 36.62681066297944, 0.0), APoint(184.25873710533142, 36.62681066297955, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(168.17427364620107, 36.26841924220173, 0.0), APoint(184.25873710533142, 36.26841924220173, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('3-3', APoint(168.86362378616286, 37.85902144751424, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(181.16602653143218, 98.92379186092637, 0.0), APoint(177.6660265314331, 98.92379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.6660265314331, 98.92379186092637, 0.0), APoint(173.1660265314331, 96.67379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.1660265314331, 96.67379186092637, 0.0), APoint(160.58269319810006, 58.92379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 98.92379186092637, 0.0), APoint(181.16602653143218, 58.92379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 58.92379186092637, 0.0), APoint(160.58269319810006, 58.92379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319810006, 58.92379186092637, 0.0), APoint(160.58269319810006, 50.92379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 58.92379186092637, 0.0), APoint(191.58269319810006, 58.92379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319810006, 58.92379186092637, 0.0), APoint(160.58269319810006, 48.923791860926485, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319810006, 48.923791860926485, 0.0), APoint(191.58269319810006, 48.923791860926485, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.58269319810006, 48.923791860926485, 0.0), APoint(191.58269319810006, 58.92379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.6660265314331, 98.92379186092637, 0.0), APoint(151.9304490792665, 105.34039198909113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(167.4238474574595, 81.29164300551395, 0.0), APoint(165.89482353034873, 81.29164300551395, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(165.89482353034873, 81.29164300551395, 0.0), APoint(165.89482353034873, 76.70457122418168, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(167.4238474574595, 81.29164300551395, 0.0), APoint(165.89482353034873, 76.70457122418168, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.70741408906997, 197.30947565572683, 0.0), APoint(245.68463405991315, 197.1157525193313, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.23390423430556, 195.1292364399504, 0.0), APoint(228.23390423430556, 197.19825226227658, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.30252516849032, 196.18900431251828, 0.0), APoint(229.30252516849214, 197.1932002699957, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(230.37114610268145, 195.1292364399504, 0.0), APoint(230.37114610268145, 197.18814827771473, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(231.43976703687167, 196.18900431251828, 0.0), APoint(231.43976703686985, 197.18309628543363, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(232.50838797105826, 195.1292364399504, 0.0), APoint(232.50838797105826, 197.17804429315265, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(233.57700890524757, 196.18900431251828, 0.0), APoint(233.57700890524757, 197.17299230087167, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(234.64562983943415, 195.1292364399504, 0.0), APoint(234.64562983943415, 197.1679403085907, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(235.7142507736262, 196.18900431251828, 0.0), APoint(235.71425077362346, 197.1628883163097, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.78287170781277, 195.1292364399504, 0.0), APoint(236.78287170781277, 197.15783632402872, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.85149264200027, 196.18900431251828, 0.0), APoint(237.85149264200027, 197.15278433174774, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(238.92011357618867, 195.1292364399504, 0.0), APoint(238.92011357618867, 197.14773233946676, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(227.16528330011897, 196.18900431251828, 0.0), APoint(227.16528330011624, 197.20330425455757, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.09666236592875, 195.1292364399504, 0.0), APoint(226.09666236592693, 197.20835624683855, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.0280414317367, 196.18900431251828, 0.0), APoint(225.02804143173944, 197.21340823911953, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.95942049755013, 195.1292364399504, 0.0), APoint(223.95942049755013, 197.2184602314005, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.89079956336263, 196.18900431251828, 0.0), APoint(222.89079956336263, 197.2235122236816, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.82217862917423, 195.1292364399504, 0.0), APoint(221.82217862917423, 197.2285642159626, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7535576949831, 196.18900431251828, 0.0), APoint(220.75355769498583, 197.23361620824346, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.68493676079743, 195.1292364399504, 0.0), APoint(219.68493676079743, 197.23866820052444, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.61631582660812, 196.18900431251828, 0.0), APoint(218.61631582660812, 197.24372019280543, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(217.54769489242153, 195.1292364399504, 0.0), APoint(217.54769489242153, 197.24877218508652, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.4790739582295, 196.18900431251828, 0.0), APoint(216.47907395823222, 197.24877218508652, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.9887345103798, 196.16879634339418, 0.0), APoint(239.98873451037616, 197.14268034718577, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(241.05735544456547, 195.10902847082636, 0.0), APoint(241.05735544456547, 197.1376283549048, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.12597637875388, 196.16879634339418, 0.0), APoint(242.12597637875388, 197.1325763626238, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.19459731294228, 195.10902847082636, 0.0), APoint(243.19459731294228, 197.12752437034283, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.2632182471334, 196.1485883742703, 0.0), APoint(244.2632182471316, 197.12247237806173, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.33183918131817, 195.0888205017025, 0.0), APoint(245.33183918131817, 197.11742038578075, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(215.41045302404382, 195.1443924167934, 0.0), APoint(215.41045302404382, 197.2538241773675, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(214.34183208985542, 196.20416028936117, 0.0), APoint(214.34183208985542, 197.2588761696485, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(213.2732111556661, 195.1443924167934, 0.0), APoint(213.2732111556661, 197.26392816192947, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(212.20459022147497, 196.20416028936117, 0.0), APoint(212.20459022147952, 197.26392816192947, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(211.1359692872902, 195.1595483936363, 0.0), APoint(211.1359692872902, 197.26898015421034, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(210.06734835310272, 196.21931626620406, 0.0), APoint(210.06734835310272, 197.27403214649144, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(208.9987274189125, 195.1595483936363, 0.0), APoint(208.9987274189125, 197.27908413877242, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.93010648472227, 196.21931626620406, 0.0), APoint(207.9301064847241, 197.27908413877242, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.8614855505375, 195.1747043704792, 0.0), APoint(206.8614855505375, 197.2841361310534, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(205.7928646163482, 196.23447224304707, 0.0), APoint(205.7928646163482, 197.28918812333438, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.7242436821598, 195.1747043704792, 0.0), APoint(204.7242436821598, 197.29424011561525, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 194.5304778217412, 0.0), APoint(320.69261141489915, 200.0579147034448, 0.0))



entity = acad.model.AddLine(APoint(320.69261141489915, 285.2804778217412, 0.0), APoint(408.4424045167525, 285.2804778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 275.5304778217412, 0.0), APoint(408.4424045167525, 275.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 269.5304778217412, 0.0), APoint(408.4424045167525, 269.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 263.5304778217412, 0.0), APoint(408.4424045167525, 263.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 257.5304778217412, 0.0), APoint(408.4424045167525, 257.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 251.53047782174107, 0.0), APoint(408.4424045167525, 251.53047782174107, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 245.53047782174107, 0.0), APoint(408.4424045167525, 245.53047782174107, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 239.53047782174107, 0.0), APoint(408.4424045167525, 239.53047782174107, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 233.53047782174107, 0.0), APoint(408.4424045167525, 233.53047782174107, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 227.53047782174107, 0.0), APoint(408.4424045167525, 227.53047782174107, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 221.53047782174121, 0.0), APoint(408.4424045167525, 221.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 209.53047782174121, 0.0), APoint(408.4424045167525, 209.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 202.03047782174107, 0.0), APoint(408.4424045167525, 202.03047782174107, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 285.2804778217412, 0.0), APoint(320.69261141489915, 194.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(327.44261141490006, 285.2804778217412, 0.0), APoint(327.44261141489915, 215.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(334.19261141489915, 285.2804778217412, 0.0), APoint(334.19261141489915, 215.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(340.94261141489915, 285.2804778217412, 0.0), APoint(340.94261141489915, 215.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.1924045167543, 285.2804778217412, 0.0), APoint(367.1924045167543, 215.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(375.4424045167525, 285.2804778217412, 0.0), APoint(375.4424045167525, 215.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(383.6924045167525, 285.2804778217412, 0.0), APoint(383.6924045167525, 215.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167525, 285.2804778217412, 0.0), APoint(391.9424045167525, 215.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167525, 285.2804778217412, 0.0), APoint(400.1924045167507, 215.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167507, 209.53047782174121, 0.0), APoint(400.1924045167507, 202.03047782174107, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.4424045167525, 285.2804778217412, 0.0), APoint(408.4424045167525, 194.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('شماره', APoint(322.08631042745037, 279.38112851168296, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('قطر', APoint(329.2257135564587, 280.9594393556175, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('تعداد', APoint(335.1867702964755, 279.3801595931065, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('mm', APoint(329.87847795749985, 277.4555687533948, 0.0), 1.125)
entity.Color = 1

entity = acad.model.AddText('شکل آرماتور', APoint(346.66820195071705, 279.2079486952227, 0.0), 1.875)
entity.Color = 1

entity = acad.model.AddText('طول', APoint(369.83289925020017, 280.9954634549688, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('وزن کل', APoint(393.18727744914213, 282.4395964145923, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('طول کل', APoint(376.70796260487987, 280.999774274183, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('وزن یکمتر', APoint(383.49721367705115, 281.0759927389772, 0.0), 1.274999999999999)
entity.Color = 1

entity = acad.model.AddText('وزن کل', APoint(400.95678790970214, 281.0316837878022, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('m', APoint(370.47990999607555, 276.9154121324991, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('m', APoint(378.3644939416099, 276.9154121324991, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('Kg/m', APoint(385.9544695478362, 276.9154121324989, 0.0), 1.274999999999999)
entity.Color = 1

entity = acad.model.AddText('Kg', APoint(394.86449394160536, 276.9154121324991, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('Kg', APoint(403.11449394160536, 276.915412132498, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('2', APoint(323.2163732246054, 265.3787338448732, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('1', APoint(323.2163732246054, 271.3787338448732, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('3', APoint(323.2163732246054, 259.3787338448733, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('4', APoint(323.2163732246054, 253.37873384487318, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('5', APoint(323.2163732246054, 247.37873384487318, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('6', APoint(323.2163732246054, 241.37873384487318, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('7', APoint(323.2163732246054, 235.37873384487318, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('8', APoint(323.2163732246054, 229.37873384487318, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('9', APoint(323.2163732246054, 223.37873384487318, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('i-001', APoint(329.10399982919535, 271.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(345.06784421645807, 271.38709408965957, 0.0), APoint(345.06784421645807, 272.2435321250472, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(345.06784421645807, 272.2435321250472, 0.0), APoint(348.8734895624684, 272.2435321250472, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.8734895624684, 272.2435321250472, 0.0), APoint(351.45795789644853, 270.7724536353503, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(363.06755981983133, 270.7724536353503, 0.0), APoint(363.06755981983133, 271.79279669681455, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(351.45795789644853, 270.7724536353503, 0.0), APoint(363.06755981983133, 270.7724536353503, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-003', APoint(341.6226798152984, 271.1663370082134, 0.0), 1.3125)


entity = acad.model.AddText('i-004', APoint(346.0291287555001, 272.4770016828236, 0.0), 1.3125)


entity = acad.model.AddText('i-005', APoint(349.8750125165543, 271.80830446860944, 0.0), 1.3125)


entity = acad.model.AddText('i-006', APoint(355.75054927572364, 270.9792029410494, 0.0), 1.3125)


entity = acad.model.AddText('i-007', APoint(363.49163431026227, 270.8854253114527, 0.0), 1.3125)


entity = acad.model.AddLine(APoint(362.9884062924066, 265.5706111532029, 0.0), APoint(362.9884062924066, 266.42704918859044, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(362.9884062924066, 266.42704918859044, 0.0), APoint(359.18276094639623, 266.42704918859044, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.18276094639623, 266.42704918859044, 0.0), APoint(356.598292612417, 264.95597069889357, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(344.98869068903423, 264.95597069889357, 0.0), APoint(344.98869068903423, 265.9763137603579, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(356.598292612417, 264.95597069889357, 0.0), APoint(344.98869068903423, 264.95597069889357, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-018', APoint(363.2255451534238, 265.3498540717567, 0.0), 1.3125)


entity = acad.model.AddText('i-017', APoint(359.33962175336546, 266.66051874636685, 0.0), 1.3125)


entity = acad.model.AddText('i-016', APoint(355.0658873918901, 265.9918215321528, 0.0), 1.3125)


entity = acad.model.AddText('i-015', APoint(349.805701233141, 265.16272000459276, 0.0), 1.3125)


entity = acad.model.AddText('i-014', APoint(341.6515985478354, 265.068942374996, 0.0), 1.3125)


entity = acad.model.AddText('i-046', APoint(329.05438256718026, 241.45060427087768, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-053', APoint(329.05438256718026, 235.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-063', APoint(329.05438256718026, 229.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-070', APoint(329.05438256718026, 223.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091379, 259.7297962671052, 0.0), APoint(359.67258082251556, 259.7297962671052, 0.0))



entity = acad.model.AddText('i-025', APoint(352.49400297420925, 260.1026205989906, 0.0), 1.3125)


entity = acad.model.AddLine(APoint(348.4624351091379, 252.4757955487325, 0.0), APoint(348.4624351091379, 254.0109376956913, 0.0))



entity = acad.model.AddLine(APoint(348.4624351091379, 254.0109376956913, 0.0), APoint(359.67258082251556, 254.0109376956913, 0.0))



entity = acad.model.AddLine(APoint(359.67258082251556, 252.4757955487325, 0.0), APoint(359.67258082251556, 254.0109376956913, 0.0))



entity = acad.model.AddText('i-032', APoint(345.2376837211086, 252.81219461117598, 0.0), 1.3125)


entity = acad.model.AddText('i-033', APoint(352.82956682788245, 254.3837620275767, 0.0), 1.3125)


entity = acad.model.AddText('i-034', APoint(359.9875729588912, 252.84660272930938, 0.0), 1.3125)


entity = acad.model.AddLine(APoint(348.4624351091379, 247.7297962671052, 0.0), APoint(359.67258082251556, 247.7297962671052, 0.0))



entity = acad.model.AddText('i-041', APoint(352.49400297420925, 248.10262059899048, 0.0), 1.3125)


entity = acad.model.AddText('i-047', APoint(335.78919988083, 241.46776131919867, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091379, 241.7297962671052, 0.0), APoint(359.67258082251556, 241.7297962671052, 0.0))



entity = acad.model.AddText('i-048', APoint(352.49400297420925, 242.10262059899048, 0.0), 1.3125)


entity = acad.model.AddText('i-049', APoint(368.80417566903185, 241.49470393207176, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-050', APoint(377.3424045167525, 241.3258687642022, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-051', APoint(385.5924045167525, 241.3553104647698, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-052', APoint(393.8424045167525, 241.34525848758338, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-054', APoint(335.78919988083, 235.14069921956778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-061', APoint(385.5924045167525, 235.3553104647698, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(352.2767216558186, 235.5282278992128, 0.0), APoint(357.8494552464563, 235.5282278992128, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(353.49945530120385, 234.19341785158207, 0.0), APoint(353.49945530120385, 237.72250549478989, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(353.34945530120604, 237.72250549478989, 0.0), 0.15, 0.0, 1.5707963267948966)


entity = acad.model.AddLine(APoint(357.9994552464577, 235.3782278992128, 0.0), APoint(357.9994552464577, 234.0494331270772, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(357.8494552464563, 235.3782278992128, 0.0), 0.15, 0.0, 1.5707963267948966)


entity = acad.model.AddArc(APoint(357.8494552464563, 234.0494331270772, 0.0), 0.15, 4.71238898038469, 0.0)


entity = acad.model.AddLine(APoint(357.8494552464563, 233.8994331270772, 0.0), APoint(352.1494553214561, 233.8994331270772, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(352.1494553214561, 234.0494331270772, 0.0), 0.15, 3.141592653590248, 4.71238898038469)


entity = acad.model.AddLine(APoint(351.99945532145466, 237.72250549478989, 0.0), APoint(351.99945532145466, 234.04943312707707, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(353.34945530120604, 237.8725054947899, 0.0), APoint(352.14945532145157, 237.87250549479006, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(352.14945532145157, 237.72250549479008, 0.0), 0.15, 1.5707963267948966, 3.141592653590248)


entity = acad.model.AddText('i-058', APoint(358.00933390082355, 234.22493257607022, 0.0), 1.3125)


entity = acad.model.AddText('i-056', APoint(348.3975740828755, 234.76630375089655, 0.0), 1.3125)


entity = acad.model.AddText('i-057', APoint(354.29545190552926, 235.67910068220706, 0.0), 1.3125)


entity = acad.model.AddText('i-055', APoint(348.2430401421316, 236.93124820837718, 0.0), 1.3125)


entity = acad.model.AddText('i-059', APoint(369.10725454831135, 235.4947039320718, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-060', APoint(377.3424045167525, 235.4352017132442, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-062', APoint(393.8424045167525, 235.40614848471895, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-064', APoint(335.78919988083, 229.46776131919867, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091379, 229.7297962671052, 0.0), APoint(359.67258082251556, 229.7297962671052, 0.0))



entity = acad.model.AddText('i-065', APoint(352.49400297420925, 230.10262059899048, 0.0), 1.3125)


entity = acad.model.AddText('i-066', APoint(369.10725454831135, 229.4947039320718, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-067', APoint(377.3424045167525, 229.32586876420208, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-068', APoint(385.5924045167525, 229.3553104647698, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-069', APoint(402.092404516751, 229.35531046476976, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-071', APoint(335.78919988083, 223.66256247382645, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddLine(APoint(352.09188232289944, 224.51603668768396, 0.0), APoint(354.66155437324323, 224.51603668768396, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(354.66155437324323, 224.66603668768428, 0.0), 0.15, 4.71238898038469, 5.408328441522121)


entity = acad.model.AddLine(APoint(355.4437269394384, 225.07853668768405, 0.0), APoint(357.07638271220094, 225.07853668768405, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(357.07638271220094, 224.9285366876838, 0.0), 0.15, 0.0, 1.5707963267948966)


entity = acad.model.AddLine(APoint(352.1319022970938, 222.26603668768396, 0.0), APoint(357.07638271220094, 222.26603668768396, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(357.07638271220094, 222.4160366876842, 0.0), 0.15, 4.71238898038469, 0.0)


entity = acad.model.AddLine(APoint(357.2263827122024, 224.9285366876838, 0.0), APoint(357.2263827122024, 222.4160366876842, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(355.3475609324232, 225.0436544495403, 0.0), APoint(354.7577203802566, 224.5509189258274, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(355.4437269394384, 224.9285366876838, 0.0), 0.15, 1.5707963267948966, 2.2667357879311565)


entity = acad.model.AddText('i-076', APoint(357.41013744495285, 223.0415634948904, 0.0), 1.3125)


entity = acad.model.AddText('i-072', APoint(348.5005467209421, 224.01255315806787, 0.0), 1.3125)


entity = acad.model.AddText('i-075', APoint(355.1454142341636, 225.26866019530246, 0.0), 1.3125)


entity = acad.model.AddText('i-073', APoint(348.45767800418344, 221.942829715737, 0.0), 1.3125)


entity = acad.model.AddText('i-074', APoint(353.7863507135544, 224.7051716830444, 0.0), 1.3125)


entity = acad.model.AddText('i-077', APoint(369.10725454831135, 223.4947039320718, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-078', APoint(377.3424045167525, 223.38275789371906, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-079', APoint(385.5924045167525, 223.3553104647698, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-080', APoint(402.092404516751, 223.34525848758307, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('وزن آرماتور برای یک متر طول آبرو', APoint(351.1185794280618, 211.2160662383678, 0.0), 1.8)
entity.Color = 1

entity = acad.model.AddText('وزن آرماتور برای ابتدا و انتها آبرو', APoint(361.76891620743663, 204.81920104019957, 0.0), 1.8)
entity.Color = 1

entity = acad.model.AddText('i-089', APoint(389.57853430496925, 211.4902574983033, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(400.1924045167534, 274.911261864831, 0.0), APoint(400.81162047366365, 275.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 273.9831842145236, 0.0), APoint(401.7396981239708, 275.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 273.0551065642162, 0.0), APoint(402.6677757742782, 275.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 272.1270289139088, 0.0), APoint(403.5958534245856, 275.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 271.19895126360143, 0.0), APoint(404.52393107489297, 275.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167534, 270.27087361329427, 0.0), APoint(405.45200872520036, 275.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755075, 269.530477821741, 0.0), APoint(406.3800863755075, 275.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258149, 269.530477821741, 0.0), APoint(407.3081640258149, 275.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761223, 269.530477821741, 0.0), APoint(408.2362416761223, 275.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264297, 269.530477821741, 0.0), APoint(408.44240451674955, 274.80856301206086, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.09239697673706, 269.530477821741, 0.0), APoint(408.4424045167498, 273.8804853617537, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.02047462704377, 269.530477821741, 0.0), APoint(408.44240451674955, 272.95240771144677, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735115, 269.530477821741, 0.0), APoint(408.44240451674955, 272.0243300611394, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765854, 269.530477821741, 0.0), APoint(408.44240451674955, 271.096252410832, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.8047075779659, 269.530477821741, 0.0), APoint(408.44240451674955, 270.1681747605246, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167534, 268.91126186483007, 0.0), APoint(400.81162047366456, 269.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 267.9831842145227, 0.0), APoint(401.7396981239717, 269.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 267.0551065642153, 0.0), APoint(402.6677757742791, 269.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 266.1270289139079, 0.0), APoint(403.5958534245865, 269.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 265.1989512636003, 0.0), APoint(404.5239310748939, 269.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 264.27087361329313, 0.0), APoint(405.45200872520127, 269.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755084, 263.530477821741, 0.0), APoint(406.3800863755084, 269.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258158, 263.530477821741, 0.0), APoint(407.3081640258156, 269.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761232, 263.530477821741, 0.0), APoint(408.2362416761232, 269.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264306, 263.530477821741, 0.0), APoint(408.44240451675023, 268.80856301206063, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.092396976738, 263.530477821741, 0.0), APoint(408.4424045167509, 267.8804853617539, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.02047462704513, 263.53047782174144, 0.0), APoint(408.4424045167507, 266.952407711447, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.9485522773525, 263.53047782174144, 0.0), APoint(408.4424045167516, 266.0243300611405, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765945, 263.530477821741, 0.0), APoint(408.4424045167523, 265.0962524108338, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796684, 263.530477821741, 0.0), APoint(408.44240451675273, 264.1681747605269, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167534, 262.91126186483007, 0.0), APoint(400.81162047366456, 263.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 261.9831842145227, 0.0), APoint(401.7396981239717, 263.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 261.0551065642153, 0.0), APoint(402.6677757742791, 263.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 260.1270289139079, 0.0), APoint(403.5958534245865, 263.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 259.1989512636003, 0.0), APoint(404.5239310748939, 263.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 258.27087361329313, 0.0), APoint(405.45200872520127, 263.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755084, 257.530477821741, 0.0), APoint(406.3800863755084, 263.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258158, 257.530477821741, 0.0), APoint(407.3081640258156, 263.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761232, 257.530477821741, 0.0), APoint(408.2362416761232, 263.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264306, 257.530477821741, 0.0), APoint(408.44240451675023, 262.80856301206063, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767375, 257.53047782174053, 0.0), APoint(408.4424045167509, 261.8804853617539, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270447, 257.530477821741, 0.0), APoint(408.4424045167509, 260.9524077114472, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735206, 257.530477821741, 0.0), APoint(408.44240451675205, 260.024330061141, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765945, 257.530477821741, 0.0), APoint(408.4424045167523, 259.0962524108338, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796684, 257.530477821741, 0.0), APoint(408.44240451675273, 258.1681747605269, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167534, 256.91126186483007, 0.0), APoint(400.81162047366456, 257.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 255.98318421452268, 0.0), APoint(401.7396981239717, 257.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 255.0551065642153, 0.0), APoint(402.6677757742791, 257.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 254.1270289139079, 0.0), APoint(403.5958534245865, 257.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 253.19895126360052, 0.0), APoint(404.5239310748939, 257.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 252.27087361329313, 0.0), APoint(405.45200872520127, 257.5304778217412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755082, 251.53047782174076, 0.0), APoint(406.3800863755084, 257.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258156, 251.53047782174076, 0.0), APoint(407.3081640258156, 257.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.236241676123, 251.53047782174076, 0.0), APoint(408.2362416761232, 257.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.16431932643036, 251.53047782174076, 0.0), APoint(408.44240451675023, 256.80856301206063, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767375, 251.53047782174053, 0.0), APoint(408.4424045167509, 255.88048536175393, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270447, 251.530477821741, 0.0), APoint(408.4424045167509, 254.95240771144722, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735206, 251.530477821741, 0.0), APoint(408.4424045167516, 254.02433006114052, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765945, 251.530477821741, 0.0), APoint(408.4424045167523, 253.0962524108338, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796684, 251.530477821741, 0.0), APoint(408.44240451675273, 252.16817476052688, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 250.9112618648296, 0.0), APoint(400.81162047366433, 251.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 249.98318421452245, 0.0), APoint(401.7396981239715, 251.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 249.05510656421507, 0.0), APoint(402.66777577427865, 251.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 248.12702891390768, 0.0), APoint(403.59585342458604, 251.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 247.1989512636003, 0.0), APoint(404.5239310748934, 251.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 246.2708736132929, 0.0), APoint(405.4520087252008, 251.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755084, 245.530477821741, 0.0), APoint(406.3800863755082, 251.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258158, 245.530477821741, 0.0), APoint(407.3081640258156, 251.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761232, 245.530477821741, 0.0), APoint(408.236241676123, 251.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264306, 245.530477821741, 0.0), APoint(408.44240451675, 250.8085630120604, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.092396976738, 245.530477821741, 0.0), APoint(408.4424045167507, 249.8804853617537, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.02047462704513, 245.53047782174144, 0.0), APoint(408.4424045167507, 248.952407711447, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.9485522773525, 245.53047782174144, 0.0), APoint(408.4424045167516, 248.02433006114052, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765945, 245.530477821741, 0.0), APoint(408.4424045167523, 247.0962524108338, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796684, 245.530477821741, 0.0), APoint(408.4424045167523, 246.16817476052643, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167534, 244.91126186483098, 0.0), APoint(400.8116204736634, 245.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 243.9831842145236, 0.0), APoint(401.7396981239706, 245.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 243.0551065642162, 0.0), APoint(402.66777577427774, 245.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 242.12702891390882, 0.0), APoint(403.59585342458513, 245.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 241.19895126360143, 0.0), APoint(404.5239310748925, 245.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167534, 240.27087361329427, 0.0), APoint(405.4520087251999, 245.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755075, 239.530477821741, 0.0), APoint(406.3800863755073, 245.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258149, 239.530477821741, 0.0), APoint(407.3081640258147, 245.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761223, 239.530477821741, 0.0), APoint(408.23624167612206, 245.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264297, 239.530477821741, 0.0), APoint(408.44240451674955, 244.80856301206086, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.09239697673706, 239.530477821741, 0.0), APoint(408.4424045167498, 243.8804853617537, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.02047462704377, 239.530477821741, 0.0), APoint(408.44240451674955, 242.95240771144677, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735115, 239.530477821741, 0.0), APoint(408.44240451674955, 242.02433006113938, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765854, 239.530477821741, 0.0), APoint(408.44240451674955, 241.096252410832, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.8047075779659, 239.530477821741, 0.0), APoint(408.44240451674955, 240.1681747605246, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 238.9112618648296, 0.0), APoint(400.81162047366433, 239.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 237.98318421452268, 0.0), APoint(401.7396981239715, 239.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 237.0551065642153, 0.0), APoint(402.66777577427865, 239.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 236.1270289139079, 0.0), APoint(403.59585342458604, 239.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 235.19895126360052, 0.0), APoint(404.5239310748934, 239.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 234.27087361329313, 0.0), APoint(405.4520087252008, 239.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755082, 233.53047782174076, 0.0), APoint(406.3800863755082, 239.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258156, 233.53047782174076, 0.0), APoint(407.30816402581536, 239.53047782174053, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.236241676123, 233.53047782174076, 0.0), APoint(408.236241676123, 239.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.16431932643036, 233.53047782174076, 0.0), APoint(408.44240451675023, 238.80856301206063, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767375, 233.53047782174053, 0.0), APoint(408.4424045167509, 237.88048536175393, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270447, 233.530477821741, 0.0), APoint(408.4424045167507, 236.952407711447, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735206, 233.530477821741, 0.0), APoint(408.4424045167516, 236.02433006114052, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765945, 233.530477821741, 0.0), APoint(408.4424045167523, 235.0962524108338, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796684, 233.530477821741, 0.0), APoint(408.44240451675273, 234.16817476052688, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167498, 232.91126186482916, 0.0), APoint(392.5616204736616, 233.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451674955, 231.98318421452177, 0.0), APoint(393.48969812396876, 233.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451674955, 231.05510656421438, 0.0), APoint(394.4177757742759, 233.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451674955, 230.127028913907, 0.0), APoint(395.3458534245833, 233.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451674955, 229.1989512635996, 0.0), APoint(396.2739310748907, 233.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451674955, 228.27087361329222, 0.0), APoint(397.2020087251981, 233.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(392.1300863755057, 227.530477821741, 0.0), APoint(398.13008637550547, 233.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.0581640258131, 227.530477821741, 0.0), APoint(399.05816402581286, 233.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.98624167612047, 227.530477821741, 0.0), APoint(399.98624167612024, 233.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.91431932642786, 227.530477821741, 0.0), APoint(400.1924045167491, 232.80856301206222, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.84239697673524, 227.530477821741, 0.0), APoint(400.1924045167498, 231.88048536175552, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.7704746270424, 227.53047782174144, 0.0), APoint(400.19240451674955, 230.9524077114486, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(397.6985522773498, 227.53047782174144, 0.0), APoint(400.19240451675023, 230.02433006114188, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(398.6266299276572, 227.53047782174144, 0.0), APoint(400.19240451675023, 229.0962524108345, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(399.55470757796456, 227.53047782174144, 0.0), APoint(400.1924045167509, 228.1681747605278, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167493, 226.9112618648296, 0.0), APoint(392.5616204736607, 227.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167493, 225.98318421452245, 0.0), APoint(393.48969812396786, 227.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167493, 225.05510656421507, 0.0), APoint(394.417775774275, 227.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167493, 224.12702891390768, 0.0), APoint(395.3458534245824, 227.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167493, 223.1989512636003, 0.0), APoint(396.2739310748898, 227.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167493, 222.2708736132929, 0.0), APoint(397.2020087251972, 227.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(392.1300863755048, 221.530477821741, 0.0), APoint(398.13008637550456, 227.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.0581640258122, 221.530477821741, 0.0), APoint(399.05816402581195, 227.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.98624167611956, 221.530477821741, 0.0), APoint(399.98624167611933, 227.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.91431932642695, 221.530477821741, 0.0), APoint(400.19240451674887, 226.8085630120629, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.84239697673434, 221.530477821741, 0.0), APoint(400.19240451674887, 225.88048536175552, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.7704746270415, 221.53047782174144, 0.0), APoint(400.19240451674864, 224.9524077114486, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(397.6985522773484, 221.530477821741, 0.0), APoint(400.19240451674864, 224.0243300611412, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(398.6266299276558, 221.530477821741, 0.0), APoint(400.19240451674864, 223.0962524108338, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(399.5547075779632, 221.530477821741, 0.0), APoint(400.19240451674864, 222.16817476052643, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-090', APoint(401.3121729414843, 204.65862849603846, 0.0), 1.875)
entity.Color = 1

entity = acad.model.AddText('i-012', APoint(329.05438256718026, 265.450604270878, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-023', APoint(329.05438256718026, 259.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-030', APoint(329.05438256718026, 253.45060427087788, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-039', APoint(329.05438256718026, 247.45060427087788, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-040', APoint(335.80438256717935, 247.45060427087788, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-031', APoint(335.80438256717935, 253.45060427087788, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-024', APoint(335.80438256717935, 259.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-013', APoint(335.80438256717935, 265.450604270878, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-002', APoint(335.78919988083, 271.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-008', APoint(369.1072545483114, 271.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-009', APoint(377.3424045167525, 271.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-010', APoint(385.5924045167525, 271.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-011', APoint(393.8424045167525, 271.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-019', APoint(369.10725454831135, 265.450604270878, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-020', APoint(377.3424045167525, 265.450604270878, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-021', APoint(385.5924045167525, 265.450604270878, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-022', APoint(393.8424045167525, 265.450604270878, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-026', APoint(369.10725454831135, 259.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-027', APoint(377.3424045167525, 259.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-028', APoint(385.5924045167525, 259.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-029', APoint(393.8424045167525, 259.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-035', APoint(369.10725454831135, 253.45060427087788, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-036', APoint(377.3424045167525, 253.45060427087788, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-037', APoint(385.5924045167525, 253.45060427087788, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-038', APoint(393.8424045167525, 253.45060427087785, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-042', APoint(369.10725454831135, 247.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-043', APoint(377.3424045167525, 247.45060427087788, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-044', APoint(385.5924045167525, 247.45060427087788, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-045', APoint(393.8424045167525, 247.45060427087788, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('وزن کل آرماتور مورد نیاز', APoint(349.02859428883676, 196.78516817530138, 0.0), 1.8)
entity.Color = 1

entity = acad.model.AddText('(Kg)', APoint(375.6643191906196, 196.96900881131748, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-091', APoint(381.4255070372601, 196.76495762539972, 0.0), 1.875)
entity.Color = 1

entity = acad.model.AddLine(APoint(320.69261141489915, 194.5304778217412, 0.0), APoint(408.4424045167525, 194.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('10', APoint(323.2163732246054, 217.37873384487318, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('i-081', APoint(329.05438256718026, 217.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-082', APoint(335.78919988083, 217.66256247382648, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddText('i-085', APoint(369.10725454831135, 217.4947039320718, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-086', APoint(377.3424045167525, 217.38275789371906, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('i-087', APoint(385.5924045167525, 217.3553104647698, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(320.69261141489915, 215.53047782174121, 0.0), APoint(408.4424045167525, 215.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('(1m)', APoint(393.5052494786587, 279.32898721149456, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(400.1924045167534, 220.91126186483007, 0.0), APoint(400.81162047366456, 221.53047782174121, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 219.98318421452268, 0.0), APoint(401.7396981239717, 221.53047782174121, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 219.0551065642153, 0.0), APoint(402.66777577427865, 221.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 218.1270289139079, 0.0), APoint(403.59585342458604, 221.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 217.19895126360052, 0.0), APoint(404.5239310748934, 221.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 216.27087361329313, 0.0), APoint(405.4520087252008, 221.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755082, 215.53047782174076, 0.0), APoint(406.3800863755082, 221.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258156, 215.53047782174076, 0.0), APoint(407.3081640258156, 221.53047782174076, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.236241676123, 215.53047782174076, 0.0), APoint(408.2362416761232, 221.530477821741, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.16431932643036, 215.53047782174076, 0.0), APoint(408.4424045167534, 220.80856301206381, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767375, 215.53047782174053, 0.0), APoint(408.4424045167534, 219.88048536175643, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270447, 215.530477821741, 0.0), APoint(408.4424045167532, 218.9524077114495, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735206, 215.530477821741, 0.0), APoint(408.4424045167532, 218.0243300611421, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765945, 215.530477821741, 0.0), APoint(408.4424045167534, 217.09625241083495, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796684, 215.530477821741, 0.0), APoint(408.4424045167534, 216.16817476052756, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-088', APoint(393.8424045167525, 217.3553104647698, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091379, 218.0109376956913, 0.0), APoint(359.67258082251556, 218.0109376956913, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.67258082251556, 218.0109376956913, 0.0), APoint(359.67258082251556, 219.54607984265007, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-083', APoint(352.82956682788245, 218.38376202757655, 0.0), 1.3125)


entity = acad.model.AddText('i-084', APoint(359.9875729588912, 217.98767638887009, 0.0), 1.3125)


entity = acad.model.AddText('جزئیات دیوارهای هدایت آب', APoint(296.791352402578, 71.8895834078578, 0.0), 3.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.13658276873866, 69.9151988460701, 0.0), APoint(408.6007428102066, 69.9151988460701, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.13658276873866, 35.75072186965133, 0.0), APoint(206.13658276873866, 69.9151988460701, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.13658276873866, 57.19848230414516, 0.0), APoint(408.6007428102066, 57.198482304145045, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('دیوار', APoint(207.99332054852312, 62.69278919685564, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('مقطع 3-3', APoint(317.3211930537309, 67.13036946344153, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('طول دیوار', APoint(215.731096517874, 62.1322761273841, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(214.61667962934462, 69.9151988460701, 0.0), APoint(214.61667962934462, 35.75072186965133, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(214.61667962934462, 65.72327429511938, 0.0), APoint(408.6007428102066, 65.72327429511938, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(253.11653101334377, 65.72327429511938, 0.0), APoint(253.11653101334377, 35.75072186965133, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.01775239053404, 65.72327429511938, 0.0), APoint(240.01775239053404, 35.75072186965133, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.33923757397952, 65.72327429511938, 0.0), APoint(226.33923757397952, 35.75072186965133, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W', APoint(219.04763168903173, 57.983280778589574, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('m (min)', APoint(303.1623172948048, 58.35186234409673, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('ارتفاع پی', APoint(302.2548438433096, 62.339657006238895, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(314.60889228584074, 65.72327429511938, 0.0), APoint(314.60889228584074, 35.75072186965133, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('کد زیر پی', APoint(256.68753309354634, 62.648545901210355, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('کد روی پی', APoint(288.67566308142614, 60.47499199449669, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(300.7950477920567, 65.72327429511938, 0.0), APoint(300.7950477920567, 35.75072186965133, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W1', APoint(208.33137632174112, 53.590857317647306, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.13658276873866, 51.8365421955217, 0.0), APoint(408.6007428102066, 51.8365421955217, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W2', APoint(208.33137632174112, 48.22891720902396, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.13658276873866, 46.47460208689813, 0.0), APoint(408.6007428102066, 46.47460208689813, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W3', APoint(208.33137632174112, 42.866977100400504, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.13658276873866, 41.11266197827479, 0.0), APoint(408.6007428102066, 41.11266197827479, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W4', APoint(208.33137632174112, 37.505036991777274, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.13658276873866, 35.75072186965133, 0.0), APoint(408.6007428102066, 35.75072186965133, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-106', APoint(217.78097239173076, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-109', APoint(259.6773836550901, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-112', APoint(305.80502733554385, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('عرض پی', APoint(331.4656002024467, 62.6723491023597, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('f (min)', APoint(331.9213532377462, 58.35186234409673, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-120', APoint(217.78097239173076, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-123', APoint(259.6773836550901, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-126', APoint(305.80502733554385, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-134', APoint(217.78097239173076, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-136', APoint(259.6773836550901, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-139', APoint(305.80502733554385, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-147', APoint(217.78097239173076, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-150', APoint(259.6773836550901, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-153', APoint(305.80502733554385, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('در ابتدای دیوار', APoint(254.21463618300368, 58.36162795460905, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('در انتهای دیوار', APoint(271.7642330456965, 58.5936658399753, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(270.50461500427264, 65.72327429511938, 0.0), APoint(270.50461500427264, 35.75072186965133, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(287.57858156394377, 65.72327429511938, 0.0), APoint(287.57858156394377, 35.75072186965133, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('کد زیر پی', APoint(273.1203370969333, 62.648545901210355, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('i-110', APoint(277.7642026801377, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-124', APoint(277.7642026801377, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-137', APoint(277.7642026801377, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-151', APoint(277.7642026801377, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-111', APoint(292.62683199408275, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-125', APoint(292.62683199408275, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-138', APoint(292.62683199408275, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-152', APoint(292.62683199408275, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('m (max)', APoint(316.6903806581813, 58.35186234409673, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('ارتفاع پی', APoint(316.61360292270547, 62.339657006238895, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(328.97745733277134, 65.72327429511938, 0.0), APoint(328.97745733277134, 35.75072186965133, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-113', APoint(319.3330906989213, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-127', APoint(319.3330906989213, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-140', APoint(319.3330906989213, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-154', APoint(319.3330906989213, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(342.3845635176731, 65.72327429511938, 0.0), APoint(342.3845635176731, 35.75072186965133, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-114', APoint(333.0433375753755, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('عرض پی', APoint(345.02665530873946, 62.6723491023597, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('f (max)', APoint(344.79550196597484, 58.35186234409673, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(355.6277993761805, 65.72327429511938, 0.0), APoint(355.6277993761805, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(368.87103523468704, 65.72327429511938, 0.0), APoint(368.87103523468704, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.11427109319357, 65.72327429511938, 0.0), APoint(382.11427109319357, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.3575069517001, 65.72327429511938, 0.0), APoint(395.3575069517001, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.6007428102066, 69.9151988460701, 0.0), APoint(408.6007428102066, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-115', APoint(345.91748630360325, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-129', APoint(345.91748630360325, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-142', APoint(345.91748630360325, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-156', APoint(345.91748630360325, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('h (max)', APoint(228.31880129540787, 58.55471331746435, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('ارتفاع', APoint(229.85054440533895, 62.44120815475844, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('h (min)', APoint(241.97732403431928, 58.55471331746435, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('ارتفاع', APoint(243.33182546583976, 62.44120815475844, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('i-107', APoint(229.79158451580952, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-121', APoint(229.79158451580952, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-134', APoint(229.79158451580952, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-148', APoint(229.79158451580952, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-149', APoint(242.87490078214432, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-135', APoint(242.87490078214432, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-122', APoint(242.87490078214432, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-108', APoint(242.87490078214432, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-116', APoint(359.6936796187838, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-130', APoint(359.6936796187838, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-143', APoint(359.6936796187838, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-157', APoint(359.6936796187838, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-117', APoint(372.34594012575417, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-118', APoint(386.18015133579775, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-132', APoint(386.18015133579775, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-145', APoint(386.18015133579775, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-159', APoint(386.18015133579775, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-119', APoint(398.82663900262924, 53.58535070684127, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s1', APoint(360.6992879011932, 62.26712392162153, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(max)', APoint(358.07829927507646, 58.36767855809421, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s1', APoint(373.9425237596988, 62.26712392162153, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(min)', APoint(371.3215351335821, 58.36767855809421, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s2', APoint(387.18575961820534, 62.267123921621305, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(max)', APoint(384.5647709920895, 58.3676785580941, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s2', APoint(400.42899547671186, 62.267123921621305, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(min)', APoint(397.80800685059603, 58.3676785580941, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-133', APoint(398.82663900262924, 48.2234105982177, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-146', APoint(398.82663900262924, 42.86147048959435, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-160', APoint(398.82663900262924, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-131', APoint(372.34594012575417, 48.22341059821804, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-144', APoint(372.34594012575417, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-158', APoint(372.34594012575417, 37.49953038097112, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-128', APoint(333.0433375753755, 48.22341059821804, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-141', APoint(333.0433375753755, 42.86147048959458, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-155', APoint(333.0433375753755, 37.49953038097112, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(0.0, 0.0, 0.0), APoint(-1.7664723202258301, 0.0, 0.0))



entity = acad.model.AddLine(APoint(0.0, 0.0, 0.0), APoint(419.99999999992724, 0.0, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(419.99999999992724, 0.0, 0.0), APoint(419.99999999992724, 297.00000000000716, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(0.0, 297.00000000000716, 0.0), APoint(0.0, 0.0, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(415.0, 4.999999999999886, 0.0), APoint(415.0, 292.0, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(5.0, 292.0, 0.0), APoint(5.0, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(5.0, 4.999999999999886, 0.0), APoint(415.0, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(415.0, 25.0, 0.0), APoint(5.0, 25.0, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(296.64869948316027, 24.999999999999886, 0.0), APoint(296.64869948316027, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(254.53226096911112, 24.999999999999886, 0.0), APoint(254.53226096911112, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(212.41582245506015, 24.999999999999886, 0.0), APoint(212.41582245506015, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.299383941011, 24.999999999999886, 0.0), APoint(170.299383941011, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(128.18294542696094, 24.999999999999886, 0.0), APoint(128.18294542696094, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.06650691291134, 24.999999999999886, 0.0), APoint(86.06650691291134, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText(': شماره نقشه', APoint(198.71097822126467, 22.072322370501524, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText(': تاریخ ابلاغ', APoint(197.69374512237755, 12.305559378681664, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText(': محل آبرو', APoint(159.38218719303973, 12.219192808258526, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(296.64869948316027, 14.999999999999773, 0.0), APoint(86.06650691291134, 15.0, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText(': زاویه تورب', APoint(114.66763273260949, 12.147955604483059, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText(': دهانه آبرو', APoint(158.8616113019698, 22.124566619728512, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('بدون مقاس', APoint(9.082975376367358, 10.257882124873959, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText(': حداکثر ارتفاع خاک روی آبرو', APoint(96.76834717021848, 21.999326525113247, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('=i-177', APoint(95.19832279330512, 7.3336372942450225, 0.0), 1.95)
entity.Color = 7

entity = acad.model.AddLine(APoint(94.84454949240836, 8.753809941266148, 0.0), APoint(93.0458950890897, 7.3083636728994055, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.96769339567963, 8.71474432190304, 0.0), APoint(95.00095674294923, 7.542761624139251, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(93.00679424238467, 8.011553997401236, 0.0), 0.7042765853597772, 1.6263440515008603, 4.7679367050899675)
entity.Color = 1

entity = acad.model.AddText(': پیمانکار', APoint(242.8157185840837, 22.091368192971686, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText(': کارفرما', APoint(286.38095070545296, 22.036906765212052, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText(': مهندس مشاور', APoint(282.64531803115824, 12.206080396302127, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText(': عنوان پروژه', APoint(240.61148489832794, 12.016791073403056, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-176', APoint(90.16912161954542, 16.748138742348033, 0.0), 2.0)
entity.Color = 7

entity = acad.model.AddLine(APoint(338.76513799721124, 25.0, 0.0), APoint(338.76513799721124, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText(': موضوع نقشه', APoint(323.9975820023019, 21.79971422139988, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-169', APoint(301.76777422148143, 17.964747298063685, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-170', APoint(301.76777422148143, 14.500738236698902, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-171', APoint(301.76777422148143, 11.166459578209922, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(11.631448686285239, 25.0, 0.0), APoint(11.631448686285239, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-174', APoint(349.22695857402596, 14.572511580924584, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-175', APoint(348.9464961603944, 7.8906915393545205, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText(': توضیحات', APoint(73.108729720464, 21.843339434359564, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-180', APoint(21.706971832195904, 12.854608686151096, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-181', APoint(21.64362394905129, 9.013810570597686, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-178', APoint(21.919262370884553, 19.195197129738062, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-179', APoint(21.717077853479623, 16.522421907421972, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText(': شماره نقشه همسان', APoint(320.10515583988035, 6.591915817642985, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-172', APoint(300.0213153431714, 6.479800353880023, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(338.76513799721124, 9.537644467135578, 0.0), APoint(296.64869948316027, 9.537644467135578, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-173', APoint(349.14922402933644, 20.926001891046212, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(415.0, 25.0, 0.0), APoint(5.0, 25.0, 0.0))



entity = acad.model.AddLine(APoint(296.64869948316027, 24.999999999999886, 0.0), APoint(296.64869948316027, 4.999999999999886, 0.0))



entity = acad.model.AddLine(APoint(254.53226096911112, 24.999999999999886, 0.0), APoint(254.53226096911112, 4.999999999999886, 0.0))



entity = acad.model.AddLine(APoint(212.41582245506015, 24.999999999999886, 0.0), APoint(212.41582245506015, 4.999999999999886, 0.0))



entity = acad.model.AddLine(APoint(170.299383941011, 24.999999999999886, 0.0), APoint(170.299383941011, 4.999999999999886, 0.0))



entity = acad.model.AddLine(APoint(128.18294542696094, 24.999999999999886, 0.0), APoint(128.18294542696094, 4.999999999999886, 0.0))



entity = acad.model.AddLine(APoint(86.06650691291134, 24.999999999999886, 0.0), APoint(86.06650691291134, 4.999999999999886, 0.0))



entity = acad.model.AddLine(APoint(296.64869948316027, 14.999999999999773, 0.0), APoint(86.06650691291134, 15.0, 0.0))



entity = acad.model.AddLine(APoint(0.0, 0.0, 0.0), APoint(0.0, 0.020340593868127144, 0.0))



entity = acad.model.AddText('-1', APoint(82.21759040567622, 19.197426807044167, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('-2', APoint(82.44655450435903, 12.901963324328108, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(419.99999999992724, 297.00000000000716, 0.0), APoint(0.0, 297.00000000000716, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(415.0, 292.0, 0.0), APoint(5.0, 292.0, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.07301469313914, 258.8015247304475, 0.0), APoint(110.42192067532267, 253.00104941953418, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(137.32301469314183, 276.2663703734348, 0.0), APoint(140.67192067532537, 270.46589506252155, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(109.05589527153823, 253.36707482331863, 0.0), APoint(141.03794607910982, 271.8319204663059, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.109761140574015, 118.29816844402245, 0.0), APoint(45.59185184783892, 118.87270177636168, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.28236296658157, 117.67064709419637, 0.0), APoint(52.764453673846475, 118.2451804265356, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.06745145376043, 124.56504708226717, 0.0), APoint(58.254183996624434, 124.78758626107961, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.454964792588626, 117.04312574437064, 0.0), APoint(59.93705549985353, 117.61765907670987, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.24005327976748, 123.93752573244144, 0.0), APoint(65.72214398703238, 124.51205906478067, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.62756661859646, 116.4156043945447, 0.0), APoint(67.10965732586136, 116.99013772688393, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.41265510577531, 123.3100043826155, 0.0), APoint(72.89474581304022, 123.88453771495473, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.8001684446039, 115.78808304471875, 0.0), APoint(74.2822591518688, 116.36261637705798, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.58525693178274, 122.68248303278958, 0.0), APoint(80.06734763904764, 123.2570163651288, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.97277027061135, 115.16056169489276, 0.0), APoint(81.45486097787625, 115.73509502723199, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.7578587577902, 122.05496168296357, 0.0), APoint(87.2399494650551, 122.6294950153028, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.14537209661913, 114.5330403450665, 0.0), APoint(88.62746280388403, 115.10757367740572, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.93046058379804, 121.42744033313724, 0.0), APoint(94.41255129106294, 122.00197366547647, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.31797392262683, 113.9055189952406, 0.0), APoint(95.80006462989174, 114.48005232757983, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.10306240980569, 120.7999189833114, 0.0), APoint(101.58515311707059, 121.37445231565063, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.94307226798742, 113.81726199799004, 0.0), APoint(102.97266645589922, 113.85253097775383, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.27566423581317, 120.1723976334854, 0.0), APoint(108.52988076940579, 120.47536110069126, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.06745160355414, 124.56504822355143, 0.0), APoint(58.66516842240919, 124.51275477790283, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.24005342981471, 123.93752687576828, 0.0), APoint(65.83777024866976, 123.88523343011968, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.41265525607527, 123.31000552798514, 0.0), APoint(73.01037207493032, 123.25771208233654, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.93046073485706, 121.42744148463574, 0.0), APoint(94.52817755371211, 121.37514803898713, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.10306256111762, 120.79992013685259, 0.0), APoint(101.70077937997267, 120.74762669120399, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.27566438737819, 120.17239878906945, 0.0), APoint(108.87338120623323, 120.12010534342085, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.58525708233589, 122.68248418020202, 0.0), APoint(80.18297390119093, 122.63019073455342, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.75785890859645, 122.05496283241888, 0.0), APoint(87.3555757274515, 122.00266938677028, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.1097612871634, 118.29816958211761, 0.0), APoint(45.70747810601845, 118.24587613646901, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.28236311342397, 117.67064823433446, 0.0), APoint(52.88007993227902, 117.61835478868586, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.45496493968454, 117.04312688655132, 0.0), APoint(60.052681758539585, 116.99083344090272, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.6275667659451, 116.41560553876818, 0.0), APoint(67.22528358480015, 116.36331209311957, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.80016859220567, 115.78808419098503, 0.0), APoint(74.39788541106071, 115.73579074533643, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.31797407098743, 113.90552014763563, 0.0), APoint(95.91569088984248, 113.85322670198703, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.97277041846625, 115.16056284320192, 0.0), APoint(81.5704872373213, 115.10826939755331, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.14537224472681, 114.53304149541877, 0.0), APoint(88.74308906358186, 114.48074804977017, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.70744660914304, 118.2458268568773, 0.0), APoint(45.591820500606495, 118.87265363569612, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.88004837885269, 117.61830542073697, 0.0), APoint(52.764422270316146, 118.2451321995558, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.05265014856249, 116.99078398459844, 0.0), APoint(59.937024040025946, 117.61761076341726, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.66513684612394, 124.51270533042431, 0.0), APoint(58.61376829146473, 124.79118210402805, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.22525191827198, 116.363262548459, 0.0), APoint(67.10962580973543, 116.99008932727783, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.83773861583343, 123.88518389428488, 0.0), APoint(65.72211250729688, 124.5120106731037, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.3978536879815, 115.73574111231981, 0.0), APoint(74.28222757944495, 116.36256789113864, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.01034038554295, 123.25766245814569, 0.0), APoint(72.8947142770064, 123.88448923696451, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.5704554576916, 115.10821967617949, 0.0), APoint(81.45482934915505, 115.73504645499831, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.18294215525304, 122.63014102200536, 0.0), APoint(80.0673160467165, 123.25696780082419, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.74305722740091, 114.48069824004095, 0.0), APoint(88.62743111886437, 115.10752501885977, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.35554392496236, 122.00261958586682, 0.0), APoint(87.23991781642582, 122.62944636468565, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.91565899711057, 113.85317680390085, 0.0), APoint(95.80003288857402, 114.48000358271968, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.52814569467202, 121.37509814972672, 0.0), APoint(94.41251958613547, 122.00192492854555, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.97906506583567, 113.81762192596784, 0.0), APoint(102.97263465828415, 113.85248214657915, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.70074746438215, 120.7475767135862, 0.0), APoint(101.5851213558456, 121.37440349240502, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.87334923409146, 120.12005527744812, 0.0), APoint(108.84426393991319, 120.27773109557879, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.60035247030207, 114.65782794820274, 0.0), APoint(47.37923742461415, 115.46959344879158, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.9469719220471, 124.39901395526888, 0.0), APoint(56.72585687635918, 125.21077945585773, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.61951895280481, 113.36402646483816, 0.0), APoint(58.051650731329985, 113.81440064086092, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.61938522876292, 122.74382114733822, 0.0), APoint(67.39827018307501, 123.55558664792707, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.29179853547855, 121.08862833940736, 0.0), APoint(77.7239928369588, 121.53906767778517, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695881, 121.53906767778517, 0.0), APoint(78.07068348979065, 121.90039383999621, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.96421184219423, 119.43343553147679, 0.0), APoint(88.74309679650632, 120.24520103206564, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.63662514890999, 117.77824272354583, 0.0), APoint(99.41551010322208, 118.59000822413468, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(109.30903845562567, 116.12304991561527, 0.0), APoint(110.08792340993776, 116.93481541620412, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.488340378568395, 114.51849447350006, 0.0), APoint(47.37785788324503, 115.46819304039526, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.101936641168805, 113.36885064172179, 0.0), APoint(58.05026728155681, 113.81299626526405, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.83495983531089, 124.25968048124535, 0.0), APoint(56.72447733998752, 125.20937904814056, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.50736923362219, 122.60448370611464, 0.0), APoint(67.39688673829882, 123.55418227300984, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.17977863193381, 120.94928693098471, 0.0), APoint(78.06929613661045, 121.89898549787992, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.85218803024526, 119.29409015585276, 0.0), APoint(88.74170553492189, 120.24378872274796, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.52459742855703, 117.63889338072171, 0.0), APoint(99.41411493323366, 118.58859194761692, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(110.19700682686853, 115.98369660558919, 0.0), APoint(110.08652433154516, 116.9333951724844, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.94561274475473, 124.39758722914272, 0.0), APoint(56.83498019863485, 124.25965415849325, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.61802220119803, 122.74239037981647, 0.0), APoint(67.50738965507816, 122.604457309167, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.29043165764134, 121.08719353049023, 0.0), APoint(77.72399283695897, 121.01995200448567, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.6352505705276, 117.77679983183772, 0.0), APoint(99.52461802440773, 117.63886676118825, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(109.30766002697091, 116.12160298251148, 0.0), APoint(110.19702748085103, 115.98366991186201, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695859, 121.01995200448573, 0.0), APoint(78.17979911152085, 120.94926045984086, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.96284111408403, 119.43199668116408, 0.0), APoint(88.85220856796415, 119.29406361051461, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.59899329420681, 114.6564012264429, 0.0), APoint(47.488360748086926, 114.51846815579343, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.40938421097425, 121.09219381315525, 0.0), APoint(49.10956953084715, 121.36096977531422, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.81160804944907, 124.31750535906295, 0.0), APoint(57.51179336932197, 124.58628132122192, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.976230893684416, 113.84069336059429, 0.0), APoint(46.67641621355732, 114.10946932275326, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.378454732159234, 117.06600490650199, 0.0), APoint(55.078640052032135, 117.33478086866096, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.78067857063405, 120.29131645240969, 0.0), APoint(63.48086389050695, 120.56009241456866, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.18290240910886, 123.51662799831739, 0.0), APoint(71.88308772898176, 123.78540396047636, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.74974909181836, 116.26512754575617, 0.0), APoint(69.44993441169126, 116.53390350791514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.15197293029317, 119.49043909166387, 0.0), APoint(77.723992836958, 119.71001696115681, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695813, 119.71001696115673, 0.0), APoint(77.8521582501662, 119.75921505382276, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.55419676876811, 122.71575063757149, 0.0), APoint(86.25438208864101, 122.98452659973046, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.12104345147849, 115.46425018501054, 0.0), APoint(83.82122877135139, 115.73302614716951, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.52326728995288, 118.68956173091817, 0.0), APoint(92.22345260982578, 118.95833769307714, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.9254911284277, 121.91487327682587, 0.0), APoint(100.6256764483006, 122.18364923898484, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.49233781113719, 114.66337282426502, 0.0), APoint(98.19252313101009, 114.932148786424, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.894561649612, 117.88868437017273, 0.0), APoint(106.5947469694849, 118.1574603323317, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.98124747844304, 113.90764375009417, 0.0), APoint(112.56381749066975, 114.13127142567815, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.92549233778993, 121.91487365865609, 0.0), APoint(100.42291488132295, 121.57935791657364, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.89456286018623, 117.88868475366671, 0.0), APoint(106.39198540371925, 117.55316901158426, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.55419797378114, 122.7157510181665, 0.0), APoint(86.05162051731416, 122.38023527608405, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.52326849617789, 118.68956211317683, 0.0), APoint(92.02069103971091, 118.35404637109438, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.49233901857419, 114.66337320818745, 0.0), APoint(97.9897615621072, 114.327857466105, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.18290360977356, 123.51662837767621, 0.0), APoint(71.68032615330658, 123.18111263559376, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.15197413216985, 119.49043947268683, 0.0), APoint(77.64939667570287, 119.15492373060438, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.12104465456605, 115.46425056769755, 0.0), APoint(83.61846719809907, 115.1287348256151, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.81160924576508, 124.317505737187, 0.0), APoint(57.3090317892981, 123.98198999510456, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.78067976816138, 120.29131683219762, 0.0), APoint(63.278102311694404, 119.95580109011517, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.74975029055767, 116.26512792720824, 0.0), APoint(69.24717283409069, 115.92961218512579, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.409385404152324, 121.09219419170783, 0.0), APoint(48.90680794768535, 120.75667844962538, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.378455926548625, 117.06600528671845, 0.0), APoint(54.87587847008165, 116.730489544636, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.97623208493726, 113.8406937412387, 0.0), APoint(46.473654628470285, 113.50517799915625, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.47361525330387, 113.50517287217443, 0.0), APoint(46.676378023402066, 114.10946455769204, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.90676856446603, 120.75667330695774, 0.0), APoint(49.109531334564224, 121.36096499247535, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.87583902060376, 116.73048440023831, 0.0), APoint(55.07860179070196, 117.33477608575592, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.30899233176592, 123.98198483502162, 0.0), APoint(57.51175510186412, 124.58627652053923, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.27806278790345, 119.95579592830175, 0.0), APoint(63.48082555800165, 120.56008761381936, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.247133244041, 115.92960702158197, 0.0), APoint(69.44989601413918, 116.53389870709958, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.68028655520314, 123.18110745636528, 0.0), APoint(71.88304932530133, 123.78539914188289, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.64935701134074, 119.15491854964542, 0.0), APoint(77.72399283695839, 119.37735489158652, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.7239928369583, 119.37735489158638, 0.0), APoint(77.85211978143877, 119.75921023516268, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.61842746747828, 115.12872964292553, 0.0), APoint(83.82119023757647, 115.73302132844314, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.05158077864044, 122.38023007770884, 0.0), APoint(86.25434354873863, 122.98452176322645, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.02065123477809, 118.35404117098929, 0.0), APoint(92.22341400487628, 118.9583328565069, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.98972169091576, 114.32785226426995, 0.0), APoint(98.19248446101395, 114.93214394978756, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.42287500207792, 121.57935269905326, 0.0), APoint(100.6256377721761, 122.18364438457087, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.39194545821539, 117.55316379233317, 0.0), APoint(106.59470822831358, 118.15745547785077, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.49045332879126, 113.91273580859774, 0.0), APoint(112.56377868445126, 114.13126657113123, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(42.60471494497403, 116.55598303936559, 0.0), APoint(42.60471494497403, 116.55598303936559, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.77737872367288, 120.52510755650245, 0.0), APoint(47.77737872367288, 120.52510755650245, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(42.48311639180203, 113.22704450105272, 0.0), APoint(42.48311639180203, 113.22704450105272, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.65578017050088, 117.19616901818958, 0.0), APoint(47.65578017050088, 117.19616901818958, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.97124755045216, 121.27487059254801, 0.0), APoint(52.97124755045216, 121.27487059254801, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.53418161732711, 113.86723047987579, 0.0), APoint(47.53418161732711, 113.86723047987579, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.84964899727838, 117.94593205423422, 0.0), APoint(52.84964899727838, 117.94593205423422, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.10561487670781, 121.978976521417, 0.0), APoint(58.10561487670781, 121.978976521417, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.72805044410539, 114.61699351592114, 0.0), APoint(52.72805044410539, 114.61699351592114, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.984016323534824, 118.65003798310391, 0.0), APoint(57.984016323534824, 118.65003798310391, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.15668010223368, 122.61916250024078, 0.0), APoint(63.15668010223368, 122.61916250024078, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.862417770361844, 115.32109944479062, 0.0), APoint(57.862417770361844, 115.32109944479062, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.0350815490607, 119.29022396192748, 0.0), APoint(63.0350815490607, 119.29022396192748, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.35054892901198, 123.36892553628591, 0.0), APoint(68.35054892901198, 123.36892553628591, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.91348299588791, 115.96128542361434, 0.0), APoint(62.91348299588791, 115.96128542361434, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.22895037583919, 120.03998699797278, 0.0), APoint(68.22895037583919, 120.03998699797278, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.48491625526863, 124.07303146515555, 0.0), APoint(73.48491625526863, 124.07303146515555, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.10735182266691, 116.71104845966003, 0.0), APoint(68.10735182266691, 116.71104845966003, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.36331770209635, 120.74409292684281, 0.0), APoint(73.36331770209635, 120.74409292684281, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.53598148079531, 124.71321744397977, 0.0), APoint(78.53598148079531, 124.71321744397977, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.24171914892246, 117.41515438852952, 0.0), APoint(73.24171914892246, 117.41515438852952, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.41438292762193, 121.38427890566687, 0.0), APoint(78.41438292762193, 121.38427890566687, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.1201205957502, 114.086215850217, 0.0), APoint(73.1201205957502, 114.086215850217, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.292784374449, 118.05534036735374, 0.0), APoint(78.292784374449, 118.05534036735374, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.60825175440027, 122.13404194171217, 0.0), APoint(83.60825175440027, 122.13404194171217, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.17118582127652, 114.72640182904038, 0.0), APoint(78.17118582127652, 114.72640182904038, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.4866532012278, 118.80510340339882, 0.0), APoint(83.4866532012278, 118.80510340339882, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.74261908065724, 122.8381478705816, 0.0), APoint(88.74261908065724, 122.8381478705816, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.36505464805455, 115.47616486508585, 0.0), APoint(83.36505464805455, 115.47616486508585, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.62102052748399, 119.50920933226863, 0.0), APoint(88.62102052748399, 119.50920933226863, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.79368430618284, 123.47833384940533, 0.0), APoint(93.79368430618284, 123.47833384940533, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.49942197431126, 116.18027079395566, 0.0), APoint(88.49942197431126, 116.18027079395566, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.67208575300991, 120.1493953110922, 0.0), APoint(93.67208575300991, 120.1493953110922, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.98755313296118, 124.22809688545064, 0.0), APoint(98.98755313296118, 124.22809688545064, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.55048719983698, 116.82045677277907, 0.0), APoint(93.55048719983698, 116.82045677277907, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.86595457978825, 120.8991583471375, 0.0), APoint(98.86595457978825, 120.8991583471375, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.74435602661437, 117.57021980882352, 0.0), APoint(98.74435602661437, 117.57021980882352, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.00032190604381, 121.6032642760063, 0.0), APoint(104.00032190604381, 121.6032642760063, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.62275747344236, 114.24128127051134, 0.0), APoint(98.62275747344236, 114.24128127051134, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.8787233528718, 118.27432573769411, 0.0), APoint(103.8787233528718, 118.27432573769411, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.75712479969881, 114.94538719938105, 0.0), APoint(103.75712479969881, 114.94538719938105, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.92978857839766, 118.91451171651791, 0.0), APoint(108.92978857839766, 118.91451171651791, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.80819002522462, 115.58557317820444, 0.0), APoint(108.80819002522462, 115.58557317820444, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.00205885200272, 116.33533621424966, 0.0), APoint(114.00205885200272, 116.33533621424966, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.053551270167205, 125.1295025964239, 0.0), APoint(56.053551270167205, 125.1295025964239, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.42285589574686, 121.18538547760045, 0.0), APoint(53.42285589574686, 121.18538547760045, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.92625417071574, 121.51496411295608, 0.0), APoint(55.92625417071574, 121.51496411295608, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.71357354116369, 122.01357416723667, 0.0), APoint(59.71357354116369, 122.01357416723667, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.02907730811486, 122.8450260116784, 0.0), APoint(66.02907730811486, 122.8450260116784, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.53247558308374, 123.17460464703403, 0.0), APoint(68.53247558308374, 123.17460464703403, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.3197949535317, 123.67321470131462, 0.0), APoint(72.3197949535317, 123.67321470131462, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.6352987204817, 124.50466654575625, 0.0), APoint(78.6352987204817, 124.50466654575625, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.13869699545057, 124.83424518111188, 0.0), APoint(81.13869699545057, 124.83424518111188, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(40.68933738392544, 115.9112064600544, 0.0), APoint(40.68933738392544, 115.9112064600544, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.476656754373394, 116.40981651433499, 0.0), APoint(44.476656754373394, 116.40981651433499, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.79216052132457, 117.24126835877672, 0.0), APoint(50.79216052132457, 117.24126835877672, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.29555879629344, 117.57084699413235, 0.0), APoint(53.29555879629344, 117.57084699413235, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.082878166741395, 118.06945704841294, 0.0), APoint(57.082878166741395, 118.06945704841294, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.39838193369257, 118.90090889285467, 0.0), APoint(63.39838193369257, 118.90090889285467, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.90178020866144, 119.2304875282103, 0.0), APoint(65.90178020866144, 119.2304875282103, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.6890995791094, 119.7290975824909, 0.0), APoint(69.6890995791094, 119.7290975824909, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.00460334606056, 120.56054942693262, 0.0), APoint(76.00460334606056, 120.56054942693262, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.11422303339685, 122.54976859636616, 0.0), APoint(91.11422303339685, 122.54976859636616, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.90154240384481, 123.04837865064675, 0.0), APoint(94.90154240384481, 123.04837865064675, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.21704617079598, 123.87983049508848, 0.0), APoint(101.21704617079598, 123.87983049508848, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.50800162102888, 120.89012806228818, 0.0), APoint(78.50800162102888, 120.89012806228818, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.29532099147684, 121.38873811656877, 0.0), APoint(82.29532099147684, 121.38873811656877, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.61082475842801, 122.2201899610105, 0.0), APoint(88.61082475842801, 122.2201899610105, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.16146514690408, 113.29715123995322, 0.0), APoint(48.16146514690408, 113.29715123995322, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.66486342187295, 113.62672987530885, 0.0), APoint(50.66486342187295, 113.62672987530885, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.452182792320905, 114.12533992958944, 0.0), APoint(54.452182792320905, 114.12533992958944, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.76768655927208, 114.95679177403117, 0.0), APoint(60.76768655927208, 114.95679177403117, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.27108483424095, 115.2863704093868, 0.0), APoint(63.27108483424095, 115.2863704093868, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.05840420468891, 115.7849804636674, 0.0), APoint(67.05840420468891, 115.7849804636674, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.37390797164008, 116.61643230810913, 0.0), APoint(73.37390797164008, 116.61643230810913, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.87730624660895, 116.94601094346476, 0.0), APoint(75.87730624660895, 116.94601094346476, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.27084702942507, 119.10426153182331, 0.0), APoint(92.27084702942507, 119.10426153182331, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.58635079637624, 119.93571337626504, 0.0), APoint(98.58635079637624, 119.93571337626504, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.08974907134511, 120.26529201162067, 0.0), APoint(101.08974907134511, 120.26529201162067, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.87706844179307, 120.76390206590126, 0.0), APoint(104.87706844179307, 120.76390206590126, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.66462561705664, 117.44462099774535, 0.0), APoint(79.66462561705664, 117.44462099774535, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.98012938400781, 118.27607284218708, 0.0), APoint(85.98012938400781, 118.27607284218708, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.48352765897668, 118.60565147754271, 0.0), APoint(88.48352765897668, 118.60565147754271, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.9556554219541, 115.99159625744134, 0.0), APoint(95.9556554219541, 115.99159625744134, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.45905369692298, 116.32117489279698, 0.0), APoint(98.45905369692298, 116.32117489279698, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.24637306737094, 116.81978494707757, 0.0), APoint(102.24637306737094, 116.81978494707757, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.5618768343221, 117.6512367915193, 0.0), APoint(108.5618768343221, 117.6512367915193, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.06527510929098, 117.98081542687493, 0.0), APoint(111.06527510929098, 117.98081542687493, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.34943400958568, 114.33195572336338, 0.0), APoint(83.34943400958568, 114.33195572336338, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.85283228455455, 114.66153435871901, 0.0), APoint(85.85283228455455, 114.66153435871901, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.64015165500251, 115.1601444129996, 0.0), APoint(89.64015165500251, 115.1601444129996, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.43457973486964, 114.03669830805148, 0.0), APoint(108.43457973486964, 114.03669830805148, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.2218991053176, 114.53530836233207, 0.0), APoint(112.2218991053176, 114.53530836233207, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.4096979625445, 121.30891000561151, 0.0), APoint(103.4096979625445, 121.30891000561151, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.13879942670786, 115.74785905922188, 0.0), APoint(112.13879942670786, 115.74785905922188, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.24727804124008, 114.40461003835482, 0.0), APoint(114.24727804124008, 114.40461003835482, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.07147360082062, 121.5344587229553, 0.0), APoint(98.07147360082062, 121.5344587229553, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.80057506498399, 115.97340777656568, 0.0), APoint(106.80057506498399, 115.97340777656568, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.9090536795162, 114.63015875569862, 0.0), APoint(108.9090536795162, 114.63015875569862, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.73324923909637, 121.76000744029916, 0.0), APoint(92.73324923909637, 121.76000744029916, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.46235070325973, 116.19895649390953, 0.0), APoint(101.46235070325973, 116.19895649390953, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.57082931779195, 114.85570747304247, 0.0), APoint(103.57082931779195, 114.85570747304247, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.3950248773725, 121.98555615764292, 0.0), APoint(87.3950248773725, 121.98555615764292, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.12412634153601, 116.42450521125349, 0.0), APoint(96.12412634153601, 116.42450521125349, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.23260495606823, 115.08125619038643, 0.0), APoint(98.23260495606823, 115.08125619038643, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.78590197981173, 116.65005392859744, 0.0), APoint(90.78590197981173, 116.65005392859744, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.89438059434394, 115.30680490773038, 0.0), APoint(92.89438059434394, 115.30680490773038, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.05680051564829, 122.21110487498699, 0.0), APoint(82.05680051564829, 122.21110487498699, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.7185761539243, 122.4366535923305, 0.0), APoint(76.7185761539243, 122.4366535923305, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.44767761808772, 116.87560264594092, 0.0), APoint(85.44767761808772, 116.87560264594092, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.55615623261994, 115.53235362507385, 0.0), APoint(87.55615623261994, 115.53235362507385, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.38035179220003, 122.6622023096743, 0.0), APoint(71.38035179220003, 122.6622023096743, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.10945325636341, 117.10115136328473, 0.0), APoint(80.10945325636341, 117.10115136328473, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.21793187089563, 115.75790234241767, 0.0), APoint(82.21793187089563, 115.75790234241767, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.04212743047633, 122.88775102701838, 0.0), APoint(66.04212743047633, 122.88775102701838, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.77122889463969, 117.32670008062875, 0.0), APoint(74.77122889463969, 117.32670008062875, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.87970750917191, 115.98345105976169, 0.0), APoint(76.87970750917191, 115.98345105976169, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.703903068752105, 123.11329974436228, 0.0), APoint(60.703903068752105, 123.11329974436228, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.43300453291548, 117.55224879797265, 0.0), APoint(69.43300453291548, 117.55224879797265, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.54148314744769, 116.20899977710559, 0.0), APoint(71.54148314744769, 116.20899977710559, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.365678707028025, 123.33884846170578, 0.0), APoint(55.365678707028025, 123.33884846170578, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.09478017119139, 117.77779751531615, 0.0), APoint(64.09478017119139, 117.77779751531615, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.2032587857236, 116.43454849444909, 0.0), APoint(66.2032587857236, 116.43454849444909, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.756555809467294, 118.0033462326603, 0.0), APoint(58.756555809467294, 118.0033462326603, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.86503442399951, 116.66009721179324, 0.0), APoint(60.86503442399951, 116.66009721179324, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.41833144774318, 118.22889495000373, 0.0), APoint(53.41833144774318, 118.22889495000373, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.526810062275395, 116.88564592913667, 0.0), APoint(55.526810062275395, 116.88564592913667, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.08010708601889, 118.45444366734756, 0.0), APoint(48.08010708601889, 118.45444366734756, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.18858570055111, 117.1111946464805, 0.0), APoint(50.18858570055111, 117.1111946464805, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.85036133882728, 117.3367433638245, 0.0), APoint(44.85036133882728, 117.3367433638245, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.09059025444348, 113.37135513606306, 0.0), APoint(46.09059025444348, 113.37135513606306, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(40.75236589271957, 113.59690385340664, 0.0), APoint(40.75236589271957, 113.59690385340664, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(116.39635762662122, 114.78618940264884, 0.0), APoint(116.39635762662122, 114.78618940264884, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.9302595583337, 124.44595305550087, 0.0), APoint(98.9302595583337, 124.44595305550087, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.3264109029666, 122.25028488074997, 0.0), APoint(101.3264109029666, 122.25028488074997, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.14550750764305, 118.75072760530085, 0.0), APoint(105.14550750764305, 118.75072760530085, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.09839786490959, 123.44490323217747, 0.0), APoint(93.09839786490959, 123.44490323217747, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.49454920954248, 121.24923505742657, 0.0), APoint(95.49454920954248, 121.24923505742657, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.31364581421893, 117.74967778197745, 0.0), APoint(99.31364581421893, 117.74967778197745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.26653617148558, 122.44385340885447, 0.0), APoint(87.26653617148558, 122.44385340885447, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.66268751611848, 120.24818523410357, 0.0), APoint(89.66268751611848, 120.24818523410357, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.48178412079503, 116.74862795865445, 0.0), APoint(93.48178412079503, 116.74862795865445, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.43467447806171, 121.44280358553122, 0.0), APoint(81.43467447806171, 121.44280358553122, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.8308258226946, 119.24713541078033, 0.0), APoint(83.8308258226946, 119.24713541078033, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.64992242737105, 115.74757813533121, 0.0), APoint(87.64992242737105, 115.74757813533121, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.60281278463772, 120.4417537622078, 0.0), APoint(75.60281278463772, 120.4417537622078, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.99896412927082, 118.24608558745705, 0.0), APoint(77.99896412927082, 118.24608558745705, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.81806073394726, 114.74652831200792, 0.0), APoint(81.81806073394726, 114.74652831200792, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.35196266565976, 124.40629196486006, 0.0), APoint(64.35196266565976, 124.40629196486006, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.77095109121416, 119.44070393888495, 0.0), APoint(69.77095109121416, 119.44070393888495, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.16710243584706, 117.24503576413406, 0.0), APoint(72.16710243584706, 117.24503576413406, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.9861990405235, 113.74547848868494, 0.0), APoint(75.9861990405235, 113.74547848868494, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.52010097223571, 123.40524214153665, 0.0), APoint(58.52010097223571, 123.40524214153665, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.93908939779012, 118.43965411556154, 0.0), APoint(63.93908939779012, 118.43965411556154, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.33524074242303, 116.24398594081065, 0.0), APoint(66.33524074242303, 116.24398594081065, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.68823927881184, 122.40419231821353, 0.0), APoint(52.68823927881184, 122.40419231821353, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.10722770436625, 117.43860429223842, 0.0), APoint(58.10722770436625, 117.43860429223842, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.50337904899916, 115.24293611748753, 0.0), APoint(60.50337904899916, 115.24293611748753, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.27536601094221, 116.4375544689155, 0.0), APoint(52.27536601094221, 116.4375544689155, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.67151735557511, 114.2418862941646, 0.0), APoint(54.67151735557511, 114.2418862941646, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.443504317518546, 115.43650464559225, 0.0), APoint(46.443504317518546, 115.43650464559225, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(40.61164262409456, 114.43545482226887, 0.0), APoint(40.61164262409456, 114.43545482226887, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(315.02616751990627, 152.8686476871818, 0.0), APoint(315.02616751990263, 167.06864768710227, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(314.4261675199015, 167.06864768710105, 0.0), 0.6000000000011028, 2.036889175841877e-12, 1.5707963267966967)


entity = acad.model.AddLine(APoint(314.42616751990045, 167.66864768710218, 0.0), APoint(311.02616751991627, 167.66864768710218, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(311.0261675199152, 167.06864768710105, 0.0), 0.6000000000011312, 1.5707963267930967, 3.1415926535862404)


entity = acad.model.AddLine(APoint(310.4261675199141, 167.06864768710318, 0.0), APoint(310.42616751988953, 153.46864768718353, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(311.0261675198906, 153.46864768718353, 0.0), 0.6000000000010459, 3.141592653589793, 4.712388980386584)


entity = acad.model.AddLine(APoint(311.0261675198917, 152.8686476871825, 0.0), APoint(322.6261675197993, 152.86864768718067, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(322.6261675197983, 153.46864768717933, 0.0), 0.5999999999986585, 4.712388980386395, 1.894780628697837e-12)


entity = acad.model.AddLine(APoint(323.22616751979695, 153.46864768718046, 0.0), APoint(323.22616751979695, 157.06864768718162, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(322.62616751979795, 157.06864768718253, 0.0), 0.5999999999989996, 6.28318530717807, 1.5707963267926228)


entity = acad.model.AddLine(APoint(322.6261675197993, 157.66864768718153, 0.0), APoint(310.42616751990045, 157.66864768719074, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 158.26864768713426, 0.0), APoint(316.02616751969526, 158.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(316.02616751969526, 158.26864768713415, 0.0), APoint(316.02616751969526, 168.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(316.02616751969526, 168.26864768713415, 0.0), APoint(377.74293745552313, 168.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.28893645538756, 168.26864768713415, 0.0), APoint(403.4582339857425, 168.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.4582339857425, 168.26864768713415, 0.0), APoint(403.4582339857425, 158.2686476871346, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.4582339857425, 158.2686476871346, 0.0), APoint(379.28893645538756, 158.2686476871346, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.82616751968453, 158.26864768713415, 0.0), APoint(323.82616751968453, 152.26864768713403, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.82616751968453, 152.26864768713403, 0.0), APoint(309.8261675197409, 152.26864768710232, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(309.8261675197409, 152.26864768710232, 0.0), APoint(309.8261675197127, 168.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(309.8261675197127, 168.26864768713415, 0.0), APoint(315.62616751967107, 168.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(315.62616751967107, 168.26864768713415, 0.0), APoint(315.62616751967107, 158.2686476871346, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(315.62616751967107, 158.2686476871346, 0.0), APoint(323.82616751968453, 158.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.28893645538756, 154.31913580746243, 0.0), APoint(379.28893645538756, 162.6943791209452, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.28893645538756, 162.6943791209452, 0.0), APoint(378.53893645538756, 163.1943791209452, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(378.53893645538756, 163.1943791209452, 0.0), APoint(380.03893645538756, 163.6943791209452, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(380.03893645538756, 163.6943791209452, 0.0), APoint(379.28893645538756, 164.1943791209452, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.28893645538756, 164.1943791209452, 0.0), APoint(379.28893645538756, 172.09340288028932, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 154.31913580746243, 0.0), APoint(377.74293745552313, 162.6943791209452, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 162.6943791209452, 0.0), APoint(376.99293745552313, 163.1943791209452, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(376.99293745552313, 163.1943791209452, 0.0), APoint(378.49293745552404, 163.6943791209452, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(378.49293745552404, 163.6943791209452, 0.0), APoint(377.74293745552313, 164.1943791209452, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 164.1943791209452, 0.0), APoint(377.74293745552313, 172.09340288028932, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 159.26864768713403, 0.0), APoint(341.7414640499137, 159.26864768713403, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('O10@30', APoint(324.828181607709, 147.22519849464652, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('8010', APoint(331.14291902084756, 151.8645674419297, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('T', APoint(332.25643835502296, 151.86980416427355, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('1', APoint(314.2010857431244, 171.80392274740734, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('2', APoint(406.5849300906753, 172.3049666152366, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('4', APoint(330.9552398123178, 175.40803199041818, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('5', APoint(376.450952383872, 176.15885197178238, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('3', APoint(376.52962994965543, 150.48328096038244, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('T', APoint(325.03889461404276, 147.22519849464655, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('7', APoint(335.37307253717023, 146.11686242166854, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('6', APoint(338.4094525674336, 151.02304437662008, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddLine(APoint(365.4585020662107, 112.75896588874241, 0.0), APoint(365.4585020662107, 115.88452399290031, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(375.95850206621253, 112.75896588874241, 0.0), APoint(375.95850206621253, 115.88452399290031, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(364.4585020662107, 114.88452399290031, 0.0), APoint(368.6846925424021, 114.88452399290031, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(376.95850206621253, 114.88452399290031, 0.0), APoint(372.73231159002114, 114.88452399290031, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(364.4585020662108, 104.85896588874408, 0.0), APoint(358.67944506520473, 104.85896588874408, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(365.0585020662103, 112.35896588874408, 0.0), APoint(358.67944506520473, 112.35896588874408, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.67944506520473, 103.85896588874408, 0.0), APoint(359.67944506520473, 107.60896588874408, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.67944506520473, 113.35896588874408, 0.0), APoint(359.67944506520473, 109.60896588874408, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(365.4585020662107, 103.85896588874402, 0.0), APoint(365.4585020662107, 100.37201537237036, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9585020662107, 103.85896588874402, 0.0), APoint(366.9585020662107, 100.37201537237036, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9585020662107, 101.37201537237036, 0.0), APoint(364.4585020662107, 101.37201537237036, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(365.4585020662107, 101.37201537237036, 0.0), APoint(362.49659730430665, 101.37201537237036, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

# Entity type AcDbSolid not supported
entity = acad.model.AddText('2*2cm', APoint(379.7241252434943, 116.13764023193869, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('O10@30', APoint(360.43487642959667, 93.43734485928803, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('T', APoint(360.6181139031104, 93.30570029709827, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('9', APoint(356.9428125836504, 92.75325551642902, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('3O10', APoint(378.2794721943138, 108.48680879816982, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('T', APoint(379.58103746574216, 108.47641912772053, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('8', APoint(385.2490016229654, 107.71824965969813, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddLine(APoint(209.7651660952879, 185.5319763098174, 0.0), APoint(209.7651660952879, 191.1579678795852, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.76516609528153, 185.5319763098174, 0.0), APoint(206.76516609528153, 191.1579678795852, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.76516609528153, 190.1579678795852, 0.0), APoint(210.7651660952879, 190.1579678795852, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 190.1579678795852, 0.0), APoint(213.66754704767015, 190.1579678795852, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.76516609528153, 185.5944763098174, 0.0), APoint(206.76516609528153, 193.78740241369192, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.5151660952879, 185.5944763098174, 0.0), APoint(204.5151660952879, 193.78740241369192, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.76516609528153, 192.78740241369192, 0.0), APoint(204.5151660952879, 192.78740241369192, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.5151660952879, 192.78740241369192, 0.0), APoint(200.2199280000502, 192.78740241369192, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 181.28197630981742, 0.0), APoint(209.7651660952879, 178.32536677489816, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.5151660952879, 181.28197630981742, 0.0), APoint(204.5151660952879, 178.32536677489816, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(210.7651660952879, 179.32536677489816, 0.0), APoint(203.5151660952879, 179.32536677489816, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 181.28197630981742, 0.0), APoint(209.7651660952879, 176.11240280644563, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.7651660952879, 181.28197630981742, 0.0), APoint(239.7651660952879, 176.11240280644563, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(208.7651660952879, 177.11240280644563, 0.0), APoint(240.7651660952879, 177.11240280644563, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 161.15697630981742, 0.0), APoint(209.7651660952879, 164.90189832989302, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.76816253149082, 161.15697630981936, 0.0), APoint(216.76816253149082, 164.90189832989302, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(208.7651660952879, 163.90189832989302, 0.0), APoint(217.76816253149082, 163.90189832989302, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 161.21947630981742, 0.0), APoint(209.7651660952879, 164.90189832989302, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.26516609529153, 161.2194763098305, 0.0), APoint(196.26516609529153, 164.90189832989302, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(210.7651660952879, 163.90189832989302, 0.0), APoint(195.26516609529153, 163.90189832989302, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.26516609529153, 161.2819763098305, 0.0), APoint(196.26516609529153, 164.90189832989302, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253149082, 161.15697630981742, 0.0), APoint(194.26816253149082, 164.90189832989302, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.26516609529153, 163.90189832989302, 0.0), APoint(197.06516609529154, 163.90189832989302, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253149082, 163.90189832989302, 0.0), APoint(193.4681625314908, 163.90189832989302, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.515166095288, 182.28197630981748, 0.0), APoint(199.56461429924775, 182.28197630981748, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(205.76516609528164, 184.53197630981745, 0.0), APoint(199.56461429924775, 184.53197630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.56461429924775, 182.28197630981748, 0.0), APoint(200.56461429924775, 181.48197630981747, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.56461429924775, 184.53197630981745, 0.0), APoint(200.56461429924775, 185.33197630981746, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.61423083116017, 184.53197630981745, 0.0), APoint(217.663679035119, 184.53197630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.61423083116017, 187.53197630981762, 0.0), APoint(217.663679035119, 187.53197630981762, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.663679035119, 184.53197630981745, 0.0), APoint(218.663679035119, 183.73197630981744, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.663679035119, 187.53197630981762, 0.0), APoint(218.663679035119, 188.33197630981763, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(195.26516609529165, 160.15697630981748, 0.0), APoint(191.12448669788446, 160.15697630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.515166095288, 184.53197630981745, 0.0), APoint(191.12448669788446, 184.53197630981742, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.1244866978845, 159.15697630981748, 0.0), APoint(192.1244866978845, 171.09447630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.1244866978845, 185.53197630981745, 0.0), APoint(192.1244866978845, 173.59447630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(193.26816253149093, 160.15697630981748, 0.0), APoint(191.12448669788446, 160.15697630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(193.26816253148365, 152.65697630981748, 0.0), APoint(191.12448669788446, 152.65697630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.1244866978845, 161.15697630981748, 0.0), APoint(192.1244866978845, 157.65697630981748, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.1244866978845, 151.65697630981748, 0.0), APoint(192.1244866978845, 155.15697630981748, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253148354, 151.65697630981742, 0.0), APoint(194.26816253148354, 148.7229991960395, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.76816253148354, 151.65697630981742, 0.0), APoint(216.76816253148354, 148.7229991960395, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(193.26816253148354, 149.7229991960395, 0.0), APoint(217.76816253148354, 149.7229991960395, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(137.32301469314186, 221.64608016422744, 0.0), APoint(140.73153008983292, 227.54980200967748, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.0730146931373, 239.11092580721538, 0.0), APoint(110.48153008982835, 245.01464765266542, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(141.0975554936174, 226.18377660589306, 0.0), APoint(109.11550468604393, 244.64862224888094, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.07301469314005, 259.09019986504654, 0.0), APoint(45.29413390984901, 254.2770371602098, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(17.82301469313913, 276.5550455080339, 0.0), APoint(15.044133909848085, 271.7418828031972, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.66015931363346, 254.6430625639942, 0.0), APoint(14.678108506063666, 273.1079082069816, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.07301469313916, 238.82225067261413, 0.0), APoint(44.279511117825905, 245.39279160375065, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(17.823014693139157, 221.35740502962733, 0.0), APoint(14.029511117825905, 227.92794596076385, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.645536521610325, 245.0267661999662, 0.0), APoint(13.663485714041471, 226.56192055697937, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

# Entity type AcDbSolid not supported
entity = acad.model.AddLine(APoint(34.118032157416565, 84.75264288110077, 0.0), APoint(34.118032157416565, 81.51599936022706, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695813, 84.67051786235209, 0.0), APoint(77.72399283695813, 81.51599936022706, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.118032157416565, 82.51599936022706, 0.0), APoint(78.72399283695813, 82.51599936022706, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695813, 84.60801786235209, 0.0), APoint(77.72399283695813, 81.51599936022706, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 85.18764288110094, 0.0), APoint(121.1180321574152, 81.51599936022706, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.72399283695813, 82.51599936022706, 0.0), APoint(122.1180321574152, 82.51599936022706, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 77.25226789047554, 0.0), APoint(34.118032157416565, 72.66976331948865, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 78.20439290922434, 0.0), APoint(121.1180321574152, 72.66976331948865, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.118032157416565, 73.66976331948865, 0.0), APoint(122.1180321574152, 73.66976331948865, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.6582339857541, 158.26864768713415, 0.0), APoint(395.6582339857541, 152.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.6582339857541, 152.26864768713415, 0.0), APoint(409.6582339856968, 152.26864768710232, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(409.6582339856968, 152.26864768710232, 0.0), APoint(409.658233985725, 168.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(409.658233985725, 168.26864768713415, 0.0), APoint(403.85823398573757, 168.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.85823398573757, 168.26864768713415, 0.0), APoint(403.85823398573757, 158.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.85823398573757, 158.26864768713415, 0.0), APoint(395.6582339857541, 158.26864768713415, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.4582339855215, 152.86864768718192, 0.0), APoint(404.4582339855215, 167.06864768710227, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(405.0582339855221, 167.0686476871015, 0.0), 0.600000000000648, 1.5707963267938545, 3.141592653588514)


entity = acad.model.AddLine(APoint(405.05823398552275, 167.66864768710218, 0.0), APoint(408.45823398551056, 167.66864768710218, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(408.45823398550937, 167.06864768710332, 0.0), 0.5999999999988574, 6.283185307179349, 1.570796326792907)


entity = acad.model.AddLine(APoint(409.0582339855082, 167.06864768710318, 0.0), APoint(409.05823398553366, 153.46864768718353, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(408.45823398553307, 153.46864768718308, 0.0), 0.6000000000005912, 4.712388980383553, 7.579122514766934e-13)


entity = acad.model.AddLine(APoint(408.4582339855324, 152.8686476871825, 0.0), APoint(396.8582339856248, 152.86864768718067, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(396.8582339856254, 153.46864768717984, 0.0), 0.5999999999991701, 3.1415926535885617, 4.712388980383647)


entity = acad.model.AddLine(APoint(396.25823398562625, 153.46864768718058, 0.0), APoint(396.25823398562625, 157.06864768718174, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(396.85823398562565, 157.06864768718214, 0.0), 0.5999999999993975, 1.5707963267963174, 3.1415926535904557)


entity = acad.model.AddLine(APoint(396.8582339856248, 157.66864768718153, 0.0), APoint(409.05823398552275, 157.66864768719086, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

# Entity type AcDbSolid not supported
entity = acad.model.AddLine(APoint(242.30347265904948, 188.52265846954268, 0.0), APoint(242.30347265904948, 191.2020622746417, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.7651660952879, 188.52265846954268, 0.0), APoint(242.7651660952879, 191.2020622746417, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.7651660952879, 190.2020622746417, 0.0), APoint(243.5651660952879, 190.2020622746417, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.30347265904948, 190.2020622746417, 0.0), APoint(238.5106155161926, 190.2020622746417, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.6660265314331, 98.92379186092637, 0.0), APoint(181.6660265314331, 98.92379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.6660265314331, 98.92379186092637, 0.0), APoint(181.6660265314331, 100.92379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.6660265314331, 100.92379186092637, 0.0), APoint(177.6660265314331, 100.92379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.6660265314331, 100.92379186092637, 0.0), APoint(177.6660265314331, 98.92379186092637, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.54253669003447, 105.38943037013513, 0.0), APoint(151.73376687556356, 105.38943037013513, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.84085401106185, 104.58943037013512, 0.0), APoint(152.64085401106186, 104.58943037013512, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.44085401106187, 104.58943037013512, 0.0), APoint(154.24085401106188, 104.58943037013512, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.04085401106167, 103.78943037013514, 0.0), APoint(151.84085401106168, 103.78943037013514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.6408540110617, 103.78943037013514, 0.0), APoint(153.4408540110617, 103.78943037013514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.2408540110617, 103.78943037013514, 0.0), APoint(155.04085401106173, 103.78943037013514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.84085401106174, 103.78943037013514, 0.0), APoint(156.64085401106175, 103.78943037013514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.44085401106176, 103.78943037013514, 0.0), APoint(158.15101636921926, 103.78943037013514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.4408540110613, 102.98943037013512, 0.0), APoint(154.24085401106132, 102.98943037013512, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.04085401106133, 102.98943037013512, 0.0), APoint(155.84085401106134, 102.98943037013512, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.64085401106135, 102.98943037013512, 0.0), APoint(157.44085401106136, 102.98943037013512, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.27368292694428, 102.18943037013514, 0.0), APoint(156.64085401106223, 102.18943037013514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.44085401106224, 102.18943037013514, 0.0), APoint(157.76629594737736, 102.18943037013514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.84085401106185, 104.88943037013507, 0.0), APoint(152.64085401106186, 104.88943037013507, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.44085401106187, 104.88943037013507, 0.0), APoint(153.73915734233108, 104.88943037013507, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.0672955077971, 104.08943037013509, 0.0), APoint(151.84085401106205, 104.08943037013509, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.64085401106206, 104.08943037013509, 0.0), APoint(153.44085401106207, 104.08943037013509, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.24085401106208, 104.08943037013509, 0.0), APoint(155.0408540110621, 104.08943037013509, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.8408540110621, 104.08943037013509, 0.0), APoint(156.64085401106212, 104.08943037013509, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.86182390005615, 103.28943037013508, 0.0), APoint(152.64085401106132, 103.28943037013508, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.44085401106133, 103.28943037013508, 0.0), APoint(154.24085401106134, 103.28943037013508, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.04085401106136, 103.28943037013508, 0.0), APoint(155.84085401106137, 103.28943037013508, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.64085401106138, 103.28943037013508, 0.0), APoint(157.4408540110614, 103.28943037013508, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.84085401106276, 102.4894303701351, 0.0), APoint(156.64085401106277, 102.4894303701351, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.44085401106278, 102.4894303701351, 0.0), APoint(157.87693262430915, 102.4894303701351, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.84085401106185, 105.18943037013503, 0.0), APoint(152.53592306227074, 105.18943037013503, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.1769665498514, 104.38943037013505, 0.0), APoint(151.84085401106205, 104.38943037013505, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.64085401106206, 104.38943037013505, 0.0), APoint(153.44085401106207, 104.38943037013505, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.24085401106208, 104.38943037013505, 0.0), APoint(155.0408540110621, 104.38943037013505, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(150.8845104377051, 103.58943037013503, 0.0), APoint(151.04085401106187, 103.58943037013503, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.84085401106188, 103.58943037013503, 0.0), APoint(152.6408540110619, 103.58943037013503, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.4408540110619, 103.58943037013503, 0.0), APoint(154.2408540110619, 103.58943037013503, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.04085401106192, 103.58943037013503, 0.0), APoint(155.84085401106194, 103.58943037013503, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.64085401106195, 103.58943037013503, 0.0), APoint(157.44085401106196, 103.58943037013503, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(158.24085401106197, 103.58943037013503, 0.0), APoint(158.2826004397267, 103.58943037013503, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.2408540110624, 102.78943037013505, 0.0), APoint(155.0408540110624, 102.78943037013505, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.84085401106242, 102.78943037013505, 0.0), APoint(156.64085401106243, 102.78943037013505, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.44085401106244, 102.78943037013505, 0.0), APoint(157.98756930124094, 102.78943037013505, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.07583911365145, 101.98943037013504, 0.0), APoint(157.4408540110624, 101.98943037013504, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.14085401106058, 103.46918835266854, 0.0), APoint(151.14085401106058, 103.68943037013553, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.94085401106076, 103.68943037013534, 0.0), APoint(151.94085401106076, 104.48943037013534, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.94085401106076, 105.28943037013534, 0.0), APoint(151.94085401106076, 105.33779774822698, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.74085401106095, 103.07026354811939, 0.0), APoint(152.74085401106095, 103.68943037013456, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.74085401106095, 104.48943037013456, 0.0), APoint(152.74085401106095, 105.13833534595238, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.54085401106022, 102.87080114584478, 0.0), APoint(153.54085401106022, 102.88943037013523, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.54085401106022, 103.68943037013523, 0.0), APoint(153.54085401106022, 104.48943037013522, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.3408540110604, 102.88943037013505, 0.0), APoint(154.3408540110604, 103.68943037013504, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.3408540110604, 104.48943037013504, 0.0), APoint(154.3408540110604, 104.73941054140322, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.14085401106058, 102.47187634129563, 0.0), APoint(155.14085401106058, 102.88943037013517, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.14085401106058, 103.68943037013517, 0.0), APoint(155.14085401106058, 104.48943037013517, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.94085401106076, 102.88943037013496, 0.0), APoint(155.94085401106076, 103.68943037013496, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.74085401106095, 102.08943037013475, 0.0), APoint(156.74085401106095, 102.88943037013475, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.74085401106095, 103.68943037013474, 0.0), APoint(156.74085401106095, 104.14102333457946, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.54085401106022, 101.87348913447187, 0.0), APoint(157.54085401106022, 102.08943037013488, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.54085401106022, 102.88943037013487, 0.0), APoint(157.54085401106022, 103.68943037013487, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.44085401106167, 103.39438995181524, 0.0), APoint(151.44085401106167, 103.6894303701353, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.44085401106167, 104.4894303701353, 0.0), APoint(151.44085401106167, 105.11128216327495, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.24085401106186, 103.68943037013506, 0.0), APoint(152.24085401106186, 104.48943037013505, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.04085401106204, 102.99546514726606, 0.0), APoint(153.04085401106204, 103.6894303701343, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.04085401106204, 104.4894303701343, 0.0), APoint(153.04085401106204, 105.06353694509906, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.8408540110613, 102.79600274499148, 0.0), APoint(153.8408540110613, 102.889430370135, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.8408540110613, 103.689430370135, 0.0), APoint(153.8408540110613, 104.489430370135, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.6408540110615, 102.88943037013476, 0.0), APoint(154.6408540110615, 103.68943037013476, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.6408540110615, 104.48943037013476, 0.0), APoint(154.6408540110615, 104.66461214054986, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.44085401106167, 102.3970779404423, 0.0), APoint(155.44085401106167, 102.88943037013492, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.44085401106167, 103.68943037013491, 0.0), APoint(155.44085401106167, 104.4651497382753, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.24085401106186, 102.8894303701347, 0.0), APoint(156.24085401106186, 103.6894303701347, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.04085401106204, 102.08943037013447, 0.0), APoint(157.04085401106204, 102.88943037013446, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.04085401106204, 103.68943037013446, 0.0), APoint(157.04085401106204, 104.0662249337261, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.8408540110613, 102.88943037013544, 0.0), APoint(157.8408540110613, 103.68943037013544, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(150.94085401106258, 103.68943037013489, 0.0), APoint(150.94085401106258, 103.74355557666661, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.74085401106277, 103.31959155096189, 0.0), APoint(151.74085401106277, 103.68943037013501, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.74085401106277, 104.48943037013501, 0.0), APoint(151.74085401106277, 105.28943037013501, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.54085401106295, 103.6894303701348, 0.0), APoint(152.54085401106295, 104.4894303701348, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.34085401106313, 102.92066674641273, 0.0), APoint(153.34085401106313, 103.68943037013405, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.34085401106313, 104.48943037013404, 0.0), APoint(153.34085401106313, 104.98873854424573, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.1408540110624, 102.72120434413813, 0.0), APoint(154.1408540110624, 102.88943037013563, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.1408540110624, 103.68943037013563, 0.0), APoint(154.1408540110624, 104.48943037013562, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.94085401106258, 102.88943037013541, 0.0), APoint(154.94085401106258, 103.68943037013541, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.94085401106258, 104.48943037013541, 0.0), APoint(154.94085401106258, 104.58981373969745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.74085401106277, 102.32227953958898, 0.0), APoint(155.74085401106277, 102.88943037013557, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.74085401106277, 103.68943037013557, 0.0), APoint(155.74085401106277, 104.39035133742289, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.54085401106295, 102.88943037013533, 0.0), APoint(156.54085401106295, 103.68943037013533, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.34085401106313, 102.08943037013512, 0.0), APoint(157.34085401106313, 102.88943037013512, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.34085401106313, 103.68943037013511, 0.0), APoint(157.34085401106313, 103.99142653287369, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(158.1408540110624, 103.20507384589487, 0.0), APoint(158.1408540110624, 103.68943037013555, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.58269319810015, 58.9237918609264, 0.0), APoint(197.13966726554503, 58.9237918609264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.58269319810015, 48.923791860926514, 0.0), APoint(197.13966726554503, 48.923791860926514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.13966726554503, 59.9237918609264, 0.0), APoint(196.13966726554503, 55.17379186092646, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.13966726554503, 47.92379186092651, 0.0), APoint(196.13966726554503, 52.67379186092646, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319810006, 47.923791860926485, 0.0), APoint(160.58269319810006, 43.43974908911014, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.58269319810006, 47.923791860926485, 0.0), APoint(191.58269319810006, 43.43974908911014, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(159.58269319810006, 44.43974908911014, 0.0), APoint(192.58269319810006, 44.43974908911014, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('1', APoint(165.85453237145967, 81.5214443089529, 0.0), 1.85)
entity.Color = 1

entity = acad.model.AddText('3', APoint(163.78766794529193, 79.14044925248034, 0.0), 1.85)
entity.Color = 1

entity = acad.model.AddLine(APoint(159.58269319810012, 58.9237918609264, 0.0), APoint(158.12022263093817, 58.9237918609264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(176.66602653143315, 98.92379186092643, 0.0), APoint(158.12022263093814, 98.92379186092641, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(159.12022263093817, 57.9237918609264, 0.0), APoint(159.12022263093814, 77.6737918609264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(159.12022263093814, 99.92379186092641, 0.0), APoint(159.12022263093814, 80.1737918609264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.66602653143315, 100.92379186092643, 0.0), APoint(189.80128000321565, 100.92379186092643, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.66602653143315, 98.92379186092643, 0.0), APoint(189.80128000321565, 98.92379186092643, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(188.80128000321565, 101.92379186092643, 0.0), APoint(188.80128000321565, 97.92379186092643, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.6660265314331, 101.92379186092637, 0.0), APoint(177.6660265314331, 105.09097843329914, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 99.92379186092637, 0.0), APoint(181.16602653143218, 105.09097843329914, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(176.6660265314331, 104.09097843329914, 0.0), APoint(182.16602653143218, 104.09097843329914, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 97.92379186092637, 0.0), APoint(181.16602653143218, 92.54065940423379, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.6660265314331, 97.92379186092637, 0.0), APoint(181.6660265314331, 92.54065940423379, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 93.54065940423379, 0.0), APoint(180.36602653143217, 93.54065940423379, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.6660265314331, 93.54065940423379, 0.0), APoint(182.4660265314331, 93.54065940423379, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.58269319810006, 59.92379186092637, 0.0), APoint(191.58269319810006, 65.38120553987585, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 59.92379186092637, 0.0), APoint(181.16602653143218, 65.38120553987585, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.58269319810006, 64.38120553987585, 0.0), APoint(180.16602653143218, 64.38120553987585, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.109858773184, 98.9237918609266, 0.0), APoint(161.39493651342593, 98.92379186092658, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(176.10985877319212, 98.9237918609266, 0.0), 13.714922259766187, 2.897246558310586, 3.1415926535897936)
entity.Color = 8

entity = acad.model.AddLine(APoint(181.16602653143218, 59.92379186092637, 0.0), APoint(181.16602653143218, 65.38120553987585, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319810006, 59.92379186092637, 0.0), APoint(160.58269319810006, 65.38120553987585, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.16602653143218, 64.38120553987585, 0.0), APoint(159.58269319810006, 64.38120553987585, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.1660265314331, 95.67379186092637, 0.0), APoint(173.1660265314331, 88.9689961736616, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 95.67379186092637, 0.0), APoint(181.16602653143218, 88.9689961736616, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.1660265314331, 89.9689961736616, 0.0), APoint(182.16602653143218, 89.9689961736616, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(230.88442357239194, 197.19044929801794, 0.0), APoint(230.96268805967927, 197.19044929801794, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(230.8844235724065, 187.53197630981762, 0.0), APoint(230.9626880596793, 187.53197630981762, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.96268805967927, 198.19044929801794, 0.0), APoint(229.96268805967927, 193.6112128039178, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.9626880596793, 186.53197630981762, 0.0), APoint(229.9626880596793, 191.11121280391777, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W1', APoint(123.27106639246571, 262.15155796575215, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(352.70155933255774, 170.52066995041716, 0.0), APoint(351.70155933255774, 170.68733661708382, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(351.70155933255774, 170.68733661708382, 0.0), APoint(352.70155933255774, 170.85400328375047, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(352.70155933255774, 170.52066995041716, 0.0), APoint(352.70155933255774, 170.85400328375047, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(351.70155933255774, 170.68733661708382, 0.0), APoint(352.70155933255774, 170.68733661708382, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(352.70155933255774, 170.68733661708382, 0.0), APoint(354.7150066166423, 170.68733661708382, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(369.1284539007265, 170.85400328375184, 0.0), APoint(370.1284539007265, 170.68733661708518, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(370.1284539007265, 170.68733661708518, 0.0), APoint(369.1284539007265, 170.52066995041852, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(369.1284539007265, 170.85400328375184, 0.0), APoint(369.1284539007265, 170.52066995041852, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(370.1284539007265, 170.68733661708518, 0.0), APoint(369.1284539007265, 170.68733661708518, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(369.1284539007265, 170.68733661708518, 0.0), APoint(367.11500661664286, 170.68733661708518, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(352.6949417565896, 154.97661755181593, 0.0), APoint(351.6952145642308, 155.14491288340935, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(351.6952145642308, 155.14491288340935, 0.0), APoint(352.69548471860054, 155.30995044293738, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(352.6949417565896, 154.97661755181593, 0.0), APoint(352.69548471860054, 155.30995044293738, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(351.6952145642308, 155.14491288340935, 0.0), APoint(352.69521323759506, 155.14328399737664, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(352.69521323759506, 155.14328399737664, 0.0), APoint(354.70865785056776, 155.14000432121804, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(369.12235749426384, 155.28319290381276, 0.0), APoint(370.12208468662266, 155.11489757221932, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(370.12208468662266, 155.11489757221932, 0.0), APoint(369.1218145322529, 154.94986001269135, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(369.12235749426384, 155.28319290381276, 0.0), APoint(369.1218145322529, 154.94986001269135, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(370.12208468662266, 155.11489757221932, 0.0), APoint(369.1220860132584, 155.11652645825205, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(369.1220860132584, 155.11652645825205, 0.0), APoint(367.1086414002848, 155.11980613441074, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.117437810965, 154.787692927628, 0.0), APoint(321.2636823923194, 155.33439162244179, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(321.2636823923194, 155.33439162244179, 0.0), APoint(322.2485965542211, 155.0941378577192, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(322.117437810965, 154.787692927628, 0.0), APoint(322.2485965542211, 155.0941378577192, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(321.2636823923194, 155.33439162244179, 0.0), APoint(322.183017182593, 154.94091539267362, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(322.183017182593, 154.94091539267362, 0.0), APoint(330.1985509669448, 151.51025874134905, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(330.1985509669448, 151.51025874134905, 0.0), APoint(337.7507905351058, 151.51025874134905, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(327.95097976619934, 164.36861468863802, 0.0), APoint(328.01230151686013, 163.35667722976336, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(328.01230151686013, 163.35667722976336, 0.0), APoint(327.6260985228163, 164.29402723118724, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(327.95097976619934, 164.36861468863802, 0.0), APoint(327.6260985228163, 164.29402723118724, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(328.01230151686013, 163.35667722976336, 0.0), APoint(327.7885391445078, 164.33132095991263, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(327.7885391445078, 164.33132095991263, 0.0), APoint(325.9461187781908, 172.3563675280767, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(325.9461187781908, 172.3563675280767, 0.0), APoint(316.0541946106432, 172.3563675280767, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(392.88910883006986, 165.4594708835225, 0.0), APoint(392.57975204881404, 164.4940299688784, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(392.57975204881404, 164.4940299688784, 0.0), APoint(392.55927086957684, 165.5076168171923, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(392.88910883006986, 165.4594708835225, 0.0), APoint(392.55927086957684, 165.5076168171923, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(392.57975204881404, 164.4940299688784, 0.0), APoint(392.72418984982335, 165.4835438503574, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(392.72418984982335, 165.4835438503574, 0.0), APoint(393.80054181733794, 172.85741139590584, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.80054181733794, 172.85741139590584, 0.0), APoint(405.7641872945878, 172.85741139590584, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(345.13274521893806, 168.36720403448913, 0.0), APoint(345.1282925950254, 167.35342005754035, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(345.1282925950254, 167.35342005754035, 0.0), APoint(344.80370973322965, 168.31384899484195, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(345.13274521893806, 168.36720403448913, 0.0), APoint(344.80370973322965, 168.31384899484195, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(345.1282925950254, 167.35342005754035, 0.0), APoint(344.9682274760839, 168.34052651466553, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(344.9682274760839, 168.34052651466553, 0.0), APoint(343.73260771560217, 175.96047677108743, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(343.73260771560217, 175.96047677108743, 0.0), APoint(332.919955822691, 175.96047677108743, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028435036, 170.69932020514705, 0.0), APoint(360.92038028435036, 176.77828219111314, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028435036, 176.77828219111314, 0.0), APoint(375.7295859249234, 176.77828219111314, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028435036, 157.1146877270179, 0.0), APoint(360.92038028435036, 151.0357257410517, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028435036, 151.0357257410517, 0.0), APoint(375.80826349070685, 151.0357257410517, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.5213750768325, 152.13076949229787, 0.0), APoint(316.8261675198446, 152.86864768718146, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(316.8261675198446, 152.86864768718146, 0.0), APoint(317.7231081369576, 152.39612752131467, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(317.5213750768325, 152.13076949229787, 0.0), APoint(317.7231081369576, 152.39612752131467, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(316.8261675198446, 152.86864768718146, 0.0), APoint(317.62224160689505, 152.26344850680627, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(317.62224160689505, 152.26344850680627, 0.0), APoint(324.95227494205665, 146.69093931611133, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(324.95227494205665, 146.69093931611133, 0.0), APoint(334.68506503997014, 146.69093931611133, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('0.35', APoint(369.04183539954494, 114.38452399290031, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddText('0.25', APoint(358.012778398538, 108.10896588874394, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddText('0.05', APoint(358.80612111383044, 100.87201537237036, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(376.40829467347413, 112.72289264839935, 0.0), APoint(379.82995862683856, 115.96825633343508, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.82995862683856, 115.96825633343508, 0.0), APoint(387.1255387366282, 115.96825633343508, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.72743483438154, 98.94032893524368, 0.0), APoint(374.4585020662107, 99.6426952786311, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(374.4585020662107, 99.6426952786311, 0.0), APoint(373.9947464717952, 98.74119179753625, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(373.72743483438154, 98.94032893524368, 0.0), APoint(373.9947464717952, 98.74119179753625, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(374.4585020662107, 99.6426952786311, 0.0), APoint(373.8610906530884, 98.84076036638997, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(373.8610906530884, 98.84076036638997, 0.0), APoint(369.7376786314426, 93.30570029709827, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(369.7376786314426, 93.30570029709827, 0.0), APoint(359.4208712720565, 93.30570029709827, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.16516609528153, 190.5579678795852, 0.0), APoint(206.36516609528152, 189.75796787958518, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(209.3651660952879, 189.75796787958518, 0.0), APoint(210.1651660952879, 190.5579678795852, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-c1', APoint(211.09611847624157, 190.6579678795852, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.36516609528152, 192.38740241369192, 0.0), APoint(207.16516609528153, 193.18740241369193, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(204.9151660952879, 193.18740241369193, 0.0), APoint(204.1151660952879, 192.38740241369192, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-c2', APoint(200.50564228576448, 193.28740241369192, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(209.3651660952879, 178.92536677489815, 0.0), APoint(210.1651660952879, 179.72536677489816, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(204.9151660952879, 179.72536677489816, 0.0), APoint(204.1151660952879, 178.92536677489815, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-b2', APoint(205.71159466671648, 179.82536677489816, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(210.1651660952879, 177.51240280644564, 0.0), APoint(209.3651660952879, 176.71240280644562, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(239.3651660952879, 176.71240280644562, 0.0), APoint(240.1651660952879, 177.51240280644564, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-D', APoint(223.97945180957362, 177.61240280644563, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(210.1651660952879, 164.30189832989302, 0.0), APoint(209.3651660952879, 163.501898329893, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(216.3681625314908, 163.501898329893, 0.0), APoint(217.16816253149082, 164.30189832989302, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-a2', APoint(211.87380717053222, 164.40189832989302, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(209.3651660952879, 163.501898329893, 0.0), APoint(210.1651660952879, 164.30189832989302, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(196.66516609529154, 164.30189832989302, 0.0), APoint(195.86516609529153, 163.501898329893, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-b1', APoint(201.80088038100402, 164.40189832989302, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(196.66516609529154, 164.30189832989302, 0.0), APoint(195.86516609529153, 163.501898329893, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(193.8681625314908, 163.501898329893, 0.0), APoint(194.66816253149082, 164.30189832989302, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-a1', APoint(194.08809288481973, 164.40189832989302, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(200.96461429924776, 181.88197630981747, 0.0), APoint(200.16461429924775, 182.6819763098175, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(200.16461429924775, 184.93197630981746, 0.0), APoint(200.96461429924776, 184.13197630981745, 0.0))
entity.Color = 8


entity = acad.model.AddText('0.30', APoint(198.06461429924772, 182.65697630981737, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(219.063679035119, 184.13197630981745, 0.0), APoint(218.263679035119, 184.93197630981746, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(218.263679035119, 187.93197630981763, 0.0), APoint(219.063679035119, 187.13197630981762, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-t', APoint(218.23510760654756, 185.28197630981745, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(191.7244866978845, 160.5569763098175, 0.0), APoint(192.5244866978845, 159.75697630981747, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(192.5244866978845, 184.13197630981745, 0.0), APoint(191.7244866978845, 184.93197630981746, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-H', APoint(191.3387724121702, 171.59447630981737, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(192.5244866978845, 159.75697630981747, 0.0), APoint(191.7244866978845, 160.5569763098175, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(191.7244866978845, 153.0569763098175, 0.0), APoint(192.5244866978845, 152.25697630981747, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-m', APoint(191.0530581264559, 155.6569763098174, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(194.66816253148355, 150.1229991960395, 0.0), APoint(193.86816253148353, 149.3229991960395, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(216.36816253148353, 149.3229991960395, 0.0), APoint(217.16816253148355, 150.1229991960395, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-f', APoint(205.08959110291212, 150.2229991960395, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('W2', APoint(123.58323997731964, 236.8730216530887, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('W4', APoint(29.10460449239546, 265.3561171349992, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('W3', APoint(27.631221005314924, 235.20354655655547, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(75.80977665059535, 127.81724055271424, 0.0), APoint(72.42278717616637, 131.90440087254785, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.42278717616637, 131.90440087254785, 0.0), APoint(65.20766424672229, 131.88937365318793, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('A=i-A', APoint(53.9686315448064, 83.01599936022706, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('B=i-B', APoint(97.18291725909143, 83.01599936022706, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('L=i-L', APoint(75.67637378933908, 74.16976331948865, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(32.44912236640675, 117.6275688784158, 0.0), APoint(30.726912704093138, 119.17146402882042, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(30.726912704093138, 119.17146402882042, 0.0), APoint(18.400569981681656, 119.17146402882042, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.1651660952879, 190.6020622746417, 0.0), APoint(242.3651660952879, 189.80206227464168, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(241.90347265904947, 189.80206227464168, 0.0), APoint(242.70347265904948, 190.6020622746417, 0.0))
entity.Color = 8


entity = acad.model.AddText('i-j', APoint(238.93918694476397, 191.2020622746417, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(196.53966726554503, 58.5237918609264, 0.0), APoint(195.73966726554502, 59.3237918609264, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(195.73966726554502, 49.32379186092651, 0.0), APoint(196.53966726554503, 48.523791860926515, 0.0))
entity.Color = 8


entity = acad.model.AddText('m', APoint(195.06823869411642, 53.173791860926386, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(160.98269319810007, 44.839749089110136, 0.0), APoint(160.18269319810005, 44.03974908911014, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(191.18269319810005, 44.03974908911014, 0.0), APoint(191.98269319810007, 44.839749089110136, 0.0))
entity.Color = 8


entity = acad.model.AddText('f', APoint(175.65412176952864, 44.93974908911014, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(158.72022263093817, 59.3237918609264, 0.0), APoint(159.52022263093818, 58.5237918609264, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(159.52022263093815, 98.52379186092641, 0.0), APoint(158.72022263093814, 99.32379186092642, 0.0))
entity.Color = 8


entity = acad.model.AddText('h', APoint(158.44165120236673, 78.17379186092634, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(189.20128000321566, 100.52379186092642, 0.0), APoint(188.40128000321565, 101.32379186092643, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(188.40128000321565, 99.32379186092643, 0.0), APoint(189.20128000321566, 98.52379186092642, 0.0))
entity.Color = 8


entity = acad.model.AddText('0.20', APoint(186.30128000321565, 99.17379186092634, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(178.0660265314331, 104.49097843329915, 0.0), APoint(177.26602653143308, 103.69097843329914, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(180.76602653143217, 103.69097843329914, 0.0), APoint(181.5660265314322, 104.49097843329915, 0.0))
entity.Color = 8


entity = acad.model.AddText('0.35', APoint(177.33269319809932, 104.59097843329914, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(180.76602653143217, 93.14065940423379, 0.0), APoint(181.5660265314322, 93.9406594042338, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(182.0660265314331, 93.9406594042338, 0.0), APoint(181.26602653143308, 93.14065940423379, 0.0))
entity.Color = 8


entity = acad.model.AddText('0.05', APoint(178.91602653143264, 94.04065940423379, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(191.18269319810005, 63.98120553987585, 0.0), APoint(191.98269319810007, 64.78120553987586, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(181.5660265314322, 64.78120553987586, 0.0), APoint(180.76602653143217, 63.98120553987585, 0.0))
entity.Color = 8


entity = acad.model.AddText('b', APoint(185.66007415048043, 64.88120553987585, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('max 14', APoint(162.3493244653659, 99.07205072480654, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(180.76602653143217, 63.98120553987585, 0.0), APoint(181.5660265314322, 64.78120553987586, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(160.98269319810007, 64.78120553987586, 0.0), APoint(160.18269319810005, 63.98120553987585, 0.0))
entity.Color = 8


entity = acad.model.AddText('s1', APoint(169.76721700762326, 64.88120553987585, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(173.5660265314331, 90.3689961736616, 0.0), APoint(172.76602653143308, 89.56899617366159, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(180.76602653143217, 89.56899617366159, 0.0), APoint(181.5660265314322, 90.3689961736616, 0.0))
entity.Color = 8


entity = acad.model.AddText('s2', APoint(175.84459796000405, 90.4689961736616, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(230.36268805967927, 196.79044929801793, 0.0), APoint(229.56268805967926, 197.59044929801794, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(229.5626880596793, 187.93197630981763, 0.0), APoint(230.3626880596793, 187.13197630981762, 0.0))
entity.Color = 8


entity = acad.model.AddText('Hs=i-Hs', APoint(227.6412594882507, 191.61121280391768, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(110.14153591759336, 254.68669006558926, 0.0), APoint(109.702305433052, 253.04745958104795, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(139.95230543305473, 270.5123052240353, 0.0), APoint(140.39153591759606, 272.15153570857666, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(366.05850206621074, 115.48452399290031, 0.0), APoint(364.8585020662107, 114.28452399290032, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(375.3585020662125, 114.28452399290032, 0.0), APoint(376.55850206621255, 115.48452399290031, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(359.0794450652047, 105.45896588874407, 0.0), APoint(360.27944506520475, 104.25896588874409, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(360.27944506520475, 111.75896588874409, 0.0), APoint(359.0794450652047, 112.95896588874407, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(366.3585020662107, 100.77201537237036, 0.0), APoint(367.55850206621074, 101.97201537237035, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(366.05850206621074, 101.97201537237035, 0.0), APoint(364.8585020662107, 100.77201537237036, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(139.4119148475623, 226.46416136362234, 0.0), APoint(141.0511453321036, 226.90339184816372, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(110.80114533209904, 244.36823749115166, 0.0), APoint(109.16191484755772, 243.92900700661028, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(44.97451866757836, 254.92344732172356, 0.0), APoint(46.61374915211969, 255.36267780626488, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(16.363749152118764, 272.8275234492523, 0.0), APoint(14.724518667577433, 272.38829296471096, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(44.559895875555256, 243.70715095769552, 0.0), APoint(44.999126360096554, 245.34638144223683, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(14.749126360096556, 227.88153579925006, 0.0), APoint(14.309895875555254, 226.24230531470874, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(34.718032157416566, 83.11599936022705, 0.0), APoint(33.51803215741656, 81.91599936022706, 0.0))



entity = acad.model.AddLine(APoint(77.12399283695814, 81.91599936022706, 0.0), APoint(78.32399283695813, 83.11599936022705, 0.0))



entity = acad.model.AddLine(APoint(78.32399283695813, 83.11599936022705, 0.0), APoint(77.12399283695814, 81.91599936022706, 0.0))



entity = acad.model.AddLine(APoint(120.5180321574152, 81.91599936022706, 0.0), APoint(121.7180321574152, 83.11599936022705, 0.0))



entity = acad.model.AddLine(APoint(34.718032157416566, 74.26976331948865, 0.0), APoint(33.51803215741656, 73.06976331948866, 0.0))



entity = acad.model.AddLine(APoint(120.5180321574152, 73.06976331948866, 0.0), APoint(121.7180321574152, 74.26976331948865, 0.0))



entity = acad.model.AddLine(APoint(163.23935261673927, 101.51440127888593, 0.0), APoint(162.3653040199277, 102.96906242513673, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(161.79493651342594, 99.52379186092658, 0.0), APoint(162.99493651342593, 98.32379186092659, 0.0))
entity.Color = 8


entity = acad.model.AddText('مقطع', APoint(177.81897612887042, 37.866373898300026, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('مقطع', APoint(365.2475268447847, 131.35166264117197, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('مقطع', APoint(226.3167547543353, 140.54628969887904, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(61.00561975160779, 229.42405144666895, 0.0), APoint(59.51747217449911, 227.93544886004662, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(61.015024072422875, 269.3290301956912, 0.0), APoint(61.01557334197196, 272.3047763874313, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(61.015024072422875, 269.3290301956912, 0.0), APoint(59.52642114675609, 270.817178111742, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(25.63339855810318, 261.1430442238922, 0.0), APoint(26.430866001661798, 262.3991541320247, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(26.430866001661798, 262.3991541320247, 0.0), APoint(24.37644064895312, 261.94105003849455, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(38.42261851791909, 250.67033194253167, 0.0), APoint(39.91021679361029, 249.18117974731354, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(39.91021679361029, 249.18117974731354, 0.0), APoint(38.42234369773723, 249.18145438208956, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(37.13291746019877, 282.1045448533092, 0.0), APoint(37.13291746019877, 280.1127245821847, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(37.13291746019877, 280.1127245821847, 0.0), APoint(39.18734281290699, 282.5626489468385, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(114.10503306805913, 250.6559498215629, 0.0), APoint(112.61485797144952, 249.16732971187122, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(112.61485797144952, 249.16732971187122, 0.0), APoint(115.59263134374805, 249.16679762634624, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(216.66321585906553, 198.517262344026, 0.0), APoint(233.88638090077438, 198.517262344026, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(233.88638090077438, 198.517262344026, 0.0), APoint(230.8592839188932, 199.35153547791856, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-096 %', APoint(220.16600460045447, 198.96823443682956, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('به سمت کیلومتر بیشتر', APoint(234.70002648266654, 198.5637218808297, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('i-092', APoint(14.420574971937555, 247.51731843973496, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('i-094', APoint(73.66342937093555, 202.50501123465074, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('i-095', APoint(129.21399861891655, 247.79745180699797, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('i-093', APoint(72.18681963028166, 283.129813015315, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(81.28558413327096, 126.65269564463642, 0.0), APoint(93.72965349272249, 126.65269564463642, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.72965349272249, 126.65269564463642, 0.0), APoint(92.2161050017819, 127.06983221181554, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-099 %', APoint(83.20649667367229, 127.24415835969967, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(74.04948792313348, 126.65269564463642, 0.0), APoint(61.60541856368195, 126.65269564463642, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.60541856368195, 126.65269564463642, 0.0), APoint(63.11896705456434, 127.06983221181554, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-098 %', APoint(66.48239742618875, 127.40024669234526, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('i-092', APoint(19.290126887625092, 96.39567746009126, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('i-095', APoint(126.44368164787397, 96.50906203607448, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('i-161', APoint(138.9004990430826, 16.310675829568027, 0.0), 4.0)
entity.Color = 1

entity = acad.model.AddText('i-162', APoint(133.21161950275015, 6.930427531728016, 0.0), 4.0)
entity.Color = 1

entity = acad.model.AddText('i-163', APoint(172.61304054557147, 16.423246599519985, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-164', APoint(172.13668673507195, 7.6274657833401225, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-165', APoint(214.14010818091788, 18.81413230542546, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-166', APoint(214.22244369193868, 7.193443505081677, 0.0), 1.5)
entity.Color = 7

entity = acad.model.AddText('i-168', APoint(256.76944855299257, 7.951570707954943, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('i-167', APoint(256.9134080336812, 17.50061594009617, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(59.580763228914634, 227.872177151313, 0.0), APoint(61.00559630206925, 229.2970102244676, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.66916508711533, 227.78380231421704, 0.0), APoint(61.005563666227445, 229.12020089332918, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.75756694531603, 227.69542747712111, 0.0), APoint(61.00553103038567, 228.94339156219075, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.84596880351678, 227.60705264002524, 0.0), APoint(61.005498394543864, 228.76658223105233, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.93437066171748, 227.5186778029293, 0.0), APoint(61.00546575870209, 228.5897728999139, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.022772519918206, 227.4303029658334, 0.0), APoint(61.00543312286031, 228.41296356877547, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.11117437811893, 227.34192812873746, 0.0), APoint(61.005400487018534, 228.23615423763707, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.19957623631966, 227.25355329164154, 0.0), APoint(61.00536785117673, 228.0593449064986, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.287978094520355, 227.1651784545456, 0.0), APoint(61.005335215334924, 227.88253557536018, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.37637995272111, 227.07680361744974, 0.0), APoint(61.005302579493176, 227.7057262442218, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.46478181092181, 226.9884287803538, 0.0), APoint(61.00526994365137, 227.52891691308335, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.55318366912253, 226.9000539432579, 0.0), APoint(61.005237307809594, 227.35210758194495, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.64158552732326, 226.81167910616196, 0.0), APoint(61.00520467196779, 227.1752982508065, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.729987385523955, 226.72330426906603, 0.0), APoint(61.005172036125984, 226.99848891966803, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.81838924372471, 226.63492943197014, 0.0), APoint(61.005139400284236, 226.82167958852966, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.906791101925435, 226.54655459487424, 0.0), APoint(61.00510676444243, 226.64487025739123, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.99519296012613, 226.45817975777828, 0.0), APoint(61.005074128600626, 226.46806092625278, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.13291746019878, 281.9686404460409, 0.0), APoint(37.307823017730826, 282.14354600357296, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.13291746019877, 281.79186375074426, 0.0), APoint(37.535330183031704, 282.1942764735772, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.13291746019878, 281.61508705544765, 0.0), APoint(37.76283734833261, 282.2450069435815, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.132917460198755, 281.438310360151, 0.0), APoint(37.99034451363353, 282.29573741358575, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.13291746019877, 281.26153366485437, 0.0), APoint(38.21785167893444, 282.34646788359004, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.132917460198726, 281.0847569695577, 0.0), APoint(38.445358844235344, 282.3971983535943, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.13291746019877, 280.9079802742611, 0.0), APoint(38.67286600953628, 282.4479288235986, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.13291746019878, 280.7312035789645, 0.0), APoint(38.900373174837185, 282.4986592936029, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.13291746019877, 280.5544268836678, 0.0), APoint(39.12788034013809, 282.5493897636071, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.13291746019878, 280.3776501883712, 0.0), APoint(38.509077363237694, 281.7538100914101, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.13291746019877, 280.20087349307454, 0.0), APoint(37.59080825606898, 280.6587642889448, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.404502038105292, 261.81560382148865, 0.0), APoint(24.574001081172824, 261.9851028645562, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.436817046878474, 261.6711421349652, 0.0), APoint(24.801508246473844, 262.0358333345606, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.46913205565167, 261.52668044844177, 0.0), APoint(25.02901541177485, 262.086563804565, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.50144706442491, 261.3822187619184, 0.0), APoint(25.25652257707587, 262.13729427456934, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.533762073198062, 261.23775707539494, 0.0), APoint(25.48402974237689, 262.18802474457374, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.5660770819713, 261.0932953888715, 0.0), APoint(25.71153690767791, 262.23875521457813, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.59839209074451, 260.9488337023481, 0.0), APoint(25.93904407297893, 262.2894856845825, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.63070709951772, 260.80437201582464, 0.0), APoint(26.16655123827998, 262.3402161545869, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.663022108290903, 260.65991032930117, 0.0), APoint(26.394058403581, 262.39094662459127, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.695337117064113, 260.51544864277776, 0.0), APoint(26.17322300688447, 261.9933345325981, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.727652125837352, 260.37098695625434, 0.0), APoint(25.865851426256967, 261.50918625667396, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.759967134610534, 260.2265252697309, 0.0), APoint(25.558479845630174, 261.02503798075054, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.792282143383773, 260.0820635832075, 0.0), APoint(25.251108265005456, 260.54088970482917, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.824597152156954, 259.93760189668404, 0.0), APoint(24.943736684380738, 260.05674142890786, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.049673396523346, 249.18170775248763, 0.0), APoint(38.48042785892248, 250.61246221488676, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.22641746802407, 249.18167512869172, 0.0), APoint(38.56877006619703, 250.5240277268647, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.4031615395248, 249.18164250489585, 0.0), APoint(38.65711227347154, 250.43559323884259, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.57990561102555, 249.18160988109997, 0.0), APoint(38.74545448074609, 250.34715875082048, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.75664968252627, 249.18157725730404, 0.0), APoint(38.83379668802064, 250.2587242627984, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.933393754026994, 249.1815446335081, 0.0), APoint(38.92213889529519, 250.17028977477634, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.54772744577342, 270.79587832525453, 0.0), APoint(61.01556576307708, 272.2637166425582, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.110137825527744, 249.18151200971224, 0.0), APoint(39.01048110256971, 250.0818552867542, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.636129303974116, 270.70750348815864, 0.0), APoint(61.015533127235415, 272.0869073114199, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.28688189702849, 249.18147938591636, 0.0), APoint(39.09882330984429, 249.99342079873213, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.724531162174756, 270.6191286510626, 0.0), APoint(61.01550049139372, 271.9100979802816, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.463625968529186, 249.1814467621204, 0.0), APoint(39.187165517118814, 249.90498631071003, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.81293302037545, 270.53075381396667, 0.0), APoint(61.01546785555206, 271.7332886491433, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.64037004002971, 249.18141413832427, 0.0), APoint(39.275507724393364, 249.81655182268793, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.90133487857615, 270.4423789768707, 0.0), APoint(61.01543521971037, 271.55647931800496, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.81711411153026, 249.1813815145282, 0.0), APoint(39.363849931667914, 249.72811733466585, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.98973673677685, 270.3540041397748, 0.0), APoint(61.015402583868706, 271.37966998686665, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.99385818303081, 249.18134889073212, 0.0), APoint(39.452192138942465, 249.63968284664378, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.07813859497752, 270.2656293026788, 0.0), APoint(61.015369948027015, 271.20286065572833, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(39.17060225453136, 249.18131626693602, 0.0), APoint(39.54053434621699, 249.55124835862165, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.166540453178214, 270.1772544655829, 0.0), APoint(61.01533731218532, 271.02605132458996, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(39.34734632603191, 249.18128364313992, 0.0), APoint(39.62887655349154, 249.46281387059958, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.25494231137891, 270.08887962848695, 0.0), APoint(61.01530467634366, 270.8492419934517, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(39.52409039753243, 249.18125101934382, 0.0), APoint(39.71721876076609, 249.37437938257747, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.34334416957955, 270.00050479139094, 0.0), APoint(61.015272040502, 270.6724326623134, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(39.70083446903298, 249.18121839554772, 0.0), APoint(39.80556096804064, 249.28594489455537, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.43174602778025, 269.912129954295, 0.0), APoint(61.015239404660335, 270.49562333117507, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(39.877578540533534, 249.18118577175164, 0.0), APoint(39.89390317531516, 249.19751040653327, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.52014788598095, 269.8237551171991, 0.0), APoint(61.01520676881864, 270.31881400003675, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.608549744181616, 269.7353802801031, 0.0), APoint(61.01517413297695, 270.14200466889844, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.696951602382285, 269.6470054430071, 0.0), APoint(61.01514149713532, 269.9651953377602, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.78535346058298, 269.55863060591116, 0.0), APoint(61.015108861293626, 269.7883860066218, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.87375531878365, 269.4702557688152, 0.0), APoint(61.01507622545196, 269.61157667548355, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.96215717698435, 269.38188093171925, 0.0), APoint(61.01504358961027, 269.4347673443452, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.69570649639212, 249.1673152653958, 0.0), APoint(114.14466636018219, 250.61627512918588, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.87245160986411, 249.16728368357116, 0.0), APoint(114.23300856745668, 250.52784064116372, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.04919672333611, 249.16725210174653, 0.0), APoint(114.3213507747312, 250.43940615314162, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.22594183680808, 249.16722051992184, 0.0), APoint(114.4096929820057, 250.35097166511946, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.4026869502801, 249.16718893809724, 0.0), APoint(114.49803518928024, 250.26253717709739, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.57943206375208, 249.1671573562726, 0.0), APoint(114.58637739655475, 250.17410268907528, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.75617717722405, 249.16712577444792, 0.0), APoint(114.67471960382927, 250.08566820105318, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.93292229069604, 249.1670941926233, 0.0), APoint(114.76306181110377, 249.99723371303102, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.10966740416804, 249.16706261079867, 0.0), APoint(114.85140401837832, 249.90879922500892, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.28641251764, 249.16703102897398, 0.0), APoint(114.93974622565284, 249.82036473698682, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.463157631112, 249.16699944714935, 0.0), APoint(115.02808843292733, 249.73193024896466, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.63990274458399, 249.1669678653247, 0.0), APoint(115.11643064020188, 249.64349576094259, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.81664785805596, 249.16693628350004, 0.0), APoint(115.20477284747638, 249.55506127292045, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.99339297152795, 249.16690470167538, 0.0), APoint(115.2931150547509, 249.46662678489832, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.17013808499995, 249.16687311985072, 0.0), APoint(115.38145726202539, 249.3781922968762, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.34688319847197, 249.16684153802612, 0.0), APoint(115.46979946929997, 249.28975780885412, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.52362831194391, 249.1668099562014, 0.0), APoint(115.55814167657446, 249.201323320832, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.41168079321346, 167.15669361111495, 0.0), APoint(314.69676463929534, 167.4417774571968, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.47294595787974, 167.0411820804846, 0.0), APoint(314.8122761699257, 167.38051229253057, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.58393039176997, 166.97538981907815, 0.0), APoint(314.87806843133217, 167.26952785864034, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.5610145241905, 157.27480442183497, 0.0), APoint(322.84475109911784, 157.5585409967623, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.62163181554047, 157.15864501788835, 0.0), APoint(322.9609105030645, 157.49792370541232, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.73199975307006, 157.09223626012124, 0.0), APoint(323.0273192608316, 157.38755576788276, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.560245760513, 153.2081716663348, 0.0), APoint(322.84088489439165, 153.4888108002135, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.61939497132505, 153.09054418185025, 0.0), APoint(322.9585123788762, 153.4296615894014, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.72839328261983, 153.02276579784842, 0.0), APoint(323.0262907628781, 153.32066327810662, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.56338872886414, 167.19748884329164, 0.0), APoint(310.8128446467115, 167.44694476113898, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.6089112863399, 167.06623470547075, 0.0), APoint(310.94409878453234, 167.4014222036632, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.70680079712616, 166.98734752096033, 0.0), APoint(311.0229859690428, 167.30353269287696, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.87407398657956, 166.97784401511714, 0.0), APoint(311.032489474886, 167.13625950342353, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.5248306832272, 153.19357186922036, 0.0), APoint(310.8220665105926, 153.49080769658576, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.59225420727444, 153.08421869797098, 0.0), APoint(310.931419681842, 153.42338417253848, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.70949745096, 153.02468524635987, 0.0), APoint(310.9909531334531, 153.30614092885298, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.50699152655335, 153.28664541602046, 0.0), APoint(314.67690348201154, 153.45655737147865, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.521039767242, 153.12391696141245, 0.0), APoint(314.8396319366195, 153.44250913079006, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.6016674216787, 153.0277679205526, 0.0), APoint(314.9357809774794, 153.36188147635323, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.73539282208924, 152.98471662566644, 0.0), APoint(314.9788322723656, 153.2281560759428, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.51613218810303, 157.42751406121545, 0.0), APoint(310.7363903268463, 157.64777219995872, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.549904182233, 157.2845093600488, 0.0), APoint(310.879395028013, 157.61400020582875, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.6401616291213, 157.19799011164045, 0.0), APoint(310.96591427642124, 157.52374275894041, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.78998006220314, 157.17103184942567, 0.0), APoint(310.9928725386361, 157.37392432585858, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.27614970495773, 159.06100741446772, 0.0), APoint(317.4916105542438, 159.2764682637537, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.30803251455734, 158.91611352877067, 0.0), APoint(317.63650443994084, 159.24458545415413, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.3972063477222, 158.82851066663892, 0.0), APoint(317.7241073020726, 159.15541162098924, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.54496027673315, 158.7994879003532, 0.0), APoint(317.75313006835825, 159.00765769197832, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.2813022445781, 166.84433454714014, 0.0), APoint(317.46039648503637, 167.02342878759833, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.29895724164373, 166.68521284890912, 0.0), APoint(317.61951818326736, 167.00577379053271, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.3810848582769, 166.59056377024558, 0.0), APoint(317.71416726193087, 166.9236461738996, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.5170307345516, 166.5497329512237, 0.0), APoint(317.75499808095276, 166.78770029762484, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.47805242504137, 159.075725799169, 0.0), APoint(323.67689216954267, 159.2745655436703, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.50342704784464, 158.92432372667565, 0.0), APoint(323.828294242036, 159.24919092086702, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.58914285723154, 158.8332628407659, 0.0), APoint(323.9193551279458, 159.16347511148015, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.73078744797203, 158.79813073620977, 0.0), APoint(323.9544872325019, 159.02183052073963, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.4861462233493, 166.86199419052895, 0.0), APoint(323.64273684164726, 167.01858480882697, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.49492467618984, 166.69399594807288, 0.0), APoint(323.8107350841034, 167.0098063559864, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.5735490552005, 166.59584363178686, 0.0), APoint(323.90888740038935, 166.93118197697578, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.70443928961987, 166.54995717090964, 0.0), APoint(323.95477386126663, 166.80029174255637, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.6811719904781, 159.0916610292235, 0.0), APoint(329.86095693948903, 159.27144597823437, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.6990976603621, 158.9328100038108, 0.0), APoint(330.01980796490164, 159.2535203083504, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.7813422331178, 158.8382778812699, 0.0), APoint(330.11434008744254, 159.17127573559466, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.91746499036134, 158.79762394321676, 0.0), APoint(330.1549940254957, 159.03515297835116, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.69353948728656, 166.88220311908398, 0.0), APoint(329.8225279130939, 167.0111915448913, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.69119267909775, 166.70307961559848, 0.0), APoint(330.00165141657936, 167.0135383530801, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.7662642286919, 166.60137446989603, 0.0), APoint(330.1033565622818, 166.93846680348594, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.8924529448743, 166.55078649078183, 0.0), APoint(330.1539445413961, 166.81227808730353, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.8859490579601, 159.1092537613232, 0.0), APoint(336.0433642073904, 159.26666891075354, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.8950552476699, 158.94158325573636, 0.0), APoint(336.21103471297727, 159.2575627210437, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.9737979232078, 158.84354923597766, 0.0), APoint(336.30906873273597, 159.1788200455058, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(336.1048516702716, 158.79782628774475, 0.0), APoint(336.3547916809689, 159.04776629844204, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.9057267292001, 166.9072060256152, 0.0), APoint(335.9975250065635, 166.99900430297856, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.88777709859414, 166.71247969971265, 0.0), APoint(336.19225133246607, 167.01695393358452, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.9592264755827, 166.6071523814045, 0.0), APoint(336.2975786507742, 166.945504556596, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(336.0809971059038, 166.552146316429, 0.0), APoint(336.3525847157497, 166.82373392627488, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.09323351729176, 159.12935388527256, 0.0), APoint(342.2232640834377, 159.25938445141853, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.09131292015803, 158.95065659284217, 0.0), APoint(342.4019613758681, 159.2613050485523, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.16650474179266, 158.8490717191802, 0.0), APoint(342.5035462495301, 159.1861132269176, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.29284633889074, 158.79863662098165, 0.0), APoint(342.5539813477286, 159.05977162981952, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.0846970081061, 166.72221527384227, 0.0), APoint(342.38251575833397, 167.02003402407013, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.15243304221957, 166.61317461265907, 0.0), APoint(342.4915564195171, 166.95229798995666, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.27001452606265, 166.5539794012056, 0.0), APoint(342.55075163097064, 166.83471650611352, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.3051829449683, 159.15411897756678, 0.0), APoint(348.39849899114427, 159.24743502374272, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.2878864285591, 158.9600457658609, 0.0), APoint(348.5925722028501, 159.26473154015196, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.35945874573645, 158.85484138774166, 0.0), APoint(348.6977765809694, 159.19315922297457, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.48137370085897, 158.7999796475675, 0.0), APoint(348.7526383211435, 159.07124426785208, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.28197546875606, 166.7323093991099, 0.0), APoint(348.57242163306563, 167.02275556341948, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.34588226317555, 166.61943949823282, 0.0), APoint(348.68529153394263, 166.9588487689999, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.4594602540759, 166.55624079383654, 0.0), APoint(348.748490238339, 166.84527077809963, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.53873727330546, 159.2004889705217, 0.0), APoint(354.5521289981896, 159.2138806954058, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.4847947269432, 158.9697697288628, 0.0), APoint(354.7828482398485, 159.26782324176804, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.55265714394153, 158.86085545056443, 0.0), APoint(354.89176251814683, 159.19996082476973, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.67037602185314, 158.8017976331794, 0.0), APoint(354.95082033553183, 159.08224194685815, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.47964056963167, 166.74279016460324, 0.0), APoint(354.7619408675731, 167.02509046254468, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.5395735249078, 166.62594642458276, 0.0), APoint(354.87878460759356, 166.96515750726854, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.64929835187337, 166.5588945562517, 0.0), APoint(354.94583647592464, 166.85543268030295, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.68206072753986, 158.97985139407712, 0.0), APoint(360.9727665746358, 159.27055724117304, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.7460982351697, 158.86711220641033, 0.0), APoint(361.08550576230255, 159.20651973354322, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.8598079985947, 158.80404527453874, 0.0), APoint(361.14857269417416, 159.0928099701182, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.6777268769553, 166.75369213654466, 0.0), APoint(360.95103889563376, 167.0270041552231, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.7335072525173, 166.63269581680998, 0.0), APoint(361.07203521536843, 166.9712237796611, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.83949967941675, 166.56191154841275, 0.0), APoint(361.14281948376566, 166.86523135276167, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(361.0380008902707, 166.5836360639701, 0.0), APoint(361.12109496820835, 166.66673014190772, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.8797123299004, 158.99031866105537, 0.0), APoint(367.1622993076578, 159.27290563881274, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.93978137090835, 158.8736110067667, 0.0), APoint(367.2790069619464, 159.21283659780474, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.0496334310275, 158.8066863715892, 0.0), APoint(367.345931597124, 159.1029845376857, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.876277504301, 166.76505842850804, 0.0), APoint(367.1396726036701, 167.0284535278771, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.92768491891604, 166.6396891478264, 0.0), APoint(367.2650418843517, 166.97704611326208, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.0300403519288, 166.56526788554248, 0.0), APoint(367.33946314663564, 166.87469068024933, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.2115462465059, 166.56999708482297, 0.0), APoint(367.3347339473552, 166.69318478567223, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.0777838534807, 159.0012058492534, 0.0), APoint(373.3514121194569, 159.27483411522954, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.13370694136995, 158.88035224184603, 0.0), APoint(373.4722657268643, 159.21891102734037, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.23982297892957, 158.80969158410898, 0.0), APoint(373.5429263846013, 159.1127949897807, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.4390773506555, 158.83216926053825, 0.0), APoint(373.520448708172, 158.91354061805475, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.07534716119517, 166.77694375001988, 0.0), APoint(373.3277872821554, 167.0293838709801, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.1221090768789, 166.64692897040698, 0.0), APoint(373.4578020617683, 166.98262195529634, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.22090063707606, 166.56894383530746, 0.0), APoint(373.5357871968678, 166.88383039509924, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.3907103747281, 166.56197687766291, 0.0), APoint(373.5427541545123, 166.71402065744712, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.085656320996, 159.1702435519369, 0.0), APoint(382.15304586882417, 159.23763309976505, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.05698941584063, 158.96479995148485, 0.0), APoint(382.3584894692762, 159.26630000492042, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.12674419205837, 158.85777803240592, 0.0), APoint(382.46551138835514, 159.1965452287027, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.2465631165471, 158.80082026159803, 0.0), APoint(382.52246915916294, 159.0767263042139, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.0514446909708, 166.737429819667, 0.0), APoint(382.33797266455906, 167.02395779325525, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.113411026541, 166.6226194599406, 0.0), APoint(382.4527830242854, 166.96199145768503, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.2250712121537, 166.55750295025666, 0.0), APoint(382.5178995339694, 166.85033127207237, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.2540710420479, 158.9746972423098, 0.0), APoint(388.54859217845154, 159.26921837871345, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.320062470197, 158.86391197516224, 0.0), APoint(388.65937744559903, 159.20322695056427, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.43578244240507, 158.80285525207373, 0.0), APoint(388.7204341686876, 159.08750697835623, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.2493128013922, 166.7481135947061, 0.0), APoint(388.52728888952026, 167.02608968283423, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.3072217917748, 166.62924588979212, 0.0), APoint(388.6461565944342, 166.96818069245154, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.4150917953163, 166.56033919803696, 0.0), APoint(388.7150632861894, 166.86031068891003, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.6280248279901, 166.59649553541408, 0.0), APoint(388.6789069488123, 166.6473776562363, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.4515234337654, 158.98496529864497, 0.0), APoint(394.73832412211385, 159.27176598699344, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.51362299124355, 158.8702881608265, 0.0), APoint(394.8530012599323, 159.2096664295153, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.62541258611026, 158.80530106039663, 0.0), APoint(394.9179883603622, 159.09787683464856, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.54564742152525, 159.00802147453942, 0.0), APoint(401.8134062289025, 159.2757802819167, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.5989561466964, 158.88455350441393, 0.0), APoint(401.936874199028, 159.22247155674552, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.7028577310154, 158.81167839343624, 0.0), APoint(402.00974931000565, 159.11856997242649, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.8906634672511, 158.82270743437536, 0.0), APoint(401.99872026906655, 158.9307642361908, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.543874898589, 166.78442354465517, 0.0), APoint(401.7891172222518, 167.02966586831792, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.58766316942194, 166.65143512019145, 0.0), APoint(401.9221056467154, 166.98587759748497, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.68432327952956, 166.5713185350025, 0.0), APoint(402.0022222319044, 166.88921748737732, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.84834286222974, 166.558561422406, 0.0), APoint(402.01497934450094, 166.7251979046772, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.4950428590958, 157.34056074038557, 0.0), APoint(314.784114293018, 157.62963217430777, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.558262176512, 157.22700336250512, 0.0), APoint(314.89767167089843, 157.5664128568916, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.67115255456645, 157.163117045263, 0.0), APoint(314.9615579881406, 157.4535224788371, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.5988654560389, 167.18776367265548, 0.0), APoint(404.85745727212674, 167.44635548874334, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.6482156502366, 167.06033717155654, 0.0), APoint(404.98488377322565, 167.39700529454566, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.7489563916053, 166.98430121762868, 0.0), APoint(405.06091972715353, 167.2962645531769, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.9247756586442, 166.9833437893709, 0.0), APoint(405.0618771554113, 167.12044528613802, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.4526652241228, 153.20793249595044, 0.0), APoint(396.73349788408444, 153.48876515591206, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.5119053282532, 153.09039590478415, 0.0), APoint(396.85103447525074, 153.4295250517817, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.620987354171, 153.0227012354053, 0.0), APoint(396.91872914462954, 153.32044302586382, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.448522653541, 167.1483335736316, 0.0), APoint(408.74001213155236, 167.43982305164297, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.5129562978022, 167.03599052259614, 0.0), APoint(408.8523551825878, 167.37538940738176, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.6270674489431, 166.9733249784404, 0.0), APoint(408.9150207267436, 167.2612782562409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.49148808763056, 153.2259400792869, 0.0), APoint(408.7633402829592, 153.4977922746155, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.5466125437042, 153.10428784006388, 0.0), APoint(408.8849925221822, 153.44266781854185, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.6520409516033, 153.03293955266628, 0.0), APoint(408.9563408095798, 153.33723941064278, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.84731390681645, 153.0514358125828, 0.0), APoint(408.9378445496633, 153.14196645542964, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.5686104144273, 153.19214970260964, 0.0), APoint(404.8642815021517, 153.487820790334, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.6352039448093, 153.08196653769494, 0.0), APoint(404.97446466706634, 153.421227259952, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.75155907038936, 153.02154496797837, 0.0), APoint(405.0348862367829, 153.30487213437195, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.4986175430206, 157.47571022179613, 0.0), APoint(408.6618361486987, 157.63892882747422, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.5100243719968, 157.3103403554757, 0.0), APoint(408.8272060150191, 157.62752199849805, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.5896206895098, 157.2131599776921, 0.0), APoint(408.9243863928027, 157.54792568098503, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.72186865462163, 157.16863124750728, 0.0), APoint(408.96891512298754, 157.4156777158732, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.5156006874164, 157.38178066271794, 0.0), APoint(404.72394620032594, 157.5901261756275, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.5446922618164, 157.23409554182138, 0.0), APoint(404.8716313212225, 157.56103460122745, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.63233195778923, 157.14495854249753, 0.0), APoint(404.9607683205463, 157.47339490525462, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.77729121537266, 157.1131411047843, 0.0), APoint(404.99258575825957, 157.3284356476712, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.4505989225363, 157.27173018618657, 0.0), APoint(396.7208917421863, 157.5420230058366, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.50502772510356, 157.14938229345717, 0.0), APoint(396.8432396349157, 157.48759420326928, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.60986523651917, 157.0774431095761, 0.0), APoint(396.9151788187968, 157.38275669185373, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.8020599118805, 157.09286108964088, 0.0), APoint(396.89976083873205, 157.19056201649235, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

try:
    acad_doc = acad.app.ActiveDocument
    acad_doc.SaveAs(file_path)
    print(f'Drawing saved successfully at {file_path}')
except Exception as e:
    print(f'Error saving drawing: {e}')
