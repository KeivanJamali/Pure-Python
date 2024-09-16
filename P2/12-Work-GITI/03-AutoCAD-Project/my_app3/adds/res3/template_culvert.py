file_path = r'D:/All Python/Pure-Python/P2/12-Work-GITI/03-AutoCAD-Project/my_app3/adds/res3\Culvert-Final.dwg'
file_to_open = r'D:/All Python/Pure-Python/P2/12-Work-GITI/03-AutoCAD-Project/my_app3/adds/res3\Culvert.dwg'
from pyautocad import Autocad, APoint, aDouble
import time

acad = Autocad(create_if_not_exists=True)
acad.app.Visible = True
acad.app.documents.Open(file_to_open)
time.sleep(5)
for entity in acad.doc.ModelSpace:
    try:
        entity.Delete()
    except Exception as e:
        print(f'[ERROR] Failed to delete entity. ---Try Again---')

entity = acad.model.AddLine(APoint(50.07301469313916, 263.45622526883085, 0.0), APoint(88.7826002666402, 263.45622526883085, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 263.45622526883085, 0.0), APoint(105.07301469314325, 263.45622526883085, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 261.95622526883085, 0.0), APoint(88.7826002666402, 261.95622526883085, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 261.95622526883085, 0.0), APoint(106.57301469313916, 261.95622526883085, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 259.956225268831, 0.0), APoint(88.7826002666402, 259.9562252688311, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 259.9562252688311, 0.0), APoint(106.57301469313916, 259.956225268831, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 239.95622526883062, 0.0), APoint(88.7826002666402, 239.95622526883065, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 239.95622526883062, 0.0), APoint(106.57301469313916, 239.95622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 237.95622526883085, 0.0), APoint(88.78260026663929, 237.9562252688309, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 237.95622526883085, 0.0), APoint(105.07301469314325, 237.95622526883085, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 235.95622526883062, 0.0), APoint(88.7826002666402, 235.95622526883065, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 235.95622526883062, 0.0), APoint(106.57301469313916, 235.95622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.07301469314325, 260.8222506726142, 0.0), APoint(105.07301469314325, 227.95685819135028, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.82301469314325, 260.1005628361312, 0.0), APoint(106.82301469314325, 227.94847715233914, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 263.45622526883085, 0.0), APoint(106.57301469313916, 227.94967444362646, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 215.95622526883062, 0.0), APoint(88.7826002666402, 215.95622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 215.95622526883062, 0.0), APoint(106.57301469313916, 215.95622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 213.95622526883062, 0.0), APoint(88.78260026663929, 213.95622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 213.95622526883062, 0.0), APoint(105.07301469314325, 213.95622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 211.95622526883062, 0.0), APoint(88.7826002666402, 211.95622526883065, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 211.95622526883062, 0.0), APoint(106.57301469313916, 211.95622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469314007, 188.45622526883062, 0.0), APoint(88.7826002666402, 188.45622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 188.45622526883062, 0.0), APoint(106.57301469313916, 188.45622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 189.95622526883062, 0.0), APoint(88.7826002666402, 189.95622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 189.95622526883062, 0.0), APoint(106.57301469313916, 189.95622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 191.95622526883062, 0.0), APoint(88.7826002666402, 191.9562252688308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 191.9562252688308, 0.0), APoint(106.57301469313916, 191.95622526883085, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313825, 263.45622526883085, 0.0), APoint(105.07301469314325, 263.45622526883085, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(106.57301469313916, 213.95622526883062, 0.0), 2.0, 4.71238898038469, 1.5707963267948966)
entity.Color = 3

entity = acad.model.AddArc(APoint(106.57301469313916, 213.95622526883062, 0.0), 4.5, 4.71238898038469, 1.5707963267948966)
entity.Color = 3

entity = acad.model.AddLine(APoint(107.16378905169131, 215.86698052717156, 0.0), APoint(107.9022569998865, 218.25542460009774, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.82301469307004, 215.94053875213103, 0.0), APoint(107.13551469308095, 218.42093060625348, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.01676672001531, 212.00607549460187, 0.0), APoint(107.57145675346419, 209.56838827783372, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.34866508401774, 212.11275938244057, 0.0), APoint(108.31822807239314, 209.80842702542873, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.6569957033903, 212.27545604838383, 0.0), APoint(109.0119719659092, 210.17449452374308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.93239010828711, 212.48922203657116, 0.0), APoint(109.63160937686689, 210.65546799709068, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.16648057907605, 212.74756217561048, 0.0), APoint(110.15831293608198, 211.23673330985753, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.35215439524245, 213.04262693111582, 0.0), APoint(110.57607902242125, 211.9006290096661, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.48376995185117, 213.36545090980167, 0.0), APoint(110.87221402477417, 212.62698296161147, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.55732817681337, 213.70622526842567, 0.0), APoint(111.0377200309349, 213.39372526841657, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.57059404067513, 214.05459575054124, 0.0), APoint(111.06756822465195, 214.17755885308566, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.52316446689383, 214.39997729533275, 0.0), APoint(110.9608516836638, 214.95466732878072, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.41648057905377, 214.731875659337, 0.0), APoint(110.7208129360697, 215.7014386477124, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.25378391311506, 215.04020627871, 0.0), APoint(110.35474543775308, 216.3951825412289, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.04001792493091, 215.31560068360818, 0.0), APoint(109.8737719644023, 217.01481995218614, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.78167778588022, 215.54969115439349, 0.0), APoint(109.2925066516259, 217.54152351139965, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.48661303036806, 215.73536497056352, 0.0), APoint(108.62861095182598, 217.9592895977487, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 218.45622526883062, 0.0), APoint(88.7826002666402, 218.45622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 218.45622526883062, 0.0), APoint(106.57301469313916, 218.45622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 209.45622526883062, 0.0), APoint(88.7826002666402, 209.4562252688308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 209.4562252688308, 0.0), APoint(106.57301469313916, 209.45622526883085, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(106.57301469313916, 237.95622526883085, 0.0), 2.0, 4.71238898038469, 1.5707963267948966)
entity.Color = 3

entity = acad.model.AddArc(APoint(106.57301469313916, 237.95622526883085, 0.0), 4.5, 4.71238898038469, 1.5707963267948966)
entity.Color = 3

entity = acad.model.AddLine(APoint(107.16378905169131, 239.8669805271718, 0.0), APoint(107.9022569998865, 242.2554246000982, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.82301469307004, 239.94053875213103, 0.0), APoint(107.13551469308095, 242.4209306062537, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.01676672001531, 236.00607549460187, 0.0), APoint(107.57145675346419, 233.56838827783372, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.34866508401774, 236.11275938244057, 0.0), APoint(108.31822807239314, 233.80842702542873, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.6569957033903, 236.27545604838383, 0.0), APoint(109.0119719659092, 234.17449452374308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.93239010828711, 236.48922203657116, 0.0), APoint(109.63160937686689, 234.65546799709068, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.16648057907605, 236.74756217561048, 0.0), APoint(110.15831293608198, 235.23673330985753, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.35215439524245, 237.04262693111582, 0.0), APoint(110.57607902242125, 235.9006290096661, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.48376995185117, 237.36545090980167, 0.0), APoint(110.87221402477417, 236.62698296161147, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.55732817681337, 237.70622526842567, 0.0), APoint(111.0377200309349, 237.39372526841657, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.57059404067513, 238.05459575054124, 0.0), APoint(111.06756822465195, 238.17755885308566, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.52316446689383, 238.39997729533275, 0.0), APoint(110.9608516836638, 238.95466732878072, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.41648057905377, 238.731875659337, 0.0), APoint(110.7208129360697, 239.7014386477124, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.25378391311506, 239.04020627871, 0.0), APoint(110.35474543775308, 240.3951825412289, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.04001792493091, 239.31560068360818, 0.0), APoint(109.8737719644023, 241.01481995218614, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.78167778588022, 239.54969115439349, 0.0), APoint(109.2925066516259, 241.54152351139965, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.48661303036806, 239.73536497056352, 0.0), APoint(108.62861095182598, 241.9592895977487, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 242.45622526883102, 0.0), APoint(88.7826002666402, 242.45622526883102, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 242.45622526883102, 0.0), APoint(106.57301469313916, 242.45622526883102, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 233.45622526883062, 0.0), APoint(88.7826002666402, 233.45622526883065, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 233.45622526883062, 0.0), APoint(106.57301469313916, 233.45622526883062, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.82301469314325, 260.1005628361312, 0.0), APoint(136.8230146931419, 277.42107091181833, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.94801469314507, 259.884056485182, 0.0), APoint(136.8230146931419, 277.13239577721936, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.07301469314325, 260.8222506726142, 0.0), APoint(136.8230146931419, 279.1531217193826, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 269.600882283639, 0.0), APoint(136.8230146931419, 282.0398730653344, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 262.8429766147777, 0.0), APoint(136.8230146931419, 280.3078222577676, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(136.8230146931419, 277.13239577721936, 0.0), APoint(136.8230146931419, 282.0398730653344, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 259.956225268831, 0.0), APoint(106.57301469313916, 269.600882283639, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 191.9562252688297, 0.0), APoint(136.8230146931419, 174.4913796258429, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.82301469314325, 192.10056283612923, 0.0), APoint(136.8230146931419, 174.78005476044194, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.07301469314325, 191.0901998650473, 0.0), APoint(136.8230146931419, 172.75932881827833, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 182.3115682540224, 0.0), APoint(136.8230146931419, 169.87257747232707, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 189.06947392288407, 0.0), APoint(136.8230146931419, 171.60462827989386, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(136.8230146931419, 174.78005476044194, 0.0), APoint(136.8230146931419, 169.87257747232707, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 191.95622526883085, 0.0), APoint(106.57301469313916, 182.3115682540224, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.07301469313916, 260.8222506726162, 0.0), APoint(50.07301469313916, 228.091674026141, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.32301469313916, 259.8118877015343, 0.0), APoint(48.32301469313916, 228.091674026141, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 263.45622526883085, 0.0), APoint(48.57301469313916, 228.091674026141, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 263.45622526883085, 0.0), APoint(50.07301469313916, 263.45622526883085, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(48.57301469313916, 213.95622526883062, 0.0), 2.0, 1.5707963267948966, 4.71238898038469)
entity.Color = 3

entity = acad.model.AddArc(APoint(48.57301469313916, 213.95622526883062, 0.0), 4.5, 1.5707963267948966, 4.71238898038469)
entity.Color = 3

entity = acad.model.AddLine(APoint(47.98224033458746, 215.86698052717156, 0.0), APoint(47.24377238639636, 218.25542460009774, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.323014693207824, 215.94053875213103, 0.0), APoint(48.01051469320146, 218.42093060625348, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.12926266626664, 212.00607549460187, 0.0), APoint(47.57457263281776, 209.56838827783372, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.797364302264214, 212.11275938244057, 0.0), APoint(46.82780131388927, 209.80842702542873, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.489033682891204, 212.27545604838383, 0.0), APoint(46.1340574203723, 210.17449452374308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.213639277994844, 212.48922203657116, 0.0), APoint(45.5144200094187, 210.65546799709068, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.979548807209994, 212.74756217561048, 0.0), APoint(44.98771645020133, 211.23673330985753, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.79387499103996, 213.04262693111582, 0.0), APoint(44.569950363859334, 211.9006290096661, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.662259434431235, 213.36545090980167, 0.0), APoint(44.2738153615046, 212.62698296161147, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.58870120947313, 213.70622526842567, 0.0), APoint(44.10830935534841, 213.39372526841657, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.57543534560409, 214.05459575054124, 0.0), APoint(44.07846116163, 214.17755885308566, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.62286491938903, 214.39997729533275, 0.0), APoint(44.1851777026186, 214.95466732878072, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.72954880723182, 214.731875659337, 0.0), APoint(44.42521645021543, 215.7014386477124, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.89224547317008, 215.04020627871, 0.0), APoint(44.791283948530236, 216.3951825412289, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.1060114613515, 215.31560068360818, 0.0), APoint(45.27225742188057, 217.01481995218614, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.36435160040219, 215.54969115439349, 0.0), APoint(45.85352273465196, 217.54152351139965, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.6594163559098, 215.73536497056352, 0.0), APoint(46.51741843445507, 217.9592895977487, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(48.57301469313916, 237.95622526883085, 0.0), 2.0, 1.5707963267948966, 4.71238898038469)
entity.Color = 3

entity = acad.model.AddArc(APoint(48.57301469313916, 237.95622526883085, 0.0), 4.5, 1.5707963267948966, 4.71238898038469)
entity.Color = 3

entity = acad.model.AddLine(APoint(47.98224033458746, 239.8669805271718, 0.0), APoint(47.24377238639636, 242.2554246000982, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.323014693207824, 239.94053875213103, 0.0), APoint(48.01051469320146, 242.4209306062537, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.12926266626664, 236.00607549460187, 0.0), APoint(47.57457263281776, 233.56838827783372, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.797364302264214, 236.11275938244057, 0.0), APoint(46.82780131388927, 233.80842702542873, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.489033682891204, 236.27545604838383, 0.0), APoint(46.1340574203723, 234.17449452374308, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.213639277994844, 236.48922203657116, 0.0), APoint(45.5144200094187, 234.65546799709068, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.979548807209994, 236.74756217561048, 0.0), APoint(44.98771645020133, 235.23673330985753, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.79387499103996, 237.04262693111582, 0.0), APoint(44.569950363859334, 235.9006290096661, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.662259434431235, 237.36545090980167, 0.0), APoint(44.2738153615046, 236.62698296161147, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.58870120947313, 237.70622526842567, 0.0), APoint(44.10830935534841, 237.39372526841657, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.57543534560409, 238.05459575054124, 0.0), APoint(44.07846116163, 238.17755885308566, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.62286491938903, 238.39997729533275, 0.0), APoint(44.1851777026186, 238.95466732878072, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.72954880723182, 238.731875659337, 0.0), APoint(44.42521645021543, 239.7014386477124, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.89224547317008, 239.04020627871, 0.0), APoint(44.791283948530236, 240.3951825412289, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.1060114613515, 239.31560068360818, 0.0), APoint(45.27225742188057, 241.01481995218614, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.36435160040219, 239.54969115439349, 0.0), APoint(45.85352273465196, 241.54152351139965, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.6594163559098, 239.73536497056352, 0.0), APoint(46.51741843445507, 241.9592895977487, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
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

entity = acad.model.AddLine(APoint(48.32301469313916, 259.8118877015343, 0.0), APoint(18.323014693139157, 277.1323957772235, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.07301469313916, 260.8222506726162, 0.0), APoint(18.323014693139157, 279.1531217193867, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 269.600882283639, 0.0), APoint(18.323014693139157, 282.0398730653344, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469314325, 262.8429766147778, 0.0), APoint(18.323014693139157, 280.3078222577676, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(18.323014693139157, 277.1323957772235, 0.0), APoint(18.323014693139157, 282.0398730653344, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 259.956225268831, 0.0), APoint(48.57301469313916, 269.600882283639, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 191.9562252688297, 0.0), APoint(18.323014693139157, 174.4913796258429, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.32301469313916, 192.1005628361271, 0.0), APoint(18.198014693140067, 174.70788597678902, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.07301469313916, 191.0901998650453, 0.0), APoint(19.073014693139157, 173.19234152016625, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 182.3115682540224, 0.0), APoint(18.323014693139157, 169.87257747232707, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 189.06947392288177, 0.0), APoint(18.323014693139157, 171.60462827989386, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(18.323014693139157, 174.4913796258429, 0.0), APoint(18.323014693139157, 169.87257747232707, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 191.95622526883085, 0.0), APoint(48.57301469313916, 182.3115682540224, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(168.48793725451378, 187.53197630978252, 0.0), APoint(170.7379372545065, 187.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.7379372545065, 187.53197630978252, 0.0), APoint(170.7379372545065, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.8879372545107, 187.53197630978252, 0.0), APoint(170.8879372545107, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.7379372545065, 184.53197630978252, 0.0), APoint(173.73793725451287, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(158.24093369071488, 160.15697630978252, 0.0), APoint(180.7409336907076, 160.15697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(158.2409336907076, 152.65697630978252, 0.0), APoint(180.7409336907076, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.73793725451287, 184.53197630978252, 0.0), APoint(173.73793725451287, 182.28197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.73793725451287, 182.28197630978252, 0.0), APoint(168.48793725451378, 182.28197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(168.48793725451378, 182.28197630978252, 0.0), APoint(168.48793725451378, 187.53197630978275, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.73793725451287, 182.28197630978252, 0.0), APoint(173.73793725451287, 160.15697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(180.74093369071488, 160.15697630978252, 0.0), APoint(180.7409336907076, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(158.24093369071488, 160.15697630978252, 0.0), APoint(158.2409336907076, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(168.48793725451378, 182.28197630978252, 0.0), APoint(160.23793725451742, 160.15697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.73793725451287, 184.53197630978252, 0.0), APoint(209.8879372545107, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.73793725451287, 182.28197630978252, 0.0), APoint(209.8879372545107, 182.28197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.73793725451287, 184.53197630978252, 0.0), APoint(203.73793725451287, 182.28197630978275, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.8879372545107, 184.53197630978252, 0.0), APoint(209.8879372545107, 182.28197630978275, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(195.18793725451087, 160.15697630978252, 0.0), APoint(195.18793725451087, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.43793725451087, 160.15697630978252, 0.0), APoint(218.43793725451087, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(195.18793725451087, 160.15697630978252, 0.0), APoint(218.43793725451087, 160.15697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(195.18793725451087, 152.65697630978252, 0.0), APoint(218.43793725451087, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.73793725451287, 182.28197630978252, 0.0), APoint(200.0629372545145, 160.15697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(213.56293725450723, 160.15697630978252, 0.0), APoint(209.8879372545107, 182.28197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.8879372545125, 184.53197630978252, 0.0), APoint(246.03793725450942, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.8879372545125, 182.28197630978252, 0.0), APoint(246.03793725450942, 182.28197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.8879372545125, 184.53197630978252, 0.0), APoint(239.8879372545125, 182.28197630978275, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(246.03793725450942, 184.53197630978252, 0.0), APoint(246.03793725450942, 182.28197630978275, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(231.3379372545096, 160.15697630978252, 0.0), APoint(231.3379372545096, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(254.58793725451233, 160.15697630978252, 0.0), APoint(254.58793725451233, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(231.3379372545096, 160.15697630978252, 0.0), APoint(254.58793725451233, 160.15697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(231.3379372545096, 152.65697630978252, 0.0), APoint(254.58793725451233, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.8879372545125, 182.28197630978252, 0.0), APoint(236.21293725451142, 160.15697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(249.71293725450414, 160.15697630978252, 0.0), APoint(246.03793725450942, 182.28197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.8879372545107, 184.53197630978252, 0.0), APoint(221.98117089486658, 184.53197630978244, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(281.28793725450487, 187.53197630978252, 0.0), APoint(279.03793725451305, 187.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(279.03793725451305, 187.53197630978252, 0.0), APoint(279.03793725451305, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(279.03793725451305, 184.53197630978252, 0.0), APoint(276.0379372545094, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(276.0379372545094, 184.53197630978252, 0.0), APoint(276.0379372545094, 182.28197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(276.0379372545094, 182.28197630978252, 0.0), APoint(281.28793725450487, 182.28197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(281.28793725450487, 182.28197630978252, 0.0), APoint(281.28793725450487, 187.53197630978275, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.73793725450923, 184.53197630978252, 0.0), APoint(206.73793725450923, 187.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.8879372545107, 184.53197630978252, 0.0), APoint(206.73793725450923, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.8879372545107, 187.53197630978252, 0.0), APoint(206.73793725450923, 187.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(25.90553028255681, 78.17014287172697, 0.0), APoint(89.70644040441721, 78.80815197294578, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 78.81862988989981, 0.0), APoint(129.3305340322754, 79.20439290922445, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(25.90553028255681, 85.6705178623522, 0.0), APoint(89.70644040441721, 86.30852696357115, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 86.31900488052523, 0.0), APoint(129.3305340322754, 86.70476789984991, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157408834, 110.12886160063385, 0.0), APoint(89.70644040441721, 110.68474568310407, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 110.24882410157056, 0.0), APoint(124.86803215741656, 110.28632410157138, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.368032157416565, 113.15151159688412, 0.0), APoint(89.70644040441721, 113.68489567935416, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 113.69537359630823, 0.0), APoint(118.8680321574152, 113.97651159688417, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(129.3305340322754, 86.70476789984991, 0.0), APoint(129.3305340322754, 79.20439290922445, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(119.01803215741347, 115.87401159688397, 0.0), APoint(121.34303215741375, 115.8740115968842, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.4930321574193, 115.72401159688478, 0.0), APoint(121.4930321574193, 113.99901159688397, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.4930321574193, 113.99901159688397, 0.0), APoint(121.3838214781963, 113.99901159688397, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.22724283664729, 113.99901159688397, 0.0), APoint(121.1180321574152, 113.99901159688397, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(119.01803215741984, 115.87401159688397, 0.0), APoint(118.8680321574152, 115.72401159688388, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.34303215741375, 115.87401159688397, 0.0), APoint(121.4930321574193, 115.72401159688388, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(121.3055321574193, 113.99901159688397, 0.0), 0.0782893207747293, 0.0, 3.141592653589793)
entity.Color = 3

entity = acad.model.AddLine(APoint(118.8680321574152, 115.72401159688388, 0.0), APoint(118.8680321574152, 113.97651159688417, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 110.12886160063385, 0.0), APoint(89.70644040441721, 110.68474568310396, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 110.695223600058, 0.0), APoint(121.1180321574152, 110.99886160063397, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 110.99886160063411, 0.0), APoint(121.1180321574152, 113.99901159688397, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.11803215741656, 108.74874910344647, 0.0), APoint(127.83053403227859, 86.68976789984981, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.11803215741656, 108.74874910344647, 0.0), APoint(124.11803215741656, 110.27882410157122, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.86803215741656, 110.28632410157138, 0.0), APoint(124.86803215741656, 111.03636160063411, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 113.99901159688397, 0.0), APoint(124.86803215741656, 111.03636160063411, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 113.99901159688397, 0.0), APoint(123.71687602449083, 111.02485003930474, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 113.99901159688397, 0.0), APoint(122.87339238496679, 111.01641520290946, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 113.99901159688397, 0.0), APoint(121.72903708919239, 111.00497164995181, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(122.21226989833485, 111.00980397804324, 0.0), APoint(121.1180321574152, 113.99901159688397, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.72903708919239, 111.00497164995181, 0.0), APoint(121.72903708919239, 110.25493415088863, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(122.21226989833485, 111.00980397804324, 0.0), APoint(122.21226989833485, 110.25976647898005, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(122.87339238496679, 111.01641520290946, 0.0), APoint(122.87339238496679, 110.2663777038465, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(123.71687602449083, 111.02485003930474, 0.0), APoint(123.71687602449083, 110.27481254024224, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 109.34882410157047, 0.0), APoint(30.368032157416565, 109.38632410157129, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(25.90553028255681, 85.6705178623522, 0.0), APoint(25.90553028255681, 78.17014287172697, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.21803215741829, 114.97401159688366, 0.0), APoint(33.89303215741802, 114.97401159688388, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.74303215741338, 114.82401159688447, 0.0), APoint(33.74303215741338, 113.09901159688366, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.74303215741338, 113.09901159688366, 0.0), APoint(33.85224283663638, 113.09901159688366, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.00882147818538, 113.09901159688366, 0.0), APoint(34.118032157416565, 113.09901159688366, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.21803215741147, 114.97401159688366, 0.0), APoint(36.368032157416565, 114.82401159688379, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.89303215741802, 114.97401159688366, 0.0), APoint(33.74303215741338, 114.82401159688379, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(33.93053215741338, 113.09901159688366, 0.0), 0.0782893207747293, 0.0, 3.141592653589793)
entity.Color = 3

entity = acad.model.AddLine(APoint(36.368032157416565, 114.82401159688379, 0.0), APoint(36.368032157416565, 113.15151159688412, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.11803215741656, 108.74874910344647, 0.0), APoint(90.75423209982318, 108.42587361901812, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.70644040441721, 108.41573369938516, 0.0), APoint(31.11803215741702, 107.84874910344638, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(31.11803215741702, 107.84874910344638, 0.0), APoint(27.405530282553173, 85.7897678998495, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(31.11803215741702, 107.84874910344638, 0.0), APoint(31.11803215741702, 109.3788241015709, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(30.368032157416565, 109.38632410157129, 0.0), APoint(30.368032157416565, 110.13636160063379, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 113.09901159688366, 0.0), APoint(30.368032157416565, 110.13636160063379, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 113.09901159688366, 0.0), APoint(31.519188290340026, 110.12485003930442, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 113.09901159688366, 0.0), APoint(32.36267192986497, 110.11641520290914, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 113.09901159688366, 0.0), APoint(33.507027225640286, 110.1049716499515, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.02379441649782, 110.10980397804292, 0.0), APoint(34.118032157416565, 113.09901159688366, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.507027225640286, 110.1049716499515, 0.0), APoint(33.507027225640286, 109.35493415088831, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.02379441649782, 110.10980397804292, 0.0), APoint(33.02379441649782, 109.35976647897974, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.36267192986497, 110.11641520290914, 0.0), APoint(32.36267192986497, 109.36637770384618, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(31.519188290340026, 110.12485003930442, 0.0), APoint(31.519188290340026, 109.37481254024192, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.11803215741656, 108.74874910344647, 0.0), APoint(124.11803215741656, 86.65264288110097, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.11803215741656, 108.74874910344647, 0.0), APoint(127.64701708954362, 86.68793273042252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.11803215741656, 108.74874910344647, 0.0), APoint(127.37856582082986, 86.68524821773508, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.11803215741656, 108.74874910344647, 0.0), APoint(126.89757388099133, 86.68043829833664, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.11803215741656, 108.74874910344647, 0.0), APoint(126.04331776791696, 86.67189573720611, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.11803215741656, 108.74874910344647, 0.0), APoint(124.82490016888005, 86.65971156121577, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(31.11803215741702, 107.84874910344638, 0.0), APoint(31.11803215741702, 85.75264288110088, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(31.11803215741702, 107.84874910344638, 0.0), APoint(27.589047225289505, 85.7879327304222, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(31.11803215741702, 107.84874910344638, 0.0), APoint(27.857498494001447, 85.78524821773499, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(31.11803215741702, 107.84874910344638, 0.0), APoint(28.338490433840434, 85.78043829833655, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(31.11803215741702, 107.84874910344638, 0.0), APoint(29.19274654691526, 85.7718957372058, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(31.11803215741702, 107.84874910344638, 0.0), APoint(30.41116414595217, 85.75971156121545, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193883, 271.0761334740793, 0.0), APoint(266.94147999192774, 271.0761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 267.8261334740793, 0.0), APoint(198.74147999193156, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 266.3261334740793, 0.0), APoint(198.74147999193156, 251.2277000613185, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 256.5761334740793, 0.0), APoint(183.24147999193428, 251.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.74147999192974, 267.8261334740793, 0.0), APoint(222.8414799919292, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.24147999193156, 267.3261334740793, 0.0), APoint(223.34147999193283, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.74147999192974, 266.3261334740793, 0.0), APoint(222.8414799919292, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.74147999192974, 267.3261334740793, 0.0), APoint(218.74147999192974, 266.3261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.24147999193156, 267.8261334740793, 0.0), APoint(218.24147999193156, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.8414799919292, 267.3261334740793, 0.0), APoint(222.8414799919292, 266.3261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.34147999193283, 267.8261334740793, 0.0), APoint(223.34147999193283, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.74147999192974, 266.3261334740793, 0.0), APoint(216.30973721964892, 251.686049436858, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.291479991929, 251.5761334740793, 0.0), APoint(222.8414799919292, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.84147999192828, 267.8261334740793, 0.0), APoint(246.94147999192774, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.84147999192828, 266.3261334740793, 0.0), APoint(246.94147999192774, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.84147999193647, 267.3261334740793, 0.0), APoint(242.84147999192828, 266.3261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(246.97033765436117, 267.8261334740793, 0.0), APoint(246.97033765436117, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.84147999192828, 266.3261334740793, 0.0), APoint(240.3914799919312, 251.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(249.39147999192846, 251.5761334740793, 0.0), APoint(246.94147999192774, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.8414799919292, 267.8261334740793, 0.0), APoint(242.84147999192828, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 267.8261334740793, 0.0), APoint(220.74147999192974, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 269.8261334740793, 0.0), APoint(220.74147999192974, 269.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 269.8261334740793, 0.0), APoint(220.74147999192974, 269.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.74147999192974, 267.8261334740793, 0.0), APoint(198.74147999193156, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.84147999193283, 269.8261334740793, 0.0), APoint(244.74147999192974, 269.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.74147999192974, 267.8261334740793, 0.0), APoint(220.84147999193283, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.84147999193283, 269.8261334740793, 0.0), APoint(266.94147999192774, 269.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(266.94147999192774, 267.8261334740793, 0.0), APoint(244.84147999193283, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.84147999193283, 269.8261334740793, 0.0), APoint(220.74147999192974, 269.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740793, 0.0), APoint(218.24147999193156, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(218.86734633320157, 267.8261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740764, 0.0), APoint(219.44791964121305, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(219.9055183861592, 267.8261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799919372, 269.8261334740773, 0.0), APoint(220.2968107023653, 267.8261334740798, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(220.65539938026814, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(221.0054858404037, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(221.3690368574562, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(221.77159786126686, 267.8261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(222.25031023747397, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(222.87033765436354, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.34147999193283, 267.8261334740793, 0.0), APoint(220.79147999190445, 269.8261334740468, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.86734633320157, 267.8261334740793, 0.0), APoint(218.86734633320157, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.44791964121305, 267.8261334740793, 0.0), APoint(219.44791964121305, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.9055183861592, 267.8261334740796, 0.0), APoint(219.9055183861592, 267.3261334740798, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.2968107023653, 267.8261334740798, 0.0), APoint(220.2968107023653, 267.3261334740798, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.65539938026814, 267.8261334740793, 0.0), APoint(220.65539938026814, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.0054858404037, 267.8261334740793, 0.0), APoint(221.0054858404037, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.3690368574562, 267.8261334740793, 0.0), APoint(221.3690368574562, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.77159786126686, 267.8261334740793, 0.0), APoint(221.77159786126686, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.25031023747397, 267.8261334740793, 0.0), APoint(222.25031023747397, 267.3261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.2994799919279, 251.5761334740793, 0.0), APoint(221.8494799919299, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.82847999192654, 251.5761334740793, 0.0), APoint(222.3784799919249, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.09297999192768, 251.5761334740793, 0.0), APoint(222.64297999192968, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.2252299919328, 251.5761334740793, 0.0), APoint(222.7752299919357, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.59427504561063, 251.5761334740793, 0.0), APoint(221.14427504561354, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(217.29972486733095, 251.67393425518412, 0.0), APoint(219.73347999193265, 266.3261334740871, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.77179798660927, 251.6803948712186, 0.0), APoint(219.20447999193766, 266.32613347409017, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.5078345462416, 251.6836251792359, 0.0), APoint(218.9399799919329, 266.32613347409233, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.37585282605232, 251.6852403332445, 0.0), APoint(218.80772999192595, 266.32613347409324, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.00349924839247, 251.6653216684474, 0.0), APoint(220.43868493824812, 266.3261334740818, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.24147999193156, 267.3261334740793, 0.0), APoint(223.34147999193283, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.74147999192974, 266.3261334740793, 0.0), APoint(222.8414799919292, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.74147999192974, 267.3261334740793, 0.0), APoint(218.74147999192974, 266.3261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.24147999193156, 267.8261334740793, 0.0), APoint(218.24147999193156, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.8414799919292, 267.3261334740793, 0.0), APoint(222.8414799919292, 266.3261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.34147999193283, 267.8261334740793, 0.0), APoint(223.34147999193283, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.74147999192974, 266.3261334740793, 0.0), APoint(216.30973721964892, 251.686049436858, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.291479991929, 251.5761334740793, 0.0), APoint(222.8414799919292, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740793, 0.0), APoint(218.24147999193156, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(218.86734633320157, 267.8261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740764, 0.0), APoint(219.44791964121305, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(219.9055183861592, 267.8261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799919372, 269.8261334740773, 0.0), APoint(220.2968107023653, 267.8261334740798, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(220.65539938026814, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(221.0054858404037, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(221.3690368574562, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(221.77159786126686, 267.8261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(222.25031023747397, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.79147999193447, 269.8261334740775, 0.0), APoint(222.87033765436354, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.34147999193283, 267.8261334740793, 0.0), APoint(220.79147999190445, 269.8261334740468, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.86734633320157, 267.8261334740793, 0.0), APoint(218.86734633320157, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.44791964121305, 267.8261334740793, 0.0), APoint(219.44791964121305, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.9055183861592, 267.8261334740796, 0.0), APoint(219.9055183861592, 267.3261334740798, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.2968107023653, 267.8261334740798, 0.0), APoint(220.2968107023653, 267.3261334740798, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.65539938026814, 267.8261334740793, 0.0), APoint(220.65539938026814, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.0054858404037, 267.8261334740793, 0.0), APoint(221.0054858404037, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.3690368574562, 267.8261334740793, 0.0), APoint(221.3690368574562, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.77159786126686, 267.8261334740793, 0.0), APoint(221.77159786126686, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.25031023747397, 267.8261334740793, 0.0), APoint(222.25031023747397, 267.3261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.87033765436354, 267.8261334740793, 0.0), APoint(222.87033765436354, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.2994799919279, 251.5761334740793, 0.0), APoint(221.8494799919299, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.82847999192654, 251.5761334740793, 0.0), APoint(222.3784799919249, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.09297999192768, 251.5761334740793, 0.0), APoint(222.64297999192968, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.2252299919328, 251.5761334740793, 0.0), APoint(222.7752299919357, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.59427504561063, 251.5761334740793, 0.0), APoint(221.14427504561354, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.88417676351946, 251.60559335271972, 0.0), APoint(220.79147999192446, 264.2044820796939, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.1775354242709, 251.6142410244592, 0.0), APoint(220.7914799919081, 259.9588604642007, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.47089408502234, 251.6228886961986, 0.0), APoint(220.79147999189354, 255.7132388487076, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(217.29972486733095, 251.67393425518412, 0.0), APoint(219.73347999193265, 266.3261334740871, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.77179798660927, 251.6803948712186, 0.0), APoint(219.20447999193766, 266.32613347409017, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.5078345462416, 251.6836251792359, 0.0), APoint(218.9399799919329, 266.32613347409233, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.37585282605232, 251.6852403332445, 0.0), APoint(218.80772999192595, 266.32613347409324, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.00349924839247, 251.6653216684474, 0.0), APoint(220.43868493824812, 266.3261334740818, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.7072736294558, 251.6567090817107, 0.0), APoint(220.79147999192446, 264.204482079694, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.41104801052006, 251.6480964949739, 0.0), APoint(220.7914799919081, 259.9588604642007, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.11482239158158, 251.6394839082372, 0.0), APoint(220.79147999189354, 255.7132388487076, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.3414799919292, 267.3261334740793, 0.0), APoint(247.44147999193137, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.84147999192828, 266.3261334740793, 0.0), APoint(246.94147999192774, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.84147999192828, 267.3261334740793, 0.0), APoint(242.84147999192828, 266.3261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.3414799919292, 267.8261334740793, 0.0), APoint(242.3414799919292, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(246.94147999192774, 267.3261334740793, 0.0), APoint(246.94147999192774, 266.3261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(247.44147999193137, 267.8261334740793, 0.0), APoint(247.44147999193137, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.84147999192828, 266.3261334740793, 0.0), APoint(240.3914799919312, 251.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(249.39147999192846, 251.5761334740793, 0.0), APoint(246.94147999192774, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.8914799919321, 269.8261334740793, 0.0), APoint(242.3414799919292, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.8914799919321, 269.8261334740775, 0.0), APoint(242.9673463331992, 267.8261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.8914799919321, 269.8261334740764, 0.0), APoint(243.5479196412125, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.8914799919321, 269.8261334740775, 0.0), APoint(244.00551838615684, 267.8261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.89147999193574, 269.8261334740773, 0.0), APoint(244.39681070236293, 267.8261334740798, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.8914799919321, 269.8261334740775, 0.0), APoint(244.7553993802676, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.8914799919321, 269.8261334740775, 0.0), APoint(245.10548584040134, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.8914799919321, 269.8261334740775, 0.0), APoint(245.46903685745383, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.8914799919321, 269.8261334740775, 0.0), APoint(245.8715978612663, 267.8261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.8914799919321, 269.8261334740775, 0.0), APoint(246.35031023747342, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.8914799919321, 269.8261334740775, 0.0), APoint(246.97033765436117, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(247.44147999193137, 267.8261334740793, 0.0), APoint(244.891479991903, 269.8261334740468, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.9673463331992, 267.8261334740793, 0.0), APoint(242.9673463331992, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.5479196412125, 267.8261334740793, 0.0), APoint(243.5479196412125, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.00551838615684, 267.8261334740796, 0.0), APoint(244.00551838615684, 267.3261334740798, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.39681070236293, 267.8261334740798, 0.0), APoint(244.39681070236293, 267.3261334740798, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.7553993802676, 267.8261334740793, 0.0), APoint(244.7553993802676, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.10548584040134, 267.8261334740793, 0.0), APoint(245.10548584040134, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.46903685745383, 267.8261334740793, 0.0), APoint(245.46903685745383, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.8715978612663, 267.8261334740793, 0.0), APoint(245.8715978612663, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(246.35031023747342, 267.8261334740793, 0.0), APoint(246.35031023747342, 267.3261334740796, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(246.97033765436117, 267.8261334740793, 0.0), APoint(246.97033765436117, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(248.39947999192646, 251.5761334740793, 0.0), APoint(245.94947999192846, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(248.9284799919251, 251.5761334740793, 0.0), APoint(246.47847999192436, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(249.19297999192622, 251.5761334740793, 0.0), APoint(246.74297999192913, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(247.69427504561008, 251.5761334740793, 0.0), APoint(245.244275045613, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(246.9890700992919, 251.5761334740793, 0.0), APoint(244.891479991923, 264.2044820796939, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(246.28386515297552, 251.5761334740793, 0.0), APoint(244.89147999190664, 259.9588604642007, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.57866020665824, 251.5761334740793, 0.0), APoint(244.89147999189208, 255.7132388487076, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(241.3834799918277, 251.57613347410432, 0.0), APoint(243.8334799919312, 266.3261334740871, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.8544799918336, 251.576133474108, 0.0), APoint(243.3044799919353, 266.32613347409017, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.58997999182793, 251.57613347411, 0.0), APoint(243.03997999193143, 266.32613347409233, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.08868493814407, 251.5761334740994, 0.0), APoint(244.53868493824757, 266.3261334740818, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.7938898844568, 251.5761334740793, 0.0), APoint(244.891479991923, 264.204482079694, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.499094830775, 251.5761334740793, 0.0), APoint(244.89147999190664, 259.9588604642007, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.20429977709227, 251.5761334740793, 0.0), APoint(244.89147999189208, 255.7132388487076, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.43868493824812, 266.3261334740818, 0.0), APoint(220.43868493824812, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.73347999193265, 266.3261334740871, 0.0), APoint(219.73347999193265, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.20447999193766, 266.32613347409017, 0.0), APoint(219.20447999193766, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.9399799919329, 266.32613347409233, 0.0), APoint(218.9399799919329, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.80772999192322, 266.3261334740793, 0.0), APoint(218.80772999192595, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.14427504561354, 266.3261334740818, 0.0), APoint(221.14427504561354, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.8494799919299, 266.3261334740871, 0.0), APoint(221.8494799919299, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.3784799919249, 266.32613347409017, 0.0), APoint(222.3784799919249, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.64297999192968, 266.32613347409233, 0.0), APoint(222.64297999192968, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.77522999194025, 266.3261334740793, 0.0), APoint(222.7752299919357, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.53868493824757, 266.3261334740818, 0.0), APoint(244.53868493824757, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.8334799919312, 266.3261334740871, 0.0), APoint(243.8334799919312, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.3044799919353, 266.32613347409017, 0.0), APoint(243.3044799919353, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.03997999193143, 266.32613347409233, 0.0), APoint(243.03997999193143, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.244275045613, 266.3261334740818, 0.0), APoint(245.244275045613, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.94947999192846, 266.3261334740871, 0.0), APoint(245.94947999192846, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(246.47847999192436, 266.32613347409017, 0.0), APoint(246.47847999192436, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(246.74297999192913, 266.32613347409233, 0.0), APoint(246.74297999192913, 267.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 251.5761334740793, 0.0), APoint(178.24147999193428, 251.5761334740793, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 256.5761334740793, 0.0), APoint(181.7792158409893, 256.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 271.0761334740793, 0.0), APoint(183.24147999193428, 257.82613347408164, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.7792158409893, 256.5761334740793, 0.0), APoint(178.24147999193428, 251.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 256.5761334740793, 0.0), APoint(183.24147999193428, 257.8261334740812, 0.0))
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

entity = acad.model.AddLine(APoint(181.7792158409893, 256.5761334740793, 0.0), APoint(181.7792158409893, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999193156, 267.8261334740793, 0.0), APoint(198.74147999193156, 271.0761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(197.27921584098476, 271.0761334740793, 0.0), APoint(181.7792158409893, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(197.27921584098476, 271.0761334740793, 0.0), APoint(198.74147999193156, 271.0761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(178.24147999193428, 251.5761334740793, 0.0), APoint(172.9335499324834, 252.0113579716691, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 251.5761334740793, 0.0), APoint(189.44101312293787, 251.0539502832964, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(189.44101312293787, 251.0539502832964, 0.0), APoint(200.64822693209408, 251.26332159110441, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.64822693209408, 251.26332159110441, 0.0), APoint(211.42529451850987, 250.90293511902672, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(211.42529451850987, 250.90293511902672, 0.0), APoint(216.04158886143887, 251.689330958686, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.04158886143887, 251.689330958686, 0.0), APoint(225.291479991929, 251.5761334740793, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.291479991929, 251.5761334740793, 0.0), APoint(234.47910830723595, 251.17996020498572, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(234.47910830723595, 251.17996020498572, 0.0), APoint(240.3914799919312, 251.5761334740793, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.3914799919312, 251.5761334740793, 0.0), APoint(249.39147999192846, 251.5761334740793, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(249.39147999192846, 251.5761334740793, 0.0), APoint(260.15800449631115, 250.9824092688311, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(266.94147999192774, 267.8261334740793, 0.0), APoint(266.94147999192774, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(266.94147999192774, 266.3261334740793, 0.0), APoint(266.94147999192774, 251.2277000613185, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(282.44147999192774, 256.5761334740793, 0.0), APoint(282.44147999192774, 251.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(282.44147999192774, 251.5761334740793, 0.0), APoint(287.44147999192774, 251.5761334740793, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(282.44147999192774, 256.5761334740793, 0.0), APoint(283.9037441428727, 256.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(266.94147999192774, 271.0761334740793, 0.0), APoint(282.44147999192774, 257.82613347408164, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(283.9037441428727, 256.5761334740793, 0.0), APoint(287.44147999192774, 251.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(282.44147999192774, 256.5761334740793, 0.0), APoint(282.44147999192774, 257.8261334740812, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(282.44147999192774, 257.8261334740814, 0.0), APoint(283.9037441428727, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(283.9037441428727, 256.5761334740793, 0.0), APoint(283.9037441428727, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(266.94147999192774, 267.8261334740793, 0.0), APoint(266.94147999192774, 271.0761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(268.40374414287635, 271.0761334740793, 0.0), APoint(283.9037441428727, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(268.40374414287635, 271.0761334740793, 0.0), APoint(266.94147999192774, 271.0761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(287.44147999192774, 251.5761334740793, 0.0), APoint(291.0836581640133, 251.9484906238674, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(282.44147999192774, 251.5761334740793, 0.0), APoint(276.24194686092505, 251.0539502832964, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(276.24194686092505, 251.0539502832964, 0.0), APoint(265.03473305176703, 251.26332159110441, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(265.03473305176703, 251.26332159110441, 0.0), APoint(260.15800449631115, 250.9824092688311, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.93354993248067, 274.3832343570766, 0.0), APoint(291.0836581640133, 274.38323435707696, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(208.1980407607016, 272.26369861194075, 0.0), APoint(208.1980407607016, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.26666169488726, 273.32346648450846, 0.0), APoint(209.26666169488908, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(210.3352826290784, 272.26369861194075, 0.0), APoint(210.3352826290784, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(211.4039035632686, 273.32346648450846, 0.0), APoint(211.40390356326589, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(212.4725244974543, 272.26369861194075, 0.0), APoint(212.4725244974543, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(213.5411454316427, 273.32346648450846, 0.0), APoint(213.5411454316427, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(214.6097663658329, 272.26369861194075, 0.0), APoint(214.6097663658329, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(215.67838730002313, 273.32346648450846, 0.0), APoint(215.67838730001858, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.7470082342088, 272.26369861194075, 0.0), APoint(216.7470082342088, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(217.8156291683963, 273.32346648450846, 0.0), APoint(217.8156291683963, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.8842501025856, 272.26369861194075, 0.0), APoint(218.8842501025856, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.1294198265159, 273.32346648450846, 0.0), APoint(207.12941982651137, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.06079889232387, 272.26369861194075, 0.0), APoint(206.06079889232387, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.99217795813274, 273.32346648450846, 0.0), APoint(204.99217795813547, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.92355702394798, 272.26369861194075, 0.0), APoint(203.92355702394798, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(202.85493608975867, 273.32346648450846, 0.0), APoint(202.85493608975867, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(201.78631515557026, 272.26369861194075, 0.0), APoint(201.78631515557026, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.71769422137913, 273.32346648450846, 0.0), APoint(200.71769422138277, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(199.64907328719437, 272.26369861194075, 0.0), APoint(199.64907328719437, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.58045235300506, 273.32346648450846, 0.0), APoint(198.58045235300506, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(197.51183141881756, 272.26369861194075, 0.0), APoint(197.51183141881756, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.44321048462643, 273.32346648450846, 0.0), APoint(196.44321048462734, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(195.3745895504362, 269.4479851934494, 0.0), APoint(195.37458955043985, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.3059686162551, 272.26664830269215, 0.0), APoint(194.30596861625145, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(193.2373476820767, 267.6209881124309, 0.0), APoint(193.23734768206305, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.16872674787373, 271.2098301208735, 0.0), APoint(192.16872674787373, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.1001058136726, 265.7939910313765, 0.0), APoint(191.10010581368624, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(190.0314848794951, 270.1530119390543, 0.0), APoint(190.03148487949784, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(188.96286394531217, 263.9669939503592, 0.0), APoint(188.96286394531035, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(187.89424301112467, 269.0961937572364, 0.0), APoint(187.89424301112103, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(186.82562207691353, 262.1399968693085, 0.0), APoint(186.82562207693263, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(185.7570011427424, 268.0393755754185, 0.0), APoint(185.75700114274332, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(184.68838020855674, 260.3129997882929, 0.0), APoint(184.68838020855674, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.61975927437106, 267.5109664845087, 0.0), APoint(183.61975927436742, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.55113834015447, 258.4860027072389, 0.0), APoint(182.55113834017902, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.4825174059897, 267.5109664845087, 0.0), APoint(181.4825174059897, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(180.41389647180222, 254.6464820989619, 0.0), APoint(180.41389647180222, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(180.4138964718304, 254.6464820990002, 0.0), APoint(180.41389647180222, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(179.3452755376111, 267.5109664845087, 0.0), APoint(179.34527553761382, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(178.27665460339085, 251.6258469249379, 0.0), APoint(178.27665460342632, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.20803366923792, 267.5109664845087, 0.0), APoint(177.20803366923792, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(176.13941273504406, 251.74849278468312, 0.0), APoint(176.13941273504952, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(175.0707918008593, 267.5109664845087, 0.0), APoint(175.0707918008593, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(174.00217086663451, 250.89405655820013, 0.0), APoint(174.0021708666727, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.9335499324834, 272.26369861194075, 0.0), APoint(172.9335499324834, 275.6006963773462, 0.0))
entity.Color = 7
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

entity = acad.model.AddLine(APoint(172.93354993248067, 262.2999875309144, 0.0), APoint(172.9335499324834, 249.8868480784354, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(172.92142691736535, 263.3998154040632, 0.0), 0.4664564201237909, 0.0, 3.141592653589793)
entity.Color = 7

entity = acad.model.AddLine(APoint(173.38788333749017, 263.3998154040632, 0.0), APoint(172.45497049724236, 262.7662863882785, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(172.92142691736535, 262.7662863882785, 0.0), 0.4664564201237909, 3.141592653589793, 0.0)
entity.Color = 7

entity = acad.model.AddLine(APoint(172.9335499324834, 263.8661142614273, 0.0), APoint(172.9335499324834, 264.7798375281452, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.9443238630838, 262.3003922782585, 0.0), APoint(172.9443238630838, 261.5411517519034, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(291.0836581640133, 275.53782902954447, 0.0), APoint(291.08365816401147, 263.80324691362557, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(291.08365816401147, 262.2371201831127, 0.0), APoint(291.0836581640133, 249.8239807306336, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(291.07153514889524, 263.3369480562615, 0.0), 0.4664564201237909, 0.0, 3.141592653589793)
entity.Color = 7

entity = acad.model.AddLine(APoint(291.53799156902005, 263.3369480562615, 0.0), APoint(290.60507872877133, 262.70341904047683, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(291.07153514889524, 262.70341904047683, 0.0), 0.4664564201237909, 3.141592653589793, 0.0)
entity.Color = 7

entity = acad.model.AddLine(APoint(291.0836581640133, 263.80324691362557, 0.0), APoint(291.0836581640133, 264.7169701803435, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(291.0944320946146, 262.2375249304568, 0.0), APoint(291.0944320946146, 261.4782844041016, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.57045944446872, 272.26369861194075, 0.0), APoint(229.57045944446872, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(230.6390803786553, 273.32346648450846, 0.0), APoint(230.63908037865622, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(231.70770131284644, 272.26369861194075, 0.0), APoint(231.70770131284644, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(232.77632224703757, 273.32346648450846, 0.0), APoint(232.77632224703393, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(233.84494318122233, 272.26369861194075, 0.0), APoint(233.84494318122233, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(234.91356411540983, 273.32346648450846, 0.0), APoint(234.91356411540983, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(235.98218504960005, 272.26369861194075, 0.0), APoint(235.98218504960005, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.05080598379118, 273.32346648450846, 0.0), APoint(237.05080598378754, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(238.11942691797594, 272.26369861194075, 0.0), APoint(238.11942691797594, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.18804785216435, 273.32346648450846, 0.0), APoint(239.18804785216435, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.25666878635275, 272.26369861194075, 0.0), APoint(240.25666878635275, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.50183851028305, 273.32346648450846, 0.0), APoint(228.50183851028032, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(227.43321757609192, 272.26369861194075, 0.0), APoint(227.43321757609192, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.3645966419008, 273.32346648450846, 0.0), APoint(226.3645966419026, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.29597570771602, 272.26369861194075, 0.0), APoint(225.29597570771602, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.2273547735258, 273.32346648450846, 0.0), APoint(224.2273547735258, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.1587338393383, 272.26369861194075, 0.0), APoint(223.1587338393383, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.0901129051481, 273.32346648450846, 0.0), APoint(222.0901129051499, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.02149197096242, 272.26369861194075, 0.0), APoint(221.02149197096242, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.9528710367731, 273.32346648450846, 0.0), APoint(219.9528710367731, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(250.94287812823768, 272.26369861194075, 0.0), APoint(250.94287812823768, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(252.01149906242335, 273.32346648450846, 0.0), APoint(252.01149906242517, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(253.08011999661448, 272.26369861194075, 0.0), APoint(253.08011999661448, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(254.1487409308047, 273.32346648450846, 0.0), APoint(254.14874093080198, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(255.21736186499038, 272.26369861194075, 0.0), APoint(255.21736186499038, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(256.2859827991788, 273.32346648450846, 0.0), APoint(256.2859827991788, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(257.3546037333681, 272.26369861194075, 0.0), APoint(257.3546037333681, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(258.4232246675592, 273.32346648450846, 0.0), APoint(258.4232246675547, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(259.491845601744, 272.26369861194075, 0.0), APoint(259.491845601744, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(260.5604665359324, 273.32346648450846, 0.0), APoint(260.5604665359324, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(261.6290874701217, 272.26369861194075, 0.0), APoint(261.6290874701217, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(249.8742571940511, 273.32346648450846, 0.0), APoint(249.87425719404837, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(248.80563625985997, 272.26369861194075, 0.0), APoint(248.80563625985997, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(247.73701532566884, 273.32346648450846, 0.0), APoint(247.73701532567156, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(246.66839439148407, 272.26369861194075, 0.0), APoint(246.66839439148407, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.59977345729385, 273.32346648450846, 0.0), APoint(245.59977345729385, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.53115252310636, 272.26369861194075, 0.0), APoint(244.53115252310636, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.46253158891523, 273.32346648450846, 0.0), APoint(243.46253158891886, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.39391065473046, 272.26369861194075, 0.0), APoint(242.39391065473046, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(241.32528972054115, 273.32346648450846, 0.0), APoint(241.32528972054115, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(269.1094340094369, 273.32346648450846, 0.0), APoint(269.1094340094387, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(268.0408130752521, 272.26369861194075, 0.0), APoint(268.0408130752521, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(266.9721921410619, 273.32346648450846, 0.0), APoint(266.9721921410619, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(265.9035712068744, 272.26369861194075, 0.0), APoint(265.9035712068744, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.8349502726833, 273.32346648450846, 0.0), APoint(264.834950272686, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(263.7663293384976, 272.26369861194075, 0.0), APoint(263.7663293384976, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(262.6977084043092, 273.32346648450846, 0.0), APoint(262.6977084043092, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(270.20837043342635, 269.4479851934494, 0.0), APoint(270.2083704334236, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(271.2769913676084, 272.26664830269215, 0.0), APoint(271.2769913676102, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(272.3456123017868, 267.6209881124309, 0.0), APoint(272.3456123017995, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(273.4142332359861, 271.2098301208735, 0.0), APoint(273.4142332359861, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(274.48285417018906, 265.7939910313765, 0.0), APoint(274.4828541701763, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(275.55147510436836, 270.1530119390543, 0.0), APoint(275.5514751043638, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(276.6200960385495, 263.9669939503592, 0.0), APoint(276.62009603855313, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(277.6887169727379, 269.0961937572364, 0.0), APoint(277.6887169727406, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(278.7573379069472, 262.1399968693085, 0.0), APoint(278.75733790692993, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(279.82595884112106, 268.0393755754185, 0.0), APoint(279.8259588411165, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(280.89457977530674, 260.3129997882929, 0.0), APoint(280.89457977530674, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(281.9632007094924, 267.5109664845087, 0.0), APoint(281.96320070949423, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(283.031821643709, 258.4860027072389, 0.0), APoint(283.03182164368354, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(284.1004425778701, 267.5109664845087, 0.0), APoint(284.1004425778701, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(285.16906351206035, 254.6464820989619, 0.0), APoint(285.16906351206035, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(285.16906351203306, 254.6464820990002, 0.0), APoint(285.16906351206035, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(286.2376844462524, 267.5109664845087, 0.0), APoint(286.23768444624784, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(287.3063053804708, 251.6258469249379, 0.0), APoint(287.30630538043715, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(288.37492631462374, 267.5109664845087, 0.0), APoint(288.37492631462374, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(289.4435472488167, 251.74849278468312, 0.0), APoint(289.44354724881396, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(290.51216818300145, 267.5109664845087, 0.0), APoint(290.51216818300145, 274.38323435707684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('مقطع', APoint(223.31996826715067, 140.55021427727573, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(213.9728878784381, 139.1331307453937, 0.0), APoint(230.76698014933118, 139.1331307453938, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(213.97288787843627, 138.77473932461615, 0.0), APoint(230.76698014933118, 138.7747393246161, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('2-2', APoint(216.6734777910624, 140.38536089075845, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(228.30937081760476, 240.368051929731, 0.0), APoint(237.70912969268284, 240.368051929731, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.26242256639034, 239.79734414452628, 0.0), APoint(237.70912969268284, 239.79734414452628, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('نما', APoint(231.18133765291282, 240.77990475410968, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(73.35269446354141, 158.94917212754376, 0.0), APoint(83.15876076241375, 158.9491721275438, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.37354065032514, 158.59078070676622, 0.0), APoint(83.15876076241375, 158.5907807067662, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText(' پلان', APoint(74.4869890745208, 160.69540403023598, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('مقطع 1-1', APoint(75.77677576198676, 60.639844677391295, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(72.41198738685307, 59.3301180327977, 0.0), APoint(87.7236828390769, 59.33011803279784, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.43552180255438, 58.97172661202018, 0.0), APoint(87.7236828390769, 58.97172661202012, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.11025403423992, 274.69918892475994, 0.0), APoint(81.11025403423992, 228.07161980957724, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(88.7826002666402, 267.4900886374305, 0.0), APoint(88.7826002666402, 228.0348756763882, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 267.274113787769, 0.0), APoint(89.83039196204527, 228.02985762891691, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('C.L.', APoint(78.3024727985262, 276.07676996262285, 0.0), 2.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(27.56191975748834, 264.215277256224, 0.0), APoint(26.430866001661798, 262.3991541320247, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.835931114548202, 259.8869343157614, 0.0), APoint(25.63339855810318, 261.14304422389233, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.37644064895312, 261.9410500384946, 0.0), APoint(24.835931114548202, 259.8869343157614, 0.0))
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

entity = acad.model.AddText('3', APoint(23.3675427593339, 261.834779785228, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddText('3', APoint(36.16797080116203, 281.88565473711094, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(41.44012526106758, 230.58516322264882, 0.0), APoint(39.30067278530646, 230.56702749068074, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.32492659356353, 230.5675767602312, 0.0), APoint(37.812799689433405, 230.56730212545676, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.81307450961435, 232.05617968589888, 0.0), APoint(36.32492659356353, 230.5675767602312, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.34133320638784, 231.285863518057, 0.0), APoint(112.27274643292003, 231.26832850117648, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.82948112243912, 232.77446644372446, 0.0), APoint(117.31707939812804, 231.2853142485078, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('1', APoint(37.18275729109678, 232.8510812662529, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddText('1', APoint(115.127625535069, 233.4719144147124, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(60.987484019639396, 185.56350392253606, 0.0), APoint(61.0056197516069, 183.424051446774, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.00507048205691, 180.44830525503244, 0.0), APoint(61.00534511683236, 181.93617835090186, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.516467556389216, 181.9364531710828, 0.0), APoint(61.00507048205691, 180.44830525503244, 0.0))
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

entity = acad.model.AddLine(APoint(59.52642114675609, 270.817178111742, 0.0), APoint(61.01557334197196, 272.3047763874314, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('2', APoint(58.72156597603498, 181.306135952565, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddText('2', APoint(58.828973175768624, 270.11532252437235, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(77.72399283695813, 134.94557844824345, 0.0), APoint(77.72399283695813, 72.0244564366833, 0.0))
entity.Color = 4


entity = acad.model.AddLine(APoint(89.70644040441721, 129.5109391929646, 0.0), APoint(89.70644040441721, 73.85204214184091, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 129.55411810967422, 0.0), APoint(90.75423209982318, 73.85204214184091, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('C.L.', APoint(74.91621160124487, 136.24193746297288, 0.0), 2.5)
entity.Color = 1

entity = acad.model.AddText('37.14', APoint(65.96961459937938, 133.0157376621494, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(118.8680321574152, 113.97651159688417, 0.0), APoint(100.89380215333131, 125.27561250566305, 0.0))
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

entity = acad.model.AddLine(APoint(54.55418352058405, 125.27561250566305, 0.0), APoint(77.72399283695813, 125.50731059882679, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.64035642685258, 124.78144798538193, 0.0), APoint(77.72924257447812, 124.98233684685817, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.70644040441994, 124.8624598738084, 0.0), APoint(77.72399283695813, 124.982284349483, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.89380215333131, 125.27561250566305, 0.0), APoint(90.75423209982318, 125.37700820619813, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.8076292470655, 124.78144798538193, 0.0), APoint(90.74898236230365, 124.85203445422951, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.70644040441812, 125.3874861231522, 0.0), APoint(77.72399283695813, 125.50731059882679, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.81287898458504, 125.30642173735055, 0.0), APoint(97.8076292470655, 124.78144798538193, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.635106689331224, 125.30642173735052, 0.0), APoint(57.64035642684985, 124.78144798538193, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.29487555533024, 119.23205178572528, 0.0), APoint(107.02600710154002, 122.07796408825197, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.02600710154002, 122.07796408825197, 0.0), APoint(111.29487555533024, 122.07796408825197, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.29487555533024, 122.07796408825197, 0.0), APoint(111.29487555533024, 119.23205178572528, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('300', APoint(108.37515465262004, 122.81487578696931, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('1', APoint(111.38367833416987, 119.49476670924184, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(پایه)', APoint(64.55888603401286, 73.66976331948877, 0.0), 2.663041818489627)
entity.Color = 1

entity = acad.model.AddText('(کوله)', APoint(62.39455737358753, 100.16276451195085, 0.0), 2.663041818489627)
entity.Color = 1

entity = acad.model.AddLine(APoint(133.5195656451442, 86.6549730989866, 0.0), APoint(133.5195656451442, 90.79824047936665, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(134.8695656451423, 86.6549730989866, 0.0), APoint(132.1695656451434, 86.6549730989866, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(133.5195656451442, 88.00497309898662, 0.0), APoint(134.8695656451423, 88.00497309898662, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(134.8695656451423, 88.00497309898662, 0.0), APoint(133.5195656451442, 86.6549730989866, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(133.5195656451442, 86.6549730989866, 0.0), APoint(132.1695656451434, 88.00497309898662, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(132.1695656451434, 88.00497309898662, 0.0), APoint(133.5195656451442, 88.00497309898662, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(133.5195656451442, 90.79824047936665, 0.0), APoint(141.61956564514367, 90.79824047936665, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(135.15069146264204, 79.11864367203293, 0.0), APoint(132.45069146264404, 79.11864367203293, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(133.8006914626435, 77.76864367203291, 0.0), APoint(135.15069146264204, 77.76864367203291, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(135.15069146264204, 77.76864367203291, 0.0), APoint(133.8006914626435, 79.11864367203293, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(133.8006914626435, 79.11864367203293, 0.0), APoint(133.8006914626435, 74.97537629165288, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(132.45069146264404, 77.76864367203291, 0.0), APoint(133.8006914626435, 77.76864367203291, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(133.8006914626435, 79.11864367203293, 0.0), APoint(132.45069146264404, 77.76864367203291, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(133.8006914626435, 74.97537629165288, 0.0), APoint(141.9006914626434, 74.97537629165288, 0.0))
entity.Color = 8


entity = acad.model.AddText('33.72', APoint(136.97790639818732, 76.21478786357744, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('34.52', APoint(135.30508836831586, 91.9844766388519, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(133.5195656451442, 108.39715845366777, 0.0), APoint(133.5195656451442, 112.54042583404782, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(134.8695656451423, 108.39715845366777, 0.0), APoint(132.1695656451434, 108.39715845366777, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(133.5195656451442, 109.7471584536678, 0.0), APoint(134.8695656451423, 109.7471584536678, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(134.8695656451423, 109.7471584536678, 0.0), APoint(133.5195656451442, 108.39715845366777, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(133.5195656451442, 108.39715845366777, 0.0), APoint(132.1695656451434, 109.7471584536678, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(132.1695656451434, 109.7471584536678, 0.0), APoint(133.5195656451442, 109.7471584536678, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(133.5195656451442, 112.54042583404782, 0.0), APoint(141.61956564514367, 112.54042583404782, 0.0))
entity.Color = 8


entity = acad.model.AddText('36.02', APoint(135.30508836831586, 113.72666199353307, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(21.352295327137654, 85.61770296069221, 0.0), APoint(21.352295327137654, 89.76097034107227, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(20.0022953271382, 85.61770296069221, 0.0), APoint(22.702295327137563, 85.61770296069221, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(21.352295327137654, 86.96770296069224, 0.0), APoint(20.0022953271382, 86.96770296069224, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(20.0022953271382, 86.96770296069224, 0.0), APoint(21.352295327137654, 85.61770296069221, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(21.352295327137654, 85.61770296069221, 0.0), APoint(22.702295327137563, 86.96770296069224, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(22.702295327137563, 86.96770296069224, 0.0), APoint(21.352295327137654, 86.96770296069224, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(21.352295327137654, 89.76097034107227, 0.0), APoint(13.2522953271382, 89.76097034107227, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(19.721169509637548, 78.08137353373854, 0.0), APoint(22.421169509637366, 78.08137353373854, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(21.071169509637457, 76.73137353373852, 0.0), APoint(19.721169509637548, 76.73137353373852, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(19.721169509637548, 76.73137353373852, 0.0), APoint(21.071169509637457, 78.08137353373854, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(21.071169509637457, 78.08137353373854, 0.0), APoint(21.071169509637457, 73.93810615335848, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(22.421169509637366, 76.73137353373852, 0.0), APoint(21.071169509637457, 76.73137353373852, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(21.071169509637457, 78.08137353373854, 0.0), APoint(22.421169509637366, 76.73137353373852, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(21.071169509637457, 73.93810615335848, 0.0), APoint(12.971169509638003, 73.93810615335848, 0.0))
entity.Color = 8


entity = acad.model.AddText('34.22', APoint(12.94157362171336, 75.17751772528305, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('35.02', APoint(14.614391651584356, 90.94720650055751, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(21.352295327137654, 107.35988831537338, 0.0), APoint(21.352295327137654, 111.50315569575343, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(20.0022953271382, 107.35988831537338, 0.0), APoint(22.702295327137563, 107.35988831537338, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(21.352295327137654, 108.7098883153734, 0.0), APoint(20.0022953271382, 108.7098883153734, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(20.0022953271382, 108.7098883153734, 0.0), APoint(21.352295327137654, 107.35988831537338, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(21.352295327137654, 107.35988831537338, 0.0), APoint(22.702295327137563, 108.7098883153734, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(22.702295327137563, 108.7098883153734, 0.0), APoint(21.352295327137654, 108.7098883153734, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(21.352295327137654, 111.50315569575343, 0.0), APoint(13.2522953271382, 111.50315569575343, 0.0))
entity.Color = 8


entity = acad.model.AddText('36.52', APoint(14.614391651584356, 112.68939185523868, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(34.118032157408834, 110.12886160063385, 0.0), APoint(34.118032157416565, 113.09901159688366, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157408834, 110.12886160063385, 0.0), APoint(34.118032157416565, 109.34882410157047, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 110.99886160063396, 0.0), APoint(121.1180321574152, 110.48446782393646, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 110.48446782393646, 0.0), APoint(121.1180321574152, 110.24882410157056, 0.0))
entity.Color = 3
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

entity = acad.model.AddLine(APoint(296.64869948316027, 24.999999999999915, 0.0), APoint(296.64869948316027, 4.999999999999915, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(254.53226096911112, 24.999999999999915, 0.0), APoint(254.53226096911112, 4.999999999999915, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(212.41582245506015, 24.999999999999915, 0.0), APoint(212.41582245506015, 4.999999999999915, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.299383941011, 24.999999999999915, 0.0), APoint(170.299383941011, 4.999999999999915, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(128.18294542696094, 24.999999999999915, 0.0), APoint(128.18294542696094, 4.999999999999915, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.06650691291134, 24.999999999999915, 0.0), APoint(86.06650691291134, 4.999999999999915, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('شماره نقشه همسان', APoint(321.4107881806342, 5.954390866480708, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('تاریخ ابلاغ', APoint(199.96219053909317, 12.510906838608207, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('محل آبرو', APoint(159.94609765275186, 12.2191928082585, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(296.64869948316027, 14.999999999999915, 0.0), APoint(86.06650691291134, 15.0, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('ch,d› jâv“', APoint(127.36282483444347, 12.147955604483002, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('دهانه آبرو', APoint(160.15979275216387, 22.124566619728498, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddCircle(APoint(95.0805428836652, 23.522472181921415, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(95.09918690330687, 22.3121487787904, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddText('بدون مقیاس', APoint(9.082975376367356, 8.95932974714492, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('حداکثر ارتفاع خاک روی آبرو', APoint(97.7318725127866, 21.9504656262568, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('=0', APoint(95.19832279330512, 7.333637294245108, 0.0), 1.95)
entity.Color = 7

entity = acad.model.AddText('پیمانکار', APoint(244.72903155492122, 22.295085065695957, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddCircle(APoint(243.58807971231425, 23.663669747499313, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(243.6067237319582, 22.453346344368214, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddText('کارفرما', APoint(288.3126927041217, 22.00217952961964, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('مهندس مشاور', APoint(284.10922445960455, 12.206080396302214, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('عنوان پروژه', APoint(241.95043663738966, 12.016791073403, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('60 cm', APoint(90.16912161954542, 16.748138742348004, 0.0), 2.0)
entity.Color = 7

entity = acad.model.AddLine(APoint(338.76513799721124, 25.0, 0.0), APoint(338.76513799721124, 5.0, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('موضوع نقشه', APoint(325.2669576431447, 21.799714221399896, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('همسطح و زیرخاکی', APoint(308.40506135298324, 14.547901980048211, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('عمود بر محور راه', APoint(309.6875154559257, 10.931976429931213, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddCircle(APoint(113.67680875801307, 13.522472181921415, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(113.6954527776561, 12.312148778790402, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddText('توضیحات', APoint(75.16847656119512, 21.80586767596901, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddCircle(APoint(74.00010781073297, 23.498059959723605, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(74.0187518303751, 22.287736556592492, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddText('ابعاد کوله و دیوارها و جزئیات میلگردگذاری طبق نقشه شماره', APoint(22.32190075241124, 12.489949274390256, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('.انتخاب شوند', APoint(45.72441714362549, 9.022069009672123, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(11.631448686285239, 25.0, 0.0), APoint(11.631448686285239, 5.0, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('تمام موارد مندرج در بخش توضیحات کلی و عمومی به طور', APoint(27.07245764084678, 19.195197129738325, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('.کامل رعایت شود', APoint(65.14676438113156, 16.113587317963326, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddCircle(APoint(34.99922576537847, 114.65987619752624, 0.0), 2.614162321993489)
entity.Color = 8

entity = acad.model.AddText('جزئیات الف', APoint(20.41373612523398, 120.91234097360027, 0.0), 1.75)
entity.Color = 1

entity = acad.model.AddCircle(APoint(123.0366685743279, 112.77927550254068, 0.0), 3.547071112992003)
entity.Color = 8

entity = acad.model.AddText('جزئیات ب', APoint(126.18554953657849, 122.15582633650409, 0.0), 1.75)
entity.Color = 1

entity = acad.model.AddText('نقشه همسان آبرو سه دهانه', APoint(304.6051989596865, 18.329263683586706, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('292-SB-SS', APoint(71.5041269059011, 9.267713204698822, 0.0), 1.5)
entity.Color = 7

entity = acad.model.AddText('و', APoint(69.361665149906, 9.435624568094113, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('292-SB-D', APoint(59.539739476647355, 9.349455114314196, 0.0), 1.5)
entity.Color = 7

entity = acad.model.AddText('وزارت راه و شهرسازی', APoint(391.3256815088255, 14.572511580924614, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('مرکز تحقیقات راه مسکن و شهرسازی', APoint(349.1322169868429, 14.378958298681216, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('نقشه های همسان آبروهای راه تا دهانه 10 متر نشریه شماره 1-292', APoint(351.08200673865576, 7.890691539354499, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(198.74147999193156, 269.8261334740793, 0.0), APoint(183.24147999193428, 256.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(266.94147999192774, 269.8261334740793, 0.0), APoint(282.44147999192774, 256.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(291.5349408183065, 160.15697630978252, 0.0), APoint(269.03494081831377, 160.15697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(291.53494081831377, 152.65697630978252, 0.0), APoint(269.03494081831377, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(276.0379372545094, 182.28197630978252, 0.0), APoint(276.0379372545094, 160.15697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(269.0349408183065, 160.15697630978252, 0.0), APoint(269.03494081831377, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(291.5349408183065, 160.15697630978252, 0.0), APoint(291.53494081831377, 152.65697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(281.2879372545094, 182.28197630978252, 0.0), APoint(289.53793725450487, 160.15697630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('مقطع 3-3', APoint(171.95850168388552, 38.0238748340316, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(168.1712378626189, 36.62681066297941, 0.0), APoint(184.25873710533142, 36.626810662979494, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(168.17427364620107, 36.268419242201816, 0.0), APoint(184.25873710533142, 36.268419242201816, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 98.92379186092647, 0.0), APoint(177.6660265314331, 98.92379186092647, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.6660265314331, 98.92379186092647, 0.0), APoint(173.1660265314331, 96.67379186092646, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.1660265314331, 96.67379186092646, 0.0), APoint(160.58269319810006, 58.92379186092647, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 98.92379186092647, 0.0), APoint(181.16602653143218, 58.92379186092647, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 58.92379186092647, 0.0), APoint(160.58269319810006, 58.92379186092647, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319810006, 58.92379186092647, 0.0), APoint(160.58269319810006, 50.92379186092646, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 58.92379186092647, 0.0), APoint(191.58269319810006, 58.92379186092647, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319810006, 58.92379186092647, 0.0), APoint(160.58269319810006, 48.92379186092646, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319810006, 48.92379186092646, 0.0), APoint(191.58269319810006, 48.92379186092646, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.58269319810006, 48.92379186092646, 0.0), APoint(191.58269319810006, 58.92379186092647, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.6660265314331, 98.92379186092647, 0.0), APoint(151.9304490792665, 105.34039198909122, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(167.4238474574595, 81.29164300551405, 0.0), APoint(165.89482353034873, 81.29164300551405, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(165.89482353034873, 81.29164300551405, 0.0), APoint(165.89482353034873, 76.70457122418178, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(167.4238474574595, 81.29164300551405, 0.0), APoint(165.89482353034873, 76.70457122418178, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(162.49788061708477, 197.50642379138193, 0.0), APoint(223.94595612010107, 197.21592302240862, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.75237853676208, 196.18900431248332, 0.0), APoint(228.7523785367648, 197.19320026996076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.8209994709532, 195.1292364399155, 0.0), APoint(229.8209994709532, 197.18814827767977, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(230.88962040514525, 196.18900431248332, 0.0), APoint(230.8896204051407, 197.1830962853988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(231.95824133933002, 195.1292364399155, 0.0), APoint(231.95824133933002, 197.1780442931178, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(233.02686227351933, 196.18900431248332, 0.0), APoint(233.02686227351933, 197.17299230083682, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(234.09548320770682, 195.1292364399155, 0.0), APoint(234.09548320770682, 197.16794030855584, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(235.16410414189795, 196.18900431248332, 0.0), APoint(235.16410414189522, 197.16288831627486, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.23272507608363, 195.1292364399155, 0.0), APoint(236.23272507608363, 197.15783632399388, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.30134601027203, 196.18900431248332, 0.0), APoint(237.30134601027203, 197.1527843317129, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(238.36996694446134, 195.1292364399155, 0.0), APoint(238.36996694446134, 197.1477323394319, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.4092738658237, 195.1292364399155, 0.0), APoint(223.4092738658237, 197.21846023136567, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.3406529316353, 196.18900431248332, 0.0), APoint(222.3406529316344, 197.22351222364674, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.272031997446, 195.1292364399155, 0.0), APoint(221.272031997446, 197.22856421592772, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.20341106325486, 196.18900431248332, 0.0), APoint(220.2034110632576, 197.2336162082087, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.1347901290692, 195.1292364399155, 0.0), APoint(219.1347901290692, 197.23866820048968, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.06616919488079, 196.18900431248332, 0.0), APoint(218.06616919488079, 197.24372019277067, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.9975482606933, 195.1292364399155, 0.0), APoint(216.9975482606933, 197.24877218505165, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(215.92892732650216, 196.18900431248332, 0.0), APoint(215.9289273265049, 197.24877218505165, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(250.12479722053376, 195.02819659429576, 0.0), APoint(250.12479722053376, 197.097212416622, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(249.0561762863481, 196.08796446686358, 0.0), APoint(249.05617628634536, 197.10226440890298, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(247.98755535215605, 195.02819659429576, 0.0), APoint(247.98755535215605, 197.10731640118397, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(246.91893441796492, 196.08796446686358, 0.0), APoint(246.91893441796856, 197.11236839346503, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.85031348377925, 195.02819659429576, 0.0), APoint(245.85031348377834, 197.11742038574593, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.78169254959084, 196.08796446686358, 0.0), APoint(244.78169254959084, 197.122472378027, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.71307161540335, 195.02819659429576, 0.0), APoint(243.71307161540335, 197.12752437030798, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.64445068121222, 196.08796446686358, 0.0), APoint(242.64445068121404, 197.13257636258896, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(241.57582974702655, 195.02819659429576, 0.0), APoint(241.57582974702655, 197.13762835486995, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.50720881283723, 196.08796446686358, 0.0), APoint(240.50720881283723, 197.14268034715093, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.43858787864883, 195.02819659429576, 0.0), APoint(239.43858787864883, 197.1477323394319, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(261.8796274966053, 194.9726246792049, 0.0), APoint(261.8796274966053, 197.04164050153116, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(260.8110065624196, 196.03239255177272, 0.0), APoint(260.8110065624169, 197.04669249381215, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(259.7423856282294, 194.9726246792049, 0.0), APoint(259.7423856282285, 197.05174448609313, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(258.67376469403825, 196.03239255177272, 0.0), APoint(258.6737646940401, 197.0567964783742, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(257.6051437598526, 194.9726246792049, 0.0), APoint(257.60514375985076, 197.0618484706551, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(256.53652282566327, 196.03239255177272, 0.0), APoint(256.53652282566236, 197.06690046293613, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(255.46790189147487, 194.9726246792049, 0.0), APoint(255.46790189147487, 197.07195245521714, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(254.39928095728374, 196.03239255177272, 0.0), APoint(254.39928095728737, 197.0770044474981, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(253.33066002309806, 194.9726246792049, 0.0), APoint(253.33066002309806, 197.0820564397791, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(252.26203908891057, 196.03239255177272, 0.0), APoint(252.26203908891057, 197.0871084320601, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(251.19341815472126, 194.9726246792049, 0.0), APoint(251.19341815472126, 197.09216042434105, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(273.6344577726786, 194.92210475639502, 0.0), APoint(273.6344577726786, 196.99112057872125, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(272.56583683849203, 195.98187262896283, 0.0), APoint(272.5658368384893, 196.99617257100223, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(271.4972159043009, 194.92210475639502, 0.0), APoint(271.4972159043009, 197.0012245632832, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(270.4285949701107, 195.98187262896283, 0.0), APoint(270.4285949701134, 197.00627655556428, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(269.359974035925, 194.92210475639502, 0.0), APoint(269.3599740359241, 197.01132854784515, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(268.2913531017366, 195.98187262896283, 0.0), APoint(268.2913531017348, 197.01638054012625, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(267.2227321675473, 194.92210475639502, 0.0), APoint(267.2227321675473, 197.02143253240723, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(266.15411123335616, 195.98187262896283, 0.0), APoint(266.1541112333598, 197.02648452468821, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(265.0854902991714, 194.92210475639502, 0.0), APoint(265.0854902991714, 197.0315365169692, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.0168693649839, 195.98187262896283, 0.0), APoint(264.0168693649839, 197.03658850925018, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(262.9482484307937, 194.92210475639502, 0.0), APoint(262.9482484307937, 197.04164050153116, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(282.1834252461822, 195.9313527061529, 0.0), APoint(282.1834252461849, 196.94060065591148, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(281.11480431199743, 194.8715848335851, 0.0), APoint(281.1148043119965, 196.96080862503527, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(280.04618337780903, 195.9313527061529, 0.0), APoint(280.0461833778081, 196.9658606173163, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(278.9775624436197, 194.8715848335851, 0.0), APoint(278.9775624436197, 196.97091260959732, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(277.9089415094295, 195.9313527061529, 0.0), APoint(277.9089415094313, 196.9759646018783, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(276.8403205752429, 194.8715848335851, 0.0), APoint(276.8403205752429, 196.98101659415926, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(275.7716996410554, 195.9313527061529, 0.0), APoint(275.7716996410554, 196.98606858644027, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(274.703078706867, 194.8715848335851, 0.0), APoint(274.703078706867, 196.99112057872125, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(214.8603063923165, 195.17470437044443, 0.0), APoint(214.86030639231467, 197.25382417733263, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(213.79168545812536, 196.23447224301225, 0.0), APoint(213.79168545812718, 197.2588761696137, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(212.72306452393877, 195.17470437044443, 0.0), APoint(212.72306452393877, 197.2639281618946, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(211.65444358975128, 196.23447224301225, 0.0), APoint(211.65444358975037, 197.26898015417567, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(210.58582265556197, 195.17470437044443, 0.0), APoint(210.58582265556197, 197.27403214645665, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.51720172137175, 196.23447224301225, 0.0), APoint(209.51720172137448, 197.27908413873763, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(208.44858078718516, 195.17470437044443, 0.0), APoint(208.44858078718516, 197.2841361310186, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.37995985299767, 196.23447224301225, 0.0), APoint(207.37995985299767, 197.2891881232996, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.31133891880927, 195.17470437044443, 0.0), APoint(206.31133891880927, 197.29424011558058, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(205.24271798461814, 196.23447224301225, 0.0), APoint(205.24271798461996, 197.29424011558058, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.17409705043247, 195.22017230097336, 0.0), APoint(204.17409705043156, 197.29929210786156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.10547611624133, 196.27994017354118, 0.0), APoint(203.10547611624315, 197.30434410014263, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(202.03685518205475, 195.22017230097336, 0.0), APoint(202.03685518205475, 197.30939609242353, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.96823424786635, 196.27994017354118, 0.0), APoint(200.96823424786635, 197.3144480847046, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(199.89961331367795, 195.22017230097336, 0.0), APoint(199.89961331367795, 197.31950007698558, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.83099237948772, 196.27994017354118, 0.0), APoint(198.83099237949045, 197.32455206926656, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(197.76237144530114, 195.22017230097336, 0.0), APoint(197.76237144530114, 197.32960406154754, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.69375051111365, 196.27994017354118, 0.0), APoint(196.69375051111365, 197.33465605382852, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(195.62512957692525, 195.22017230097336, 0.0), APoint(195.62512957692525, 197.3397080461095, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.55650864273412, 196.27994017354118, 0.0), APoint(194.55650864273593, 197.3397080461095, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(193.48788770854753, 195.2656402315023, 0.0), APoint(193.48788770854753, 197.3447600383905, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.4192667743564, 196.3254081040701, 0.0), APoint(192.41926677435913, 197.34981203067156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.35064584017164, 195.2656402315023, 0.0), APoint(191.35064584017164, 197.35486402295246, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(190.28202490598323, 196.3254081040701, 0.0), APoint(190.28202490598233, 197.35991601523352, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(189.21340397179483, 195.2656402315023, 0.0), APoint(189.21340397179483, 197.3649680075145, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(188.1447830376028, 196.3254081040701, 0.0), APoint(188.14478303760643, 197.3700199997955, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(187.07616210341712, 195.2656402315023, 0.0), APoint(187.07616210341712, 197.37507199207647, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(186.00754116922872, 196.3254081040701, 0.0), APoint(186.00754116922872, 197.38012398435745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(184.93892023504122, 195.2656402315023, 0.0), APoint(184.93892023504122, 197.38517597663844, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.8702993008501, 196.3254081040701, 0.0), APoint(183.8702993008519, 197.38517597663844, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.80167836666442, 195.31110816203122, 0.0), APoint(182.8016783666635, 197.39022796891942, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.7330574324733, 196.37087603459904, 0.0), APoint(181.7330574324751, 197.3952799612005, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(180.6644364982876, 195.31110816203122, 0.0), APoint(180.6644364982876, 197.40033195348138, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(179.5958155640992, 196.37087603459904, 0.0), APoint(179.5958155640983, 197.40538394576245, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(178.5271946299099, 195.31110816203122, 0.0), APoint(178.5271946299099, 197.41043593804343, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.45857369571877, 196.37087603459904, 0.0), APoint(177.4585736957224, 197.41548793032442, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(176.3899527615331, 195.31110816203122, 0.0), APoint(176.3899527615331, 197.4205399226054, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(175.3213318273447, 196.37087603459904, 0.0), APoint(175.3213318273447, 197.42559191488638, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(174.2527108931563, 195.31110816203122, 0.0), APoint(174.2527108931563, 197.43064390716737, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.18408995896607, 196.37087603459904, 0.0), APoint(173.1840899589688, 197.43064390716737, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.1154690247804, 195.35657609256015, 0.0), APoint(172.11546902477858, 197.43569589944835, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(171.04684809058836, 196.41634396512796, 0.0), APoint(171.04684809059108, 197.44074789172942, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(169.9782271564036, 195.35657609256015, 0.0), APoint(169.9782271564036, 197.4457998840103, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(168.9096062222152, 196.41634396512796, 0.0), APoint(168.90960622221428, 197.45085187629138, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(167.84098528802588, 195.35657609256015, 0.0), APoint(167.84098528802588, 197.45590386857236, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(166.77236435383566, 196.41634396512796, 0.0), APoint(166.77236435383838, 197.46095586085335, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(165.70374341964907, 195.35657609256015, 0.0), APoint(165.70374341964907, 197.46600785313433, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(164.63512248546158, 196.41634396512796, 0.0), APoint(164.63512248546158, 197.4710598454153, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(163.56650155127318, 195.35657609256015, 0.0), APoint(163.56650155127318, 197.4761118376963, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(162.49788061708205, 196.41634396512796, 0.0), APoint(162.49788061708477, 197.50642379138193, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(314.64631940552044, 116.84772047753398, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(322.796013843059, 106.96412331052983, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(322.796013843059, 102.89362435031893, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(310.80319464512104, 116.84772047753398, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(310.75537976149553, 102.90084025096934, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(314.7388572787886, 102.86527325188803, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddLine(APoint(321.2636823923194, 104.97497325509374, 0.0), APoint(312.7261675199061, 104.97497325509352, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(312.7355260958093, 115.5455050777802, 0.0), APoint(312.7261675199061, 104.97497325509352, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(316.1013226850464, 104.97497325509352, 0.0), APoint(314.7388572787886, 102.86527325188803, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.75537976149553, 102.90084025096934, 0.0), APoint(312.7261675199061, 104.97497325509352, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.75537976149553, 107.0491062592177, 0.0), APoint(312.7261675199061, 104.97497325509352, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.64631940552044, 116.84772047753398, 0.0), APoint(312.7355260958093, 115.56001982308014, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.8031946451365, 116.84772047753194, 0.0), APoint(312.7355260958093, 115.5455050777802, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.834470150754, 102.85474082629975, 0.0), APoint(321.2636823923194, 104.97497325509374, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.834470150754, 107.00300683454856, 0.0), APoint(321.2636823923194, 104.97497325509374, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.7320544214044, 106.99398067572423, 0.0), APoint(316.1013226850464, 104.97497325509352, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.7150066166423, 116.99589079406468, 0.0), APoint(354.7150066166423, 120.32791824973577, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.11500661664286, 116.99589079406468, 0.0), APoint(367.11500661664286, 120.32791824973577, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.11500661664286, 120.32791824973714, 0.0), APoint(354.7150066166423, 120.32791824973577, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(354.7150066166423, 116.43030604818676, 0.0), 0.5655847458779121)
entity.Color = 8

entity = acad.model.AddCircle(APoint(367.11500661664286, 116.43030604818676, 0.0), 0.5655847458779121)
entity.Color = 8

entity = acad.model.AddLine(APoint(360.91500661664304, 116.99589079406468, 0.0), APoint(360.91500661664304, 120.32791824973577, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(360.91500661664304, 116.43030604818676, 0.0), 0.5655847458779121)
entity.Color = 8

entity = acad.model.AddLine(APoint(395.6582339857541, 107.9092293197861, 0.0), APoint(395.6582339857541, 101.90922931978612, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.6582339857541, 101.90922931978612, 0.0), APoint(403.45823398572975, 101.9092293197684, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.4582339857425, 107.9092293197861, 0.0), APoint(395.6582339857541, 107.9092293197861, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.02616751966616, 110.9092293197861, 0.0), APoint(317.02616751966616, 116.30922931978611, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(317.6261675196665, 116.30922931978611, 0.0), 0.6, 1.5707963267948966, 3.141592653589793)
entity.Color = 6

entity = acad.model.AddLine(APoint(317.6261675196665, 116.9092293197861, 0.0), APoint(324.1261675197011, 116.9092293197861, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(324.1261675197011, 116.9092293197861, 0.0), APoint(332.1261675197002, 108.9092293197861, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(332.1261675197002, 108.9092293197861, 0.0), APoint(377.74293745552313, 108.9092293197861, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.28893645538756, 108.9092293197861, 0.0), APoint(401.8582339857139, 108.9092293197861, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(401.8582339857139, 109.5092293197861, 0.0), 0.6, 4.71238898038469, 0.0)
entity.Color = 6

entity = acad.model.AddLine(APoint(402.4582339857143, 109.5092293197861, 0.0), APoint(402.4582339857143, 114.90922931978565, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2587412368357, 110.89499404240559, 0.0), APoint(402.2587412368357, 116.29499404240559, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(401.65874123683625, 116.29499404240559, 0.0), 0.6, 0.0, 1.5707963267948966)
entity.Color = 6

entity = acad.model.AddLine(APoint(401.65874123683625, 116.89499404240559, 0.0), APoint(395.1587412368008, 116.89499404240559, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.1587412368008, 116.89499404240559, 0.0), APoint(387.1587412368008, 108.89499404240559, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(387.1587412368008, 108.89499404240559, 0.0), APoint(379.0894437064517, 108.89499404240559, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(340.9073363251282, 108.9092293197861, 0.0), APoint(318.33803879480365, 108.9092293197861, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(318.33803879480365, 109.5092293197861, 0.0), 0.6, 3.141592653589793, 4.71238898038469)
entity.Color = 6

entity = acad.model.AddLine(APoint(317.73803879480056, 109.5092293197861, 0.0), APoint(317.73803879480056, 114.90922931978565, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 116.9092293197861, 0.0), APoint(317.6261675196647, 116.9092293197861, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(317.6261675196647, 116.30922931978688, 0.0), 0.599999999999227, 1.5707963267962606, 3.1415926535909295)
entity.Color = 6

entity = acad.model.AddLine(APoint(317.02616751966616, 116.3092293197862, 0.0), APoint(317.02616751966616, 113.50922931978602, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.45823398573157, 102.50922931983368, 0.0), APoint(396.8582339856248, 102.50922931983263, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(396.8582339856266, 103.1092293198318, 0.0), 0.5999999999991701, 3.141592653588571, 4.712388980383325)
entity.Color = 6

entity = acad.model.AddLine(APoint(396.25823398562625, 103.10922931983254, 0.0), APoint(396.25823398562625, 106.70922931983358, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(396.8582339856266, 106.70922931983404, 0.0), 0.5999999999994543, 1.5707963267962606, 3.14159265359056)
entity.Color = 6

entity = acad.model.AddLine(APoint(396.8582339856248, 107.30922931983349, 0.0), APoint(403.4582339857425, 107.30922931983852, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(396.68838766236695, 106.96412331052983, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(396.68838766236695, 102.89362435031893, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(310.75537976149553, 107.0491062592177, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(317.5150066166425, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(317.5150066166425, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(323.7150066166414, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(323.7150066166414, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(329.91500661664213, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(329.91500661664213, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(336.1150066166447, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(336.1150066166447, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(342.31500661664086, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(342.31500661664086, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(348.5150066166416, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(348.5150066166416, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(354.7150066166423, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(354.7150066166423, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(360.91500661664304, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(360.91500661664304, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(367.11500661664286, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(367.11500661664286, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(373.31500661663995, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(373.31500661663995, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(382.2856780686916, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(382.2856780686916, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(388.4856780686923, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(388.4856780686923, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(394.6856780686885, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(395.2778431286588, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(401.7838163513725, 108.67819298470721, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(401.7838163513725, 116.43030604818676, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddLine(APoint(354.7140853435503, 108.11260898915424, 0.0), APoint(354.70865785056776, 104.78058595387, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.11406889326736, 108.09241080234841, 0.0), APoint(367.1086414002848, 104.76038776706417, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.1086414002848, 104.76038776706281, 0.0), APoint(354.70865785056776, 104.78058595387, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(354.7150066166423, 108.67819298470721, 0.0), 0.565584745877912)
entity.Color = 8

entity = acad.model.AddCircle(APoint(367.11499016636117, 108.65799479790138, 0.0), 0.565584745877912)
entity.Color = 8

entity = acad.model.AddLine(APoint(360.9140771184093, 108.10250989575133, 0.0), APoint(360.9086496254258, 104.77048686046709, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(360.9149983915004, 108.6680938913043, 0.0), 0.565584745877912)
entity.Color = 8

entity = acad.model.AddCircle(APoint(314.7285135327602, 107.03674313329492, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(314.7416946106432, 121.99694916072866, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(398.72971331406643, 122.4979930285578, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(331.6074558226919, 125.60105840373939, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(377.0420859249225, 126.4188638237651, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(377.12076349070503, 100.67630737370376, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(307.52362976688437, 96.30988883498907, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(339.0616685778068, 101.21607078994128, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddLine(APoint(411.25823398573266, 107.90922931975064, 0.0), APoint(411.2582339857063, 101.90922931975064, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(411.2582339857063, 101.90922931975064, 0.0), APoint(403.45823398573157, 101.9092293197684, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.4582339857443, 107.9092293197861, 0.0), APoint(411.25823398573266, 107.90922931975064, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.4582339857325, 102.50922931983368, 0.0), APoint(410.05823398583834, 102.50922931980261, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(410.05823398584016, 103.10922931980178, 0.0), 0.5999999999991701, 4.712388980381052, 6.283185307176261)
entity.Color = 6

entity = acad.model.AddLine(APoint(410.6582339858378, 103.1092293197998, 0.0), APoint(410.658233985856, 106.70922931980084, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(410.05823398585653, 106.70922931980402, 0.0), 0.5999999999994543, 6.283185307174271, 1.5707963267894396)
entity.Color = 6

entity = acad.model.AddLine(APoint(410.05823398585926, 107.30922931980348, 0.0), APoint(403.4582339857425, 107.30922931983852, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(410.2280803091153, 106.96412331049905, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(410.2280803090962, 102.89362435028815, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(400.8678707940426, 106.96412331052983, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(400.8678707940426, 102.89362435031893, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(405.8203140928972, 106.96412331052983, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(405.8203140928972, 102.89362435031893, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddText('جزئیات الف', APoint(265.97845218115026, 82.72440588400264, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(265.1042130111282, 81.48056196095217, 0.0), APoint(280.8724889914565, 81.48056196095217, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(265.1042130111282, 80.90985417574734, 0.0), APoint(280.8724889914565, 80.90985417574734, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(273.3819427904791, 101.51951951664503, 0.0), APoint(282.0711255537062, 101.6064113442774, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.38194279048, 93.92914452601966, 0.0), APoint(282.14612180398944, 94.10678631615477, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.38194279048, 93.92914452601966, 0.0), APoint(264.38194279048, 101.42951951664512, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(265.88194279048, 94.5834585123794, 0.0), APoint(265.88194279048, 100.58997727941963, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(265.48194279047857, 100.58997727941963, 0.0), 0.4, 0.0, 0.6959394611362671)
entity.Color = 6

entity = acad.model.AddLine(APoint(262.88194279048, 101.42951951664512, 0.0), APoint(262.88194279048, 108.32951951664361, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.38194279048, 102.6757707892721, 0.0), APoint(264.38194279048, 107.02951951664502, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(264.78194279048057, 107.02951951664502, 0.0), 0.4, 1.5707963267948966, 3.141592653589793)
entity.Color = 6

entity = acad.model.AddLine(APoint(273.3819427904791, 101.51951951664503, 0.0), APoint(273.3819427904791, 108.32951951664452, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(271.8819427904791, 94.73847264530835, 0.0), APoint(271.8819427904791, 107.02951951664502, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(271.48194279047857, 107.02951951664502, 0.0), 0.4, 0.0, 1.5707963267948966)
entity.Color = 6

entity = acad.model.AddLine(APoint(263.4819427904822, 108.92951951664512, 0.0), APoint(272.78194279047693, 108.92951951664512, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.78194279048057, 107.42951951664512, 0.0), APoint(271.48194279047857, 107.42951951664512, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(262.88194279048, 101.42951951664512, 0.0), APoint(263.37133905541214, 101.42951951664512, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(263.89254652554337, 101.42951951664512, 0.0), APoint(264.38194279048, 101.42951951664512, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(263.63194279048, 101.42951951664512, 0.0), 0.2606037350650894, 0.0, 3.141592653589793)
entity.Color = 3

entity = acad.model.AddLine(APoint(262.88194279048, 108.32951951664498, 0.0), APoint(263.48194279047857, 108.92951951664512, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(273.3819427904791, 108.32951951664498, 0.0), APoint(272.78194279047693, 108.92951951664512, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(282.0711255537062, 102.90038180295986, 0.0), APoint(282.0711255537062, 98.07299023453291, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(282.0711255537062, 95.9848212605157, 0.0), APoint(282.0711255537062, 92.40870868832738, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(282.0872895738621, 97.4512584247141, 0.0), 0.6219418934983878, 0.0, 3.141592653589793)
entity.Color = 7

entity = acad.model.AddLine(APoint(281.46534768036327, 97.4512584247141, 0.0), APoint(282.70923146735913, 96.60655307033451, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(282.0872895738621, 96.60655307033451, 0.0), 0.6219418934983878, 3.141592653589793, 0.0)
entity.Color = 7

entity = acad.model.AddLine(APoint(264.4749620921957, 102.41932810389952, 0.0), APoint(265.78892348876343, 100.84641996479198, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(264.78194279048057, 102.6757707892721, 0.0), 0.4, 3.1415926535895657, 3.8375321147260597)
entity.Color = 6

entity = acad.model.AddCircle(APoint(271.42284768611444, 106.9478192608099, 0.0), 0.408)
entity.Color = 6

entity = acad.model.AddCircle(APoint(264.85900158729237, 106.91236600415462, 0.0), 0.408)
entity.Color = 6

entity = acad.model.AddCircle(APoint(264.8202653172457, 102.73467687572705, 0.0), 0.408)
entity.Color = 6

entity = acad.model.AddCircle(APoint(254.96931199632854, 89.87625392499947, 0.0), 1.875)
entity.Color = 8

entity = acad.model.AddLine(APoint(271.42284768611444, 106.9478192608099, 0.0), APoint(264.8202653172457, 102.73467687572705, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.85900158729237, 106.91236600415462, 0.0), APoint(268.12155650168006, 104.84124806826847, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(268.12155650168006, 104.84124806826847, 0.0), APoint(281.9842565718918, 104.84124806826847, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(283.29675657189, 104.84124806826847, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddLine(APoint(344.93487556371656, 82.73290771530867, 0.0), APoint(375.2157554761552, 82.7329077153085, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(344.93487556371474, 82.16219993010384, 0.0), APoint(375.2157554761552, 82.16219993010412, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('آرماتور بندی دال و شناژ', APoint(346.9367059697204, 84.16695861427338, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('مقطع', APoint(363.06179578275965, 78.91080012903826, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('2-2', APoint(356.186264123633, 78.78716008915029, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(224.764347850808, 101.28359477603627, 0.0), APoint(238.68568021985448, 101.42280809972976, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.24157733153424, 101.42836707084669, 0.0), APoint(239.764347850808, 101.43359477603954, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.5881502943521, 116.1325827817262, 0.0), APoint(215.764347850808, 116.19434475729068, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.36434785079928, 123.78434475728992, 0.0), APoint(225.6643478508022, 123.78434475729082, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.26434785082256, 123.18434475729319, 0.0), APoint(226.26434785082256, 116.28434475728992, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.26434785082256, 116.28434475728992, 0.0), APoint(225.82750513392602, 116.28434475728992, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.20119056773274, 116.28434475728992, 0.0), APoint(224.764347850808, 116.28434475728992, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.36434785082838, 123.78434475728992, 0.0), APoint(215.764347850808, 123.18434475728955, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.6643478508022, 123.78434475728992, 0.0), APoint(226.26434785082256, 123.18434475728955, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(225.51434785082256, 116.28434475728992, 0.0), 0.3131572830989171, 0.0, 3.141592653589793)
entity.Color = 3

entity = acad.model.AddLine(APoint(215.764347850808, 123.18434475728955, 0.0), APoint(215.764347850808, 116.19434475729068, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.5881502943521, 104.1319827967254, 0.0), APoint(224.764347850808, 104.28374477228991, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.76434785080528, 104.28374477229048, 0.0), APoint(224.764347850808, 116.28434475728992, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.764347850808, 95.2832947835399, 0.0), APoint(236.764347850808, 101.40359477603889, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.764347850808, 101.43359477603954, 0.0), APoint(239.764347850808, 104.43374477229045, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.764347850808, 116.28434475728992, 0.0), APoint(239.764347850808, 104.43374477229045, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.764347850808, 116.28434475728992, 0.0), APoint(235.15972331911144, 104.38769852697297, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.764347850808, 116.28434475728992, 0.0), APoint(231.78578876101164, 104.35395918139184, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.764347850808, 116.28434475728992, 0.0), APoint(227.2083675779113, 104.30818496956127, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.1412988144857, 104.32751428192697, 0.0), APoint(224.764347850808, 116.28434475728992, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(227.2083675779113, 104.30818496956127, 0.0), APoint(227.2083675779113, 101.30803497330854, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.1412988144857, 104.32751428192697, 0.0), APoint(229.1412988144857, 101.32736428567424, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(231.78578876101164, 104.35395918139184, 0.0), APoint(231.78578876101164, 101.35380918514002, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(235.15972331911144, 104.38769852697297, 0.0), APoint(235.15972331911144, 101.38754853072297, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.764347850808, 95.2832947835399, 0.0), APoint(209.5881502943521, 95.02029932331598, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.76434785080528, 104.28374477228985, 0.0), APoint(224.76434785080528, 102.22616966549984, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.76434785080528, 102.22616966549984, 0.0), APoint(224.76434785080528, 101.28359477603621, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.5881502943521, 118.35353637227067, 0.0), APoint(209.5881502943521, 108.08665495315373, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.5881502943521, 105.99848597913652, 0.0), APoint(209.5881502943521, 92.12152255753139, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(209.60431431450706, 107.46492314333491, 0.0), 0.6219418934983878, 0.0, 3.141592653589793)
entity.Color = 7

entity = acad.model.AddLine(APoint(208.98237242100822, 107.46492314333491, 0.0), APoint(210.2262562080041, 106.62021778895533, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(209.60431431450706, 106.62021778895533, 0.0), 0.6219418934983878, 3.141592653589793, 0.0)
entity.Color = 7

entity = acad.model.AddText('جزئیات ب', APoint(223.6523603124665, 82.9932537326658, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(221.5007338288451, 81.59241066605043, 0.0), APoint(237.26900980917435, 81.59241066605043, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.5007338288451, 81.0217028808456, 0.0), APoint(237.26900980917435, 81.0217028808456, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(238.96362877569481, 101.42558758528824, 0.0), 0.2779624529207136, 0.009999666686875549, 3.1515923202766682)
entity.Color = 3

entity = acad.model.AddLine(APoint(206.13658276873866, 65.07248737158714, 0.0), APoint(408.6007428102066, 65.07248737158714, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.13658276873866, 30.908010395168304, 0.0), APoint(206.13658276873866, 65.07248737158714, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.13658276873866, 52.35577082966209, 0.0), APoint(408.6007428102066, 52.355770829662035, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('ndâhv', APoint(213.70289683596457, 57.85007772237256, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('مقطع 3-3', APoint(315.91600164268675, 62.2876579889585, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('xâ– ndâhv', APoint(226.4969280759815, 57.28956465290108, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(214.61667962934462, 65.07248737158714, 0.0), APoint(214.61667962934462, 30.908010395168304, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(214.61667962934462, 60.88056282063641, 0.0), APoint(408.6007428102066, 60.88056282063641, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(253.11653101334377, 60.88056282063641, 0.0), APoint(253.11653101334377, 30.908010395168304, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.01775239053404, 60.88056282063641, 0.0), APoint(240.01775239053404, 30.908010395168304, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.33923757397952, 60.88056282063647, 0.0), APoint(226.33923757397952, 30.908010395168304, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W', APoint(219.04763168903173, 53.140569304106606, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('m (min)', APoint(301.6466688004666, 53.50915086961376, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('hvj»—À `Œ', APoint(313.3015785136886, 57.49694553175591, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(314.60889228584074, 60.88056282063641, 0.0), APoint(314.60889228584074, 30.908010395168304, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText(';© cdÁ `Œ', APoint(267.8804404319271, 57.8058344267274, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText(';© v, `Œ', APoint(299.7551423105715, 55.63228052001361, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(300.7950477920567, 60.88056282063641, 0.0), APoint(300.7950477920567, 30.908010395168304, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W1', APoint(208.33137632174112, 48.74814584316445, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.13658276873866, 46.993830721038634, 0.0), APoint(408.6007428102066, 46.99383072103869, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W2', APoint(208.33137632174112, 43.386205734540994, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.13658276873866, 41.631890612415205, 0.0), APoint(408.6007428102066, 41.631890612415106, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W3', APoint(208.33137632174112, 38.02426562591761, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.13658276873866, 36.269950503791705, 0.0), APoint(408.6007428102066, 36.269950503791705, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W4', APoint(208.33137632174112, 32.66232551729411, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.13658276873866, 30.908010395168304, 0.0), APoint(408.6007428102066, 30.908010395168304, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('--', APoint(217.78097239173076, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(259.0461927245615, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(305.1738364050152, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('uÁ´ `Œ', APoint(339.7239971194276, 57.82963762787675, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('f (min)', APoint(330.405704743408, 53.50915086961376, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(217.78097239173076, 43.38069912373484, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(259.0461927245615, 43.38069912373484, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(305.1738364050152, 43.38069912373484, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(217.78097239173076, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(259.0461927245615, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(305.1738364050152, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(217.78097239173076, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(259.0461927245615, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(305.1738364050152, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('nv hf©h ', APoint(270.618556575233, 53.51891648012608, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('ndâhv', APoint(259.4497797516806, 53.45757396985606, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('nv hkš—', APoint(287.53690036901116, 53.75095436549233, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(270.50461500427264, 60.88056282063641, 0.0), APoint(270.50461500427264, 30.908010395168304, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(287.57858156394377, 60.88056282063641, 0.0), APoint(287.57858156394377, 30.908010395168304, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText(';© cdÁ `Œ', APoint(285.5432026276767, 57.8058344267274, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('ndâhv', APoint(277.1125419474283, 53.45757396985606, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('--', APoint(277.13301174960907, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(277.13301174960907, 43.38069912373484, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(277.13301174960907, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(277.13301174960907, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(291.9956410635541, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(291.9956410635541, 43.38069912373484, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(291.9956410635541, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(291.9956410635541, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('m (max)', APoint(315.17473216384315, 53.50915086961376, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('hvj»—À `Œ', APoint(326.8296418770651, 57.49694553175591, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(328.97745733277134, 60.88056282063641, 0.0), APoint(328.97745733277134, 30.908010395168304, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('--', APoint(318.70189976839265, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(318.70189976839265, 43.38069912373484, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(318.70189976839265, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(318.70189976839265, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(342.3845635176731, 60.88056282063641, 0.0), APoint(342.3845635176731, 30.908010395168304, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('0.85', APoint(333.0433375753755, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('uÁ´ `Œ', APoint(352.59814584765445, 57.82963762787675, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('f (max)', APoint(343.27985347163667, 53.50915086961376, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(355.6277993761805, 60.88056282063636, 0.0), APoint(355.6277993761805, 30.90801039516822, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(368.87103523468704, 60.88056282063636, 0.0), APoint(368.87103523468704, 30.90801039516822, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.11427109319357, 60.88056282063636, 0.0), APoint(382.11427109319357, 30.90801039516822, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.3575069517001, 60.88056282063636, 0.0), APoint(395.3575069517001, 30.90801039516822, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.6007428102066, 65.07248737158714, 0.0), APoint(408.6007428102066, 30.90801039516822, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('--', APoint(345.91748630360325, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(345.91748630360325, 43.38069912373484, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(345.91748630360325, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(345.91748630360325, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('h (max)', APoint(227.04246764148138, 53.71200184298125, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('hvj»—À', APoint(236.53260876242803, 57.598496680275474, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('h (min)', APoint(240.7009903803928, 53.71200184298125, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('hvj»—À', APoint(250.19113150133944, 57.598496680275474, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('--', APoint(229.79158451580952, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(229.79158451580952, 43.38069912373484, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(229.79158451580952, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(229.79158451580952, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('1.00', APoint(242.87490078214432, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('1.00', APoint(242.87490078214432, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('1.00', APoint(242.87490078214432, 43.38069912373484, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('1.00', APoint(242.87490078214432, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(359.6936796187838, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(359.6936796187838, 43.38069912373484, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(359.6936796187838, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(359.6936796187838, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.68', APoint(372.34594012575417, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(386.18015133579775, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(386.18015133579775, 43.38069912373484, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(386.18015133579775, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('--', APoint(386.18015133579775, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.35', APoint(398.82663900262924, 48.7426392323583, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s1', APoint(360.6992879011932, 57.42441244713845, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(max)', APoint(358.07829927507646, 54.05708092634775, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s1', APoint(373.9425237596988, 57.42441244713845, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(min)', APoint(371.3215351335821, 54.05708092634775, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s2', APoint(387.18575961820534, 57.424412447138394, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(max)', APoint(384.5647709920895, 54.057080926347695, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s2', APoint(400.42899547671186, 57.424412447138394, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(min)', APoint(397.80800685059603, 54.057080926347695, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.35', APoint(398.82663900262924, 43.38069912373473, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.35', APoint(398.82663900262924, 38.018759015111314, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.35', APoint(398.82663900262924, 32.65681890648791, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.68', APoint(372.34594012575417, 43.38069912373497, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.68', APoint(372.34594012575417, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.68', APoint(372.34594012575417, 32.656818906488, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.85', APoint(333.0433375753755, 43.38069912373497, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.85', APoint(333.0433375753755, 38.018759015111414, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.85', APoint(333.0433375753755, 32.656818906488, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(397.94156194723837, 104.90922931982922, 0.0), APoint(408.9749060242302, 104.90922931980415, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(410.2280803091153, 106.96412331049905, 0.0), APoint(408.9749060242293, 104.90922931980415, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.9749060242293, 104.90922931980415, 0.0), APoint(410.2280803090962, 102.89362435028815, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.6883876623506, 106.96412331052983, 0.0), APoint(397.94156194723473, 104.90922931983494, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(397.94156194723473, 104.90922931983494, 0.0), APoint(396.68838766236695, 102.89362435031893, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.8203140928972, 106.96412331052983, 0.0), APoint(404.56713980801123, 104.90922931983494, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.56713980801123, 104.90922931983494, 0.0), APoint(405.8203140928781, 102.89362435031893, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.8678707940426, 106.96412331052983, 0.0), APoint(399.6146965091566, 104.90922931983494, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(399.6146965091566, 104.90922931983494, 0.0), APoint(400.8678707940235, 102.89362435031893, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(381.959966673342, 101.3461073333273, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddLine(APoint(398.8004953406644, 114.98597863822661, 0.0), APoint(398.8004953406644, 93.04087518465613, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(398.8004953406644, 114.98597863822661, 0.0), APoint(389.22825509333234, 114.98597863822661, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(388.0510633021486, 95.3159920403431, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddLine(APoint(321.03703930305255, 113.8055684767941, 0.0), APoint(321.03703930305255, 91.86046502322361, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(330.6092795503846, 113.8055684767941, 0.0), APoint(321.03703930305255, 113.8055684767941, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(330.5264206947095, 91.57301153409927, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(413.19595221749296, 98.28444247989647, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddLine(APoint(320.69261141489915, 191.64810354151902, 0.0), APoint(408.4424045167525, 191.64810354151902, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 184.14810354151902, 0.0), APoint(408.4424045167525, 184.14810354151902, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141489915, 285.21972888328287, 0.0), APoint(320.69261141489915, 176.64810354151905, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(327.44261141489864, 215.46972888328222, 0.0), APoint(327.44261141489824, 197.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(334.19261141489915, 215.46972888328222, 0.0), APoint(334.19261141489915, 197.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(340.94261141489915, 215.46972888328222, 0.0), APoint(340.94261141489915, 197.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.19240451675284, 215.46972888328222, 0.0), APoint(367.1924045167525, 197.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(375.4424045167525, 215.46972888328222, 0.0), APoint(375.4424045167525, 197.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(383.6924045167511, 215.46972888328222, 0.0), APoint(383.6924045167507, 197.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675256, 215.46972888328222, 0.0), APoint(391.9424045167525, 197.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167489, 215.46972888328222, 0.0), APoint(400.19240451674796, 197.5304778217412, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167507, 191.64810354151902, 0.0), APoint(400.1924045167507, 184.14810354151902, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.44240451675256, 285.21972888328287, 0.0), APoint(408.4424045167525, 176.64810354151902, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('وزن آرماتور برای یکمتر طول آبرو', APoint(354.5046880968873, 193.71302036404586, 0.0), 1.8)
entity.Color = 1

entity = acad.model.AddText('وزن آرماتور برای ابتدا و انتهای آبرو', APoint(360.7562876100187, 186.9368267599775, 0.0), 1.8)
entity.Color = 1

entity = acad.model.AddText('226.5', APoint(392.1907055852889, 193.58335592557157, 0.0), 1.875)
entity.Color = 1

entity = acad.model.AddText('21.1', APoint(401.3121729414843, 186.77625421581635, 0.0), 1.875)
entity.Color = 1

entity = acad.model.AddText('وزن کل آرماتور مورد نیاز', APoint(346.2889121367077, 178.90279389507924, 0.0), 1.8)
entity.Color = 1

entity = acad.model.AddText('(Kg)', APoint(373.9109409713328, 179.0866345310953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('3768.6', APoint(379.6721288179733, 178.8825833451776, 0.0), 1.875)
entity.Color = 1

entity = acad.model.AddLine(APoint(320.69261141489915, 176.64810354151902, 0.0), APoint(408.4424045167525, 176.64810354151902, 0.0))
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

entity = acad.model.AddText('11', APoint(322.99762028208465, 211.3787338448733, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(320.69261141489915, 203.53047782174121, 0.0), APoint(408.4424045167525, 203.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('12', APoint(322.94748409843805, 205.3787338448733, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(320.69261141489915, 197.53047782174121, 0.0), APoint(408.4424045167525, 197.53047782174121, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('13', APoint(322.69650189868776, 199.3787338448733, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091379, 212.01093769569138, 0.0), APoint(359.67258082251374, 212.01093769569138, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.67258082251374, 212.01093769569138, 0.0), APoint(359.67258082251374, 213.54607984265022, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('65 / 50', APoint(352.82956682788245, 212.38376202757672, 0.0), 1.3125)


entity = acad.model.AddText('20', APoint(359.98757295889027, 211.98767638887023, 0.0), 1.3125)


entity = acad.model.AddText('14', APoint(329.1209481209744, 211.53100282919138, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddText('132.4', APoint(335.5393902606993, 211.66256247382654, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.0417154911811, 205.67752710312163, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddText('10', APoint(328.9666787576275, 199.66256247382654, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddText('16', APoint(335.23877206094403, 205.66256247382654, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddText('109.23', APoint(335.39312666491514, 199.66256247382654, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddText('1.208', APoint(386.27020849300425, 211.4947039320719, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('108.0', APoint(394.120890332877, 211.3827578937192, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('89.37', APoint(378.02020849300516, 211.4947039320719, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('1.4', APoint(369.77020849300516, 211.4947039320719, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091379, 205.72979626710526, 0.0), APoint(359.67258082251556, 205.72979626710526, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('None', APoint(352.49400297420925, 206.1026205989906, 0.0), 1.3125)


entity = acad.model.AddText('0.617', APoint(386.248439897817, 205.35531046476984, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.6722544293557, 199.35531046476984, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('None', APoint(377.41201468753434, 205.4947039320719, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('None', APoint(369.65392158378904, 205.4947039320719, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('None', APoint(377.2468844929406, 199.4947039320719, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('None', APoint(369.23733154801675, 199.4947039320719, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.6', APoint(394.120890332877, 205.3827578937192, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.6', APoint(394.120890332877, 199.3827578937192, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(358.85379208291124, 200.68906872310887, 0.0), APoint(348.1179503982976, 200.68906872310887, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(348.1179503982976, 200.3890687231089, 0.0), 0.3, 1.5707963267948966, 3.141592653589793)


entity = acad.model.AddArc(APoint(358.85379208291124, 200.3890687231089, 0.0), 0.3, 0.0, 1.5707963267948966)


entity = acad.model.AddLine(APoint(347.8179503982974, 200.3890687231089, 0.0), APoint(347.8179503982974, 198.7154963997998, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.1179503982976, 198.41549639979982, 0.0), APoint(358.85379208291124, 198.41549639979982, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(358.85379208291124, 198.7154963997998, 0.0), 0.3, 4.71238898038469, 0.0)


entity = acad.model.AddArc(APoint(348.1179503982976, 198.7154963997998, 0.0), 0.3, 3.141592653589793, 4.71238898038469)


entity = acad.model.AddLine(APoint(359.15379208291233, 198.7154963997998, 0.0), APoint(359.15379208291233, 200.3890687231089, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.15379208291233, 200.3890687231089, 0.0), APoint(358.3310948932467, 199.68581487575463, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(358.85379208291124, 200.68906872310887, 0.0), APoint(358.05031141926975, 199.9802884969922, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('22', APoint(359.86804869750085, 199.00520870831213, 0.0), 1.3125)


entity = acad.model.AddText('22', APoint(344.7727208832903, 199.00520870831213, 0.0), 1.3125)


entity = acad.model.AddText('-9', APoint(350.5611616053784, 201.46718298779786, 0.0), 1.3125)


entity = acad.model.AddText('10', APoint(355.94728639500136, 198.67720478718627, 0.0), 1.3125)


entity = acad.model.AddText('*', APoint(336.05593197573216, 206.40504346661538, 0.0), 2.625)


entity = acad.model.AddText('*', APoint(410.2780320499678, 162.1100296035723, 0.0), 2.625)


entity = acad.model.AddText('.در آبرو های دهانه یک متری و دو متری تعداد برابر 6*2 منظور شود', APoint(326.9669094143835, 160.65198452745514, 0.0), 2.25)
entity.Color = 1

entity = acad.model.AddText('جزئیات دیوارهای هدایت آب', APoint(295.7881762318739, 67.04687193337489, 0.0), 3.0)
entity.Color = 1

entity = acad.model.AddText('292-SB-3S-1/3', APoint(300.63252846825685, 6.479800353879995, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('شماره نقشه اجرایی', APoint(193.523297256962, 21.481158218250105, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(338.76513799721124, 9.537644467135607, 0.0), APoint(296.64869948316027, 9.537644467135607, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('- ', APoint(373.6320728534538, 20.135243960929756, 0.0), 2.663041818489627)
entity.Color = 7

entity = acad.model.AddText('سازمان مدیریت و برنامه ریزی کشور', APoint(375.4814744737048, 20.643935199664156, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('امور نظام فنی اجرایی', APoint(349.36619202546876, 20.919852803038314, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(320.6926114148991, 285.21972888328287, 0.0), APoint(408.44240451675245, 285.21972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.6926114148991, 275.46972888328287, 0.0), APoint(408.44240451675245, 275.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.6926114148991, 269.46972888328287, 0.0), APoint(408.44240451675245, 269.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.6926114148991, 263.46972888328287, 0.0), APoint(408.44240451675245, 263.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.6926114148991, 257.46972888328287, 0.0), APoint(408.44240451675245, 257.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.6926114148991, 251.46972888328273, 0.0), APoint(408.44240451675245, 251.46972888328273, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.6926114148991, 245.46972888328273, 0.0), APoint(408.44240451675245, 245.46972888328273, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.6926114148991, 239.46972888328273, 0.0), APoint(408.44240451675245, 239.46972888328273, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.6926114148991, 233.46972888328273, 0.0), APoint(408.44240451675245, 233.46972888328273, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.6926114148991, 227.46972888328273, 0.0), APoint(408.44240451675245, 227.46972888328273, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.6926114148991, 221.46972888328287, 0.0), APoint(408.44240451675245, 221.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(327.4426114149, 285.21972888328287, 0.0), APoint(327.4426114148991, 215.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(334.1926114148991, 285.21972888328287, 0.0), APoint(334.1926114148991, 215.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(340.9426114148991, 285.21972888328287, 0.0), APoint(340.9426114148991, 215.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.19240451675427, 285.21972888328287, 0.0), APoint(367.19240451675427, 215.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(375.44240451675245, 285.21972888328287, 0.0), APoint(375.44240451675245, 215.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(383.69240451675245, 285.21972888328287, 0.0), APoint(383.69240451675245, 215.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675245, 285.21972888328287, 0.0), APoint(391.94240451675245, 215.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675245, 285.21972888328287, 0.0), APoint(400.1924045167506, 215.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('شماره', APoint(322.0863104274503, 279.3203795732246, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('قطر', APoint(329.22571355645863, 280.8986904171592, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('تعداد', APoint(335.18677029647546, 279.3194106546482, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('mm', APoint(329.8784779574998, 277.39481981493645, 0.0), 1.125)
entity.Color = 1

entity = acad.model.AddText('شکل آرماتور', APoint(346.668201950717, 279.1471997567644, 0.0), 1.875)
entity.Color = 1

entity = acad.model.AddText('طول', APoint(369.8328992502001, 280.93471451651044, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('وزن کل', APoint(393.1872774491421, 282.37884747613396, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('طول کل', APoint(376.7079626048798, 280.93902533572464, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('وزن یکمتر', APoint(383.4972136770511, 281.0152438005189, 0.0), 1.274999999999999)
entity.Color = 1

entity = acad.model.AddText('وزن کل', APoint(400.9567879097021, 280.97093484934385, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('m', APoint(370.4799099960755, 276.85466319404077, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('m', APoint(378.36449394160985, 276.85466319404077, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('Kg/m', APoint(385.95446954783614, 276.85466319404054, 0.0), 1.274999999999999)
entity.Color = 1

entity = acad.model.AddText('Kg', APoint(394.8644939416053, 276.85466319404077, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('Kg', APoint(403.1144939416053, 276.85466319403963, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('2', APoint(323.2163732246053, 265.31798490641484, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('1', APoint(323.2163732246053, 271.31798490641484, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('3', APoint(323.2163732246053, 259.31798490641495, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('4', APoint(323.2163732246053, 253.31798490641484, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('5', APoint(323.2163732246053, 247.31798490641484, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('6', APoint(323.2163732246053, 241.31798490641484, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('7', APoint(323.2163732246053, 235.31798490641484, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('8', APoint(323.2163732246053, 229.31798490641484, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('9', APoint(323.2163732246053, 223.31798490641484, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('18', APoint(329.1039998291953, 271.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(345.067844216458, 271.3263451512013, 0.0), APoint(345.067844216458, 272.18278318658884, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(345.067844216458, 272.18278318658884, 0.0), APoint(348.87348956246836, 272.18278318658884, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.87348956246836, 272.18278318658884, 0.0), APoint(351.4579578964485, 270.71170469689196, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(363.0675598198313, 270.71170469689196, 0.0), APoint(363.0675598198313, 271.7320477583562, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(351.4579578964485, 270.71170469689196, 0.0), APoint(363.0675598198313, 270.71170469689196, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('22', APoint(341.62267981529834, 271.1055880697551, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('27', APoint(346.02912875550004, 272.41625274436524, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('20', APoint(349.87501251655425, 271.7475555301511, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('209', APoint(355.7505492757236, 270.91845400259103, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('22', APoint(363.4916343102622, 270.8246763729944, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddLine(APoint(362.9884062924065, 265.50986221474454, 0.0), APoint(362.9884062924065, 266.3663002501321, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(362.9884062924065, 266.3663002501321, 0.0), APoint(359.1827609463962, 266.3663002501321, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.1827609463962, 266.3663002501321, 0.0), APoint(356.59829261241697, 264.8952217604352, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(344.9886906890342, 264.8952217604352, 0.0), APoint(344.9886906890342, 265.9155648218996, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(356.59829261241697, 264.8952217604352, 0.0), APoint(344.9886906890342, 264.8952217604352, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('22', APoint(363.22554515342375, 265.28910513329834, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('27', APoint(359.3396217533654, 266.5997698079085, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('20', APoint(355.06588739189004, 265.93107259369447, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('209', APoint(349.80570123314095, 265.1019710661344, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('22', APoint(341.65159854783536, 265.0081934365377, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.0543825671802, 241.38985533241933, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.0543825671802, 235.38985533241944, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.0543825671802, 229.38985533241944, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.0543825671802, 223.38985533241944, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.46243510913786, 259.6690473286469, 0.0), APoint(359.6725808225155, 259.6690473286469, 0.0))
entity.Color = 1


entity = acad.model.AddText('18.1', APoint(352.4940029742092, 260.04187166053225, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.46243510913786, 252.41504661027415, 0.0), APoint(348.46243510913786, 253.95018875723295, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(348.46243510913786, 253.95018875723295, 0.0), APoint(359.6725808225155, 253.95018875723295, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(359.6725808225155, 252.41504661027415, 0.0), APoint(359.6725808225155, 253.95018875723295, 0.0))
entity.Color = 1


entity = acad.model.AddText('15', APoint(345.23768372110857, 252.75144567271764, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('250', APoint(352.8295668278824, 254.32301308911835, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('15', APoint(359.9875729588911, 252.78585379085104, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.46243510913786, 247.66904732864685, 0.0), APoint(359.6725808225155, 247.66904732864685, 0.0))
entity.Color = 1


entity = acad.model.AddText('17.7', APoint(352.4940029742092, 248.04187166053214, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('8*2', APoint(335.7891998808299, 241.40701238074033, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.46243510913786, 241.66904732864685, 0.0), APoint(359.6725808225155, 241.66904732864685, 0.0))
entity.Color = 1


entity = acad.model.AddText('17.7', APoint(352.4940029742092, 242.04187166053214, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('17.7', APoint(368.8041756690318, 241.4339549936134, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('282.72', APoint(377.3424045167524, 241.26511982574385, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167524, 241.29456152631144, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('174.31', APoint(393.8424045167524, 241.28450954912503, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('55*2', APoint(335.7891998808299, 235.07995028110943, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167524, 235.29456152631144, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(352.27672165581856, 235.46747896075445, 0.0), APoint(357.8494552464562, 235.46747896075445, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(353.4994553012038, 234.13266891312372, 0.0), APoint(353.4994553012038, 237.66175655633154, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(353.349455301206, 237.66175655633154, 0.0), 0.15, 0.0, 1.5707963267948966)
entity.Color = 1

entity = acad.model.AddLine(APoint(357.99945524645767, 235.31747896075444, 0.0), APoint(357.99945524645767, 233.98868418861886, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(357.8494552464562, 235.31747896075444, 0.0), 0.15, 0.0, 1.5707963267948966)
entity.Color = 1

entity = acad.model.AddArc(APoint(357.8494552464562, 233.98868418861886, 0.0), 0.15, 4.71238898038469, 0.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(357.8494552464562, 233.83868418861886, 0.0), APoint(352.14945532145606, 233.83868418861886, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(352.14945532145606, 233.98868418861886, 0.0), 0.15, 3.141592653590248, 4.71238898038469)
entity.Color = 1

entity = acad.model.AddLine(APoint(351.9994553214546, 237.66175655633154, 0.0), APoint(351.9994553214546, 233.98868418861872, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(353.349455301206, 237.81175655633155, 0.0), APoint(352.1494553214515, 237.81175655633172, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(352.1494553214515, 237.66175655633174, 0.0), 0.15, 1.5707963267948966, 3.141592653590248)
entity.Color = 1

entity = acad.model.AddText('22', APoint(358.0093339008235, 234.16418363761187, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('45', APoint(348.39757408287545, 234.7055548124382, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('45', APoint(354.2954519055292, 235.61835174374872, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('17', APoint(348.2430401421315, 236.87049926991884, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('2.2', APoint(369.1072545483113, 235.43395499361344, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('240.9', APoint(377.3424045167524, 235.37445277478585, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('148.52', APoint(393.8424045167524, 235.3453995462606, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('3*2', APoint(335.7891998808299, 229.40701238074033, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.46243510913786, 229.66904732864685, 0.0), APoint(359.6725808225155, 229.66904732864685, 0.0))
entity.Color = 1


entity = acad.model.AddText('2.5', APoint(352.4940029742092, 230.04187166053214, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('2.5', APoint(369.1072545483113, 229.43395499361344, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('15.0', APoint(377.3424045167524, 229.26511982574374, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167524, 229.29456152631144, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('9.25', APoint(402.09240451675095, 229.2945615263114, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('9*2', APoint(335.7891998808299, 223.6018135353681, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddLine(APoint(352.0918823228994, 224.45528774922562, 0.0), APoint(354.6615543732432, 224.45528774922562, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(354.6615543732432, 224.60528774922594, 0.0), 0.15, 4.71238898038469, 5.408328441522121)
entity.Color = 1

entity = acad.model.AddLine(APoint(355.44372693943836, 225.0177877492257, 0.0), APoint(357.0763827122009, 225.0177877492257, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(357.0763827122009, 224.86778774922544, 0.0), 0.15, 0.0, 1.5707963267948966)
entity.Color = 1

entity = acad.model.AddLine(APoint(352.13190229709375, 222.20528774922562, 0.0), APoint(357.0763827122009, 222.20528774922562, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(357.0763827122009, 222.35528774922585, 0.0), 0.15, 4.71238898038469, 0.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(357.22638271220234, 224.86778774922544, 0.0), APoint(357.22638271220234, 222.35528774922585, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(355.34756093242316, 224.98290551108195, 0.0), APoint(354.75772038025656, 224.49016998736906, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(355.44372693943836, 224.86778774922544, 0.0), 0.15, 1.5707963267948966, 2.2667357879311565)
entity.Color = 1

entity = acad.model.AddText('25', APoint(357.4101374449528, 222.98081455643205, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('20', APoint(348.50054672094205, 223.95180421960953, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('15', APoint(355.1454142341635, 225.2079112568441, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('40', APoint(348.4576780041834, 221.88208077727865, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('7', APoint(353.7863507135543, 224.64442274458605, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('1.1', APoint(369.1072545483113, 223.43395499361344, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('19.26', APoint(377.3424045167524, 223.3220089552607, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167524, 223.29456152631144, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('11.87', APoint(402.09240451675095, 223.28450954912472, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(400.19240451675336, 274.85051292637263, 0.0), APoint(400.8116204736636, 275.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 273.92243527606524, 0.0), APoint(401.73969812397075, 275.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 272.99435762575786, 0.0), APoint(402.66777577427814, 275.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 272.06627997545047, 0.0), APoint(403.5958534245855, 275.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 271.1382023251431, 0.0), APoint(404.5239310748929, 275.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675336, 270.2101246748359, 0.0), APoint(405.4520087252003, 275.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.38008637550746, 269.46972888328264, 0.0), APoint(406.38008637550746, 275.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.30816402581485, 269.46972888328264, 0.0), APoint(407.30816402581485, 275.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.23624167612223, 269.46972888328264, 0.0), APoint(408.23624167612223, 275.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264296, 269.46972888328264, 0.0), APoint(408.4424045167495, 274.7478140736025, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.092396976737, 269.46972888328264, 0.0), APoint(408.4424045167497, 273.81973642329535, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270437, 269.46972888328264, 0.0), APoint(408.4424045167495, 272.8916587729884, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.9485522773511, 269.46972888328264, 0.0), APoint(408.4424045167495, 271.96358112268103, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.8766299276585, 269.46972888328264, 0.0), APoint(408.4424045167495, 271.03550347237365, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796587, 269.46972888328264, 0.0), APoint(408.4424045167495, 270.10742582206626, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675336, 268.8505129263717, 0.0), APoint(400.8116204736645, 269.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 267.92243527606433, 0.0), APoint(401.73969812397166, 269.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 266.99435762575695, 0.0), APoint(402.66777577427905, 269.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 266.06627997544956, 0.0), APoint(403.59585342458644, 269.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167529, 265.13820232514195, 0.0), APoint(404.5239310748938, 269.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 264.2101246748348, 0.0), APoint(405.4520087252012, 269.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.38008637550837, 263.46972888328264, 0.0), APoint(406.38008637550837, 269.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.30816402581576, 263.46972888328264, 0.0), APoint(407.30816402581553, 269.4697288832824, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.23624167612314, 263.46972888328264, 0.0), APoint(408.23624167612314, 269.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.16431932643053, 263.46972888328264, 0.0), APoint(408.4424045167502, 268.7478140736023, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767379, 263.46972888328264, 0.0), APoint(408.44240451675086, 267.8197364232956, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270451, 263.4697288832831, 0.0), APoint(408.4424045167506, 266.89165877298865, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735246, 263.4697288832831, 0.0), APoint(408.44240451675154, 265.96358112268217, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.8766299276594, 263.46972888328264, 0.0), APoint(408.4424045167522, 265.03550347237547, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.8047075779668, 263.46972888328264, 0.0), APoint(408.4424045167527, 264.10742582206854, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675336, 262.8505129263717, 0.0), APoint(400.8116204736645, 263.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 261.92243527606433, 0.0), APoint(401.73969812397166, 263.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 260.99435762575695, 0.0), APoint(402.66777577427905, 263.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 260.06627997544956, 0.0), APoint(403.59585342458644, 263.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167529, 259.13820232514195, 0.0), APoint(404.5239310748938, 263.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 258.2101246748348, 0.0), APoint(405.4520087252012, 263.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.38008637550837, 257.46972888328264, 0.0), APoint(406.38008637550837, 263.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.30816402581576, 257.46972888328264, 0.0), APoint(407.30816402581553, 263.4697288832824, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.23624167612314, 257.46972888328264, 0.0), APoint(408.23624167612314, 263.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.16431932643053, 257.46972888328264, 0.0), APoint(408.4424045167502, 262.7478140736023, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.09239697673746, 257.4697288832822, 0.0), APoint(408.44240451675086, 261.8197364232956, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270446, 257.46972888328264, 0.0), APoint(408.44240451675086, 260.8916587729889, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.948552277352, 257.46972888328264, 0.0), APoint(408.442404516752, 259.9635811226826, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.8766299276594, 257.46972888328264, 0.0), APoint(408.4424045167522, 259.03550347237547, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.8047075779668, 257.46972888328264, 0.0), APoint(408.4424045167527, 258.10742582206854, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675336, 256.8505129263717, 0.0), APoint(400.8116204736645, 257.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 255.92243527606433, 0.0), APoint(401.73969812397166, 257.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 254.99435762575695, 0.0), APoint(402.66777577427905, 257.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 254.06627997544956, 0.0), APoint(403.59585342458644, 257.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 253.13820232514217, 0.0), APoint(404.5239310748938, 257.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 252.2101246748348, 0.0), APoint(405.4520087252012, 257.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.38008637550814, 251.46972888328241, 0.0), APoint(406.38008637550837, 257.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.30816402581553, 251.46972888328241, 0.0), APoint(407.30816402581553, 257.4697288832824, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761229, 251.46972888328241, 0.0), APoint(408.23624167612314, 257.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264303, 251.46972888328241, 0.0), APoint(408.4424045167502, 256.7478140736023, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.09239697673746, 251.4697288832822, 0.0), APoint(408.44240451675086, 255.81973642329558, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270446, 251.46972888328264, 0.0), APoint(408.44240451675086, 254.89165877298888, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.948552277352, 251.46972888328264, 0.0), APoint(408.44240451675154, 253.96358112268217, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.8766299276594, 251.46972888328264, 0.0), APoint(408.4424045167522, 253.03550347237547, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.8047075779668, 251.46972888328264, 0.0), APoint(408.4424045167527, 252.10742582206854, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167529, 250.85051292637127, 0.0), APoint(400.8116204736643, 251.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167529, 249.9224352760641, 0.0), APoint(401.73969812397144, 251.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167529, 248.99435762575672, 0.0), APoint(402.6677757742786, 251.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167529, 248.06627997544933, 0.0), APoint(403.595853424586, 251.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167529, 247.13820232514195, 0.0), APoint(404.52393107489337, 251.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167529, 246.21012467483456, 0.0), APoint(405.45200872520076, 251.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.38008637550837, 245.46972888328264, 0.0), APoint(406.38008637550814, 251.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.30816402581576, 245.46972888328264, 0.0), APoint(407.30816402581553, 251.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.23624167612314, 245.46972888328264, 0.0), APoint(408.2362416761229, 251.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.16431932643053, 245.46972888328264, 0.0), APoint(408.44240451674995, 250.74781407360206, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767379, 245.46972888328264, 0.0), APoint(408.4424045167506, 249.81973642329535, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270451, 245.4697288832831, 0.0), APoint(408.4424045167506, 248.89165877298865, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735246, 245.4697288832831, 0.0), APoint(408.44240451675154, 247.96358112268217, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.8766299276594, 245.46972888328264, 0.0), APoint(408.4424045167522, 247.03550347237547, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.8047075779668, 245.46972888328264, 0.0), APoint(408.4424045167522, 246.10742582206808, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675336, 244.85051292637263, 0.0), APoint(400.81162047366337, 245.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 243.92243527606524, 0.0), APoint(401.7396981239705, 245.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 242.99435762575786, 0.0), APoint(402.6677757742777, 245.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 242.06627997545047, 0.0), APoint(403.5958534245851, 245.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 241.13820232514308, 0.0), APoint(404.52393107489246, 245.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675336, 240.21012467483592, 0.0), APoint(405.45200872519985, 245.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.38008637550746, 239.46972888328264, 0.0), APoint(406.38008637550723, 245.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.30816402581485, 239.46972888328264, 0.0), APoint(407.3081640258146, 245.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.23624167612223, 239.46972888328264, 0.0), APoint(408.236241676122, 245.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264296, 239.46972888328264, 0.0), APoint(408.4424045167495, 244.7478140736025, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.092396976737, 239.46972888328264, 0.0), APoint(408.4424045167497, 243.81973642329535, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270437, 239.46972888328264, 0.0), APoint(408.4424045167495, 242.89165877298842, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.9485522773511, 239.46972888328264, 0.0), APoint(408.4424045167495, 241.96358112268103, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.8766299276585, 239.46972888328264, 0.0), APoint(408.4424045167495, 241.03550347237365, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796587, 239.46972888328264, 0.0), APoint(408.4424045167495, 240.10742582206626, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167529, 238.85051292637127, 0.0), APoint(400.8116204736643, 239.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 237.92243527606433, 0.0), APoint(401.73969812397144, 239.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 236.99435762575695, 0.0), APoint(402.6677757742786, 239.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 236.06627997544956, 0.0), APoint(403.595853424586, 239.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 235.13820232514217, 0.0), APoint(404.52393107489337, 239.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 234.2101246748348, 0.0), APoint(405.45200872520076, 239.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.38008637550814, 233.46972888328241, 0.0), APoint(406.38008637550814, 239.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.30816402581553, 233.46972888328241, 0.0), APoint(407.3081640258153, 239.4697288832822, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761229, 233.46972888328241, 0.0), APoint(408.2362416761229, 239.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264303, 233.46972888328241, 0.0), APoint(408.4424045167502, 238.74781407360229, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.09239697673746, 233.4697288832822, 0.0), APoint(408.44240451675086, 237.81973642329558, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270446, 233.46972888328264, 0.0), APoint(408.4424045167506, 236.89165877298865, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.948552277352, 233.46972888328264, 0.0), APoint(408.44240451675154, 235.96358112268217, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.8766299276594, 233.46972888328264, 0.0), APoint(408.4424045167522, 235.03550347237547, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.8047075779668, 233.46972888328264, 0.0), APoint(408.4424045167527, 234.10742582206854, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167497, 232.8505129263708, 0.0), APoint(392.56162047366155, 233.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167495, 231.92243527606342, 0.0), APoint(393.4896981239687, 233.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167495, 230.99435762575604, 0.0), APoint(394.41777577427587, 233.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167495, 230.06627997544865, 0.0), APoint(395.34585342458325, 233.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167495, 229.13820232514126, 0.0), APoint(396.27393107489064, 233.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167495, 228.21012467483388, 0.0), APoint(397.202008725198, 233.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(392.13008637550564, 227.46972888328264, 0.0), APoint(398.1300863755054, 233.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.058164025813, 227.46972888328264, 0.0), APoint(399.0581640258128, 233.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.9862416761204, 227.46972888328264, 0.0), APoint(399.9862416761202, 233.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.9143193264278, 227.46972888328264, 0.0), APoint(400.19240451674904, 232.74781407360388, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.8423969767352, 227.46972888328264, 0.0), APoint(400.1924045167497, 231.81973642329717, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.77047462704235, 227.4697288832831, 0.0), APoint(400.1924045167495, 230.89165877299024, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(397.69855227734973, 227.4697288832831, 0.0), APoint(400.1924045167502, 229.96358112268354, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(398.6266299276571, 227.4697288832831, 0.0), APoint(400.1924045167502, 229.03550347237615, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(399.5547075779645, 227.4697288832831, 0.0), APoint(400.19240451675086, 228.10742582206944, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451674926, 226.85051292637127, 0.0), APoint(392.56162047366064, 227.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451674926, 225.9224352760641, 0.0), APoint(393.4896981239678, 227.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451674926, 224.99435762575672, 0.0), APoint(394.41777577427496, 227.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451674926, 224.06627997544933, 0.0), APoint(395.34585342458234, 227.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451674926, 223.13820232514195, 0.0), APoint(396.27393107488973, 227.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451674926, 222.21012467483456, 0.0), APoint(397.2020087251971, 227.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(392.13008637550473, 221.46972888328264, 0.0), APoint(398.1300863755045, 227.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.0581640258121, 221.46972888328264, 0.0), APoint(399.0581640258119, 227.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.9862416761195, 221.46972888328264, 0.0), APoint(399.9862416761193, 227.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.9143193264269, 221.46972888328264, 0.0), APoint(400.1924045167488, 226.74781407360456, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.8423969767343, 221.46972888328264, 0.0), APoint(400.1924045167488, 225.81973642329717, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.77047462704144, 221.4697288832831, 0.0), APoint(400.1924045167486, 224.89165877299024, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(397.69855227734837, 221.46972888328264, 0.0), APoint(400.1924045167486, 223.96358112268285, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(398.62662992765576, 221.46972888328264, 0.0), APoint(400.1924045167486, 223.03550347237547, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(399.55470757796314, 221.46972888328264, 0.0), APoint(400.1924045167486, 222.10742582206808, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('18', APoint(329.0543825671802, 265.38985533241964, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('14', APoint(329.0543825671802, 259.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.0543825671802, 253.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.0543825671802, 247.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('24', APoint(335.8043825671793, 247.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('178', APoint(335.8043825671793, 253.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('33', APoint(335.8043825671793, 259.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('178', APoint(335.8043825671793, 265.38985533241964, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('178', APoint(335.7891998808299, 271.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('3.0', APoint(369.10725454831135, 271.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('534.0', APoint(377.3424045167524, 271.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('1.998', APoint(385.5924045167524, 271.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('1066.71', APoint(393.8424045167524, 271.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('3.0', APoint(369.1072545483113, 265.38985533241964, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('534.0', APoint(377.3424045167524, 265.38985533241964, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('1.998', APoint(385.5924045167524, 265.38985533241964, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('1066.71', APoint(393.8424045167524, 265.38985533241964, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('18.1', APoint(369.1072545483113, 259.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('597.89', APoint(377.3424045167524, 259.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('1.208', APoint(385.5924045167524, 259.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('722.5', APoint(393.8424045167524, 259.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('2.8', APoint(369.1072545483113, 253.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('498.4', APoint(377.3424045167524, 253.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167524, 253.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('307.28', APoint(393.8424045167524, 253.3898553324195, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('17.7', APoint(369.1072545483113, 247.38985533241956, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('424.08', APoint(377.3424045167524, 247.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167524, 247.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('261.46', APoint(393.8424045167524, 247.38985533241953, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('10', APoint(323.2163732246053, 217.31798490641484, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('-', APoint(329.0543825671802, 217.38985533241944, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('66.2', APoint(335.7891998808299, 217.60181353536814, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddText('-', APoint(369.1072545483113, 217.43395499361344, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('-', APoint(377.3424045167524, 217.3220089552607, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('-', APoint(385.5924045167524, 217.29456152631144, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(320.6926114148991, 215.46972888328287, 0.0), APoint(408.44240451675245, 215.46972888328287, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('(1m)', APoint(393.50524947865864, 279.2682382730362, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(400.19240451675336, 220.85051292637172, 0.0), APoint(400.8116204736645, 221.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 219.92243527606433, 0.0), APoint(401.73969812397166, 221.46972888328287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 218.99435762575695, 0.0), APoint(402.6677757742786, 221.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 218.06627997544956, 0.0), APoint(403.595853424586, 221.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 217.13820232514217, 0.0), APoint(404.52393107489337, 221.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675313, 216.2101246748348, 0.0), APoint(405.45200872520076, 221.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.38008637550814, 215.46972888328241, 0.0), APoint(406.38008637550814, 221.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.30816402581553, 215.46972888328241, 0.0), APoint(407.30816402581553, 221.46972888328241, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761229, 215.46972888328241, 0.0), APoint(408.23624167612314, 221.46972888328264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264303, 215.46972888328241, 0.0), APoint(408.44240451675336, 220.74781407360547, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.09239697673746, 215.4697288832822, 0.0), APoint(408.44240451675336, 219.81973642329808, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270446, 215.46972888328264, 0.0), APoint(408.44240451675313, 218.89165877299115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.948552277352, 215.46972888328264, 0.0), APoint(408.44240451675313, 217.96358112268376, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.8766299276594, 215.46972888328264, 0.0), APoint(408.44240451675336, 217.0355034723766, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.8047075779668, 215.46972888328264, 0.0), APoint(408.44240451675336, 216.10742582206922, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('-', APoint(393.8424045167524, 217.29456152631144, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.46243510913786, 217.95018875723295, 0.0), APoint(359.6725808225155, 217.95018875723295, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.6725808225155, 217.95018875723295, 0.0), APoint(359.6725808225155, 219.48533090419173, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('- / -', APoint(352.8295668278824, 218.3230130891182, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('-', APoint(359.9875729588911, 217.92692745041174, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('UP', APoint(14.029511117826075, 223.1234692798704, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('i-094', APoint(73.2275392569984, 171.15719325662212, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('DOWN', APoint(131.1044928410347, 223.37262015862916, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('i-093', APoint(75.25607167294993, 282.9679116980152, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(48.32301469313916, 223.71035349895288, 0.0), APoint(48.32301469313916, 192.1005628361271, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.57301469313916, 223.71035349895288, 0.0), APoint(48.57301469313916, 191.9562252688297, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.07301469313916, 223.71035349895288, 0.0), APoint(50.07301469313916, 191.0901998650453, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.11025403423992, 223.71035349895288, 0.0), APoint(81.11025403423992, 183.16114307839965, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(88.7826002666402, 223.71035349895288, 0.0), APoint(88.7826002666402, 184.53771911071613, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.83039196204527, 223.71035349895288, 0.0), APoint(89.83039196204527, 184.45339622859478, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.07301469314325, 223.7103534989529, 0.0), APoint(105.07301469314325, 191.09019986504728, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.57301469313916, 223.7103534989529, 0.0), APoint(106.57301469313916, 191.95622526882974, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.82301469314325, 223.7103534989529, 0.0), APoint(106.82301469314325, 192.10056283612923, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.03958438290385, 197.19657006223048, 0.0), APoint(282.1834252461849, 196.94060065591148, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.0747991576693, 184.5319763097824, 0.0), APoint(239.8879372545125, 184.5319763097823, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(0.0, 0.0, 0.0), APoint(419.99999999992724, 0.0, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(419.99999999992724, 0.0, 0.0), APoint(419.99999999992724, 297.0000000000072, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(419.99999999992724, 297.0000000000072, 0.0), APoint(0.0, 297.0000000000072, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(0.0, 297.0000000000072, 0.0), APoint(0.0, 0.0, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(415.0, 5.0, 0.0), APoint(415.0, 292.0, 0.0))
entity.Color = 7
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

entity = acad.model.AddLine(APoint(5.0, 292.0, 0.0), APoint(5.0, 5.0, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(5.0, 5.0, 0.0), APoint(415.0, 5.0, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.07301469313914, 259.09019986504654, 0.0), APoint(110.42192067532257, 253.2897245541334, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(137.3230146931419, 276.5550455080339, 0.0), APoint(140.67192067532528, 270.75457019712076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(109.05589527153813, 253.65574995791786, 0.0), APoint(141.03794607910976, 272.1205956009052, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.8879372545107, 187.53197630978252, 0.0), APoint(206.73793725450923, 187.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.73793725450923, 187.53197630978252, 0.0), APoint(206.73793725450923, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.73793725450923, 184.53197630978252, 0.0), APoint(170.8879372545107, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.8879372545107, 184.53197630978252, 0.0), APoint(170.8879372545107, 187.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.03958438290385, 187.53197630978252, 0.0), APoint(242.73793725451014, 187.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.73793725451014, 187.53197630978252, 0.0), APoint(242.73793725451014, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.73793725451014, 184.53197630978252, 0.0), APoint(226.0747991576691, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.98117089486644, 184.53197630978252, 0.0), APoint(206.8879372545107, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.8879372545107, 184.53197630978252, 0.0), APoint(206.8879372545107, 187.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.8879372545107, 187.53197630978252, 0.0), APoint(223.94595612010107, 187.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.88793725451524, 187.53197630978252, 0.0), APoint(278.7379372545138, 187.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(278.7379372545138, 187.53197630978252, 0.0), APoint(278.7379372545138, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(278.7379372545138, 184.53197630978252, 0.0), APoint(242.88793725451524, 184.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.88793725451524, 184.53197630978252, 0.0), APoint(242.88793725451524, 187.53197630978252, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.21501551782976, 118.00677443353422, 0.0), APoint(44.697106225094664, 118.58130776587345, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.38761734383719, 117.37925308370825, 0.0), APoint(51.869708051102094, 117.95378641604748, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.172705831016046, 124.27365307177905, 0.0), APoint(57.63986696637232, 124.83039403316027, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.56021916984507, 116.75173173388237, 0.0), APoint(59.04230987710997, 117.3262650662216, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.34530765702392, 123.64613172195317, 0.0), APoint(64.82739836428883, 124.2206650542924, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.73282099585225, 116.12421038405655, 0.0), APoint(66.21491170311715, 116.69874371639578, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.5179094830311, 123.01861037212736, 0.0), APoint(72.000000190296, 123.59314370446658, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.9054228218598, 115.49668903423047, 0.0), APoint(73.3875135291247, 116.0712223665697, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.69051130903875, 122.39108902230119, 0.0), APoint(79.17260201630366, 122.96562235464042, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.07802464786751, 114.86916768440467, 0.0), APoint(80.56011535513241, 115.4437010167439, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.86311313504636, 121.76356767247547, 0.0), APoint(86.34520384231126, 122.3381010048147, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.25062647387496, 114.24164633457868, 0.0), APoint(87.73271718113986, 114.8161796669179, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.03571496105383, 121.13604632264945, 0.0), APoint(93.51780566831873, 121.71057965498868, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.52302793179842, 113.73306155462797, 0.0), APoint(94.90531900714737, 114.18865831709178, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.20831678706132, 120.50852497282335, 0.0), APoint(100.69040749432622, 121.08305830516258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.38091861306893, 119.88100362299764, 0.0), APoint(107.86300932033383, 120.45553695533687, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.172706096179056, 124.27365419174731, 0.0), APoint(57.7704229150341, 124.22136074609871, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.34530792243962, 123.64613284396417, 0.0), APoint(64.94302474129466, 123.59383939831557, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.51790974870018, 123.01861149618102, 0.0), APoint(72.11562656755522, 122.96631805053242, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.03571522748162, 121.13604745283159, 0.0), APoint(93.63343204633667, 121.08375400718299, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.20831705374218, 120.50852610504845, 0.0), APoint(100.80603387259723, 120.45623265939984, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.38091888000274, 119.8810047572653, 0.0), APoint(107.97863569885779, 119.8287113116167, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.6905115749609, 122.39109014839784, 0.0), APoint(79.28822839381594, 122.33879670274924, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.86311340122145, 121.76356880061469, 0.0), APoint(86.4608302200765, 121.71127535496609, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.2150157797874, 118.0067755503135, 0.0), APoint(44.81273259864245, 117.9544821046649, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.38761760604797, 117.37925420253036, 0.0), APoint(51.985334424903016, 117.32696075688176, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.560219432308536, 116.75173285474722, 0.0), APoint(59.157936251163584, 116.69943940909862, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.7328212585691, 116.12421150696407, 0.0), APoint(66.33053807742415, 116.07191806131547, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.90542308482966, 115.49669015918093, 0.0), APoint(73.50313990368471, 115.44439671353233, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.07802491109035, 114.86916881139778, 0.0), APoint(80.6757417299454, 114.81687536574918, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.25062673735091, 114.24164746361464, 0.0), APoint(87.84834355620596, 114.18935401796604, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.81270206440426, 117.95443248890336, 0.0), APoint(44.69707595586772, 118.58125926772219, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.985303834113665, 117.32691105276437, 0.0), APoint(51.86967772557712, 117.9537378315832, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.157905603823636, 116.69938961662496, 0.0), APoint(59.04227949528709, 117.32621639544378, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.77039230138509, 124.22131096245083, 0.0), APoint(57.667018777730526, 124.78171460889075, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.33050737353328, 116.07186818048497, 0.0), APoint(66.21488126499673, 116.6986949593038, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.94299407109473, 123.59378952631084, 0.0), APoint(64.82736796255818, 124.22061630512967, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.50310914324288, 115.44434674434508, 0.0), APoint(73.38748303470634, 116.0711735231639, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.11559584080433, 122.96626809017096, 0.0), APoint(71.99996973226779, 123.59309486898978, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.67571091295243, 114.81682530820532, 0.0), APoint(80.56008480441588, 115.44365208702415, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.28819761051388, 122.3387466540312, 0.0), APoint(79.17257150197733, 122.96557343285002, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.8483126826624, 114.18930387206578, 0.0), APoint(87.73268657412585, 114.8161306508846, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.46079938022385, 121.71122521789165, 0.0), APoint(86.3451732716873, 122.33805199671048, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.98846130717106, 113.73771588838167, 0.0), APoint(94.90528834383527, 114.18860921474588, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.63340114993326, 121.08370378175293, 0.0), APoint(93.51777504139672, 121.71053056057175, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.80600291964284, 120.45618234561304, 0.0), APoint(100.69037681110629, 121.08300912443187, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.97860468935286, 119.82866090947329, 0.0), APoint(107.86297858081632, 120.45548768829211, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.16777775798599, 115.94374413284977, 0.0), APoint(52.94666271229807, 116.75550963343862, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.84019106470157, 114.28855132491887, 0.0), APoint(63.619076019013654, 115.10031682550772, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.1868105164466, 124.02973733198502, 0.0), APoint(72.96569547075869, 124.84150283257387, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.8592238231624, 122.37454452405446, 0.0), APoint(83.63810877747449, 123.1863100246433, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.53163712987802, 120.71935171612333, 0.0), APoint(94.31052208419011, 121.53111721671218, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.20405043659363, 119.06415890819305, 0.0), APoint(104.98293539090572, 119.8759244087819, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.055859607878546, 115.80450588997428, 0.0), APoint(52.94537711255518, 116.75420445686949, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.72826900619034, 114.14930911484316, 0.0), APoint(63.61778651086697, 115.09900768173837, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.07488846293238, 123.89049512258862, 0.0), APoint(72.96440596760901, 124.84019368948383, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.74729786124416, 122.23529834745746, 0.0), APoint(83.6368153659208, 123.18499691435267, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.41970725955584, 120.58010157232725, 0.0), APoint(94.30922476423247, 121.52980013922246, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.09211665786724, 118.92490479719575, 0.0), APoint(104.98163416254387, 119.87460336409096, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.18553986189524, 124.02840343569964, 0.0), APoint(73.07490731577536, 123.89047036505018, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.53035877478113, 120.71800973704737, 0.0), APoint(94.41972622866126, 120.5800766663979, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.20276823122444, 119.06281288772112, 0.0), APoint(105.09213568510457, 118.92487981707166, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.85794931833846, 122.37320658637347, 0.0), APoint(83.74731677221858, 122.235273515724, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.16651095490373, 115.9424142823261, 0.0), APoint(53.05587840878385, 115.80448121167663, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.83892041134703, 114.28721743299985, 0.0), APoint(63.72828786522715, 114.14928436235039, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.002763019546606, 120.06943494239684, 0.0), APoint(50.70294833941951, 120.33821090455581, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.404986858021424, 123.29474648830454, 0.0), APoint(59.105172177894325, 123.56352245046351, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.97183354073134, 116.04324603574351, 0.0), APoint(56.67201886060424, 116.31202199790248, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.37405737920615, 119.26855758165121, 0.0), APoint(65.07424269907905, 119.53733354381018, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.77628121768096, 122.49386912755891, 0.0), APoint(73.47646653755386, 122.76264508971788, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.34312790039053, 115.24236867499782, 0.0), APoint(71.04331322026343, 115.51114463715679, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.7453517388652, 118.46768022090566, 0.0), APoint(79.4455370587381, 118.73645618306463, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.14757557734, 121.69299176681336, 0.0), APoint(87.84776089721291, 121.96176772897233, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.71442226005013, 114.44149131425206, 0.0), APoint(85.41460757992303, 114.71026727641103, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.11664609852478, 117.66680286015982, 0.0), APoint(93.81683141839768, 117.93557882231879, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.5188699369996, 120.89211440606752, 0.0), APoint(102.2190552568725, 121.16089036822649, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.45503400534017, 113.78238161536342, 0.0), APoint(99.7859019395831, 113.90938991566574, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.48794045818501, 116.86592549941447, 0.0), APoint(108.18812577805791, 117.13470146157344, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.72177337654875, 124.80230654408729, 0.0), APoint(96.04722321793254, 124.5827878542689, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.51887119679581, 120.89211469136197, 0.0), APoint(102.01629374032883, 120.55659894927952, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.48794171919211, 116.86592578637259, 0.0), APoint(107.98536426272513, 116.53041004429014, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.14757683278748, 121.69299205087192, 0.0), APoint(87.6449993763205, 121.35747630878947, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.1166473551838, 117.66680314588253, 0.0), APoint(93.61406989871682, 117.33128740380008, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.77628246877921, 122.49386941038213, 0.0), APoint(73.27370501231223, 122.15835366829968, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.74535299117542, 118.46768050539276, 0.0), APoint(79.24277553470844, 118.13216476331031, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.71442351357172, 114.44149160040338, 0.0), APoint(85.21184605710474, 114.10597585832093, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.40498810477029, 123.29474676989291, 0.0), APoint(58.90241064830332, 122.95923102781046, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.37405862716659, 119.26855786490353, 0.0), APoint(64.87148117069961, 118.93304212282108, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.34312914956288, 115.24236895991415, 0.0), APoint(70.8405516930959, 114.9068532178317, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.00276426315842, 120.06943522441345, 0.0), APoint(50.500186806691445, 119.733919482331, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.97183478555472, 116.04324631942407, 0.0), APoint(56.469257329087746, 115.70773057734162, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.75284956192445, 116.74138986655612, 0.0), APoint(42.09796296507963, 116.50860793685148, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(42.09792430191634, 116.5086022868433, 0.0), APoint(42.29797310329244, 117.10480556080131, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.500148069216124, 119.73391381490696, 0.0), APoint(50.70291083931432, 120.33820550042456, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.469218525353725, 115.70772490818706, 0.0), APoint(56.67198129545192, 116.31201659370467, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.90237183651588, 122.95922534297037, 0.0), APoint(59.10513460661408, 123.56351702848798, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.87144229265343, 118.93303643625049, 0.0), APoint(65.07420506275162, 119.5373281217681, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.84051274879096, 114.90684752953062, 0.0), APoint(71.04327551888915, 115.51113921504823, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.27366605995311, 122.15834796431393, 0.0), APoint(73.4764288300513, 122.76263964983154, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.24273651609069, 118.13215905759428, 0.0), APoint(79.44549928618888, 118.73645074311189, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.2118069722283, 114.1059701508746, 0.0), APoint(85.41456974232649, 114.7102618363922, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.64496028339045, 121.35747058565791, 0.0), APoint(87.84772305348864, 121.96176227117552, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.61403073952799, 117.33128167893804, 0.0), APoint(93.81679350962618, 117.93557336445565, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.04718405069013, 124.58278211372135, 0.0), APoint(96.11950826823038, 124.79832919517011, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.74422002601301, 113.78527347556997, 0.0), APoint(99.78586396576372, 113.90938445773578, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.01625450682769, 120.55659320700148, 0.0), APoint(102.21901727692588, 121.16088489251909, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.98532496296536, 116.53040430028203, 0.0), APoint(108.18808773306355, 117.13469598579964, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.70674279019321, 116.83041727233966, 0.0), APoint(43.70674279019321, 116.83041727233966, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.02221017014449, 120.90911884669809, 0.0), APoint(49.02221017014449, 120.90911884669809, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.27817604957392, 124.94216331388087, 0.0), APoint(54.27817604957392, 124.94216331388087, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.585144237020224, 113.50147873402614, 0.0), APoint(43.585144237020224, 113.50147873402614, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.9006116169715, 117.58018030838457, 0.0), APoint(48.9006116169715, 117.58018030838457, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.156577496400935, 121.61322477556735, 0.0), APoint(54.156577496400935, 121.61322477556735, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.779013063798246, 114.25124177007139, 0.0), APoint(48.779013063798246, 114.25124177007139, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.03497894322768, 118.28428623725416, 0.0), APoint(54.03497894322768, 118.28428623725416, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.20764272192653, 122.25341075439103, 0.0), APoint(59.20764272192653, 122.25341075439103, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.9133803900547, 114.9553476989411, 0.0), APoint(53.9133803900547, 114.9553476989411, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.08604416875355, 118.92447221607796, 0.0), APoint(59.08604416875355, 118.92447221607796, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.40151154870483, 123.00317379043639, 0.0), APoint(64.40151154870483, 123.00317379043639, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.96444561558031, 115.59553367776459, 0.0), APoint(58.96444561558031, 115.59553367776459, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.27991299553159, 119.67423525212303, 0.0), APoint(64.27991299553159, 119.67423525212303, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.53587887496103, 123.7072797193058, 0.0), APoint(69.53587887496103, 123.7072797193058, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.15831444235931, 116.34529671381028, 0.0), APoint(64.15831444235931, 116.34529671381028, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.41428032178875, 120.37834118099306, 0.0), APoint(69.41428032178875, 120.37834118099306, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.5869441004876, 124.34746569812992, 0.0), APoint(74.5869441004876, 124.34746569812992, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.29268176861504, 117.04940264267942, 0.0), APoint(69.29268176861504, 117.04940264267942, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.46534554731389, 121.01852715981629, 0.0), APoint(74.46534554731389, 121.01852715981629, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.17108321544205, 113.72046410436636, 0.0), APoint(69.17108321544205, 113.72046410436636, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.3437469941409, 117.68958862150322, 0.0), APoint(74.3437469941409, 117.68958862150322, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.65921437409285, 121.76829019586235, 0.0), APoint(79.65921437409285, 121.76829019586235, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.22214844096794, 114.36065008319018, 0.0), APoint(74.22214844096794, 114.36065008319018, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.5376158209192, 118.43935165754866, 0.0), APoint(79.5376158209192, 118.43935165754866, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.79358170034864, 122.47239612473143, 0.0), APoint(84.79358170034864, 122.47239612473143, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.41601726774601, 115.11041311923475, 0.0), APoint(79.41601726774601, 115.11041311923475, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.67198314717545, 119.14345758641753, 0.0), APoint(84.67198314717545, 119.14345758641753, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.55038459400384, 115.81451904810558, 0.0), APoint(84.55038459400384, 115.81451904810558, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.03851575265422, 123.86234513960103, 0.0), APoint(95.03851575265422, 123.86234513960103, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.6014498195292, 116.45470502692896, 0.0), APoint(89.6014498195292, 116.45470502692896, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.91691719948057, 120.53340660128735, 0.0), APoint(94.91691719948057, 120.53340660128735, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.17288307891, 124.56645106847013, 0.0), APoint(100.17288307891, 124.56645106847013, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.79531864630763, 117.20446806297444, 0.0), APoint(94.79531864630763, 117.20446806297444, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.05128452573707, 121.23751253015722, 0.0), APoint(100.05128452573707, 121.23751253015722, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.6737200931354, 113.87552952466126, 0.0), APoint(94.6737200931354, 113.87552952466126, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.92968597256484, 117.90857399184404, 0.0), APoint(99.92968597256484, 117.90857399184404, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.10234975126369, 121.8776985089809, 0.0), APoint(105.10234975126369, 121.8776985089809, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.80808741939212, 114.5796354535313, 0.0), APoint(99.80808741939212, 114.5796354535313, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.98075119809097, 118.54875997066816, 0.0), APoint(104.98075119809097, 118.54875997066816, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.85915264491656, 115.21982143235446, 0.0), APoint(104.85915264491656, 115.21982143235446, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(110.17462002486783, 119.2985230067129, 0.0), APoint(110.17462002486783, 119.2985230067129, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(110.05302147169458, 115.96958446839926, 0.0), APoint(110.05302147169458, 115.96958446839926, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.381368047791, 123.2581257983066, 0.0), APoint(55.381368047791, 123.2581257983066, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.88476632275987, 123.58770443366222, 0.0), APoint(57.88476632275987, 123.58770443366222, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.672085693207826, 124.08631448794281, 0.0), APoint(61.672085693207826, 124.08631448794281, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.43516890641904, 118.48255683504128, 0.0), APoint(46.43516890641904, 118.48255683504128, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.75067267337021, 119.31400867948301, 0.0), APoint(52.75067267337021, 119.31400867948301, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.254070948339084, 119.64358731483864, 0.0), APoint(55.254070948339084, 119.64358731483864, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.04139031878704, 120.14219736911923, 0.0), APoint(59.04139031878704, 120.14219736911923, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.3568940857382, 120.97364921356096, 0.0), APoint(65.3568940857382, 120.97364921356096, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.86029236070708, 121.30322784891659, 0.0), APoint(67.86029236070708, 121.30322784891659, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.64761173115504, 121.80183790319718, 0.0), APoint(71.64761173115504, 121.80183790319718, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.96311549810605, 122.63328974763898, 0.0), APoint(77.96311549810605, 122.63328974763898, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.46651377307492, 122.96286838299461, 0.0), APoint(80.46651377307492, 122.96286838299461, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.25383314352288, 123.4614784372752, 0.0), APoint(84.25383314352288, 123.4614784372752, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.07273518544335, 124.62250891707258, 0.0), APoint(93.07273518544335, 124.62250891707258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.51375588658121, 113.71025102658152, 0.0), APoint(37.51375588658121, 113.71025102658152, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(40.01715416155008, 114.03982966193715, 0.0), APoint(40.01715416155008, 114.03982966193715, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.804473531998035, 114.53843971621774, 0.0), APoint(43.804473531998035, 114.53843971621774, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.11997729894921, 115.36989156065947, 0.0), APoint(50.11997729894921, 115.36989156065947, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.62337557391808, 115.6994701960151, 0.0), APoint(52.62337557391808, 115.6994701960151, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.410694944366035, 116.19808025029569, 0.0), APoint(56.410694944366035, 116.19808025029569, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.72619871131721, 117.02953209473742, 0.0), APoint(62.72619871131721, 117.02953209473742, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.22959698628608, 117.35911073009305, 0.0), APoint(65.22959698628608, 117.35911073009305, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.01691635673404, 117.85772078437364, 0.0), APoint(69.01691635673404, 117.85772078437364, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.33242012368521, 118.68917262881537, 0.0), APoint(75.33242012368521, 118.68917262881537, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.22935918146975, 121.17700185252961, 0.0), APoint(94.22935918146975, 121.17700185252961, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.54486294842091, 122.00845369697134, 0.0), APoint(100.54486294842091, 122.00845369697134, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.04826122338979, 122.33803233232697, 0.0), APoint(103.04826122338979, 122.33803233232697, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.83581839865322, 119.01875126417092, 0.0), APoint(77.83581839865322, 119.01875126417092, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.62313776910118, 119.5173613184515, 0.0), APoint(81.62313776910118, 119.5173613184515, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.93864153605234, 120.34881316289324, 0.0), APoint(87.93864153605234, 120.34881316289324, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.59890161186302, 113.41499361126924, 0.0), APoint(62.59890161186302, 113.41499361126924, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.38622098231097, 113.91360366554983, 0.0), APoint(66.38622098231097, 113.91360366554983, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.70172474926214, 114.74505550999156, 0.0), APoint(72.70172474926214, 114.74505550999156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.20512302423101, 115.07463414534719, 0.0), APoint(75.20512302423101, 115.07463414534719, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.59866380704761, 117.2328847337058, 0.0), APoint(91.59866380704761, 117.2328847337058, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.91416757399878, 118.06433657814753, 0.0), APoint(97.91416757399878, 118.06433657814753, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.41756584896766, 118.39391521350316, 0.0), APoint(100.41756584896766, 118.39391521350316, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.20488521941562, 118.89252526778375, 0.0), APoint(104.20488521941562, 118.89252526778375, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.99244239467919, 115.57324419962782, 0.0), APoint(78.99244239467919, 115.57324419962782, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.30794616163035, 116.40469604406955, 0.0), APoint(85.30794616163035, 116.40469604406955, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.81134443659923, 116.73427467942518, 0.0), APoint(87.81134443659923, 116.73427467942518, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.28347219957882, 114.12021945932432, 0.0), APoint(95.28347219957882, 114.12021945932432, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.7868704745477, 114.44979809467995, 0.0), APoint(97.7868704745477, 114.44979809467995, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.57418984499566, 114.94840814896054, 0.0), APoint(101.57418984499566, 114.94840814896054, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.88969361194683, 115.77985999340227, 0.0), APoint(107.88969361194683, 115.77985999340227, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(110.3930918869157, 116.1094386287579, 0.0), APoint(110.3930918869157, 116.1094386287579, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.18041125736366, 116.60804868303849, 0.0), APoint(114.18041125736366, 116.60804868303849, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.07468473042323, 120.87032367323339, 0.0), APoint(104.07468473042323, 120.87032367323339, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.80378619458659, 115.30927272684376, 0.0), APoint(112.80378619458659, 115.30927272684376, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.91226480911881, 113.9660237059767, 0.0), APoint(114.91226480911881, 113.9660237059767, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.73646036869965, 121.09587239057683, 0.0), APoint(98.73646036869965, 121.09587239057683, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.46556183286302, 115.5348214441872, 0.0), APoint(107.46556183286302, 115.5348214441872, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(109.57404044739523, 114.19157242332014, 0.0), APoint(109.57404044739523, 114.19157242332014, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.39823600697551, 121.32142110792084, 0.0), APoint(93.39823600697551, 121.32142110792084, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.12733747113887, 115.76037016153121, 0.0), APoint(102.12733747113887, 115.76037016153121, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.23581608567109, 114.41712114066415, 0.0), APoint(104.23581608567109, 114.41712114066415, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.06001164525111, 121.5469698252645, 0.0), APoint(88.06001164525111, 121.5469698252645, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.78911310941444, 115.9859188788748, 0.0), APoint(96.78911310941444, 115.9859188788748, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.89759172394666, 114.64266985800774, 0.0), APoint(98.89759172394666, 114.64266985800774, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.45088874769036, 116.21146759621904, 0.0), APoint(91.45088874769036, 116.21146759621904, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.55936736222257, 114.86821857535197, 0.0), APoint(93.55936736222257, 114.86821857535197, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.72178728352694, 121.77251854260858, 0.0), APoint(82.72178728352694, 121.77251854260858, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.3835629218034, 121.9980672599522, 0.0), APoint(77.3835629218034, 121.9980672599522, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.11266438596668, 116.43701631356248, 0.0), APoint(86.11266438596668, 116.43701631356248, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.2211430004989, 115.09376729269542, 0.0), APoint(88.2211430004989, 115.09376729269542, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.04533856007913, 122.22361597729612, 0.0), APoint(72.04533856007913, 122.22361597729612, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.77444002424251, 116.66256503090642, 0.0), APoint(80.77444002424251, 116.66256503090642, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.88291863877473, 115.31931601003936, 0.0), APoint(82.88291863877473, 115.31931601003936, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.70711419835489, 122.44916469463996, 0.0), APoint(66.70711419835489, 122.44916469463996, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.43621566251825, 116.88811374825033, 0.0), APoint(75.43621566251825, 116.88811374825033, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.54469427705047, 115.54486472738327, 0.0), APoint(77.54469427705047, 115.54486472738327, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.36888983663051, 122.67471341198367, 0.0), APoint(61.36888983663051, 122.67471341198367, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.09799130079386, 117.11366246559405, 0.0), APoint(70.09799130079386, 117.11366246559405, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.20646991532608, 115.77041344472698, 0.0), APoint(72.20646991532608, 115.77041344472698, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.03066547490686, 122.90026212932709, 0.0), APoint(56.03066547490686, 122.90026212932709, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.75976693907023, 117.33921118293746, 0.0), APoint(64.75976693907023, 117.33921118293746, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.86824555360245, 115.9959621620704, 0.0), APoint(66.86824555360245, 115.9959621620704, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.42154257734606, 117.5647599002815, 0.0), APoint(59.42154257734606, 117.5647599002815, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.53002119187828, 116.22151087941444, 0.0), APoint(61.53002119187828, 116.22151087941444, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.08331821562175, 117.79030861762529, 0.0), APoint(54.08331821562175, 117.79030861762529, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.19179683015397, 116.44705959675822, 0.0), APoint(56.19179683015397, 116.44705959675822, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.74509385389756, 118.01585733496928, 0.0), APoint(48.74509385389756, 118.01585733496928, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.853572468429775, 116.67260831410222, 0.0), APoint(50.853572468429775, 116.67260831410222, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.515348106706114, 116.89815703144559, 0.0), APoint(45.515348106706114, 116.89815703144559, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.69782257742992, 116.97038007156776, 0.0), APoint(113.69782257742992, 116.97038007156776, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.05082111381871, 123.13058644897045, 0.0), APoint(100.05082111381871, 123.13058644897045, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.46980953937312, 118.16499842299534, 0.0), APoint(105.46980953937312, 118.16499842299534, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.86596088400601, 115.96933024824445, 0.0), APoint(107.86596088400601, 115.96933024824445, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.21895942039458, 122.12953662564716, 0.0), APoint(94.21895942039458, 122.12953662564716, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.63794784594899, 117.16394859967205, 0.0), APoint(99.63794784594899, 117.16394859967205, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.03409919058188, 114.96828042492116, 0.0), APoint(102.03409919058188, 114.96828042492116, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.56800112229422, 124.62804407777298, 0.0), APoint(84.56800112229422, 124.62804407777298, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.38709772697067, 121.12848680232386, 0.0), APoint(88.38709772697067, 121.12848680232386, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.80608615252498, 116.16289877634874, 0.0), APoint(93.80608615252498, 116.16289877634874, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.20223749715788, 113.96723060159785, 0.0), APoint(96.20223749715788, 113.96723060159785, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.73613942887032, 123.62699425444981, 0.0), APoint(78.73613942887032, 123.62699425444981, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.55523603354676, 120.12743697900069, 0.0), APoint(82.55523603354676, 120.12743697900069, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.97422445910117, 115.16184895302558, 0.0), APoint(87.97422445910117, 115.16184895302558, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.50812639081346, 124.82161260587752, 0.0), APoint(70.50812639081346, 124.82161260587752, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.90427773544636, 122.62594443112663, 0.0), APoint(72.90427773544636, 122.62594443112663, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.7233743401228, 119.1263871556775, 0.0), APoint(76.7233743401228, 119.1263871556775, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.14236276567725, 114.1607991297026, 0.0), APoint(82.14236276567725, 114.1607991297026, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.6762646973899, 123.82056278255467, 0.0), APoint(64.6762646973899, 123.82056278255467, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.0724160420228, 121.62489460780378, 0.0), APoint(67.0724160420228, 121.62489460780378, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.89151264669924, 118.12533733235466, 0.0), APoint(70.89151264669924, 118.12533733235466, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.84440300396611, 122.81951295923149, 0.0), APoint(58.84440300396611, 122.81951295923149, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.24055434859901, 120.6238447844806, 0.0), APoint(61.24055434859901, 120.6238447844806, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.05965095327545, 117.12428750903148, 0.0), APoint(65.05965095327545, 117.12428750903148, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.01254131054214, 121.81846313590836, 0.0), APoint(53.01254131054214, 121.81846313590836, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.408692655175045, 119.62279496115747, 0.0), APoint(55.408692655175045, 119.62279496115747, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.227789259851484, 116.12323768570835, 0.0), APoint(59.227789259851484, 116.12323768570835, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.57683096175115, 118.6217451378344, 0.0), APoint(49.57683096175115, 118.6217451378344, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.39592756642759, 115.12218786238527, 0.0), APoint(53.39592756642759, 115.12218786238527, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.74496926832712, 117.62069531451085, 0.0), APoint(43.74496926832712, 117.62069531451085, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.56406587300356, 114.12113803906173, 0.0), APoint(47.56406587300356, 114.12113803906173, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.73793725451287, 185.53197630978252, 0.0), APoint(173.73793725451287, 191.15796787955037, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.7379372545065, 185.53197630978252, 0.0), APoint(170.7379372545065, 191.15796787955037, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.7379372545065, 190.15796787955037, 0.0), APoint(174.73793725451287, 190.15796787955037, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.73793725451287, 190.15796787955037, 0.0), APoint(177.64031820689513, 190.15796787955037, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.7379372545065, 185.59447630978252, 0.0), APoint(170.7379372545065, 193.787402413657, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(168.48793725451378, 185.59447630978252, 0.0), APoint(168.48793725451378, 193.787402413657, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(171.7379372545065, 192.787402413657, 0.0), APoint(168.48793725451378, 192.787402413657, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(168.48793725451378, 192.787402413657, 0.0), APoint(164.1926991592761, 192.787402413657, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.73793725451287, 181.28197630978252, 0.0), APoint(173.73793725451287, 178.32536677486337, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(168.48793725451378, 181.28197630978252, 0.0), APoint(168.48793725451378, 178.32536677486337, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(174.73793725451287, 179.32536677486337, 0.0), APoint(167.48793725451378, 179.32536677486337, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.73793725451287, 181.28197630978252, 0.0), APoint(173.73793725451287, 176.11240280641073, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.73793725451287, 181.28197630978252, 0.0), APoint(203.73793725451287, 176.11240280641073, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.73793725451287, 177.11240280641073, 0.0), APoint(204.73793725451287, 177.11240280641073, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.73793725451287, 161.15697630978252, 0.0), APoint(173.73793725451287, 164.9018983298581, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(180.74093369071488, 161.15697630978445, 0.0), APoint(180.74093369071488, 164.9018983298581, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.73793725451287, 163.9018983298581, 0.0), APoint(181.74093369071488, 163.9018983298581, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.73793725451287, 161.21947630978252, 0.0), APoint(173.73793725451287, 164.9018983298581, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.23793725451742, 161.21947630979562, 0.0), APoint(160.23793725451742, 164.9018983298581, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(174.73793725451287, 163.9018983298581, 0.0), APoint(159.23793725451742, 163.9018983298581, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.23793725451742, 161.28197630979562, 0.0), APoint(160.23793725451742, 164.9018983298581, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(158.24093369071488, 161.15697630978252, 0.0), APoint(158.24093369071488, 164.9018983298581, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.23793725451742, 163.9018983298581, 0.0), APoint(161.03793725451743, 163.9018983298581, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(158.24093369071488, 163.9018983298581, 0.0), APoint(157.44093369071487, 163.9018983298581, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(167.48793725451384, 182.28197630978258, 0.0), APoint(163.5373854584733, 182.28197630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(169.73793725450656, 184.53197630978258, 0.0), APoint(163.5373854584733, 184.53197630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(164.5373854584733, 182.28197630978258, 0.0), APoint(164.5373854584733, 181.48197630978257, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(164.5373854584733, 184.53197630978258, 0.0), APoint(164.5373854584733, 185.3319763097826, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.035686104473, 184.53197630978255, 0.0), APoint(187.08513430843334, 184.53197630978255, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.035686104473, 187.53197630978278, 0.0), APoint(187.08513430843334, 187.53197630978278, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(188.08513430843334, 184.53197630978255, 0.0), APoint(188.08513430843334, 183.73197630978254, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(188.08513430843334, 187.53197630978278, 0.0), APoint(188.08513430843334, 188.3319763097828, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(159.23793725451748, 160.15697630978258, 0.0), APoint(155.09725785710918, 160.15697630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(167.48793725451384, 184.53197630978258, 0.0), APoint(155.09725785710918, 184.53197630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.09725785710918, 159.15697630978258, 0.0), APoint(156.09725785710918, 171.09447630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.09725785710918, 185.53197630978258, 0.0), APoint(156.09725785710918, 173.59447630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.24093369071494, 160.15697630978258, 0.0), APoint(155.09725785710918, 160.15697630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.24093369070766, 152.65697630978258, 0.0), APoint(155.09725785710918, 152.65697630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.09725785710918, 161.15697630978258, 0.0), APoint(156.09725785710918, 157.65697630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.09725785710918, 151.65697630978258, 0.0), APoint(156.09725785710918, 155.15697630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(158.2409336907076, 151.65697630978252, 0.0), APoint(158.2409336907076, 148.7229991960046, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(180.7409336907076, 151.65697630978252, 0.0), APoint(180.7409336907076, 148.7229991960046, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.2409336907076, 149.7229991960046, 0.0), APoint(181.7409336907076, 149.7229991960046, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.73793725451287, 181.28197630978252, 0.0), APoint(203.73793725451287, 176.11240280641073, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.8879372545107, 181.28197630978252, 0.0), APoint(209.8879372545107, 176.11240280641073, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(202.73793725451287, 177.11240280641073, 0.0), APoint(210.8879372545107, 177.11240280641073, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(213.56293725450723, 161.15697630978252, 0.0), APoint(213.56293725450723, 165.0855853186988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.0629372545145, 161.15697630978252, 0.0), APoint(200.0629372545145, 165.0855853186988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(214.56293725450723, 164.0855853186988, 0.0), APoint(199.0629372545145, 164.0855853186988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.0629372545145, 161.15697630978252, 0.0), APoint(200.0629372545145, 165.0855853186988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(195.18793725451087, 161.15697630978252, 0.0), APoint(195.18793725451087, 165.0855853186988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(201.0629372545145, 164.0855853186988, 0.0), APoint(194.18793725451087, 164.0855853186988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(213.56293725450723, 161.15697630978252, 0.0), APoint(213.56293725450723, 165.0855853186988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.43793725451087, 161.15697630978252, 0.0), APoint(218.43793725451087, 165.0855853186988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(212.56293725450723, 164.0855853186988, 0.0), APoint(219.43793725451087, 164.0855853186988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.43793725451098, 160.15697630978258, 0.0), APoint(223.21060531336775, 160.15697630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.43793725451098, 152.65697630978258, 0.0), APoint(223.21060531336775, 152.65697630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.21060531336775, 161.15697630978258, 0.0), APoint(222.21060531336775, 157.65697630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.21060531336775, 151.65697630978258, 0.0), APoint(222.21060531336775, 155.15697630978258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(195.18793725451087, 151.65697630978252, 0.0), APoint(195.18793725451087, 148.08176703999038, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.43793725451087, 151.65697630978252, 0.0), APoint(218.43793725451087, 148.08176703999038, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.18793725451087, 149.08176703999038, 0.0), APoint(219.43793725451087, 149.08176703999038, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(137.32301469314183, 175.35740502962733, 0.0), APoint(140.73153008983317, 181.2611268750778, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.07301469313731, 192.82225067261533, 0.0), APoint(110.48153008982861, 198.72597251806573, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(141.09755549361765, 179.89510147129334, 0.0), APoint(109.11550468604419, 198.35994711428125, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.07301469314005, 259.0901998650466, 0.0), APoint(45.29413390984938, 254.2770371602105, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(17.823014693139143, 276.5550455080339, 0.0), APoint(15.044133909848483, 271.7418828031978, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.66015931363383, 254.64306256399493, 0.0), APoint(14.678108506064078, 273.1079082069823, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.07301469313916, 192.82225067261413, 0.0), APoint(44.279511117826075, 199.39279160375034, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(17.823014693139157, 175.35740502962733, 0.0), APoint(14.029511117826075, 181.92794596076354, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.64553652161051, 199.02676619996595, 0.0), APoint(13.663485714041656, 180.56192055697912, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(25.90553028255681, 84.6705178623522, 0.0), APoint(25.90553028255681, 81.51599936022717, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695813, 84.6705178623522, 0.0), APoint(77.72399283695813, 81.51599936022717, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.90553028255681, 82.51599936022717, 0.0), APoint(78.72399283695813, 82.51599936022717, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695813, 84.6080178623522, 0.0), APoint(77.72399283695813, 81.51599936022717, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(129.3305340322754, 85.18764288110106, 0.0), APoint(129.3305340322754, 81.51599936022717, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.72399283695813, 82.51599936022717, 0.0), APoint(130.3305340322754, 82.51599936022717, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(25.90553028255681, 77.17014287172697, 0.0), APoint(25.90553028255681, 72.66976331948877, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(129.3305340322754, 78.20439290922445, 0.0), APoint(129.3305340322754, 72.66976331948877, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.90553028255681, 73.66976331948877, 0.0), APoint(130.3305340322754, 73.66976331948877, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 108.34882410157047, 0.0), APoint(34.118032157416565, 98.4448981246405, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.1180321574152, 109.24882410157056, 0.0), APoint(121.1180321574152, 98.4448981246405, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.118032157416565, 99.4448981246405, 0.0), APoint(122.1180321574152, 99.4448981246405, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(27.405530282553173, 86.7897678998495, 0.0), APoint(27.405530282553173, 96.53422367574218, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(25.90553028255681, 86.6705178623522, 0.0), APoint(25.90553028255681, 96.53422367574218, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.405530282553173, 95.53422367574218, 0.0), APoint(25.90553028255681, 95.53422367574218, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(25.90553028255681, 95.53422367574218, 0.0), APoint(17.61029218731872, 95.53422367574218, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.84454949240836, 8.75380994126612, 0.0), APoint(93.0458950890897, 7.308363672899377, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.96769339567963, 8.714744321903012, 0.0), APoint(95.00095674294923, 7.542761624139223, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(93.00679424238467, 8.011553997401208, 0.0), 0.7042765853597772, 1.6263440515008603, 4.7679367050899675)
entity.Color = 1

entity = acad.model.AddCircle(APoint(157.1216043330005, 13.765197280705252, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(157.14024835264354, 12.55487387757421, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(198.65312747755888, 13.608239394461975, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(198.67177149720192, 12.397915991330933, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(320.8364129777301, 7.868212973627691, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(320.85505699737314, 6.65788957049665, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(287.5198035687728, 23.360720553618, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(287.5328543825229, 22.51349417142627, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(240.22373963735686, 13.477188212659712, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(240.2423836569999, 12.26686480952867, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(281.8444881512452, 13.360720553618, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(281.8575389649953, 12.51349417142627, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(323.69733720395845, 23.360720553618, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(323.71038801770857, 22.51349417142627, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(158.05234717831354, 23.765197280705266, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(158.07099119795657, 22.554873877574224, 0.0), 0.2655928118261954)
entity.Color = 7

# Entity type AcDbSolid not supported
entity = acad.model.AddLine(APoint(177.6660265314331, 98.92379186092647, 0.0), APoint(181.6660265314331, 98.92379186092647, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.6660265314331, 98.92379186092647, 0.0), APoint(181.6660265314331, 100.92379186092647, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.6660265314331, 100.92379186092647, 0.0), APoint(177.6660265314331, 100.92379186092647, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.6660265314331, 100.92379186092647, 0.0), APoint(177.6660265314331, 98.92379186092647, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.577739485665, 105.3836332674214, 0.0), APoint(151.75701778460007, 105.3836332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.8574119741279, 104.6336332674214, 0.0), APoint(152.6074119741279, 104.6336332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.3574119741279, 104.6336332674214, 0.0), APoint(154.1074119741279, 104.6336332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.1074119741279, 103.8836332674214, 0.0), APoint(151.8574119741279, 103.8836332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.6074119741279, 103.8836332674214, 0.0), APoint(153.3574119741279, 103.8836332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.1074119741279, 103.8836332674214, 0.0), APoint(154.8574119741279, 103.8836332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.6074119741279, 103.8836332674214, 0.0), APoint(156.3574119741279, 103.8836332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.1074119741279, 103.8836332674214, 0.0), APoint(157.77318918490164, 103.8836332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.3574119741279, 103.1336332674214, 0.0), APoint(154.1074119741279, 103.1336332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.8574119741279, 103.1336332674214, 0.0), APoint(155.6074119741279, 103.1336332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.3574119741279, 103.1336332674214, 0.0), APoint(157.1074119741279, 103.1336332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.0131890827679, 102.3836332674214, 0.0), APoint(156.3574119741279, 102.3836332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.1074119741279, 102.3836332674214, 0.0), APoint(157.41251378942434, 102.3836332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.8574119741279, 104.9148832674214, 0.0), APoint(152.6074119741279, 104.9148832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.3574119741279, 104.9148832674214, 0.0), APoint(153.63707134719425, 104.9148832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.13220087731588, 104.1648832674214, 0.0), APoint(151.8574119741279, 104.1648832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.6074119741279, 104.1648832674214, 0.0), APoint(153.3574119741279, 104.1648832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.1074119741279, 104.1648832674214, 0.0), APoint(154.8574119741279, 104.1648832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.6074119741279, 104.1648832674214, 0.0), APoint(156.3574119741279, 104.1648832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.8770712450587, 103.4148832674214, 0.0), APoint(152.6074119741279, 103.4148832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.3574119741279, 103.4148832674214, 0.0), APoint(154.1074119741279, 103.4148832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.8574119741279, 103.4148832674214, 0.0), APoint(155.6074119741279, 103.4148832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.3574119741279, 103.4148832674214, 0.0), APoint(157.1074119741279, 103.4148832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.6074119741279, 102.6648832674214, 0.0), APoint(156.3574119741279, 102.6648832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.1074119741279, 102.6648832674214, 0.0), APoint(157.5162356740475, 102.6648832674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.8574119741279, 105.1961332674214, 0.0), APoint(152.5090392096372, 105.1961332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.23501747924274, 104.4461332674214, 0.0), APoint(151.8574119741279, 104.4461332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.6074119741279, 104.4461332674214, 0.0), APoint(153.3574119741279, 104.4461332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.1074119741279, 104.4461332674214, 0.0), APoint(154.8574119741279, 104.4461332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(150.96083987410566, 103.6961332674214, 0.0), APoint(151.1074119741279, 103.6961332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.8574119741279, 103.6961332674214, 0.0), APoint(152.6074119741279, 103.6961332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.3574119741279, 103.6961332674214, 0.0), APoint(154.1074119741279, 103.6961332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.8574119741279, 103.6961332674214, 0.0), APoint(155.6074119741279, 103.6961332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.3574119741279, 103.6961332674214, 0.0), APoint(157.1074119741279, 103.6961332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.8574119741279, 103.6961332674214, 0.0), APoint(157.89654925100058, 103.6961332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.1074119741279, 102.9461332674214, 0.0), APoint(154.8574119741279, 102.9461332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.6074119741279, 102.9461332674214, 0.0), APoint(156.3574119741279, 102.9461332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.1074119741279, 102.9461332674214, 0.0), APoint(157.61995755867156, 102.9461332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.76521050780593, 102.1961332674214, 0.0), APoint(157.1074119741279, 102.1961332674214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.2011619741279, 103.58340637604583, 0.0), APoint(151.2011619741279, 103.78988326742187, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.9511619741279, 103.7898832674217, 0.0), APoint(151.9511619741279, 104.5398832674217, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.9511619741279, 105.2898832674217, 0.0), APoint(151.9511619741279, 105.33522768438239, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.7011619741279, 103.20941437178108, 0.0), APoint(152.7011619741279, 103.78988326742156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.7011619741279, 104.53988326742156, 0.0), APoint(152.7011619741279, 105.14823168225003, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.4511619741279, 103.02241836964869, 0.0), APoint(153.4511619741279, 103.03988326742139, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.4511619741279, 103.78988326742139, 0.0), APoint(153.4511619741279, 104.53988326742139, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.2011619741279, 103.03988326742213, 0.0), APoint(154.2011619741279, 103.78988326742213, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.2011619741279, 104.53988326742213, 0.0), APoint(154.2011619741279, 104.77423967798616, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.9511619741279, 102.64842636538391, 0.0), APoint(154.9511619741279, 103.03988326742196, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.9511619741279, 103.78988326742196, 0.0), APoint(154.9511619741279, 104.53988326742196, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.7011619741279, 103.03988326742179, 0.0), APoint(155.7011619741279, 103.78988326742179, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.4511619741279, 102.28988326742162, 0.0), APoint(156.4511619741279, 103.03988326742162, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.4511619741279, 103.78988326742162, 0.0), APoint(156.4511619741279, 104.21325167158808, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.2011619741279, 102.08743835898674, 0.0), APoint(157.2011619741279, 102.28988326742144, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.2011619741279, 103.03988326742144, 0.0), APoint(157.2011619741279, 103.78988326742144, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.4824119741279, 103.51328287524616, 0.0), APoint(151.4824119741279, 103.78988326742224, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.4824119741279, 104.53988326742224, 0.0), APoint(151.4824119741279, 105.12286932349294, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.2324119741279, 103.7898832674221, 0.0), APoint(152.2324119741279, 104.5398832674221, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.9824119741279, 103.13929087098141, 0.0), APoint(152.9824119741279, 103.78988326742193, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.9824119741279, 104.53988326742193, 0.0), APoint(152.9824119741279, 105.07810818145036, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.7324119741279, 102.95229486884905, 0.0), APoint(153.7324119741279, 103.03988326742179, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.7324119741279, 103.78988326742179, 0.0), APoint(153.7324119741279, 104.53988326742179, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.4824119741279, 103.03988326742162, 0.0), APoint(154.4824119741279, 103.78988326742162, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.4824119741279, 104.53988326742162, 0.0), APoint(154.4824119741279, 104.70411617718561, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.2324119741279, 102.57830286458427, 0.0), APoint(155.2324119741279, 103.03988326742144, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.2324119741279, 103.78988326742144, 0.0), APoint(155.2324119741279, 104.51712017505322, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.9824119741279, 103.03988326742218, 0.0), APoint(155.9824119741279, 103.78988326742218, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.7324119741279, 102.28988326742201, 0.0), APoint(156.7324119741279, 103.03988326742201, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.7324119741279, 103.78988326742201, 0.0), APoint(156.7324119741279, 104.14312817078844, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.4824119741279, 103.03988326742139, 0.0), APoint(157.4824119741279, 103.78988326742139, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.0136619741279, 103.7898832674219, 0.0), APoint(151.0136619741279, 103.8406256485451, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.7636619741279, 103.44315937444652, 0.0), APoint(151.7636619741279, 103.78988326742173, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.7636619741279, 104.53988326742173, 0.0), APoint(151.7636619741279, 105.28988326742173, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.5136619741279, 103.78988326742156, 0.0), APoint(152.5136619741279, 104.53988326742156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.2636619741279, 103.06916737018177, 0.0), APoint(153.2636619741279, 103.78988326742142, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.2636619741279, 104.53988326742142, 0.0), APoint(153.2636619741279, 105.00798468065072, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.0136619741279, 102.88217136804938, 0.0), APoint(154.0136619741279, 103.03988326742216, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.0136619741279, 103.78988326742216, 0.0), APoint(154.0136619741279, 104.53988326742216, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.7636619741279, 103.03988326742201, 0.0), APoint(154.7636619741279, 103.78988326742201, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.7636619741279, 104.53988326742201, 0.0), APoint(154.7636619741279, 104.63399267638597, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.5136619741279, 102.50817936378463, 0.0), APoint(155.5136619741279, 103.03988326742184, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.5136619741279, 103.78988326742184, 0.0), APoint(155.5136619741279, 104.44699667425358, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.2636619741279, 103.03988326742167, 0.0), APoint(156.2636619741279, 103.78988326742167, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.0136619741279, 102.2898832674215, 0.0), APoint(157.0136619741279, 103.0398832674215, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.0136619741279, 103.7898832674215, 0.0), APoint(157.0136619741279, 104.0730046699888, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.7636619741279, 103.33579902594381, 0.0), APoint(157.7636619741279, 103.7898832674219, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.58269319810015, 58.9237918609265, 0.0), APoint(197.13966726554486, 58.9237918609265, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.58269319810015, 48.923791860926485, 0.0), APoint(197.13966726554486, 48.923791860926485, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.13966726554486, 59.9237918609265, 0.0), APoint(196.13966726554486, 55.17379186092649, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.13966726554486, 47.92379186092648, 0.0), APoint(196.13966726554486, 52.67379186092649, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319810006, 47.92379186092646, 0.0), APoint(160.58269319810006, 43.43974908911011, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.58269319810006, 47.92379186092646, 0.0), APoint(191.58269319810006, 43.43974908911011, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(159.58269319810006, 44.43974908911011, 0.0), APoint(192.58269319810006, 44.43974908911011, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('1', APoint(165.85453237145967, 81.52144430895298, 0.0), 1.85)
entity.Color = 1

entity = acad.model.AddText('3', APoint(163.78766794529193, 79.14044925248044, 0.0), 1.85)
entity.Color = 1

entity = acad.model.AddLine(APoint(159.58269319810012, 58.9237918609265, 0.0), APoint(158.120222630938, 58.9237918609265, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(176.66602653143315, 98.92379186092653, 0.0), APoint(158.12022263093797, 98.92379186092651, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(159.120222630938, 57.9237918609265, 0.0), APoint(159.12022263093797, 77.6737918609265, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(159.12022263093797, 99.92379186092651, 0.0), APoint(159.12022263093797, 80.1737918609265, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.66602653143315, 100.92379186092653, 0.0), APoint(189.80128000321565, 100.92379186092653, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.66602653143315, 98.92379186092653, 0.0), APoint(189.80128000321565, 98.92379186092653, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(188.80128000321565, 101.92379186092653, 0.0), APoint(188.80128000321565, 97.92379186092653, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.6660265314331, 101.92379186092647, 0.0), APoint(177.6660265314331, 105.09097843329911, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 99.92379186092647, 0.0), APoint(181.16602653143218, 105.09097843329911, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(176.6660265314331, 104.09097843329911, 0.0), APoint(182.16602653143218, 104.09097843329911, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 97.92379186092647, 0.0), APoint(181.16602653143218, 92.54065940423388, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.6660265314331, 97.92379186092647, 0.0), APoint(181.6660265314331, 92.54065940423388, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 93.54065940423388, 0.0), APoint(180.36602653143217, 93.54065940423388, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.6660265314331, 93.54065940423388, 0.0), APoint(182.4660265314331, 93.54065940423388, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.58269319810006, 59.92379186092647, 0.0), APoint(191.58269319810006, 65.38120553987594, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 59.92379186092647, 0.0), APoint(181.16602653143218, 65.38120553987594, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.58269319810006, 64.38120553987594, 0.0), APoint(180.16602653143218, 64.38120553987594, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.109858773184, 98.92379186092668, 0.0), APoint(161.3949365134259, 98.92379186092671, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(176.10985877319223, 98.92379186092668, 0.0), 13.714922259766311, 2.897246558310589, 3.1415926535897913)
entity.Color = 8

entity = acad.model.AddLine(APoint(181.16602653143218, 59.92379186092647, 0.0), APoint(181.16602653143218, 65.38120553987594, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319810006, 59.92379186092647, 0.0), APoint(160.58269319810006, 65.38120553987594, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.16602653143218, 64.38120553987594, 0.0), APoint(159.58269319810006, 64.38120553987594, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.1660265314331, 95.67379186092646, 0.0), APoint(173.1660265314331, 88.96899617366168, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143218, 95.67379186092646, 0.0), APoint(181.16602653143218, 88.96899617366168, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.1660265314331, 89.96899617366168, 0.0), APoint(182.16602653143218, 89.96899617366168, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.9888556250251, 197.19044929798312, 0.0), APoint(219.06712011231141, 197.19044929798312, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.06712011231141, 198.19044929798312, 0.0), APoint(218.06712011231141, 193.61121280388298, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.06712011231144, 186.5319763097828, 0.0), APoint(218.06712011231144, 191.11121280388295, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(315.02616751990627, 102.50922931983376, 0.0), APoint(315.02616751990263, 116.70922931975423, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(314.4261675199015, 116.70922931975302, 0.0), 0.6000000000011028, 2.0132044179832503e-12, 1.5707963267966967)
entity.Color = 6

entity = acad.model.AddLine(APoint(314.42616751990045, 117.30922931975414, 0.0), APoint(311.02616751991627, 117.30922931975414, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(311.0261675199152, 116.709229319753, 0.0), 0.6000000000011312, 1.5707963267930967, 3.1415926535862404)
entity.Color = 6

entity = acad.model.AddLine(APoint(310.4261675199141, 116.70922931975514, 0.0), APoint(310.42616751988953, 103.10922931983549, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(311.0261675198906, 103.1092293198355, 0.0), 0.6000000000010459, 3.1415926535898167, 4.712388980386584)
entity.Color = 6

entity = acad.model.AddLine(APoint(311.0261675198917, 102.50922931983445, 0.0), APoint(322.6261675197993, 102.50922931983263, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(322.62616751979823, 103.10922931983136, 0.0), 0.5999999999987295, 4.712388980386489, 1.9658349022738197e-12)
entity.Color = 6

entity = acad.model.AddLine(APoint(323.22616751979695, 103.10922931983254, 0.0), APoint(323.22616751979695, 106.70922931983358, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(322.62616751979795, 106.70922931983449, 0.0), 0.5999999999989996, 6.28318530717807, 1.5707963267926228)
entity.Color = 6

entity = acad.model.AddLine(APoint(322.6261675197993, 107.30922931983349, 0.0), APoint(310.42616751990045, 107.30922931984281, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 107.9092293197863, 0.0), APoint(316.02616751969526, 107.9092293197861, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(316.02616751969526, 107.9092293197861, 0.0), APoint(316.02616751969526, 117.9092293197861, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(316.02616751969526, 117.9092293197861, 0.0), APoint(377.74293745552313, 117.9092293197861, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.28893645538756, 117.9092293197861, 0.0), APoint(403.4582339857425, 117.9092293197861, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.4582339857425, 117.9092293197861, 0.0), APoint(403.4582339857425, 107.90922931978656, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.4582339857425, 107.90922931978656, 0.0), APoint(379.28893645538756, 107.90922931978656, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.82616751968453, 107.9092293197861, 0.0), APoint(323.82616751968453, 101.90922931978612, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.82616751968453, 101.90922931978612, 0.0), APoint(309.8261675197409, 101.90922931975427, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(309.8261675197409, 101.90922931975427, 0.0), APoint(309.8261675197127, 117.9092293197861, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(309.8261675197127, 117.9092293197861, 0.0), APoint(315.62616751967107, 117.9092293197861, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(315.62616751967107, 117.9092293197861, 0.0), APoint(315.62616751967107, 107.90922931978656, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(315.62616751967107, 107.90922931978656, 0.0), APoint(323.82616751968453, 107.9092293197861, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.28893645538756, 103.95971744011439, 0.0), APoint(379.28893645538756, 112.33496075359716, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.28893645538756, 112.33496075359716, 0.0), APoint(378.53893645538756, 112.83496075359716, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(378.53893645538756, 112.83496075359716, 0.0), APoint(380.03893645538756, 113.33496075359716, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(380.03893645538756, 113.33496075359716, 0.0), APoint(379.28893645538756, 113.83496075359716, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.28893645538756, 113.83496075359716, 0.0), APoint(379.28893645538756, 121.73398451294128, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 103.95971744011439, 0.0), APoint(377.74293745552313, 112.33496075359716, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 112.33496075359716, 0.0), APoint(376.99293745552313, 112.83496075359716, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(376.99293745552313, 112.83496075359716, 0.0), APoint(378.49293745552404, 113.33496075359716, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(378.49293745552404, 113.33496075359716, 0.0), APoint(377.74293745552313, 113.83496075359716, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 113.83496075359716, 0.0), APoint(377.74293745552313, 121.73398451294128, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 108.9092293197861, 0.0), APoint(341.7414640499137, 108.9092293197861, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.658233985715, 113.50922931978602, 0.0), APoint(402.65823398576595, 116.30922931977597, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(402.0582339857667, 116.3092293197869, 0.0), 0.5999999999992269, 6.283185307161372, 1.5707963267937597)
entity.Color = 6

entity = acad.model.AddLine(APoint(402.0582339857674, 116.9092293197861, 0.0), APoint(379.4889364553883, 116.9092293197861, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('O10@30', APoint(309.70869566330225, 96.54098408111153, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('8010', APoint(331.14291902084756, 101.50514907458171, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('T', APoint(332.25142306120733, 101.44202302073836, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('1', APoint(314.2010857431253, 121.44450438005941, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('2', APoint(398.23795611015754, 121.94554824788855, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('4', APoint(331.1789180816436, 125.04861362307014, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('5', APoint(376.65720264953984, 125.78539616138335, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('3', APoint(376.52962994965816, 100.12386259303452, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('T', APoint(309.9194086696342, 96.52737448650805, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('7', APoint(307.10107082356785, 95.75744405432025, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('6', APoint(338.40945256743544, 100.66362600927204, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddLine(APoint(262.88194279048, 109.32951951664361, 0.0), APoint(262.88194279048, 112.45507762080139, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(273.3819427904791, 109.32951951664361, 0.0), APoint(273.3819427904791, 112.45507762080139, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(261.88194279048, 111.45507762080139, 0.0), APoint(266.10813326667005, 111.45507762080139, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(274.3819427904791, 111.45507762080139, 0.0), APoint(270.1557523142891, 111.45507762080139, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(261.88194279048014, 101.42951951664517, 0.0), APoint(256.1028857894719, 101.42951951664517, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(262.4819427904787, 108.92951951664517, 0.0), APoint(256.1028857894719, 108.92951951664517, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(257.1028857894719, 100.42951951664517, 0.0), APoint(257.1028857894719, 104.17951951664517, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(257.1028857894719, 109.92951951664517, 0.0), APoint(257.1028857894719, 106.17951951664517, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(262.88194279048, 100.42951951664512, 0.0), APoint(262.88194279048, 96.94256900027156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.38194279048, 100.42951951664512, 0.0), APoint(264.38194279048, 96.94256900027156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.38194279048, 97.94256900027156, 0.0), APoint(261.88194279048, 97.94256900027156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(262.88194279048, 97.94256900027156, 0.0), APoint(259.92003802857414, 97.94256900027156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

# Entity type AcDbSolid not supported
entity = acad.model.AddText('2*2cm', APoint(277.1475659677627, 112.7081938598399, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('O10@30', APoint(257.88308480359433, 90.00789848718912, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('T', APoint(258.06632227710804, 90.01541583730386, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('9', APoint(254.39102095764804, 89.32380914433023, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('3O10', APoint(275.70291291858223, 105.05736242607102, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('T', APoint(277.0696950391623, 105.0017734024085, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('8', APoint(282.6724423472338, 104.28880328759922, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddLine(APoint(240.76434785080812, 104.43374477229051, 0.0), APoint(244.32244825006933, 104.43374477229051, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.79434635092105, 101.43389476104073, 0.0), APoint(244.32244825006933, 101.43389476104073, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.32244825006933, 104.43374477229051, 0.0), APoint(243.32244825006933, 105.2337447722905, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.32244825006933, 101.43389476104073, 0.0), APoint(243.32244825006933, 100.63389476104074, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.76434785080812, 101.4335947760396, 0.0), APoint(244.32244825006933, 101.4335947760396, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.76434785080812, 95.28329478353993, 0.0), APoint(244.32244825006933, 95.28329478353993, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.32244825006933, 102.4335947760396, 0.0), APoint(243.32244825006933, 99.35844477978978, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.32244825006933, 94.28329478353993, 0.0), APoint(243.32244825006933, 97.35844477978978, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.764347850808, 100.43359477603954, 0.0), APoint(239.764347850808, 91.77479212159867, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.764347850808, 100.40359477603889, 0.0), APoint(236.764347850808, 91.77479212159867, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.764347850808, 92.77479212159867, 0.0), APoint(240.56434785080802, 92.77479212159867, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.764347850808, 92.77479212159867, 0.0), APoint(235.964347850808, 92.77479212159867, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.764347850808, 94.2832947835399, 0.0), APoint(236.764347850808, 91.77479212159867, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.764347850808, 100.28359477603627, 0.0), APoint(224.764347850808, 91.77479212159867, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.764347850808, 92.77479212159867, 0.0), APoint(233.02625261271277, 92.77479212159867, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.764347850808, 92.77479212159867, 0.0), APoint(228.50244308890325, 92.77479212159867, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('8010', APoint(384.3298232010568, 101.58479733322625, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('T', APoint(385.4424978159034, 101.5528047732995, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('12', APoint(381.0323550316243, 100.94901329663003, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('11', APoint(387.1372743358829, 94.76354725967386, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.54665725483596, 91.02056675343002, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('13', APoint(412.22225568500403, 97.73199769922722, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('010@30', APoint(402.9516031866146, 98.38776100375878, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('T', APoint(402.8603217771745, 98.40580311475412, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(400.1924045167534, 214.91126186483007, 0.0), APoint(400.81162047366433, 215.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 213.9831842145229, 0.0), APoint(401.7396981239715, 215.53047782174121, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 213.05510656421552, 0.0), APoint(402.66777577427865, 215.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 212.12702891390813, 0.0), APoint(403.5958534245858, 215.53047782174076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 211.19895126360075, 0.0), APoint(404.5239310748932, 215.53047782174076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 210.27087361329336, 0.0), APoint(405.4520087252006, 215.53047782174076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755082, 209.530477821741, 0.0), APoint(406.380086375508, 215.53047782174076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258156, 209.530477821741, 0.0), APoint(407.30816402581536, 215.53047782174076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.236241676123, 209.530477821741, 0.0), APoint(408.236241676123, 215.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.16431932643036, 209.530477821741, 0.0), APoint(408.44240451675023, 214.80856301206086, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767375, 209.53047782174076, 0.0), APoint(408.4424045167509, 213.88048536175415, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270447, 209.530477821741, 0.0), APoint(408.4424045167509, 212.95240771144722, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735206, 209.530477821741, 0.0), APoint(408.4424045167516, 212.02433006114052, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765945, 209.530477821741, 0.0), APoint(408.4424045167523, 211.0962524108338, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796684, 209.530477821741, 0.0), APoint(408.44240451675273, 210.16817476052688, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167534, 208.91126186483007, 0.0), APoint(400.81162047366433, 209.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 207.9831842145229, 0.0), APoint(401.7396981239715, 209.53047782174121, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 207.05510656421552, 0.0), APoint(402.66777577427865, 209.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 206.12702891390813, 0.0), APoint(403.5958534245858, 209.53047782174076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 205.19895126360075, 0.0), APoint(404.5239310748932, 209.53047782174076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167532, 204.27087361329336, 0.0), APoint(405.4520087252006, 209.53047782174076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755082, 203.530477821741, 0.0), APoint(406.380086375508, 209.53047782174076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258156, 203.530477821741, 0.0), APoint(407.30816402581536, 209.53047782174076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.236241676123, 203.530477821741, 0.0), APoint(408.236241676123, 209.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.16431932643036, 203.530477821741, 0.0), APoint(408.44240451675023, 208.80856301206086, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767375, 203.53047782174076, 0.0), APoint(408.4424045167509, 207.88048536175415, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270447, 203.530477821741, 0.0), APoint(408.4424045167509, 206.95240771144722, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735206, 203.530477821741, 0.0), APoint(408.4424045167516, 206.02433006114052, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765945, 203.530477821741, 0.0), APoint(408.4424045167523, 205.0962524108338, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796684, 203.530477821741, 0.0), APoint(408.44240451675273, 204.16817476052688, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 202.9112618648296, 0.0), APoint(400.81162047366433, 203.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 201.98318421452268, 0.0), APoint(401.7396981239715, 203.53047782174121, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 201.0551065642153, 0.0), APoint(402.66777577427865, 203.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 200.1270289139079, 0.0), APoint(403.59585342458604, 203.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 199.19895126360052, 0.0), APoint(404.5239310748934, 203.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675296, 198.27087361329313, 0.0), APoint(405.4520087252008, 203.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755084, 197.53047782174121, 0.0), APoint(406.3800863755082, 203.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258158, 197.53047782174121, 0.0), APoint(407.3081640258156, 203.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761232, 197.53047782174121, 0.0), APoint(408.236241676123, 203.530477821741, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264306, 197.53047782174121, 0.0), APoint(408.44240451675, 202.80856301206063, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.092396976738, 197.53047782174121, 0.0), APoint(408.4424045167507, 201.88048536175393, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.02047462704513, 197.53047782174144, 0.0), APoint(408.4424045167507, 200.952407711447, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.9485522773525, 197.53047782174144, 0.0), APoint(408.4424045167516, 200.02433006114052, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765945, 197.530477821741, 0.0), APoint(408.4424045167523, 199.0962524108338, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796684, 197.530477821741, 0.0), APoint(408.44240451675273, 198.16817476052688, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(192.2083934237562, 22.974567684367344, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(192.22703744339924, 21.7642442812363, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddLine(APoint(29.09123173051739, 223.71035349895288, 0.0), APoint(72.67187959516767, 223.71035349895288, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.67187959516767, 223.71035349895288, 0.0), APoint(74.0888664520713, 225.83583378430836, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.0888664520713, 225.83583378430836, 0.0), APoint(75.50585330897493, 221.5848732135974, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.50585330897493, 221.5848732135974, 0.0), APoint(76.92284016587857, 223.71035349895288, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.92284016587857, 223.71035349895288, 0.0), APoint(126.16758664598503, 223.7103534989529, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(29.091231730517393, 228.091674026141, 0.0), APoint(72.67187959516767, 228.091674026141, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.67187959516767, 228.091674026141, 0.0), APoint(74.0888664520713, 230.21715431149647, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.0888664520713, 230.21715431149647, 0.0), APoint(75.50585330897493, 225.9661937407829, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.50585330897493, 225.9661937407829, 0.0), APoint(76.92284016587857, 228.091674026141, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.92284016587857, 228.091674026141, 0.0), APoint(126.16758664598501, 227.8558328025158, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.03958438290385, 146.0322455046006, 0.0), APoint(228.03958438290385, 183.2221194929594, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.03958438290385, 183.2221194929594, 0.0), APoint(226.05367029280978, 184.54606221968874, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.05367029280978, 184.54606221968874, 0.0), APoint(230.0254984729978, 185.87000494641813, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(230.0254984729978, 185.87000494641813, 0.0), APoint(228.03958438290385, 187.19394767314748, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.03958438290385, 187.19394767314748, 0.0), APoint(228.03958438290385, 208.10965778203945, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.94595612010107, 146.0322455046006, 0.0), APoint(223.94595612010107, 183.2221194929594, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.94595612010107, 183.2221194929594, 0.0), APoint(221.96004203000712, 184.54606221968874, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.96004203000712, 184.54606221968874, 0.0), APoint(225.93187021019753, 185.87000494641813, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.93187021019753, 185.87000494641813, 0.0), APoint(223.94595612010107, 187.19394767314748, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.94595612010107, 187.19394767314748, 0.0), APoint(223.94595612010107, 208.10965778203945, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W1', APoint(123.27106639246564, 262.44023310035135, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(171.1379372545065, 190.55796787955038, 0.0), APoint(170.3379372545065, 189.75796787955036, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(173.33793725451287, 189.75796787955036, 0.0), APoint(174.13793725451288, 190.55796787955038, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.3', APoint(175.06888963546655, 190.65796787955037, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(170.3379372545065, 192.387402413657, 0.0), APoint(171.1379372545065, 193.187402413657, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(168.8879372545138, 193.187402413657, 0.0), APoint(168.08793725451378, 192.387402413657, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.25', APoint(164.47841344499037, 193.287402413657, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(173.33793725451287, 178.92536677486336, 0.0), APoint(174.13793725451288, 179.72536677486337, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(168.8879372545138, 179.72536677486337, 0.0), APoint(168.08793725451378, 178.92536677486336, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.55', APoint(169.6843658259419, 179.82536677486337, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(174.13793725451288, 177.51240280641073, 0.0), APoint(173.33793725451287, 176.71240280641072, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(203.33793725451287, 176.71240280641072, 0.0), APoint(204.13793725451288, 177.51240280641073, 0.0))
entity.Color = 7


entity = acad.model.AddText('2.0', APoint(187.9522229687986, 177.61240280641073, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(174.13793725451288, 164.30189832985812, 0.0), APoint(173.33793725451287, 163.5018983298581, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(180.34093369071488, 163.5018983298581, 0.0), APoint(181.1409336907149, 164.30189832985812, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.8', APoint(175.84657832975674, 164.4018983298581, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(173.33793725451287, 163.5018983298581, 0.0), APoint(174.13793725451288, 164.30189832985812, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(160.63793725451742, 164.30189832985812, 0.0), APoint(159.8379372545174, 163.5018983298581, 0.0))
entity.Color = 7


entity = acad.model.AddText('1.2', APoint(165.77365154022945, 164.4018983298581, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(160.63793725451742, 164.30189832985812, 0.0), APoint(159.8379372545174, 163.5018983298581, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(157.84093369071488, 163.5018983298581, 0.0), APoint(158.6409336907149, 164.30189832985812, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.0', APoint(158.0608640440447, 164.4018983298581, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(164.9373854584733, 181.88197630978257, 0.0), APoint(164.1373854584733, 182.68197630978258, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(164.1373854584733, 184.93197630978258, 0.0), APoint(164.9373854584733, 184.13197630978257, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.30', APoint(162.0373854584733, 182.65697630978252, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(188.48513430843335, 184.13197630978254, 0.0), APoint(187.68513430843333, 184.93197630978256, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(187.68513430843333, 187.93197630978278, 0.0), APoint(188.48513430843335, 187.13197630978277, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.25', APoint(187.65656287986192, 185.2819763097826, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(155.69725785710918, 160.55697630978258, 0.0), APoint(156.4972578571092, 159.75697630978257, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(156.4972578571092, 184.13197630978257, 0.0), APoint(155.69725785710918, 184.93197630978258, 0.0))
entity.Color = 7


entity = acad.model.AddText('1.8', APoint(155.3115435713949, 171.59447630978252, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(156.4972578571092, 159.75697630978257, 0.0), APoint(155.69725785710918, 160.55697630978258, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(155.69725785710918, 153.05697630978258, 0.0), APoint(156.4972578571092, 152.25697630978257, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.8', APoint(155.02582928568063, 155.65697630978252, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(158.6409336907076, 150.1229991960046, 0.0), APoint(157.8409336907076, 149.3229991960046, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(180.3409336907076, 149.3229991960046, 0.0), APoint(181.1409336907076, 150.1229991960046, 0.0))
entity.Color = 7


entity = acad.model.AddText('2.0', APoint(169.0623622621362, 150.2229991960046, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(204.13793725451288, 177.51240280641073, 0.0), APoint(203.33793725451287, 176.71240280641072, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(209.48793725451068, 176.71240280641072, 0.0), APoint(210.2879372545107, 177.51240280641073, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.6', APoint(205.38436582594036, 178.11240280641073, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(213.16293725450723, 163.6855853186988, 0.0), APoint(213.96293725450724, 164.4855853186988, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(200.46293725451451, 164.4855853186988, 0.0), APoint(199.6629372545145, 163.6855853186988, 0.0))
entity.Color = 7


entity = acad.model.AddText('1.2', APoint(205.59865154022518, 165.0855853186988, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(199.6629372545145, 163.6855853186988, 0.0), APoint(200.46293725451451, 164.4855853186988, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(195.58793725451088, 164.4855853186988, 0.0), APoint(194.78793725451087, 163.6855853186988, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.3', APoint(196.98258011165555, 164.5855853186988, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(213.96293725450724, 164.4855853186988, 0.0), APoint(213.16293725450723, 163.6855853186988, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(218.03793725451087, 163.6855853186988, 0.0), APoint(218.83793725451088, 164.4855853186988, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.3', APoint(215.3575801116519, 164.5855853186988, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(222.61060531336776, 159.75697630978257, 0.0), APoint(221.81060531336774, 160.55697630978258, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(221.81060531336774, 153.05697630978258, 0.0), APoint(222.61060531336776, 152.25697630978257, 0.0))
entity.Color = 7


entity = acad.model.AddText('3', APoint(221.5320338847963, 155.6569763097825, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(195.58793725451088, 149.4817670399904, 0.0), APoint(194.78793725451087, 148.68176703999038, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(218.03793725451087, 148.68176703999038, 0.0), APoint(218.83793725451088, 149.4817670399904, 0.0))
entity.Color = 7


entity = acad.model.AddText('1.8', APoint(206.0272229687966, 149.58176703999038, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('W2', APoint(123.5832399773199, 190.58434651848904, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('W4', APoint(29.10460449239586, 265.35611713499986, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('W3', APoint(27.631221005315094, 189.20354655655515, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(75.80977665059535, 127.8172405527143, 0.0), APoint(72.42278717616637, 131.90440087254794, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.42278717616637, 131.90440087254794, 0.0), APoint(65.20766424672229, 131.8893736531879, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('A=5.95', APoint(49.86238060737652, 83.01599936022717, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('B=10.6', APoint(101.28916819652153, 83.01599936022717, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('L=17.75', APoint(75.67637378933908, 74.16976331948877, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('L=16.55', APoint(72.67637378933908, 99.9448981246405, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('0.20', APoint(17.82457790160443, 96.03422367574218, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(32.42937517499639, 118.44784780102694, 0.0), APoint(30.707165512682423, 119.99174295143166, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(30.707165512682423, 119.99174295143166, 0.0), APoint(21.0655890145581, 119.99174295143166, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.12319730416048, 117.9776023047815, 0.0), APoint(126.18554953657849, 120.99688340090731, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.18554953657849, 120.99688340090731, 0.0), APoint(135.82712603470327, 120.99688340090731, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.53966726554486, 58.5237918609265, 0.0), APoint(195.73966726554485, 59.3237918609265, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(195.73966726554485, 49.323791860926484, 0.0), APoint(196.53966726554486, 48.52379186092649, 0.0))
entity.Color = 7


entity = acad.model.AddText('m', APoint(195.06823869411625, 53.17379186092642, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(160.98269319810007, 44.83974908911011, 0.0), APoint(160.18269319810005, 44.03974908911011, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(191.18269319810005, 44.03974908911011, 0.0), APoint(191.98269319810007, 44.83974908911011, 0.0))
entity.Color = 7


entity = acad.model.AddText('f', APoint(175.65412176952864, 44.93974908911011, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(158.720222630938, 59.3237918609265, 0.0), APoint(159.520222630938, 58.5237918609265, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(159.52022263093798, 98.52379186092651, 0.0), APoint(158.72022263093797, 99.32379186092652, 0.0))
entity.Color = 7


entity = acad.model.AddText('h', APoint(158.44165120236656, 78.17379186092644, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(189.20128000321566, 100.52379186092652, 0.0), APoint(188.40128000321565, 101.32379186092653, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(188.40128000321565, 99.32379186092653, 0.0), APoint(189.20128000321566, 98.52379186092652, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.20', APoint(186.30128000321565, 99.17379186092644, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(178.0660265314331, 104.49097843329912, 0.0), APoint(177.26602653143308, 103.69097843329911, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(180.76602653143217, 103.69097843329911, 0.0), APoint(181.5660265314322, 104.49097843329912, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.35', APoint(176.91602653143264, 104.59097843329911, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(180.76602653143217, 93.14065940423387, 0.0), APoint(181.5660265314322, 93.94065940423388, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(182.0660265314331, 93.94065940423388, 0.0), APoint(181.26602653143308, 93.14065940423387, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.05', APoint(178.91602653143264, 94.04065940423388, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(191.18269319810005, 63.98120553987594, 0.0), APoint(191.98269319810007, 64.78120553987594, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(181.5660265314322, 64.78120553987594, 0.0), APoint(180.76602653143217, 63.98120553987594, 0.0))
entity.Color = 7


entity = acad.model.AddText('b', APoint(185.66007415048043, 64.88120553987594, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('max 14', APoint(162.3493244653659, 99.07205072480662, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(180.76602653143217, 63.98120553987594, 0.0), APoint(181.5660265314322, 64.78120553987594, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(160.98269319810007, 64.78120553987594, 0.0), APoint(160.18269319810005, 63.98120553987594, 0.0))
entity.Color = 7


entity = acad.model.AddText('s1', APoint(169.76721700762326, 64.88120553987594, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(173.5660265314331, 90.36899617366169, 0.0), APoint(172.76602653143308, 89.56899617366167, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(180.76602653143217, 89.56899617366167, 0.0), APoint(181.5660265314322, 90.36899617366169, 0.0))
entity.Color = 7


entity = acad.model.AddText('s2', APoint(175.84459796000405, 90.46899617366168, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(218.46712011231142, 196.79044929798312, 0.0), APoint(217.6671201123114, 197.59044929798313, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(217.66712011231144, 187.9319763097828, 0.0), APoint(218.46712011231145, 187.1319763097828, 0.0))
entity.Color = 7


entity = acad.model.AddText('Hs=0.25', APoint(216.63854868374, 191.61121280388286, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(352.70155933255774, 120.1612515830691, 0.0), APoint(351.70155933255774, 120.32791824973577, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(351.70155933255774, 120.32791824973577, 0.0), APoint(352.70155933255774, 120.49458491640245, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(352.70155933255774, 120.1612515830691, 0.0), APoint(352.70155933255774, 120.49458491640245, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(351.70155933255774, 120.32791824973577, 0.0), APoint(352.70155933255774, 120.32791824973577, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(352.70155933255774, 120.32791824973577, 0.0), APoint(354.7150066166423, 120.32791824973577, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(369.1284539007265, 120.49458491640381, 0.0), APoint(370.1284539007265, 120.32791824973714, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(370.1284539007265, 120.32791824973714, 0.0), APoint(369.1284539007265, 120.16125158307047, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(369.1284539007265, 120.49458491640381, 0.0), APoint(369.1284539007265, 120.16125158307047, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(370.1284539007265, 120.32791824973714, 0.0), APoint(369.1284539007265, 120.32791824973714, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(369.1284539007265, 120.32791824973714, 0.0), APoint(367.11500661664286, 120.32791824973714, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(352.6949417565896, 104.6171991844679, 0.0), APoint(351.6952145642308, 104.7854945160613, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(351.6952145642308, 104.7854945160613, 0.0), APoint(352.69548471860054, 104.95053207558932, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(352.6949417565896, 104.6171991844679, 0.0), APoint(352.69548471860054, 104.95053207558932, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(351.6952145642308, 104.7854945160613, 0.0), APoint(352.69521323759506, 104.78386563002861, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(352.69521323759506, 104.78386563002861, 0.0), APoint(354.70865785056776, 104.78058595387, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(369.12235749426384, 104.92377453646476, 0.0), APoint(370.12208468662266, 104.75547920487128, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(370.12208468662266, 104.75547920487128, 0.0), APoint(369.1218145322529, 104.59044164534333, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(369.12235749426384, 104.92377453646476, 0.0), APoint(369.1218145322529, 104.59044164534333, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(370.12208468662266, 104.75547920487128, 0.0), APoint(369.1220860132584, 104.75710809090404, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(369.1220860132584, 104.75710809090404, 0.0), APoint(367.1086414002848, 104.76038776706281, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.117437810965, 104.42827456027996, 0.0), APoint(321.2636823923194, 104.97497325509374, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(321.2636823923194, 104.97497325509374, 0.0), APoint(322.2485965542211, 104.73471949037116, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(322.117437810965, 104.42827456027996, 0.0), APoint(322.2485965542211, 104.73471949037116, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(321.2636823923194, 104.97497325509374, 0.0), APoint(322.183017182593, 104.58149702532556, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(322.183017182593, 104.58149702532556, 0.0), APoint(330.1985509669448, 101.15084037400095, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(330.1985509669448, 101.15084037400095, 0.0), APoint(337.7507905351058, 101.15084037400095, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(326.5588718726443, 115.58262258360054, 0.0), APoint(326.4619216330402, 114.5734752064457, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(326.4619216330402, 114.5734752064457, 0.0), APoint(326.22634027791275, 115.55951739767998, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(326.5588718726443, 115.58262258360054, 0.0), APoint(326.22634027791275, 115.55951739767998, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(326.4619216330402, 114.5734752064457, 0.0), APoint(326.39260607527854, 115.57106999064027, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(326.39260607527854, 115.57106999064027, 0.0), APoint(325.9461187781908, 121.99694916072866, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(325.9461187781908, 121.99694916072866, 0.0), APoint(316.0541946106432, 121.99694916072866, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(389.1833254488159, 112.08506193946313, 0.0), APoint(389.34857377777826, 111.08482658338292, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(389.34857377777826, 111.08482658338292, 0.0), APoint(388.8678571348959, 111.97740111082234, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(389.1833254488159, 112.08506193946313, 0.0), APoint(388.8678571348959, 111.97740111082234, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(389.34857377777826, 111.08482658338292, 0.0), APoint(389.0255912918559, 112.03123152514274, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(389.0255912918559, 112.03123152514274, 0.0), APoint(385.45356783681837, 122.4979930285578, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(385.45356783681837, 122.4979930285578, 0.0), APoint(397.41721331406825, 122.4979930285578, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(345.13274521893806, 118.00778566714108, 0.0), APoint(345.1282925950254, 116.9940016901923, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(345.1282925950254, 116.9940016901923, 0.0), APoint(344.80370973322965, 117.95443062749389, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(345.13274521893806, 118.00778566714108, 0.0), APoint(344.80370973322965, 117.95443062749389, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(345.1282925950254, 116.9940016901923, 0.0), APoint(344.9682274760839, 117.98110814731749, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(344.9682274760839, 117.98110814731749, 0.0), APoint(343.73260771560217, 125.60105840373939, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(343.73260771560217, 125.60105840373939, 0.0), APoint(332.919955822691, 125.60105840373939, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028435036, 120.339901837799, 0.0), APoint(360.92038028435036, 126.4188638237651, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028435036, 126.4188638237651, 0.0), APoint(375.7295859249234, 126.4188638237651, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028435036, 106.75526935966985, 0.0), APoint(360.92038028435036, 100.67630737370376, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028435036, 100.67630737370376, 0.0), APoint(375.80826349070685, 100.67630737370376, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(318.1482107164846, 101.49630069535675, 0.0), APoint(318.1063373419638, 102.50922931983334, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(318.1063373419638, 102.50922931983334, 0.0), APoint(318.47446468255697, 101.56463414787575, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(318.1482107164846, 101.49630069535675, 0.0), APoint(318.47446468255697, 101.56463414787575, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(318.1063373419638, 102.50922931983334, 0.0), APoint(318.3113376995208, 101.53046742161625, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(318.3113376995208, 101.53046742161625, 0.0), APoint(319.40025001598497, 96.33152094876314, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(319.40025001598497, 96.33152094876314, 0.0), APoint(308.72144134273094, 96.33152094876314, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(263.28194279048, 111.8550776208014, 0.0), APoint(262.48194279048005, 111.05507762080138, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(272.98194279047914, 111.05507762080138, 0.0), APoint(273.7819427904791, 111.8550776208014, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.35', APoint(266.4652761238129, 110.95507762080139, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(256.7028857894719, 101.82951951664518, 0.0), APoint(257.50288578947186, 101.02951951664517, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(257.50288578947186, 108.52951951664517, 0.0), APoint(256.7028857894719, 109.32951951664518, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.25', APoint(255.43621912280517, 104.67951951664507, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(263.98194279048005, 97.54256900027156, 0.0), APoint(264.78194279048, 98.34256900027157, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(263.28194279048, 98.34256900027157, 0.0), APoint(262.48194279048005, 97.54256900027156, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.05', APoint(256.22956183809794, 97.44256900027156, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(273.8317353977417, 109.29344627630037, 0.0), APoint(277.25339935110696, 112.53880996133628, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(277.25339935110696, 112.53880996133628, 0.0), APoint(284.5489794608957, 112.53880996133628, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(271.1508755586501, 95.51088256314469, 0.0), APoint(271.8819427904791, 96.2132489065323, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(271.8819427904791, 96.2132489065323, 0.0), APoint(271.4181871960639, 95.31174542543732, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(271.1508755586501, 95.51088256314469, 0.0), APoint(271.4181871960639, 95.31174542543732, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(271.8819427904791, 96.2132489065323, 0.0), APoint(271.284531377357, 95.411313994291, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(271.284531377357, 95.411313994291, 0.0), APoint(267.1611193557137, 89.87625392499947, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(267.1611193557137, 89.87625392499947, 0.0), APoint(256.84431199632854, 89.87625392499947, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.92244825006932, 104.83374477229052, 0.0), APoint(243.72244825006933, 104.0337447722905, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(243.72244825006933, 101.03389476104073, 0.0), APoint(242.92244825006932, 101.83389476104074, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.10', APoint(241.65578158340264, 102.43381976666552, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(243.72244825006933, 101.03359477603959, 0.0), APoint(242.92244825006932, 101.8335947760396, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(242.92244825006932, 95.68329478353994, 0.0), APoint(243.72244825006933, 94.88329478353992, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.20', APoint(241.65578158340264, 97.85844477978968, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(240.164347850808, 93.17479212159867, 0.0), APoint(239.364347850808, 92.37479212159866, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(236.364347850808, 92.37479212159866, 0.0), APoint(237.164347850808, 93.17479212159867, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.10', APoint(236.59768118414135, 92.27479212159867, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(236.364347850808, 92.37479212159866, 0.0), APoint(237.164347850808, 93.17479212159867, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(225.164347850808, 93.17479212159867, 0.0), APoint(224.364347850808, 92.37479212159866, 0.0))
entity.Color = 7


entity = acad.model.AddText('p2/2', APoint(228.81196689842704, 92.44145878826534, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(396.97307597330615, 104.60954165560452, 0.0), APoint(397.9415619472311, 104.90922931982922, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(397.9415619472311, 104.90922931982922, 0.0), APoint(397.1226225656993, 104.31163742969507, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(396.97307597330615, 104.60954165560452, 0.0), APoint(397.1226225656993, 104.31163742969507, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(397.9415619472311, 104.90922931982922, 0.0), APoint(397.04784926950276, 104.4605895426498, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(397.04784926950276, 104.4605895426498, 0.0), APoint(390.39175622130097, 101.1192605266834, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(390.39175622130097, 101.1192605266834, 0.0), APoint(383.21361545825584, 101.1192605266834, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(397.83200936673944, 98.85308810462067, 0.0), APoint(398.8004953406644, 99.15277576884537, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(398.8004953406644, 99.15277576884537, 0.0), APoint(397.9815559591326, 98.55518387871122, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(397.83200936673944, 98.85308810462067, 0.0), APoint(397.9815559591326, 98.55518387871122, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(398.8004953406644, 99.15277576884537, 0.0), APoint(397.90678266293605, 98.70413599166595, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(397.90678266293605, 98.70413599166595, 0.0), APoint(391.25068961473426, 95.36280697569956, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.25068961473426, 95.36280697569956, 0.0), APoint(389.36677125838924, 95.36280697569956, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(321.7635498498111, 93.4193910143877, 0.0), APoint(321.03703930305255, 94.12646965444574, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(321.03703930305255, 94.12646965444574, 0.0), APoint(321.9536018116268, 93.69323652360984, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(321.7635498498111, 93.4193910143877, 0.0), APoint(321.9536018116268, 93.69323652360984, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(321.03703930305255, 94.12646965444574, 0.0), APoint(321.85857583071896, 93.55631376899878, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(321.85857583071896, 93.55631376899878, 0.0), APoint(324.4190982246382, 91.77928150865765, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(324.4190982246382, 91.77928150865765, 0.0), APoint(329.04030034400967, 91.77928150865765, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.4378614060101, 101.50292132749286, 0.0), APoint(402.56083295690314, 102.50922931983354, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(402.56083295690314, 102.50922931983354, 0.0), APoint(402.7708786765472, 101.51743368895136, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(402.4378614060101, 101.50292132749286, 0.0), APoint(402.7708786765472, 101.51743368895136, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(402.56083295690314, 102.50922931983354, 0.0), APoint(402.6043700412787, 101.51017750822211, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(402.6043700412787, 101.51017750822211, 0.0), APoint(402.74786971164576, 98.21726968717115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.74786971164576, 98.21726968717115, 0.0), APoint(411.88410221134654, 98.2157921752686, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(110.14153591759326, 254.9753652001885, 0.0), APoint(109.7023054330519, 253.33613471564718, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(139.95230543305465, 270.8009803586345, 0.0), APoint(140.39153591759597, 272.44021084317586, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(139.41191484756254, 180.17548622902265, 0.0), APoint(141.05114533210386, 180.61471671356404, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(110.8011453320993, 198.07956235655197, 0.0), APoint(109.16191484755798, 197.6403318720106, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(44.97451866757873, 254.92344732172427, 0.0), APoint(46.61374915212006, 255.3626778062656, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(16.363749152119162, 272.8275234492529, 0.0), APoint(14.724518667577831, 272.3882929647116, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(44.55989587555544, 197.70715095769526, 0.0), APoint(44.99912636009674, 199.34638144223658, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(14.74912636009674, 181.88153579924978, 0.0), APoint(14.309895875555439, 180.24230531470846, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(26.505530282556812, 83.11599936022716, 0.0), APoint(25.30553028255681, 81.91599936022718, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(77.12399283695814, 81.91599936022718, 0.0), APoint(78.32399283695813, 83.11599936022716, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(78.32399283695813, 83.11599936022716, 0.0), APoint(77.12399283695814, 81.91599936022718, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(128.73053403227541, 81.91599936022718, 0.0), APoint(129.9305340322754, 83.11599936022716, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(26.505530282556812, 74.26976331948876, 0.0), APoint(25.30553028255681, 73.06976331948877, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(128.73053403227541, 73.06976331948877, 0.0), APoint(129.9305340322754, 74.26976331948876, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(34.718032157416566, 100.0448981246405, 0.0), APoint(33.51803215741656, 98.84489812464051, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(120.5180321574152, 98.84489812464051, 0.0), APoint(121.7180321574152, 100.0448981246405, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(26.805530282553175, 94.93422367574219, 0.0), APoint(28.00553028255317, 96.13422367574218, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(26.505530282556812, 96.13422367574218, 0.0), APoint(25.30553028255681, 94.93422367574219, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(163.23935261673924, 101.51440127888601, 0.0), APoint(162.36530401992766, 102.96906242513681, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(161.7949365134259, 99.5237918609267, 0.0), APoint(162.9949365134259, 98.32379186092672, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(81.11057782742273, 126.90909326196413, 0.0), APoint(93.55464718687426, 126.90909326196413, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.55464718687426, 126.90909326196413, 0.0), APoint(92.04109869593367, 127.32622982914324, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('-3 %', APoint(83.03149036782406, 127.50055597702737, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(73.87448161728526, 126.90909326196413, 0.0), APoint(61.43041225783372, 126.90909326196413, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.43041225783372, 126.90909326196413, 0.0), APoint(62.94396074871611, 127.32622982914324, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('3 %', APoint(66.30739112034053, 127.65664430967297, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('DOWN', APoint(136.55470679358086, 98.66042560726392, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('UP', APoint(13.479687887512227, 101.24274471522433, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('- ', APoint(389.2388533121279, 13.648828014805037, 0.0), 2.663041818489627)
entity.Color = 7

entity = acad.model.AddLine(APoint(37.132917460198854, 282.1045448533092, 0.0), APoint(37.59240792579385, 280.0504291305756, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(37.59240792579385, 280.0504291305756, 0.0), APoint(39.18734281290699, 282.5626489468385, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(24.37644064895312, 261.9410500384946, 0.0), APoint(26.430866001661798, 262.3991541320247, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(26.430866001661798, 262.3991541320247, 0.0), APoint(25.63339855810318, 261.14304422389233, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(59.52642114675609, 270.817178111742, 0.0), APoint(61.015024072422875, 269.3290301956912, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(61.015024072422875, 269.3290301956912, 0.0), APoint(61.01557334197196, 272.3047763874314, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(39.30067278530646, 230.56702749068074, 0.0), APoint(37.812799689433405, 230.56730212545676, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(39.30067278530646, 230.56702749068074, 0.0), APoint(37.81307450961435, 232.05617968589888, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(115.82948112243912, 232.77446644372446, 0.0), APoint(114.34133320638784, 231.285863518057, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(114.34133320638784, 231.285863518057, 0.0), APoint(117.31707939812804, 231.2853142485078, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(59.516467556389216, 181.9364531710828, 0.0), APoint(61.0056197516069, 183.424051446774, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(61.0056197516069, 183.424051446774, 0.0), APoint(61.00534511683236, 181.93617835090186, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(76.19476497624328, 128.13627658377476, 0.0), APoint(77.72399283695813, 125.50731059882679, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(77.72399283695813, 125.50731059882679, 0.0), APoint(75.42478832494744, 127.49820452165383, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(75.42478832494744, 127.49820452165383, 0.0), APoint(75.80977665059535, 127.81724055271428, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(75.80977665059535, 127.81724055271428, 0.0), APoint(76.19476497624328, 128.13627658377476, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(32.206872545324785, 118.19964689268788, 0.0), APoint(33.9185806250307, 117.11283202299728, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(33.9185806250307, 117.11283202299728, 0.0), APoint(32.651877804668, 118.69604870936598, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(32.206872545324785, 118.19964689268788, 0.0), APoint(32.429375174996395, 118.44784780102692, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(32.429375174996395, 118.44784780102692, 0.0), APoint(32.651877804668, 118.69604870936598, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(57.63651874323893, 125.16521634655425, 0.0), APoint(57.77916471428477, 125.30786231760007, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.63826900754841, 124.99018991556707, 0.0), APoint(57.95772703276622, 125.30964794078488, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.640019271857945, 124.81516348457998, 0.0), APoint(58.13628935124769, 125.31143356396973, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.78452212493743, 124.78288964236282, 0.0), APoint(58.314851669729116, 125.31321918715452, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.963084443418886, 124.78467526554763, 0.0), APoint(58.493413988210584, 125.31500481033933, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.14164676190034, 124.78646088873245, 0.0), APoint(58.67197630669204, 125.31679043352415, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.320209080381794, 124.78824651191727, 0.0), APoint(58.85053862517349, 125.31857605670896, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.498771398863234, 124.79003213510208, 0.0), APoint(59.02910094365493, 125.32036167989378, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.67733371734469, 124.7918177582869, 0.0), APoint(59.207663262136386, 125.3221473030786, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.85589603582615, 124.79360338147173, 0.0), APoint(59.38622558061783, 125.32393292626341, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.034458354307574, 124.79538900465651, 0.0), APoint(59.56478789909927, 125.32571854944821, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.21302067278904, 124.79717462784134, 0.0), APoint(59.743350217580726, 125.32750417263303, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.3915829912705, 124.79896025102616, 0.0), APoint(59.921912536062194, 125.32928979581786, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.57014530975195, 124.80074587421097, 0.0), APoint(60.10047485454365, 125.33107541900267, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.74870762823339, 124.80253149739578, 0.0), APoint(60.2790371730251, 125.33286104218749, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.927269946714844, 124.80431712058059, 0.0), APoint(60.45759949150654, 125.33464666537229, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.1058322651963, 124.80610274376541, 0.0), APoint(60.636161809987996, 125.3364322885571, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.284394583677766, 124.80788836695024, 0.0), APoint(60.81472412846945, 125.33821791174192, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.46295690215919, 124.80967399013502, 0.0), APoint(60.99328644695092, 125.34000353492675, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.64151922064065, 124.81145961331987, 0.0), APoint(61.171848765432365, 125.34178915811157, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.820081539122114, 124.81324523650467, 0.0), APoint(61.35041108391381, 125.34357478129637, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.998643857603554, 124.81503085968947, 0.0), APoint(61.528973402395266, 125.34536040448118, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.177206176085, 124.81681648287429, 0.0), APoint(61.70753572087671, 125.34714602766601, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.355768494566455, 124.8186021060591, 0.0), APoint(61.88609803935815, 125.3489316508508, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.53433081304791, 124.82038772924392, 0.0), APoint(62.06466035783961, 125.35071727403562, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.71289313152936, 124.82217335242873, 0.0), APoint(62.24322267632106, 125.35250289722043, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.8914554500108, 124.82395897561355, 0.0), APoint(62.421784994802515, 125.35428852040525, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.070017768492264, 124.82574459879838, 0.0), APoint(62.60034731328395, 125.35607414359006, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.24858008697372, 124.8275302219832, 0.0), APoint(62.778909631765416, 125.3578597667749, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.42714240545516, 124.829315845168, 0.0), APoint(62.95747195024687, 125.35964538995971, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.605704723936626, 124.83110146835283, 0.0), APoint(63.136034268728324, 125.36143101314453, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.784267042418065, 124.83288709153763, 0.0), APoint(63.31459658720976, 125.36321663632933, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.96282936089952, 124.83467271472244, 0.0), APoint(63.49315890569122, 125.36500225951414, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.14139167938096, 124.83645833790725, 0.0), APoint(63.67172122417267, 125.36678788269896, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.31995399786241, 124.83824396109206, 0.0), APoint(63.850283542654125, 125.36857350588377, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.49851631634387, 124.84002958427688, 0.0), APoint(64.02884586113557, 125.37035912906858, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.677078634825335, 124.8418152074617, 0.0), APoint(64.20740817961703, 125.3721447522534, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.855640953306775, 124.84360083064651, 0.0), APoint(64.38597049809849, 125.37393037543822, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.03420327178823, 124.84538645383132, 0.0), APoint(64.56453281657994, 125.37571599862304, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.21276559026968, 124.84717207701614, 0.0), APoint(64.74309513506138, 125.37750162180784, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.39132790875112, 124.84895770020094, 0.0), APoint(64.92165745354284, 125.37928724499265, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.56989022723258, 124.85074332338576, 0.0), APoint(65.10021977202429, 125.38107286817747, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.74845254571403, 124.85252894657057, 0.0), APoint(65.27878209050573, 125.3828584913623, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.92701486419548, 124.85431456975539, 0.0), APoint(65.45734440898721, 125.38464411454711, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.10557718267691, 124.8561001929402, 0.0), APoint(65.63590672746864, 125.3864297377319, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.28413950115839, 124.85788581612502, 0.0), APoint(65.81446904595009, 125.38821536091675, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.46270181963985, 124.85967143930984, 0.0), APoint(65.99303136443154, 125.39000098410156, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.64126413812129, 124.86145706249467, 0.0), APoint(66.17159368291298, 125.39178660728636, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.81982645660273, 124.86324268567947, 0.0), APoint(66.35015600139445, 125.3935722304712, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.99838877508418, 124.86502830886428, 0.0), APoint(66.52871831987589, 125.395357853656, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.17695109356563, 124.8668139320491, 0.0), APoint(66.70728063835735, 125.39714347684081, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.35551341204707, 124.8685995552339, 0.0), APoint(66.88584295683879, 125.39892910002561, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.53407573052856, 124.87038517841874, 0.0), APoint(67.06440527532024, 125.40071472321043, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.71263804900998, 124.87217080160353, 0.0), APoint(67.24296759380171, 125.40250034639526, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.89120036749142, 124.87395642478833, 0.0), APoint(67.42152991228316, 125.40428596958007, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.0697626859729, 124.87574204797318, 0.0), APoint(67.60009223076462, 125.40607159276489, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.24832500445434, 124.87752767115798, 0.0), APoint(67.77865454924606, 125.40785721594969, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.4268873229358, 124.8793132943428, 0.0), APoint(67.95721686772751, 125.4096428391345, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.60544964141725, 124.88109891752761, 0.0), APoint(68.13577918620896, 125.41142846231932, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.78401195989869, 124.88288454071241, 0.0), APoint(68.31434150469043, 125.41321408550415, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.96257427838015, 124.88467016389723, 0.0), APoint(68.49290382317186, 125.41499970868894, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.1411365968616, 124.88645578708204, 0.0), APoint(68.67146614165333, 125.41678533187377, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.31969891534305, 124.88824141026689, 0.0), APoint(68.85002846013478, 125.41857095505858, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.49826123382448, 124.89002703345167, 0.0), APoint(69.0285907786162, 125.4203565782434, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.67682355230596, 124.89181265663649, 0.0), APoint(69.20715309709766, 125.42214220142822, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.85538587078739, 124.8935982798213, 0.0), APoint(69.38571541557911, 125.42392782461303, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.03394818926887, 124.89538390300612, 0.0), APoint(69.56427773406057, 125.42571344779785, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.2125105077503, 124.89716952619094, 0.0), APoint(69.74284005254205, 125.42749907098266, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.39107282623173, 124.89895514937574, 0.0), APoint(69.92140237102346, 125.42928469416746, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.5696351447132, 124.90074077256057, 0.0), APoint(70.09996468950493, 125.4310703173523, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.74819746319464, 124.90252639574537, 0.0), APoint(70.27852700798638, 125.43285594053711, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.92675978167613, 124.90431201893021, 0.0), APoint(70.45708932646784, 125.43464156372193, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.10532210015757, 124.90609764211501, 0.0), APoint(70.63565164494929, 125.43642718690674, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.283884418639, 124.90788326529982, 0.0), APoint(70.81421396343073, 125.43821281009154, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.46244673712046, 124.90966888848463, 0.0), APoint(70.99277628191219, 125.43999843327636, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.64100905560191, 124.91145451166945, 0.0), APoint(71.17133860039365, 125.44178405646119, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.81957137408337, 124.91324013485426, 0.0), APoint(71.34990091887508, 125.44356967964598, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.9981336925648, 124.91502575803906, 0.0), APoint(71.52846323735655, 125.4453553028308, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.17669601104626, 124.91681138122388, 0.0), APoint(71.707025555838, 125.44714092601562, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.35525832952771, 124.9185970044087, 0.0), APoint(71.88558787431944, 125.44892654920042, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.53382064800918, 124.92038262759353, 0.0), APoint(72.0641501928009, 125.45071217238524, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.71238296649061, 124.92216825077831, 0.0), APoint(72.24271251128235, 125.45249779557005, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.89094528497208, 124.92395387396314, 0.0), APoint(72.4212748297638, 125.45428341875487, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.06950760345353, 124.92573949714796, 0.0), APoint(72.59983714824526, 125.45606904193971, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.24806992193498, 124.92752512033277, 0.0), APoint(72.77839946672668, 125.4578546651245, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.42663224041644, 124.92931074351759, 0.0), APoint(72.95696178520816, 125.45964028830932, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.60519455889786, 124.9310963667024, 0.0), APoint(73.13552410368962, 125.46142591149413, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.78375687737932, 124.93288198988719, 0.0), APoint(73.31408642217107, 125.46321153467895, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.96231919586079, 124.93466761307205, 0.0), APoint(73.49264874065251, 125.46499715786378, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.14088151434221, 124.93645323625684, 0.0), APoint(73.67121105913395, 125.46678278104858, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.31944383282368, 124.93823885944167, 0.0), APoint(73.8497733776154, 125.4685684042334, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.49800615130513, 124.94002448262648, 0.0), APoint(74.02833569609687, 125.47035402741822, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.67656846978657, 124.94181010581129, 0.0), APoint(74.2068980145783, 125.47213965060301, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.85513078826803, 124.9435957289961, 0.0), APoint(74.38546033305977, 125.47392527378784, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.03369310674948, 124.94538135218092, 0.0), APoint(74.56402265154122, 125.47571089697266, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.21225542523094, 124.94716697536573, 0.0), APoint(74.74258497002268, 125.47749652015747, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.39081774371238, 124.94895259855053, 0.0), APoint(74.92114728850412, 125.47928214334227, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.56938006219383, 124.95073822173535, 0.0), APoint(75.09970960698557, 125.48106776652709, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.74794238067527, 124.95252384492015, 0.0), APoint(75.27827192546702, 125.4828533897119, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.92650469915675, 124.954309468105, 0.0), APoint(75.45683424394848, 125.48463901289672, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.10506701763819, 124.9560950912898, 0.0), APoint(75.63539656242995, 125.48642463608155, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.28362933611965, 124.95788071447461, 0.0), APoint(75.81395888091139, 125.48821025926635, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.4621916546011, 124.95966633765943, 0.0), APoint(75.99252119939284, 125.48999588245117, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.64075397308255, 124.96145196084424, 0.0), APoint(76.17108351787428, 125.491781505636, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.81931629156401, 124.96323758402909, 0.0), APoint(76.34964583635573, 125.49356712882081, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.99787861004543, 124.96502320721387, 0.0), APoint(76.52820815483719, 125.4953527520056, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.17644092852692, 124.96680883039869, 0.0), APoint(76.70677047331864, 125.49713837519042, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.35500324700834, 124.96859445358348, 0.0), APoint(76.8853327918001, 125.49892399837523, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.5335655654898, 124.97038007676832, 0.0), APoint(77.06389511028152, 125.50070962156005, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.71212788397125, 124.97216569995314, 0.0), APoint(77.24245742876299, 125.50249524474488, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.89069020245269, 124.97395132313794, 0.0), APoint(77.42101974724444, 125.5042808679297, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.06925252093414, 124.97573694632275, 0.0), APoint(77.5995820657259, 125.50606649111451, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.2478148394156, 124.97752256950757, 0.0), APoint(77.72399283695692, 125.4537005670489, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695815, 125.45370056705012, 0.0), APoint(77.777072076341, 125.50677980643297, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.42637715789705, 124.97930819269239, 0.0), APoint(77.72399283695736, 125.2769238717527, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695815, 125.27692387175348, 0.0), APoint(77.95209850732779, 125.50502954212313, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.60493947637852, 124.98109381587722, 0.0), APoint(77.72399283695783, 125.10014717645653, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695815, 125.10014717645684, 0.0), APoint(78.12712493831455, 125.50327927781325, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.78232339965399, 124.98170104385605, 0.0), APoint(78.30215136930133, 125.50152901350339, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.95734983064077, 124.97995077954619, 0.0), APoint(78.47717780028809, 125.49977874919351, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.13237626162753, 124.97820051523631, 0.0), APoint(78.65220423127485, 125.49802848488363, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.30740269261432, 124.97645025092646, 0.0), APoint(78.82723066226164, 125.49627822057379, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.48242912360107, 124.97469998661657, 0.0), APoint(79.0022570932484, 125.49452795626391, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.65745555458786, 124.97294972230672, 0.0), APoint(79.17728352423518, 125.49277769195405, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.83248198557462, 124.97119945799685, 0.0), APoint(79.35230995522194, 125.49102742764417, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.00750841656138, 124.96944919368697, 0.0), APoint(79.52733638620872, 125.48927716333431, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.18253484754815, 124.96769892937711, 0.0), APoint(79.70236281719548, 125.48752689902443, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.35756127853492, 124.96594866506723, 0.0), APoint(79.87738924818225, 125.4857766347146, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.53258770952169, 124.9641984007574, 0.0), APoint(80.052415679169, 125.4840263704047, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.70761414050844, 124.9624481364475, 0.0), APoint(80.22744211015578, 125.48227610609484, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.88264057149524, 124.96069787213764, 0.0), APoint(80.40246854114255, 125.48052584178498, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.05766700248199, 124.95894760782778, 0.0), APoint(80.57749497212933, 125.47877557747509, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.23269343346875, 124.9571973435179, 0.0), APoint(80.75252140311608, 125.47702531316523, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.40771986445554, 124.95544707920806, 0.0), APoint(80.92754783410285, 125.47527504885537, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.58274629544229, 124.95369681489817, 0.0), APoint(81.10257426508961, 125.47352478454549, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.75777272642908, 124.95194655058832, 0.0), APoint(81.2776006960764, 125.47177452023564, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.93279915741584, 124.95019628627844, 0.0), APoint(81.45262712706315, 125.47002425592575, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.10782558840262, 124.94844602196858, 0.0), APoint(81.62765355804994, 125.4682739916159, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.28285201938938, 124.9466957576587, 0.0), APoint(81.8026799890367, 125.46652372730603, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.45787845037614, 124.94494549334883, 0.0), APoint(81.97770642002347, 125.46477346299615, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.63290488136293, 124.94319522903898, 0.0), APoint(82.15273285101024, 125.46302319868629, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.80793131234971, 124.94144496472911, 0.0), APoint(82.327759281997, 125.46127293437641, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.98295774333647, 124.93969470041924, 0.0), APoint(82.5027857129838, 125.45952267006656, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.15798417432323, 124.93794443610936, 0.0), APoint(82.67781214397056, 125.45777240575669, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.33301060531001, 124.9361941717995, 0.0), APoint(82.85283857495733, 125.45602214144682, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.50803703629678, 124.93444390748964, 0.0), APoint(83.0278650059441, 125.45427187713695, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.68306346728356, 124.93269364317977, 0.0), APoint(83.20289143693086, 125.45252161282707, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.85808989827032, 124.9309433788699, 0.0), APoint(83.37791786791763, 125.45077134851721, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.03311632925707, 124.92919311456004, 0.0), APoint(83.55294429890438, 125.44902108420735, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.20814276024385, 124.92744285025017, 0.0), APoint(83.72797072989115, 125.44727081989748, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.38316919123062, 124.92569258594028, 0.0), APoint(83.90299716087793, 125.44552055558759, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.5581956222174, 124.92394232163045, 0.0), APoint(84.0780235918647, 125.44377029127776, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.73322205320417, 124.92219205732056, 0.0), APoint(84.25305002285148, 125.44202002696787, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.90824848419093, 124.92044179301071, 0.0), APoint(84.42807645383823, 125.440269762658, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.0832749151777, 124.91869152870083, 0.0), APoint(84.603102884825, 125.43851949834814, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.25830134616446, 124.91694126439096, 0.0), APoint(84.77812931581177, 125.43676923403827, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.43332777715123, 124.9151910000811, 0.0), APoint(84.95315574679856, 125.43501896972842, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.60835420813802, 124.91344073577125, 0.0), APoint(85.12818217778532, 125.43326870541854, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.78338063912477, 124.91169047146136, 0.0), APoint(85.3032086087721, 125.43151844110868, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.95840707011155, 124.9099402071515, 0.0), APoint(85.47823503975886, 125.4297681767988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.1334335010983, 124.9081899428416, 0.0), APoint(85.65326147074562, 125.42801791248893, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.30845993208509, 124.90643967853175, 0.0), APoint(85.8282879017324, 125.42626764817906, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.48348636307185, 124.90468941422188, 0.0), APoint(86.00331433271917, 125.4245173838692, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.65851279405862, 124.90293914991202, 0.0), APoint(86.17834076370595, 125.42276711955934, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.83353922504541, 124.90118888560217, 0.0), APoint(86.35336719469271, 125.42101685524946, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.00856565603216, 124.89943862129228, 0.0), APoint(86.52839362567948, 125.4192665909396, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.18359208701894, 124.89768835698241, 0.0), APoint(86.70342005666625, 125.41751632662972, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.35861851800571, 124.89593809267255, 0.0), APoint(86.87844648765301, 125.41576606231985, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.53364494899247, 124.89418782836267, 0.0), APoint(87.05347291863978, 125.41401579800998, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.70867137997925, 124.89243756405284, 0.0), APoint(87.22849934962653, 125.41226553370012, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.883697810966, 124.89068729974295, 0.0), APoint(87.40352578061334, 125.41051526939026, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.0587242419528, 124.88893703543309, 0.0), APoint(87.57855221160008, 125.4087650050804, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.23375067293952, 124.8871867711232, 0.0), APoint(87.75357864258686, 125.40701474077053, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.40877710392631, 124.88543650681335, 0.0), APoint(87.92860507357362, 125.40526447646066, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.58380353491309, 124.88368624250349, 0.0), APoint(88.10363150456038, 125.40351421215078, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.75882996589985, 124.88193597819361, 0.0), APoint(88.27865793554717, 125.40176394784093, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.93385639688661, 124.88018571388373, 0.0), APoint(88.45368436653392, 125.40001368353104, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.10888282787339, 124.87843544957387, 0.0), APoint(88.62871079752071, 125.3982634192212, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.28390925886015, 124.876685185264, 0.0), APoint(88.80373722850747, 125.39651315491132, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.45893568984691, 124.87493492095412, 0.0), APoint(88.97876365949425, 125.39476289060146, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.6339621208337, 124.87318465664427, 0.0), APoint(89.15379009048101, 125.39301262629158, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.80898855182048, 124.87143439233441, 0.0), APoint(89.32881652146777, 125.3912623619817, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.98401498280724, 124.86968412802453, 0.0), APoint(89.50384295245455, 125.38951209767184, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.159041413794, 124.86793386371465, 0.0), APoint(89.67886938344131, 125.38776183336196, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.33406784478078, 124.86618359940479, 0.0), APoint(89.70644040441722, 125.23855615904124, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.50909427576755, 124.86443333509493, 0.0), APoint(89.70644040441722, 125.0617794637446, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.68412070675433, 124.86268307078507, 0.0), APoint(89.70644040441722, 124.88500276844796, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 125.2256876826674, 0.0), APoint(90.90405440034868, 125.3755099831929, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 125.04891098737076, 0.0), APoint(91.07908083133546, 125.37375971888301, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 124.87213429207412, 0.0), APoint(91.25410726232224, 125.37200945457315, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.9093057236617, 124.850431220616, 0.0), APoint(91.42913369330901, 125.37025919026328, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.08433215464846, 124.84868095630613, 0.0), APoint(91.60416012429575, 125.3685089259534, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.25935858563524, 124.84693069199626, 0.0), APoint(91.77918655528254, 125.36675866164356, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.434385016622, 124.84518042768639, 0.0), APoint(91.95421298626928, 125.36500839733367, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.60941144760879, 124.84343016337654, 0.0), APoint(92.12923941725607, 125.36325813302382, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.78443787859555, 124.84167989906666, 0.0), APoint(92.30426584824282, 125.36150786871393, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.95946430958232, 124.83992963475679, 0.0), APoint(92.47929227922961, 125.35975760440408, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.13449074056909, 124.83817937044692, 0.0), APoint(92.65431871021637, 125.3580073400942, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.30951717155585, 124.83642910613705, 0.0), APoint(92.82934514120313, 125.35625707578433, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.48454360254264, 124.8346788418272, 0.0), APoint(93.00437157218991, 125.35450681147447, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.65957003352939, 124.83292857751731, 0.0), APoint(93.1793980031767, 125.35275654716462, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.83459646451618, 124.83117831320746, 0.0), APoint(93.35442443416346, 125.35100628285474, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.00962289550293, 124.82942804889757, 0.0), APoint(93.52945086515022, 125.34925601854486, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.1846493264897, 124.8276777845877, 0.0), APoint(93.704477296137, 125.347505754235, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.35967575747645, 124.82592752027782, 0.0), APoint(93.87950372712375, 125.34575548992511, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.53470218846324, 124.82417725596797, 0.0), APoint(94.05453015811052, 125.34400522561525, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.70972861945, 124.82242699165809, 0.0), APoint(94.2295565890973, 125.34225496130539, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.88475505043678, 124.82067672734823, 0.0), APoint(94.40458302008406, 125.34050469699551, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.05978148142356, 124.8189264630384, 0.0), APoint(94.57960945107084, 125.33875443268568, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.23480791241033, 124.8171761987285, 0.0), APoint(94.75463588205758, 125.33700416837578, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.40983434339708, 124.81542593441864, 0.0), APoint(94.92966231304437, 125.33525390406594, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.58486077438386, 124.81367567010878, 0.0), APoint(95.10468874403114, 125.33350363975606, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.75988720537062, 124.8119254057989, 0.0), APoint(95.2797151750179, 125.33175337544618, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.93491363635738, 124.81017514148903, 0.0), APoint(95.45474160600469, 125.33000311113634, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.10994006734417, 124.80842487717918, 0.0), APoint(95.62976803699144, 125.32825284682644, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.28496649833092, 124.80667461286929, 0.0), APoint(95.80479446797823, 125.3265025825166, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.4599929293177, 124.80492434855944, 0.0), APoint(95.97982089896497, 125.3247523182067, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.63501936030447, 124.80317408424956, 0.0), APoint(96.15484732995176, 125.32300205389686, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.81004579129124, 124.8014238199397, 0.0), APoint(96.32987376093851, 125.32125178958697, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.985072222278, 124.79967355562982, 0.0), APoint(96.50490019192529, 125.3195015252771, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.16009865326477, 124.79792329131995, 0.0), APoint(96.67992662291203, 125.31775126096721, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.33512508425154, 124.79617302701008, 0.0), APoint(96.85495305389883, 125.31600099665737, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.51015151523833, 124.79442276270024, 0.0), APoint(97.02997948488562, 125.31425073234752, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.68517794622508, 124.79267249839035, 0.0), APoint(97.20500591587236, 125.31250046803763, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.86020437721186, 124.79092223408048, 0.0), APoint(97.38003234685915, 125.31075020372778, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.03523080819863, 124.78917196977062, 0.0), APoint(97.55505877784589, 125.30899993941787, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.2102572391854, 124.78742170546074, 0.0), APoint(97.73008520883268, 125.30724967510803, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.38528367017219, 124.7856714411509, 0.0), APoint(97.81193802517309, 125.2123257961518, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.56031010115893, 124.783921176841, 0.0), APoint(97.81015240198832, 125.03376347767042, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.73533653214571, 124.78217091253117, 0.0), APoint(97.80836677880356, 124.85520115918902, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.4687657928115, 117.0091971464681, 0.0), APoint(314.48484273659415, 117.02527409025072, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.4161340888504, 116.77978874721036, 0.0), APoint(314.71425113585184, 117.07790579421179, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.4840307614562, 116.67090872451948, 0.0), APoint(314.82313115854276, 117.01000912160603, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.60178693991236, 116.611888207679, 0.0), APoint(314.8821516753832, 116.8922529431499, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.5653618061992, 106.89779354430215, 0.0), APoint(322.86234360930257, 107.19477534740554, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.632649717684, 106.7883047604903, 0.0), APoint(322.9718323931144, 107.12748743592077, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.7497468426916, 106.72862519020131, 0.0), APoint(323.03151196340343, 107.01039031091312, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.5643504320682, 102.83091817834853, 0.0), APoint(322.8587200150299, 103.12528776131026, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.63026298643024, 102.7200540374139, 0.0), APoint(322.9695841559646, 103.05937520694827, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.74590031396815, 102.65891466965516, 0.0), APoint(323.03072352372334, 102.94373787941038, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.56506601983995, 116.81780797472592, 0.0), APoint(310.8331071479291, 117.0858491028151, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.6184989255262, 116.6944641851155, 0.0), APoint(310.95645093753956, 117.03241619712885, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.72250334430544, 116.62169190859811, 0.0), APoint(311.02922321405697, 116.92841177834961, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.9107665948652, 116.63317846386126, 0.0), APoint(311.0177366587938, 116.74014852778983, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.5376546382112, 103.00181435995948, 0.0), APoint(310.65440565250543, 103.11856537425366, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.53026111117816, 102.81764413762977, 0.0), APoint(310.8385758748351, 103.12595890128674, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.6039983784567, 102.71460470961166, 0.0), APoint(310.9416153028532, 103.0522216340082, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.7285185307961, 102.66234816665448, 0.0), APoint(310.9938718458104, 102.92770148166875, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.5013282796253, 102.89962400955089, 0.0), APoint(314.7045065211331, 103.10280225105869, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.5283982530462, 102.74991728767515, 0.0), APoint(314.85421324300887, 103.0757322776378, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.6149750792065, 102.65971741853883, 0.0), APoint(314.9444131121452, 102.9891554514775, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.7580785486105, 102.6260441926462, 0.0), APoint(314.97808633803777, 102.84605198207349, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.4577993269162, 106.89757243102494, 0.0), APoint(396.7549385418582, 107.19471164596692, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.5251712332391, 106.78816764205126, 0.0), APoint(396.86434333083184, 107.12733973964399, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.642358813438, 106.72857852695344, 0.0), APoint(396.9239324459297, 107.01015215944517, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.4567850137154, 102.83069412600145, 0.0), APoint(396.75131788668546, 103.1252269989715, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.52278255457327, 102.71991497156276, 0.0), APoint(396.8620970411241, 103.05922945811358, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.63850893710753, 102.65886465880033, 0.0), APoint(396.9231473538865, 102.94350307557934, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.51540789451616, 107.04543160808707, 0.0), APoint(310.7590544126267, 107.2890781261976, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.55854368935684, 106.91179070763107, 0.0), APoint(310.89269531308264, 107.24594233135693, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.6547509891337, 106.83122131211131, 0.0), APoint(310.97326470860247, 107.14973503158008, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.81762492877033, 106.81731855645134, 0.0), APoint(310.9871674642624, 106.98686109194341, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.2750068212575, 108.67850637122592, 0.0), APoint(317.5146932301375, 108.91819278010593, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.31653270842037, 108.54325556309216, 0.0), APoint(317.64994403827126, 108.87666689294305, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.4116449602024, 108.46159111957758, 0.0), APoint(317.7316084817858, 108.781554641161, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.5718530084702, 108.44502247254876, 0.0), APoint(317.74817712881463, 108.62134659289318, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.27664736223625, 116.4583215052567, 0.0), APoint(317.4869911595717, 116.66866530259212, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.3065217848778, 116.31141923260166, 0.0), APoint(317.6338934322267, 116.63879087995055, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.39458385459045, 116.22270460701765, 0.0), APoint(317.72260805781076, 116.55072881023796, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.5402983625203, 116.19164241965082, 0.0), APoint(317.75367024517755, 116.40501430230812, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.4753871326251, 108.69170234721119, 0.0), APoint(323.7014972541525, 108.91781246873862, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.51147459995343, 108.55101311924291, 0.0), APoint(323.8421864821208, 108.88172500141026, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.6031117397405, 108.46587356373331, 0.0), APoint(323.92732603763034, 108.79008786162322, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.75567936376194, 108.44166449245814, 0.0), APoint(323.95153510890555, 108.63752023760175, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.4789065920735, 116.47339639971165, 0.0), APoint(323.6719162651166, 116.66640607275477, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.5020040423867, 116.31971715472825, 0.0), APoint(323.8255955101, 116.64330862244152, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.5866057108269, 116.22754212787177, 0.0), APoint(323.9177705369565, 116.55870695400137, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.72641775948296, 116.19057748123119, 0.0), APoint(323.95473518359705, 116.41889490534528, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.6765906355773, 108.70572151478119, 0.0), APoint(329.8874780865832, 108.91660896578706, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.70667816636166, 108.55903235026886, 0.0), APoint(330.03416725109554, 108.88652143500275, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.7948562727871, 108.47043376139767, 0.0), APoint(330.12276583996675, 108.7983433285773, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.94078010610883, 108.4395808994228, 0.0), APoint(330.1536187019416, 108.65241949525554, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.68249857883325, 116.48980405108914, 0.0), APoint(329.8555086137407, 116.6628140859966, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.6977656632465, 116.32829444020575, 0.0), APoint(330.01701822462417, 116.64754700158338, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.7788881679576, 116.23264024962016, 0.0), APoint(330.1126724152097, 116.5664244968723, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.9133364731076, 116.19031185947361, 0.0), APoint(330.1550008053563, 116.43197619172224, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.8788112866763, 108.72075783049783, 0.0), APoint(336.0724417708677, 108.91438831468929, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.90215122259787, 108.56732107112278, 0.0), APoint(336.22587853024277, 108.8910483787677, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.98686925850427, 108.47526241173259, 0.0), APoint(336.31793718963297, 108.80633034286126, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(336.12686990967603, 108.4384863676077, 0.0), APoint(336.3547132337578, 108.66632969168948, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.88795708776036, 116.50807822463392, 0.0), APoint(336.0372344401967, 116.65735557707029, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.8938182156789, 116.33716265725586, 0.0), APoint(336.2081500075747, 116.65149444915168, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.97142512910693, 116.23799287538725, 0.0), APoint(336.30731978944334, 116.57388753572369, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(336.10092826940985, 116.19071932039354, 0.0), APoint(336.3545933444371, 116.44438439542076, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.08235165825477, 108.73711386669405, 0.0), APoint(342.25608573466815, 108.9108479431074, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.0979032900125, 108.5758888031551, 0.0), APoint(342.4173107982071, 108.89529631134974, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.17914307436706, 108.48035189221305, 0.0), APoint(342.5128477091491, 108.81405652699515, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.31376407863445, 108.43819620118384, 0.0), APoint(342.55500340017835, 108.67943552272772, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.0963830380448, 116.52931983953604, 0.0), APoint(342.2159928252921, 116.64892962678337, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.09017560709606, 116.34633571329069, 0.0), APoint(342.39897695153746, 116.65513705773212, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.1642118199867, 116.24359523088467, 0.0), APoint(342.50171743394344, 116.58110084484147, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.2891015014875, 116.19170821708887, 0.0), APoint(342.55360444773925, 116.45621116334063, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.2877345501686, 108.75531242322556, 0.0), APoint(348.43788717813743, 108.90546505119441, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.2939458649781, 108.58474704273846, 0.0), APoint(348.60845255862455, 108.8992537363849, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.37167157672997, 108.48569605919364, 0.0), APoint(348.7075035421694, 108.82152802463308, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.5013349207691, 108.43858270793618, 0.0), APoint(348.7546168934268, 108.69186468059391, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.31104771000867, 116.55680017611768, 0.0), APoint(348.38851248870986, 116.63426495481885, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.28685454914887, 116.35583031996123, 0.0), APoint(348.58948234486627, 116.65845811567863, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.357244676408, 116.24944375192375, 0.0), APoint(348.69586891290373, 116.58806798841947, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.4777872366408, 116.19320961685989, 0.0), APoint(348.75210304796764, 116.46752542818672, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.4960300007283, 108.77642353840298, 0.0), APoint(354.6167760629602, 108.8971696006349, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.4902927695592, 108.59390961193724, 0.0), APoint(354.799289989426, 108.902906831804, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.56444994892564, 108.49129009600705, 0.0), APoint(354.9019095053561, 108.82874965243755, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.6894898568963, 108.43955330868103, 0.0), APoint(354.95364629268215, 108.70370974446693, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.48387517539425, 116.36566661082433, 0.0), APoint(354.77964605400393, 116.661437489434, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.55052126331685, 116.25553600345029, 0.0), APoint(354.88977666137794, 116.5947914015114, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.6669321921559, 116.1951702369927, 0.0), APoint(354.95014242783554, 116.47838047267236, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.7103564278493, 108.80356563014173, 0.0), APoint(360.7896339712231, 108.8828431735155, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.6869606122448, 108.60339311924051, 0.0), APoint(360.9898064821243, 108.90623898912008, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.75747458761646, 108.4971303993156, 0.0), APoint(361.09606920204925, 108.83572501374836, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.8781593255658, 108.44103844196826, 0.0), APoint(361.15216115939654, 108.71504027579903, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.68126187358115, 116.3758689736289, 0.0), APoint(360.9694436912015, 116.66405079124924, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.7440402209627, 116.26187062571383, 0.0), APoint(361.0834420391165, 116.60127244386767, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.85649429278635, 116.19754800224084, 0.0), APoint(361.1477646625895, 116.48881837204402, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.8839693996369, 108.61321757125035, 0.0), APoint(367.17998203011484, 108.90923020172826, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9507430208602, 108.50321449717705, 0.0), APoint(367.2899851041881, 108.84245658050494, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.06728960163366, 108.44298438265386, 0.0), APoint(367.3502152187113, 108.72590999973147, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.8790444275122, 116.38646719217766, 0.0), APoint(367.1588454726525, 116.66626823731795, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9378012353509, 116.26844730471971, 0.0), APoint(367.27686536011043, 116.60751142947926, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.04643975051533, 116.20030912458753, 0.0), APoint(367.3450035402426, 116.4988729143148, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.2698254526628, 116.24691813143836, 0.0), APoint(367.2983945333918, 116.27548721216733, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.0813433602206, 108.62340719645181, 0.0), APoint(373.36979240491047, 108.91185624114166, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.1442538534201, 108.50954099435461, 0.0), APoint(373.48365860700767, 108.84894574794222, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.2568382875056, 108.44534873314356, 0.0), APoint(373.54785086821875, 108.73636131385666, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.0772596185369, 116.39749804782008, 0.0), APoint(373.3478146170072, 116.66805304629034, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.13180503147464, 116.27526676546123, 0.0), APoint(373.470045899366, 116.61350763335258, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.2367410744925, 116.20342611318239, 0.0), APoint(373.5418865516449, 116.50857159033478, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.42943043052946, 116.21933877392274, 0.0), APoint(373.52597389090454, 116.31588223429779, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.0620262005027, 108.76525527190208, 0.0), APoint(382.19861578151097, 108.9018448529103, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.06277605421417, 108.58922843031687, 0.0), APoint(382.3746426230962, 108.90109499919885, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.13874923818736, 108.48842491899342, 0.0), APoint(382.4754461344196, 108.82512181522569, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.26609433881777, 108.43899332432713, 0.0), APoint(382.5248777290859, 108.6977767145953, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.0961825379624, 116.57758620241378, 0.0), APoint(382.13839791446424, 116.6198015789156, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.0560120083747, 116.36063897752939, 0.0), APoint(382.35534513934863, 116.65997210850333, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.1245687588472, 116.25241903270532, 0.0), APoint(382.4635650841727, 116.59141535803079, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.24304876476407, 116.19412234332549, 0.0), APoint(382.52186177355253, 116.47293535211395, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.2726090273694, 108.78865376338644, 0.0), APoint(388.3752172900268, 108.89126202604382, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.2592790240193, 108.59854706473973, 0.0), APoint(388.5653239886735, 108.90459202939391, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.33164948513655, 108.4941408305603, 0.0), APoint(388.6697302228529, 108.83222156827665, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.4545106999576, 108.44022535008475, 0.0), APoint(388.72364570332843, 108.7093603534556, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.25320988500835, 116.37065251878076, 0.0), APoint(388.5453315980975, 116.66277423186997, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.3179650246159, 116.25863096309163, 0.0), APoint(388.65735315378663, 116.5980190922624, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.4324042076445, 116.19629345082362, 0.0), APoint(388.71969066605465, 116.48357990923381, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.49474727850503, 108.82360767913974, 0.0), APoint(394.54026337427103, 108.86912377490577, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.4561123321778, 108.60819603751588, 0.0), APoint(394.7556750158949, 108.90775872123302, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.5247946416398, 108.50010165168132, 0.0), APoint(394.86376940172954, 108.839076411771, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.6434134355021, 108.44194375024696, 0.0), APoint(394.92192730316384, 108.72045761790866, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.0379630233486, 116.43789123584878, 0.0), APoint(395.2702579409969, 116.67018615349707, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.0765145518384, 116.29966606904193, 0.0), APoint(395.4084831078037, 116.63163462500731, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.16968442040996, 116.21605924231693, 0.0), APoint(395.49208993452874, 116.5384647564357, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.3254838558198, 116.19508198243014, 0.0), APoint(395.5130671944155, 116.38266532102583, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.54875242109426, 108.62976831456686, 0.0), APoint(401.83224102152707, 108.91325691499969, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.6092511028585, 108.51349030103447, 0.0), APoint(401.94851903505946, 108.85275823323542, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.7195069851483, 108.44696948802763, 0.0), APoint(402.0150398480663, 108.74250235094564, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.5452177296403, 116.40440821616494, 0.0), APoint(401.80971418339396, 116.66890466991862, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.59710192682513, 116.27951571805312, 0.0), APoint(401.9346066815058, 116.61702047273377, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.69984013822034, 116.20547723415169, 0.0), APoint(402.0086451654072, 116.5142822613386, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.8828153865343, 116.21167578716901, 0.0), APoint(402.0024466123899, 116.3313070130246, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.5285961026485, 107.1695325196934, 0.0), APoint(314.59572414636216, 107.23666056340707, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.4998121151395, 106.96397183688772, 0.0), APoint(314.80128482916786, 107.26544455091611, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.56955159291186, 106.85693461936347, 0.0), APoint(314.9083220466921, 107.19570507314373, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.6893532106934, 106.79995954184837, 0.0), APoint(314.9652971242072, 107.0759034553622, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(409.9900479149952, 106.99479217655951, 0.0), APoint(410.19741144306863, 107.20215570463293, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(410.0187550302785, 106.84672259654619, 0.0), APoint(410.3454810230819, 107.17344858934959, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(410.1061895188543, 106.75738038982536, 0.0), APoint(410.43482322980276, 107.08601410077381, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(410.2507855669874, 106.7251997426618, 0.0), APoint(410.4670038769663, 106.9414180526407, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(409.99080490612755, 102.92968517586925, 0.0), APoint(410.19201948351565, 103.13089975325735, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(410.01710738301836, 102.77921095746333, 0.0), APoint(410.3424937019215, 103.10459727636655, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(410.1032910377177, 102.68861791686612, 0.0), APoint(410.4330867425188, 103.01841362166721, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(410.24572355347834, 102.65427373733007, 0.0), APoint(410.46743092205486, 102.87598110590659, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.6314376616971, 107.00534677398312, 0.0), APoint(400.82664733057385, 107.20055644285992, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.6553943928824, 106.85252680987188, 0.0), APoint(400.97946729468515, 107.17659971167458, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.74041085084536, 106.76076657253816, 0.0), APoint(401.07122753201884, 107.09158325371163, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.8808981094172, 106.72447713581337, 0.0), APoint(401.10751696874365, 106.95109599513981, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.6325025719734, 102.94054769243684, 0.0), APoint(400.82094745192427, 103.12899257238769, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.65381657380016, 102.78508499896697, 0.0), APoint(400.97641014539414, 103.10767857056095, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.73757871901915, 102.6920704488893, 0.0), APoint(401.06942469547187, 103.02391642534198, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.87604868518736, 102.65376371976086, 0.0), APoint(401.1077314246003, 102.88544645917378, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.58447895821087, 107.00864060219112, 0.0), APoint(405.77579680122136, 107.19995844520162, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.6069155315974, 106.85430048028098, 0.0), APoint(405.93013692313156, 107.17752187181515, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.6912027627932, 106.76181101618013, 0.0), APoint(406.0226263872323, 107.09323464061933, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.8305083564487, 106.72433991453906, 0.0), APoint(406.06009748887345, 106.9539290469638, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.5856491081987, 102.94394676035631, 0.0), APoint(405.76999168285994, 103.12828933501754, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.60535908937175, 102.78688004623268, 0.0), APoint(405.92705839698357, 103.1085793538445, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.6883903639742, 102.6931346255385, 0.0), APoint(406.02080381767774, 103.02554807924207, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.8257176211838, 102.65368518745143, 0.0), APoint(406.0602532557648, 102.88822082203248, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(271.0152756819639, 106.9665024466848, 0.0), APoint(271.40416450023866, 107.35539126495961, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(271.0379697830915, 106.81241985251583, 0.0), APoint(271.55824709440765, 107.33269716383194, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(271.100296485751, 106.69796985987865, 0.0), APoint(271.6726970870448, 107.27037046117248, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(271.1911174403016, 106.61201411913257, 0.0), APoint(271.7586528277909, 107.17954950662192, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(271.3112564268431, 106.55537641037753, 0.0), APoint(271.81529053654594, 107.05941052008032, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(271.4759458999034, 106.5432891881412, 0.0), APoint(271.8273777587823, 106.89472104702004, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.4522462388787, 106.9442107295752, 0.0), APoint(264.82715686187095, 107.31912135256748, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.47100211221317, 106.78618990761305, 0.0), APoint(264.9851776838331, 107.300365479233, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.53112974748507, 106.6695408475883, 0.0), APoint(265.1018267438579, 107.24023784396111, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.62003611527746, 106.58167052008409, 0.0), APoint(265.1896970713621, 107.1513314761687, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.7378962970448, 106.52275400655476, 0.0), APoint(265.2486135848914, 107.0334712944014, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.8981693863008, 106.50625040051415, 0.0), APoint(265.2651171909321, 106.87319820514537, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.431095654121, 102.85719615299486, 0.0), APoint(264.6977460399784, 103.12384653885228, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.41788272317825, 102.66720652675548, 0.0), APoint(264.8877356662178, 103.13705946979502, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.4637443265207, 102.5362914348013, 0.0), APoint(265.018650758172, 103.09119786645256, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.5412369227289, 102.43700733571285, 0.0), APoint(265.1179348572604, 103.01370527024437, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.6465244874598, 102.36551820514715, 0.0), APoint(265.1894239878261, 102.90841770551343, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(264.7859089465694, 102.32812596896005, 0.0), APoint(265.2268162240132, 102.7690332464039, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(265.00592724929055, 102.3713675763846, 0.0), APoint(265.18357461658866, 102.5490149436827, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.15776096180305, 281.9934839476452, 0.0), APoint(37.30782301773077, 282.1435460035729, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.19007597057626, 281.8490222611217, 0.0), APoint(37.535330183031704, 282.1942764735772, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.22239097934944, 281.7045605745983, 0.0), APoint(37.76283734833261, 282.2450069435815, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.25470598812264, 281.5600988880749, 0.0), APoint(37.9903445136335, 282.29573741358575, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.28702099689585, 281.4156372015515, 0.0), APoint(38.21785167893444, 282.34646788359004, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.31933600566906, 281.271175515028, 0.0), APoint(38.445358844235344, 282.3971983535943, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.35165101444224, 281.12671382850453, 0.0), APoint(38.67286600953625, 282.44792882359855, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.38396602321542, 280.9822521419811, 0.0), APoint(38.900373174837185, 282.4986592936029, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.41628103198863, 280.8377904554577, 0.0), APoint(39.12788034013809, 282.5493897636071, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.448596040761814, 280.69332876893424, 0.0), APoint(38.960307489904935, 282.20504021807733, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.480911049535024, 280.54886708241077, 0.0), APoint(38.65293590927894, 281.7208919421547, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.513226058308206, 280.40440539588735, 0.0), APoint(38.34556432865294, 281.2367436662321, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.545541067081416, 280.25994370936394, 0.0), APoint(38.038192748026944, 280.75259539030947, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.5778560758546, 280.11548202284047, 0.0), APoint(37.73082116740092, 280.2684471143868, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.40450203810532, 261.8156038214887, 0.0), APoint(24.57400108117288, 261.98510286455627, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.436817046878474, 261.6711421349652, 0.0), APoint(24.8015082464739, 262.0358333345606, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.4691320556517, 261.5266804484418, 0.0), APoint(25.029015411774935, 262.08656380456506, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.50144706442491, 261.3822187619184, 0.0), APoint(25.2565225770759, 262.1372942745694, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.533762073198062, 261.23775707539494, 0.0), APoint(25.484029742376947, 262.1880247445738, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.5660770819713, 261.0932953888715, 0.0), APoint(25.711536907677967, 262.2387552145782, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.59839209074451, 260.9488337023481, 0.0), APoint(25.93904407297896, 262.28948568458253, 0.0))
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

entity = acad.model.AddLine(APoint(24.663022108290903, 260.65991032930117, 0.0), APoint(26.394058403581028, 262.3909466245913, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.695337117064142, 260.5154486427778, 0.0), APoint(26.173223006884385, 261.99333453259806, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.727652125837352, 260.37098695625434, 0.0), APoint(25.865851426256825, 261.50918625667384, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.759967134610534, 260.2265252697309, 0.0), APoint(25.558479845629975, 261.02503798075037, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.792282143383773, 260.0820635832075, 0.0), APoint(25.25110826500537, 260.5408897048291, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(24.824597152156954, 259.93760189668404, 0.0), APoint(24.94373668438068, 260.0567414289078, 0.0))
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

entity = acad.model.AddLine(APoint(59.636129303974116, 270.70750348815864, 0.0), APoint(61.015533127235415, 272.0869073114199, 0.0))
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

entity = acad.model.AddLine(APoint(59.81293302037545, 270.53075381396667, 0.0), APoint(61.01546785555206, 271.7332886491433, 0.0))
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

entity = acad.model.AddLine(APoint(59.98973673677682, 270.35400413977476, 0.0), APoint(61.015402583868706, 271.37966998686665, 0.0))
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

entity = acad.model.AddLine(APoint(60.166540453178214, 270.1772544655829, 0.0), APoint(61.01533731218532, 271.02605132458996, 0.0))
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

entity = acad.model.AddLine(APoint(60.34334416957955, 270.00050479139094, 0.0), APoint(61.015272040502, 270.6724326623134, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.43174602778025, 269.912129954295, 0.0), APoint(61.015239404660306, 270.49562333117507, 0.0))
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

entity = acad.model.AddLine(APoint(60.696951602382285, 269.6470054430071, 0.0), APoint(61.01514149713529, 269.9651953377601, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.78535346058298, 269.55863060591116, 0.0), APoint(61.0151088612936, 269.7883860066218, 0.0))
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

entity = acad.model.AddLine(APoint(36.46673914846147, 230.5675505841688, 0.0), APoint(37.884184239903476, 231.9849956756108, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.64348321996219, 230.56751796037287, 0.0), APoint(37.972526447178055, 231.89656118758876, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.82022729146294, 230.567485336577, 0.0), APoint(38.060868654452634, 231.80812669956669, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.99697136296365, 230.5674527127811, 0.0), APoint(38.1492108617272, 231.71969221154464, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.1737154344644, 230.56742008898522, 0.0), APoint(38.23755306900175, 231.63125772352254, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.35045950596512, 230.56738746518928, 0.0), APoint(38.32589527627633, 231.5428232355005, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.52720357746587, 230.5673548413934, 0.0), APoint(38.414237483550906, 231.45438874747845, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.70394764896659, 230.56732221759748, 0.0), APoint(38.502579690825485, 231.36595425945637, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.880691720467254, 230.5672895938015, 0.0), APoint(38.59092189810006, 231.2775197714343, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.05743579196778, 230.5672569700054, 0.0), APoint(38.679264105374614, 231.18908528341223, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.234179863468356, 230.56722434620934, 0.0), APoint(38.76760631264919, 231.10065079539015, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.410923934968906, 230.56719172241324, 0.0), APoint(38.85594851992374, 231.01221630736808, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.58766800646946, 230.56715909861714, 0.0), APoint(38.94429072719829, 230.923781819346, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.76441207797001, 230.56712647482107, 0.0), APoint(39.03263293447287, 230.83534733132393, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(38.94115614947053, 230.56709385102494, 0.0), APoint(39.12097514174745, 230.74691284330186, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(39.11790022097108, 230.56706122722886, 0.0), APoint(39.20931734902203, 230.6584783552798, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(39.29464429247163, 230.5670286034328, 0.0), APoint(39.29765955629661, 230.57004386725777, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.561730708716595, 181.89120385398934, 0.0), APoint(61.00560332841749, 183.33507647369024, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.650132566917286, 181.8028290168934, 0.0), APoint(61.00557069257581, 183.15826714255192, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.738534425118026, 181.7144541797975, 0.0), APoint(61.00553805673413, 182.9814578114136, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.826936283318766, 181.62607934270162, 0.0), APoint(61.00550542089244, 182.8046484802753, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.91533814151948, 181.5377045056057, 0.0), APoint(61.00547278505076, 182.62783914913697, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.00373999972019, 181.44932966850976, 0.0), APoint(61.005440149209086, 182.45102981799866, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.09214185792093, 181.36095483141386, 0.0), APoint(61.00540751336741, 182.27422048686034, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.18054371612167, 181.27257999431797, 0.0), APoint(61.00537487752576, 182.09741115572206, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.26894557432235, 181.184205157222, 0.0), APoint(61.005342241684055, 181.9206018245837, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.35734743252309, 181.0958303201261, 0.0), APoint(61.00530960584228, 181.74379249344528, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.4457492907238, 181.00745548303018, 0.0), APoint(61.00527697000047, 181.56698316230685, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.53415114892453, 180.91908064593426, 0.0), APoint(61.00524433415871, 181.39017383116845, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.62255300712525, 180.83070580883836, 0.0), APoint(61.00521169831691, 181.21336450003002, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.71095486532599, 180.74233097174246, 0.0), APoint(61.00517906247512, 181.0365551688916, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.799356723526685, 180.65395613464653, 0.0), APoint(61.005146426633345, 180.85974583775317, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.88775858172741, 180.5655812975506, 0.0), APoint(61.00511379079157, 180.68293650661477, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.97616043992815, 180.4772064604547, 0.0), APoint(61.00508115494978, 180.50612717547634, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.43645037005209, 231.28584596112907, 0.0), APoint(115.87725103772809, 232.72664662880507, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.61319444155274, 231.2858133373331, 0.0), APoint(115.96559324500262, 232.638212140783, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.78993851305346, 231.28578071353718, 0.0), APoint(116.05393545227712, 232.54977765276084, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.9666825845542, 231.2857480897413, 0.0), APoint(116.14227765955164, 232.46134316473874, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.14342665605487, 231.28571546594532, 0.0), APoint(116.23061986682616, 232.37290867671663, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.32017072755559, 231.2856828421494, 0.0), APoint(116.31896207410071, 232.28447418869453, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.49691479905634, 231.2856502183535, 0.0), APoint(116.4073042813752, 232.19603970067237, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.67365887055706, 231.2856175945576, 0.0), APoint(116.49564648864973, 232.10760521265027, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.85040294205776, 231.28558497076165, 0.0), APoint(116.58398869592422, 232.0191707246281, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(116.02714701355848, 231.28555234696574, 0.0), APoint(116.67233090319877, 231.93073623660604, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(116.2038910850592, 231.28551972316984, 0.0), APoint(116.76067311047329, 231.8423017485839, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(116.38063515655992, 231.2854870993739, 0.0), APoint(116.84901531774779, 231.75386726056178, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(116.55737922806063, 231.285454475578, 0.0), APoint(116.93735752502229, 231.66543277253967, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(116.73412329956133, 231.28542185178205, 0.0), APoint(117.02569973229686, 231.57699828451757, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(116.91086737106204, 231.28538922798614, 0.0), APoint(117.11404193957136, 231.48856379649547, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.08761144256277, 231.2853566041902, 0.0), APoint(117.20238414684587, 231.4001293084733, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.26435551406348, 231.2853239803943, 0.0), APoint(117.29072635412041, 231.31169482045124, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.352295327137654, 108.6799828036763, 0.0), APoint(21.382200838834777, 108.70988831537342, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.352295327137654, 108.50320610837966, 0.0), APoint(21.558977534131415, 108.70988831537342, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.352295327137654, 108.32642941308302, 0.0), APoint(21.735754229428053, 108.70988831537342, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.352295327137654, 108.14965271778638, 0.0), APoint(21.91253092472469, 108.70988831537342, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.352295327137654, 107.97287602248974, 0.0), APoint(22.08930762002133, 108.70988831537342, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.352295327137654, 107.7960993271931, 0.0), APoint(22.26608431531797, 108.70988831537342, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.352295327137654, 107.61932263189647, 0.0), APoint(22.442861010614607, 108.70988831537342, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.352295327137654, 107.44254593659983, 0.0), APoint(22.619637705911245, 108.70988831537342, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.25537641493133, 118.16885032909687, 0.0), APoint(32.709968654647916, 118.62344256881346, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.36350134480127, 118.10019856367018, 0.0), APoint(32.788540536407304, 118.52523775527621, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.471626274671245, 118.03154679824351, 0.0), APoint(32.86711241816668, 118.42703294173896, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.5797512045412, 117.96289503281685, 0.0), APoint(32.945684299926064, 118.3288281282017, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.68787613441116, 117.89424326739015, 0.0), APoint(33.02425618168544, 118.23062331466443, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.79600106428112, 117.82559150196349, 0.0), APoint(33.10282806344481, 118.13241850112718, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.90412599415108, 117.7569397365368, 0.0), APoint(33.1813999452042, 118.03421368758993, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.01225092402104, 117.68828797111013, 0.0), APoint(33.25997182696357, 117.93600887405265, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.120375853891, 117.61963620568343, 0.0), APoint(33.33854370872296, 117.8378040605154, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.22850078376096, 117.55098444025677, 0.0), APoint(33.41711559048233, 117.73959924697814, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.33662571363091, 117.48233267483009, 0.0), APoint(33.49568747224171, 117.6413944334409, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.44475064350085, 117.4136809094034, 0.0), APoint(33.5742593540011, 117.54318961990364, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.55287557337083, 117.34502914397673, 0.0), APoint(33.65283123576047, 117.44498480636638, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.66100050324077, 117.27637737855004, 0.0), APoint(33.73140311751985, 117.34677999282911, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.769125433110744, 117.20772561312337, 0.0), APoint(33.809974999279234, 117.24857517929186, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.87725036298069, 117.13907384769668, 0.0), APoint(33.88854688103861, 117.1503703657546, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.35229532713766, 86.93644928218995, 0.0), APoint(21.38354900563995, 86.96770296069225, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.35229532713766, 86.75967258689332, 0.0), APoint(21.560325700936588, 86.96770296069225, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.35229532713766, 86.58289589159668, 0.0), APoint(21.737102396233226, 86.96770296069225, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.35229532713766, 86.40611919630004, 0.0), APoint(21.913879091529864, 86.96770296069225, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.35229532713766, 86.2293425010034, 0.0), APoint(22.090655786826495, 86.96770296069224, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.35229532713766, 86.05256580570676, 0.0), APoint(22.267432482123134, 86.96770296069224, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.35229532713766, 85.87578911041012, 0.0), APoint(22.444209177419772, 86.96770296069224, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.35229532713766, 85.69901241511349, 0.0), APoint(22.62098587271641, 86.96770296069224, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.07116950963746, 77.99326539515455, 0.0), APoint(21.115223578929463, 78.03731946444655, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.07116950963746, 77.81648869985791, 0.0), APoint(21.203611926577782, 77.94893111679824, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.071169509637457, 77.63971200456128, 0.0), APoint(21.292000274226083, 77.8605427691499, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.071169509637457, 77.46293530926464, 0.0), APoint(21.380388621874403, 77.77215442150158, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.071169509637464, 77.28615861396801, 0.0), APoint(21.46877696952272, 77.68376607385326, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.071169509637464, 77.10938191867137, 0.0), APoint(21.557165317171034, 77.59537772620493, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.07116950963747, 76.93260522337474, 0.0), APoint(21.64555366481934, 77.5069893785566, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.07116950963747, 76.7558285280781, 0.0), APoint(21.733942012467658, 77.41860103090829, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.223491210594542, 76.73137353373853, 0.0), APoint(21.822330360115973, 77.33021268325997, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.40026790589118, 76.73137353373853, 0.0), APoint(21.910718707764286, 77.24182433561164, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.57704460118782, 76.73137353373853, 0.0), APoint(21.999107055412605, 77.15343598796332, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.75382129648445, 76.73137353373853, 0.0), APoint(22.08749540306091, 77.06504764031499, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(21.930597991781088, 76.73137353373853, 0.0), APoint(22.17588375070923, 76.97665929266667, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(22.107374687077723, 76.73137353373853, 0.0), APoint(22.264272098357537, 76.88827094501835, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(22.28415138237436, 76.73137353373853, 0.0), APoint(22.352660446005856, 76.79988259737003, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.47895386407521, 127.45130228128647, 0.0), APoint(76.01475893094648, 127.98710734815775, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.5736942952373, 127.36926601715193, 0.0), APoint(76.24843619681604, 128.04400791873067, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.66843472639941, 127.2872297530174, 0.0), APoint(76.31344804032466, 127.93224306694265, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.76317515756149, 127.20519348888284, 0.0), APoint(76.37845988383327, 127.82047821515462, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.8579155887236, 127.12315722474831, 0.0), APoint(76.44347172734189, 127.7087133633666, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.9526560198857, 127.04112096061377, 0.0), APoint(76.50848357085052, 127.59694851157859, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.0473964510478, 126.95908469647924, 0.0), APoint(76.57349541435912, 127.48518365979055, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.14213688220988, 126.87704843234468, 0.0), APoint(76.63850725786774, 127.37341880800254, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.23687731337199, 126.79501216821015, 0.0), APoint(76.70351910137636, 127.26165395621452, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.33161774453409, 126.7129759040756, 0.0), APoint(76.76853094488497, 127.14988910442649, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.42635817569618, 126.63093963994106, 0.0), APoint(76.83354278839359, 127.03812425263847, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.5210986068583, 126.54890337580655, 0.0), APoint(76.89855463190221, 126.92635940085046, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.61583903802038, 126.46686711167199, 0.0), APoint(76.96356647541081, 126.81459454906242, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.71057946918248, 126.38483084753744, 0.0), APoint(77.02857831891944, 126.70282969727441, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.80531990034459, 126.30279458340291, 0.0), APoint(77.09359016242804, 126.59106484548637, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.9000603315067, 126.22075831926838, 0.0), APoint(77.15860200593667, 126.47929999369836, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.99480076266877, 126.13872205513383, 0.0), APoint(77.22361384944526, 126.36753514191034, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.08954119383088, 126.0566857909993, 0.0), APoint(77.28862569295387, 126.25577029012231, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.18428162499296, 125.97464952686477, 0.0), APoint(77.35363753646251, 126.14400543833429, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.27902205615504, 125.89261326273021, 0.0), APoint(77.4186493799711, 126.03224058654627, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.37376248731718, 125.81057699859568, 0.0), APoint(77.48366122347974, 125.92047573475824, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.46850291847926, 125.72854073446115, 0.0), APoint(77.54867306698833, 125.80871088297022, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.56324334964135, 125.6465044703266, 0.0), APoint(77.61368491049697, 125.69694603118222, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.65798378080343, 125.56446820619205, 0.0), APoint(77.67869675400557, 125.58518117939418, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.18368220074206, 109.73304189806916, 0.0), APoint(132.1977987563407, 109.74715845366781, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.27207054839042, 109.64465355042088, 0.0), APoint(132.37457545163733, 109.74715845366781, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.36045889603872, 109.55626520277256, 0.0), APoint(132.55135214693397, 109.74715845366781, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.44884724368708, 109.46787685512429, 0.0), APoint(132.7281288422306, 109.74715845366781, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.53723559133542, 109.37948850747598, 0.0), APoint(132.90490553752724, 109.74715845366781, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.62562393898378, 109.29110015982769, 0.0), APoint(133.08168223282388, 109.74715845366782, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.71401228663214, 109.20271181217942, 0.0), APoint(133.25845892812052, 109.74715845366782, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.80240063428047, 109.11432346453111, 0.0), APoint(133.43523562341716, 109.74715845366782, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.89078898192884, 109.02593511688285, 0.0), APoint(133.51956564514427, 109.65471178009828, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.97917732957717, 108.93754676923454, 0.0), APoint(133.51956564514427, 109.47793508480164, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.0675656772255, 108.84915842158625, 0.0), APoint(133.51956564514427, 109.301158389505, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.15595402487384, 108.76077007393795, 0.0), APoint(133.51956564514427, 109.12438169420837, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.2443423725222, 108.67238172628966, 0.0), APoint(133.51956564514424, 108.94760499891171, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.33273072017056, 108.5839933786414, 0.0), APoint(133.51956564514424, 108.77082830361508, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.4211190678189, 108.49560503099308, 0.0), APoint(133.51956564514424, 108.59405160831844, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.50950741546723, 108.40721668334477, 0.0), APoint(133.51956564514424, 108.4172749130218, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.18435628414463, 87.9901824599854, 0.0), APoint(132.19914692314583, 88.00497309898661, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.272744631793, 87.90179411233711, 0.0), APoint(132.37592361844247, 88.00497309898661, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.36113297944135, 87.81340576468884, 0.0), APoint(132.5527003137391, 88.00497309898661, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.44952132708968, 87.72501741704053, 0.0), APoint(132.72947700903575, 88.00497309898661, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.53790967473802, 87.63662906939226, 0.0), APoint(132.90625370433239, 88.00497309898662, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.62629802238638, 87.54824072174395, 0.0), APoint(133.08303039962905, 88.00497309898665, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.71468637003468, 87.45985237409565, 0.0), APoint(133.2598070949257, 88.00497309898665, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.80307471768305, 87.37146402644737, 0.0), APoint(133.43658379022233, 88.00497309898665, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.8914630653314, 87.28307567879907, 0.0), APoint(133.51956564514424, 87.9111782586119, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.97985141297974, 87.19468733115077, 0.0), APoint(133.51956564514424, 87.73440156331527, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.0682397606281, 87.1062989835025, 0.0), APoint(133.51956564514424, 87.55762486801865, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.15662810827644, 87.0179106358542, 0.0), APoint(133.51956564514424, 87.38084817272201, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.2450164559248, 86.92952228820592, 0.0), APoint(133.51956564514424, 87.20407147742537, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.33340480357313, 86.84113394055761, 0.0), APoint(133.51956564514424, 87.02729478212873, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.42179315122146, 86.75274559290932, 0.0), APoint(133.51956564514424, 86.8505180868321, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.5101814988698, 86.66435724526102, 0.0), APoint(133.51956564514424, 86.67374139153546, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.56941921399036, 77.76864367203291, 0.0), APoint(133.80069146264353, 78.99991592068608, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.746195909287, 77.76864367203291, 0.0), APoint(133.80069146264353, 78.82313922538944, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(132.92297260458363, 77.76864367203291, 0.0), APoint(133.80069146264353, 78.6463625300928, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.09974929988027, 77.76864367203291, 0.0), APoint(133.80069146264353, 78.46958583479616, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.2765259951769, 77.76864367203291, 0.0), APoint(133.80069146264353, 78.29280913949952, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.45330269047355, 77.76864367203291, 0.0), APoint(133.80069146264353, 78.11603244420289, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(133.6300793857702, 77.76864367203291, 0.0), APoint(133.80069146264353, 77.93925574890625, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

try:
    acad_doc = acad.app.ActiveDocument
    acad_doc.SaveAs(file_path)
    print(f'[INFO] Drawing saved successfully at {file_path}')
except Exception as e:
    print(f'[Error] Failed saving drawing: {e}')
