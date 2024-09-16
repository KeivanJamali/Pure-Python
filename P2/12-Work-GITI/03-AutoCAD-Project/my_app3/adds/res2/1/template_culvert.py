file_path = r'D:/All Python/Pure-Python/P2/12-Work-GITI/03-AutoCAD-Project/my_app3/adds/res2/1\Culvert-Final.dwg'
file_to_open = r'D:/All Python/Pure-Python/P2/12-Work-GITI/03-AutoCAD-Project/my_app3/adds/res2/1\Culvert.dwg'
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

entity = acad.model.AddLine(APoint(53.62958936968698, 210.9027016323535, 0.0), APoint(99.73930419797307, 237.5241579007216, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.78709589337814, 238.1291007181182, 0.0), APoint(117.27653103445755, 247.6492805356052, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306439, 208.2956508247851, 0.0), APoint(99.73930419797307, 235.7921070931526, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.7870958933795, 236.3970499105493, 0.0), APoint(117.27653103445755, 245.9172297280362, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306439, 205.98624974802672, 0.0), APoint(99.73930419797307, 233.48270601639447, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.7870958933795, 234.0876488337913, 0.0), APoint(117.27653103445755, 243.6078286512784, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306439, 180.5828379036829, 0.0), APoint(99.73930419797443, 208.0792941720508, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.78709589337723, 208.6842369894473, 0.0), APoint(117.27653103445755, 218.20441680693438, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306439, 176.5413860193549, 0.0), APoint(99.73930419797443, 204.0378422877233, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.78709589337723, 204.64278510511969, 0.0), APoint(117.27653103445755, 214.162964922607, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306439, 178.2734368269234, 0.0), APoint(99.73930419797443, 205.7698930952921, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.78709589337814, 206.3748359126889, 0.0), APoint(105.99166308000895, 209.3796941789054, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.78685906850751, 210.9935013353027, 0.0), APoint(117.27653103445755, 215.895015730176, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.27653103445755, 214.16296492260662, 0.0), APoint(115.7609865778345, 213.28796492260662, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306439, 210.0277016323535, 0.0), APoint(53.62958936968698, 210.9027016323535, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.73930419797307, 241.40818145969308, 0.0), APoint(99.73930419797307, 200.2499297671699, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.78709589337814, 241.4767699351834, 0.0), APoint(100.78709589337723, 200.2108079112833, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.85056195639527, 191.0360341695378, 0.0), APoint(46.00680962818069, 189.95060192705637, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.42946319614248, 188.4632045125698, 0.0), APoint(44.71813641215931, 189.2069032198129, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.973935633197016, 190.49644642037111, 0.0), APoint(43.42946319614248, 188.4632045125698, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.20275686482546, 235.02811202907623, 0.0), APoint(122.42007567750898, 233.9786328722677, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.74722930188045, 237.0613539368773, 0.0), APoint(126.7801032968614, 236.5155094435628, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('1', APoint(43.03061411934004, 190.8696927732072, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddText('1', APoint(123.79068054793515, 237.3144338038862, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(79.02815774840928, 188.7400294138938, 0.0), APoint(80.11358999089043, 186.8962770856786, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.60098740537842, 184.31893065364062, 0.0), APoint(80.8572886981342, 185.60760386965813, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.5677454975762, 184.86340309069521, 0.0), APoint(81.60098740537842, 184.31893065364062, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('2', APoint(79.1944991447399, 183.92008157683892, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(117.52653103446119, 218.454416806938, 0.0), APoint(142.05026723020728, 218.4544168069389, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.27653103445755, 218.20441680693438, 0.0), APoint(142.0502672302082, 218.20441680693528, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.77653103446119, 216.704416806938, 0.0), APoint(142.0502672302082, 216.7044168069387, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.27653103445755, 209.4737966518999, 0.0), APoint(142.0502672302082, 212.8001043871217, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.27653103445937, 215.9544168069404, 0.0), APoint(142.0502672302082, 215.95441680693912, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.276531034458, 216.704416806938, 0.0), APoint(117.27653103445755, 209.4737966518999, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.55536980237548, 243.53311402859728, 0.0), APoint(142.05026723020728, 268.0280114564275, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.276531034458, 243.60782865127896, 0.0), APoint(142.0502672302082, 268.3815648470254, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.77653103446119, 244.22914899483487, 0.0), APoint(142.05026723020728, 270.50288519057995, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.276531034458, 254.4932338864627, 0.0), APoint(142.05026723020728, 273.4018496901802, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.27653103445755, 246.7898091666109, 0.0), APoint(142.05026723020728, 271.563545362362, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.27653103445755, 218.20441680693438, 0.0), APoint(117.27653103445755, 243.60782865127823, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.52653103446119, 218.454416806938, 0.0), APoint(117.52653103446119, 243.60782865127823, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.77653103446119, 216.704416806938, 0.0), APoint(115.77653103446119, 244.22914899483487, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.276531034458, 216.70441680693813, 0.0), APoint(117.276531034458, 218.454416806938, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(142.05026723020728, 268.0280114564275, 0.0), APoint(142.05026723020728, 273.4018496901802, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.276531034458, 245.7291489948321, 0.0), APoint(117.276531034458, 254.4932338864627, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.276531034458, 245.7291489948321, 0.0), APoint(117.276531034458, 243.60782865127896, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(142.0502672302082, 212.8001043871217, 0.0), APoint(142.0502672302082, 218.4544168069389, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.8640449130603, 205.73624974802297, 0.0), APoint(27.3403087173142, 205.7362497480221, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306439, 205.98624974802672, 0.0), APoint(27.34030871731329, 205.9862497480257, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.6140449130603, 207.48624974802297, 0.0), APoint(27.34030871731329, 207.4862497480224, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306439, 214.71686990306114, 0.0), APoint(27.34030871731329, 211.3905621678394, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.114044913062116, 208.2362497480207, 0.0), APoint(27.34030871731329, 208.23624974802186, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306348, 207.48624974802297, 0.0), APoint(52.11404491306439, 214.71686990306114, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.83520614514646, 180.6575525263637, 0.0), APoint(27.3403087173142, 156.1626550985335, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306348, 180.582837903682, 0.0), APoint(27.34030871731329, 155.8091017079356, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.6140449130603, 179.96151756012608, 0.0), APoint(27.3403087173142, 153.68778136438095, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306348, 169.69743266849838, 0.0), APoint(27.3403087173142, 150.7888168647808, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306439, 177.40085738835012, 0.0), APoint(27.34030871731511, 152.62712119259913, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306439, 205.98624974802672, 0.0), APoint(52.11404491306439, 180.5828379036829, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.8640449130603, 205.73624974802297, 0.0), APoint(51.8640449130603, 180.5828379036829, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.6140449130603, 207.48624974802297, 0.0), APoint(53.6140449130603, 179.96151756012608, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306348, 207.4862497480229, 0.0), APoint(52.11404491306348, 205.73624974802297, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(27.3403087173142, 156.1626550985335, 0.0), APoint(27.3403087173142, 150.7888168647808, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306348, 178.46151756012887, 0.0), APoint(52.11404491306348, 169.69743266849838, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.11404491306348, 178.46151756012887, 0.0), APoint(52.11404491306348, 180.582837903682, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(27.34030871731329, 211.3905621678394, 0.0), APoint(27.34030871731329, 205.7362497480221, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.16902490551638, 220.18533754350688, 0.0), APoint(59.08359266303387, 222.02908987172196, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.55177486430239, 224.58028565622172, 0.0), APoint(58.317683763666544, 223.33008892181417, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.041224714041164, 222.53826179876546, 0.0), APoint(57.55177486430239, 224.58028565622172, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('2', APoint(56.955163804822405, 221.1369836965229, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(39.46502585435837, 158.60694944306317, 0.0), APoint(41.059810658867264, 157.18067905210415, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.260639260739026, 155.17782629552318, 0.0), APoint(42.1602249598036, 156.1792526738123, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.158122517594165, 155.07809548211395, 0.0), APoint(43.260639260739026, 155.17782629552318, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(30.46863345962811, 166.86201483149364, 0.0), APoint(32.010593746435916, 165.48298720664445, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.36611671648234, 166.76228401808442, 0.0), APoint(28.26780485775771, 168.8648675880723, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('3', APoint(41.08946924533666, 154.06594181462117, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddText('3', APoint(28.415960030249153, 165.77407827946945, 0.0), 1.9756799999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(87.46973602635308, 239.6221832259758, 0.0), APoint(87.46973602635308, 174.03201884511384, 0.0))
entity.Color = 4


entity = acad.model.AddText('C.L.', APoint(84.66195479064027, 240.99976426383873, 0.0), 2.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(95.80199862056634, 214.6544390849809, 0.0), APoint(87.46973602635308, 214.6544390849809, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.46973602635308, 214.6544390849809, 0.0), APoint(94.90755915350155, 218.94866826962348, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(76.50307971466736, 208.29873342747382, 0.0), 7.795971336203397)
entity.Color = 8

entity = acad.model.AddLine(APoint(83.46646360184195, 204.7932443154194, 0.0), APoint(83.46646360184195, 211.8042225395283, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.46646360184332, 201.5854065891778, 0.0), APoint(80.4664636018415, 215.01206026576992, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.46646360184332, 200.56251596925583, 0.0), APoint(77.46646360184332, 216.0349508856917, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.4664636018415, 200.7734850007515, 0.0), APoint(74.46646360184332, 215.82398185419618, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.4664636018415, 202.3481311716566, 0.0), APoint(71.46646360184332, 213.8939751761904, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.23488100304212, 212.2306566831763, 0.0), APoint(69.73203364530991, 204.43478412636298, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.28327193222049, 208.7944935840256, 0.0), APoint(72.18364271613336, 201.8087693990222, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.02381781133136, 204.0258955239707, 0.0), APoint(76.94309683702204, 200.5151896325859, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.7491190991932, 214.8369532631751, 0.0), APoint(68.71779554915929, 207.89066537285547, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.88512089724009, 216.0701744762671, 0.0), APoint(70.08179375111149, 212.71962198625423, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('امتداد آرماتورگذاری', APoint(58.51325416543182, 194.0241121810668, 0.0), 1.2)
entity.Color = 1

entity = acad.model.AddLine(APoint(415.0, 25.0, 0.0), APoint(5.0, 25.0, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(296.64869948316027, 24.999999999999886, 0.0), APoint(296.64869948316027, 4.9999999999998295, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(254.5322609691102, 24.999999999999886, 0.0), APoint(254.5322609691102, 4.9999999999998295, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(212.4158224550606, 24.999999999999886, 0.0), APoint(212.4158224550606, 4.9999999999998295, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(170.2993839410101, 24.999999999999886, 0.0), APoint(170.2993839410101, 4.9999999999998295, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(128.1829454269605, 24.999999999999886, 0.0), APoint(128.1829454269605, 4.9999999999998295, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.06650691290997, 24.999999999999886, 0.0), APoint(86.06650691290997, 4.9999999999998295, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('شماره نقشه', APoint(200.49368829635068, 22.072322370501468, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('تاریخ ابلاغ', APoint(199.9868519745794, 12.305559378681723, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('محل آبرو', APoint(159.40757956441485, 12.219192808258414, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(296.64869948316027, 14.99999999999983, 0.0), APoint(86.06650691290997, 14.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('زاویه تورب', APoint(115.25055671659129, 12.147955604483004, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('دهانه آبرو', APoint(159.59764318507905, 22.124566619728455, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddCircle(APoint(95.0805428836643, 23.522472181921273, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(95.09918690330733, 22.3121487787904, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddText('بدون مقیاس', APoint(9.082975376366447, 8.349448666068952, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('حداکثر ارتفاع خاک روی آبرو', APoint(96.87525120747978, 21.999326525113194, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('پیمانکار', APoint(244.8114845156615, 22.091368192971686, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddCircle(APoint(243.94873313952917, 23.686461049723675, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(243.96737715917084, 22.476137646592463, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddText('کارفرما', APoint(288.39520168956074, 22.149569209571723, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('مهندس مشاور', APoint(283.709085654845, 12.372419330405478, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('عنوان پروژه', APoint(241.94294470532304, 11.987507165165084, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(204.5151660952879, 187.53197630981737, 0.0), APoint(206.76516609528153, 187.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.76516609528153, 187.53197630981737, 0.0), APoint(206.76516609528153, 184.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.91516609528617, 187.53197630981737, 0.0), APoint(206.91516609528617, 184.53197630981737, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.76516609528153, 184.53197630981737, 0.0), APoint(209.7651660952879, 184.53197630981737, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253149036, 160.15697630981742, 0.0), APoint(216.76816253148309, 160.15697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253148309, 152.65697630981742, 0.0), APoint(216.76816253148309, 152.65697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 184.53197630981737, 0.0), APoint(209.7651660952879, 182.2819763098173, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 182.2819763098173, 0.0), APoint(204.5151660952879, 182.2819763098173, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.5151660952879, 182.2819763098173, 0.0), APoint(204.5151660952879, 187.5319763098176, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 182.2819763098173, 0.0), APoint(209.7651660952879, 160.15697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.76816253149036, 160.15697630981742, 0.0), APoint(216.76816253148309, 152.65697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253149036, 160.15697630981742, 0.0), APoint(194.26816253148309, 152.65697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.5151660952879, 182.2819763098173, 0.0), APoint(196.26516609529244, 160.15697630981742, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.01516609527698, 187.53197630981737, 0.0), APoint(242.76516609528426, 187.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.76516609528426, 187.53197630981737, 0.0), APoint(242.76516609528426, 184.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.76516609528426, 184.53197630981737, 0.0), APoint(239.76516609528153, 184.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.76516609528153, 184.53197630981737, 0.0), APoint(239.76516609528153, 182.2819763098173, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.76516609528153, 182.2819763098173, 0.0), APoint(245.01516609527698, 182.2819763098173, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.01516609527698, 182.2819763098173, 0.0), APoint(245.01516609527698, 187.5319763098176, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.76516609528426, 184.53197630981737, 0.0), APoint(242.76516609528426, 187.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.91516609528617, 184.53197630981737, 0.0), APoint(242.76516609528426, 184.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.91516609528617, 187.53197630981737, 0.0), APoint(242.76516609528426, 187.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 78.25226789047542, 0.0), APoint(89.70644040441812, 78.80815197294567, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 78.81862988989968, 0.0), APoint(121.11803215741656, 79.12226789047565, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 85.75264288110066, 0.0), APoint(89.70644040441812, 86.30852696357101, 0.0))
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

entity = acad.model.AddLine(APoint(34.11803215740838, 110.12886160063368, 0.0), APoint(89.70644040441812, 110.68474568310398, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 110.69522360005794, 0.0), APoint(121.11803215741656, 110.99886160063397, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.3680321574152, 113.151511596884, 0.0), APoint(89.70644040441812, 113.6848956793541, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 113.69537359630812, 0.0), APoint(118.8680321574152, 113.976511596884, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(119.01803215741347, 115.87401159688392, 0.0), APoint(121.34303215741465, 115.87401159688409, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.4930321574202, 115.72401159688468, 0.0), APoint(121.4930321574202, 113.99901159688392, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.4930321574202, 113.99901159688392, 0.0), APoint(121.38382147819493, 113.99901159688392, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.22724283664729, 113.99901159688392, 0.0), APoint(121.11803215741656, 113.99901159688392, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(119.01803215741984, 115.87401159688392, 0.0), APoint(118.8680321574152, 115.72401159688377, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.34303215741465, 115.87401159688392, 0.0), APoint(121.4930321574202, 115.72401159688377, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(121.3055321574193, 113.99901159688392, 0.0), 0.0782893207747293, 0.0, 3.141592653589793)
entity.Color = 3

entity = acad.model.AddLine(APoint(118.8680321574152, 115.72401159688377, 0.0), APoint(118.8680321574152, 113.976511596884, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 110.12886160063368, 0.0), APoint(89.70644040441812, 110.68474568310393, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 110.69522360005794, 0.0), APoint(121.11803215741656, 110.99886160063392, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.11803215741656, 86.622642881101, 0.0), APoint(121.11803215741656, 110.99886160063392, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.21803215741829, 114.97401159688349, 0.0), APoint(33.89303215741711, 114.97401159688377, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.74303215741202, 114.82401159688442, 0.0), APoint(33.74303215741202, 113.0990115968836, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.74303215741202, 113.0990115968836, 0.0), APoint(33.85224283663638, 113.0990115968836, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.00882147818538, 113.0990115968836, 0.0), APoint(34.118032157416565, 113.0990115968836, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.21803215741011, 114.97401159688349, 0.0), APoint(36.3680321574152, 114.82401159688368, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.89303215741711, 114.97401159688349, 0.0), APoint(33.74303215741202, 114.82401159688368, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(33.93053215741202, 113.0990115968836, 0.0), 0.0782893207747293, 0.0, 3.141592653589793)
entity.Color = 3

entity = acad.model.AddLine(APoint(36.3680321574152, 114.82401159688368, 0.0), APoint(36.3680321574152, 113.151511596884, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.1180321574152, 85.75264288110066, 0.0), APoint(34.118032157416565, 110.12886160063368, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.11803215741656, 108.71971684538181, 0.0), APoint(90.75423209982318, 108.42587361901809, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.70644040441812, 108.41573369938516, 0.0), APoint(34.118032157416565, 107.8777813615107, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.741479991937, 271.0761334740793, 0.0), APoint(220.7914799918617, 271.0761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999192928, 267.8261334740793, 0.0), APoint(198.74147999192928, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999192928, 266.3261334740793, 0.0), APoint(198.74147999192928, 251.2277000613184, 0.0))
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

entity = acad.model.AddLine(APoint(198.74147999192928, 267.8261334740793, 0.0), APoint(220.74147999192928, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999192928, 269.8261334740793, 0.0), APoint(220.74147999192928, 269.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999192928, 269.8261334740793, 0.0), APoint(220.74147999192928, 269.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 267.8261334740793, 0.0), APoint(198.74147999192928, 267.8261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 251.5761334740793, 0.0), APoint(178.24147999193337, 251.5761334740793, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 256.5761334740793, 0.0), APoint(181.77921584098794, 256.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999192928, 271.0761334740793, 0.0), APoint(183.24147999193428, 257.8261334740816, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.77921584098794, 256.5761334740793, 0.0), APoint(178.24147999193337, 251.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 256.5761334740793, 0.0), APoint(183.24147999193428, 257.8261334740811, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 257.8261334740813, 0.0), APoint(181.77921584098794, 257.8261334740813, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.77921584098794, 256.5761334740793, 0.0), APoint(181.77921584098794, 257.8261334740813, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999192928, 267.8261334740793, 0.0), APoint(198.74147999192928, 271.0761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(197.27921584098522, 271.0761334740793, 0.0), APoint(181.77921584098794, 257.8261334740813, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(197.27921584098522, 271.0761334740793, 0.0), APoint(198.74147999192928, 271.0761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(178.24147999193337, 251.5761334740793, 0.0), APoint(172.9335499324834, 252.01135797166899, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.24147999193428, 251.5761334740793, 0.0), APoint(189.4410131229365, 251.0539502832963, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(189.4410131229365, 251.0539502832963, 0.0), APoint(200.64822693209362, 251.2633215911043, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.64822693209362, 251.2633215911043, 0.0), APoint(211.42529451850942, 250.9029351190267, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(211.42529451850942, 250.9029351190267, 0.0), APoint(216.04158886143932, 251.6893309586859, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.04158886143932, 251.6893309586859, 0.0), APoint(225.29147999192946, 251.5761334740793, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.29147999192946, 251.5761334740793, 0.0), APoint(232.5669078654314, 251.2624148575024, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 267.8261334740793, 0.0), APoint(220.7914799918617, 266.3261334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 266.3261334740793, 0.0), APoint(220.7914799918617, 251.2277000613184, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.2914799918617, 256.5761334740793, 0.0), APoint(236.2914799918617, 251.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.2914799918617, 251.5761334740793, 0.0), APoint(241.29147999186216, 251.5761334740793, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.2914799918617, 256.5761334740793, 0.0), APoint(237.7537441428076, 256.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 271.0761334740793, 0.0), APoint(236.2914799918617, 257.8261334740816, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.7537441428076, 256.5761334740793, 0.0), APoint(241.29147999186216, 251.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.2914799918617, 256.5761334740793, 0.0), APoint(236.2914799918617, 257.8261334740811, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.2914799918617, 257.8261334740814, 0.0), APoint(237.7537441428076, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.7537441428076, 256.5761334740793, 0.0), APoint(237.7537441428076, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 267.8261334740793, 0.0), APoint(220.7914799918617, 271.0761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.25374414280986, 271.0761334740793, 0.0), APoint(237.7537441428076, 257.8261334740814, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.25374414280986, 271.0761334740793, 0.0), APoint(220.7914799918617, 271.0761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(241.29147999186216, 251.5761334740793, 0.0), APoint(244.93365816394726, 251.9484906238674, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.2914799918617, 251.5761334740793, 0.0), APoint(232.5669078654314, 251.2624148575024, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(314.64631940552, 152.1282230355635, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(322.796013843059, 142.24462586855947, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(322.796013843059, 138.1741269083485, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(310.8031946451215, 152.1282230355635, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(310.75537976149417, 138.1813428089988, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(314.7388572787886, 138.1457758099176, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddLine(APoint(321.26368239231806, 140.25547581312333, 0.0), APoint(312.7261675199061, 140.2554758131231, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(312.7355260958079, 150.8260076358098, 0.0), APoint(312.7261675199061, 140.2554758131231, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(316.10132268504685, 140.2554758131231, 0.0), APoint(314.7388572787886, 138.1457758099176, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.75537976149417, 138.1813428089988, 0.0), APoint(312.7261675199061, 140.2554758131231, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.75537976149417, 142.32960881724716, 0.0), APoint(312.7261675199061, 140.2554758131231, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.64631940552, 152.1282230355635, 0.0), APoint(312.7355260958079, 150.84052238110968, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.80319464513605, 152.12822303556146, 0.0), APoint(312.7355260958079, 150.8260076358098, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.83447015075444, 138.13524338432916, 0.0), APoint(321.26368239231806, 140.25547581312333, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.83447015075444, 142.28350939257808, 0.0), APoint(321.26368239231806, 140.25547581312333, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.73205442140306, 142.2744832337538, 0.0), APoint(316.10132268504685, 140.2554758131231, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.7150066166414, 152.2763933520942, 0.0), APoint(354.7150066166414, 155.6084208077653, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.11500661664286, 152.2763933520942, 0.0), APoint(367.11500661664286, 155.6084208077653, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.11500661664286, 155.60842080776666, 0.0), APoint(354.7150066166414, 155.6084208077653, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(354.7150066166414, 151.7108086062163, 0.0), 0.5655847458779121)
entity.Color = 8

entity = acad.model.AddCircle(APoint(367.11500661664286, 151.7108086062163, 0.0), 0.5655847458779121)
entity.Color = 8

entity = acad.model.AddLine(APoint(360.9150066166426, 152.2763933520942, 0.0), APoint(360.9150066166426, 155.6084208077653, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(360.9150066166426, 151.7108086062163, 0.0), 0.5655847458779121)
entity.Color = 8

entity = acad.model.AddLine(APoint(403.4582339857434, 143.18973187781563, 0.0), APoint(395.6582339857546, 143.18973187781563, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.0261675196657, 146.18973187781563, 0.0), APoint(317.0261675196657, 151.5897318778156, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(317.62616751966607, 151.5897318778156, 0.0), 0.6, 1.5707963267948966, 3.141592653589793)
entity.Color = 6

entity = acad.model.AddLine(APoint(317.62616751966607, 152.18973187781563, 0.0), APoint(324.12616751970154, 152.18973187781563, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(324.12616751970154, 152.18973187781563, 0.0), APoint(332.1261675197002, 144.18973187781563, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(332.1261675197002, 144.18973187781563, 0.0), APoint(377.74293745552313, 144.18973187781563, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.2889364553862, 144.18973187781563, 0.0), APoint(401.85823398571347, 144.18973187781563, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(401.85823398571347, 144.7897318778156, 0.0), 0.6, 4.71238898038469, 0.0)
entity.Color = 6

entity = acad.model.AddLine(APoint(402.4582339857134, 144.7897318778156, 0.0), APoint(402.4582339857134, 150.18973187781518, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.25874123683525, 146.1754966004351, 0.0), APoint(402.25874123683525, 151.57549660043514, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.65874123683534, 152.1754966004351, 0.0), APoint(395.15874123680123, 152.1754966004351, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(401.65874123683534, 151.57549660043514, 0.0), 0.6, 0.0, 1.5707963267948966)
entity.Color = 6

entity = acad.model.AddLine(APoint(395.15874123680123, 152.1754966004351, 0.0), APoint(387.15874123680123, 144.1754966004351, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(387.15874123680123, 144.1754966004351, 0.0), APoint(379.0894437064512, 144.1754966004351, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(340.9073363251282, 144.18973187781563, 0.0), APoint(318.3380387948009, 144.18973187781563, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(318.3380387948009, 144.7897318778156, 0.0), 0.6, 3.141592653589793, 4.71238898038469)
entity.Color = 6

entity = acad.model.AddLine(APoint(317.7380387948024, 144.7897318778156, 0.0), APoint(317.7380387948024, 150.18973187781518, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.6582339857141, 148.78973187781548, 0.0), APoint(402.6582339857655, 151.5897318778055, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(402.05823398576604, 151.5897318778164, 0.0), 0.5999999999994543, 6.283185307161396, 1.5707963267935323)
entity.Color = 6

entity = acad.model.AddLine(APoint(402.05823398576604, 152.18973187781563, 0.0), APoint(379.4889364553883, 152.18973187781563, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 152.18973187781563, 0.0), APoint(317.62616751966607, 152.18973187781563, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(317.62616751966425, 151.5897318778164, 0.0), 0.599999999999227, 1.5707963267962606, 3.1415926535909295)
entity.Color = 6

entity = acad.model.AddLine(APoint(317.0261675196657, 151.5897318778156, 0.0), APoint(317.0261675196657, 148.78973187781548, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(317.62616751966607, 151.5897318778156, 0.0), 0.6, 1.5707963267948966, 3.141592653589793)
entity.Color = 6

entity = acad.model.AddCircle(APoint(310.75537976149417, 142.32960881724716, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(317.51500661663977, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(317.51500661663977, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(323.7150066166423, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(323.7150066166423, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(329.9150066166426, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(329.9150066166426, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(336.1150066166424, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(336.1150066166424, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(342.31500661663995, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(342.31500661663995, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(348.51500661664113, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(348.51500661664113, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(354.7150066166414, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(354.7150066166414, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(360.9150066166426, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(360.9150066166426, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(367.11500661664286, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(367.11500661664286, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(373.31500661663995, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(373.31500661663995, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(382.2856780686916, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(382.2856780686916, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(388.4856780686914, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(388.4856780686914, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(394.6856780686894, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(395.3785645887642, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(401.783816351372, 143.95869554273668, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(401.783816351372, 151.7108086062163, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddLine(APoint(354.7140853435503, 143.39311154718376, 0.0), APoint(354.7086578505682, 140.06108851189947, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.114068893266, 143.37291336037788, 0.0), APoint(367.10864140028434, 140.0408903250937, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.10864140028434, 140.04089032509228, 0.0), APoint(354.7086578505682, 140.06108851189947, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(354.7150066166414, 143.95869554273668, 0.0), 0.565584745877912)
entity.Color = 8

entity = acad.model.AddCircle(APoint(367.11499016636117, 143.9384973559309, 0.0), 0.565584745877912)
entity.Color = 8

entity = acad.model.AddLine(APoint(360.9140771184084, 143.3830124537808, 0.0), APoint(360.9086496254258, 140.0509894184966, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(360.914998391499, 143.94859644933376, 0.0), 0.565584745877912)
entity.Color = 8

entity = acad.model.AddCircle(APoint(314.7285135327602, 142.3172456913245, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(314.7416946106432, 157.2774517187582, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(407.07668729458555, 157.77849558658727, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(331.607455822691, 160.8815609617689, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(377.04208592492114, 161.69936638179462, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(377.1207634907055, 135.9568099317333, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(335.9973867618255, 131.59039139301876, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddCircle(APoint(339.06166857780636, 136.4965733479708, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddText('جزئیات الف', APoint(368.6567824975498, 83.95959904378628, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(367.68077228686025, 82.71575512073593, 0.0), APoint(383.4490482671895, 82.71575512073593, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.68077228686025, 82.14504733553099, 0.0), APoint(383.4490482671895, 82.14504733553099, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(375.9585020662121, 102.75471267642865, 0.0), APoint(384.6476848294401, 102.84160450406114, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9585020662116, 95.16433768580328, 0.0), APoint(384.72268107972104, 95.34197947593839, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9585020662116, 95.16433768580328, 0.0), APoint(366.9585020662116, 102.66471267642879, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(368.4585020662116, 95.81865167216313, 0.0), APoint(368.4585020662116, 101.8251704392033, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(368.05850206621017, 101.8251704392033, 0.0), 0.4, 0.0, 0.6959394611362671)
entity.Color = 6

entity = acad.model.AddLine(APoint(365.4585020662116, 102.66471267642879, 0.0), APoint(365.4585020662116, 109.56471267642729, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9585020662116, 103.91096394905577, 0.0), APoint(366.9585020662116, 108.26471267642864, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(367.35850206621353, 108.26471267642864, 0.0), 0.4, 1.5707963267948966, 3.141592653589793)
entity.Color = 6

entity = acad.model.AddLine(APoint(375.9585020662121, 102.75471267642865, 0.0), APoint(375.9585020662121, 109.5647126764282, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(374.4585020662121, 95.97366580509197, 0.0), APoint(374.4585020662121, 108.26471267642864, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(374.05850206621017, 108.26471267642864, 0.0), 0.4, 0.0, 1.5707963267948966)
entity.Color = 6

entity = acad.model.AddLine(APoint(366.05850206621335, 110.16471267642879, 0.0), APoint(375.358502066209, 110.16471267642879, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.35850206621353, 108.66471267642879, 0.0), APoint(374.05850206621017, 108.66471267642879, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(365.4585020662116, 102.66471267642879, 0.0), APoint(365.9478983311442, 102.66471267642879, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.46910580127496, 102.66471267642879, 0.0), APoint(366.9585020662116, 102.66471267642879, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(366.2085020662116, 102.66471267642879, 0.0), 0.2606037350650894, 0.0, 3.141592653589793)


entity = acad.model.AddLine(APoint(365.4585020662116, 109.56471267642866, 0.0), APoint(366.05850206621017, 110.16471267642879, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(375.9585020662121, 109.56471267642866, 0.0), APoint(375.358502066209, 110.16471267642879, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(384.6476848294401, 104.13557496274353, 0.0), APoint(384.6476848294401, 99.30818339431664, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(384.6476848294401, 97.22001442029944, 0.0), APoint(384.6476848294401, 93.643901848111, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(384.66384884959416, 98.68645158449783, 0.0), 0.6219418934983878, 0.0, 3.141592653589793)
entity.Color = 7

entity = acad.model.AddLine(APoint(384.0419069560958, 98.68645158449783, 0.0), APoint(385.2857907430903, 97.84174623011819, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(384.66384884959416, 97.84174623011819, 0.0), 0.6219418934983878, 3.141592653589793, 0.0)
entity.Color = 7

entity = acad.model.AddLine(APoint(367.0515213679282, 103.65452126368314, 0.0), APoint(368.3654827644964, 102.08161312457565, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(367.35850206621353, 103.91096394905577, 0.0), 0.4, 3.1415926535895657, 3.8375321147260597)
entity.Color = 6

entity = acad.model.AddCircle(APoint(373.9994069618474, 108.18301242059363, 0.0), 0.408)
entity.Color = 6

entity = acad.model.AddCircle(APoint(367.4355608630244, 108.1475591639383, 0.0), 0.408)
entity.Color = 6

entity = acad.model.AddCircle(APoint(367.39682459297865, 103.96987003551072, 0.0), 0.408)
entity.Color = 6

entity = acad.model.AddCircle(APoint(357.5458712720606, 91.1114470847831, 0.0), 1.875)
entity.Color = 8

entity = acad.model.AddLine(APoint(373.9994069618474, 108.18301242059363, 0.0), APoint(367.39682459297865, 103.96987003551072, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.4355608630244, 108.1475591639383, 0.0), APoint(370.6981157774135, 106.0764412280522, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(370.6981157774135, 106.0764412280522, 0.0), APoint(384.5608158476234, 106.0764412280522, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(385.87331584762205, 106.0764412280522, 0.0), 1.3125)
entity.Color = 8

entity = acad.model.AddLine(APoint(172.93354993248113, 274.3832343570766, 0.0), APoint(220.7914799918617, 274.38323435707673, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.7914799918617, 274.3832343570768, 0.0), APoint(244.93365816394817, 274.3832343570769, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(208.19804076070113, 272.26369861194064, 0.0), APoint(208.19804076070113, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.26666169488635, 273.32346648450834, 0.0), APoint(209.26666169488954, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(210.3352826290784, 272.26369861194064, 0.0), APoint(210.3352826290784, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(211.40390356326907, 273.32346648450834, 0.0), APoint(211.40390356326589, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(212.4725244974543, 272.26369861194064, 0.0), APoint(212.4725244974543, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(213.54114543164314, 273.32346648450834, 0.0), APoint(213.54114543164314, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(214.6097663658311, 272.26369861194064, 0.0), APoint(214.6097663658311, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(215.67838730002268, 273.32346648450834, 0.0), APoint(215.67838730001995, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.74700823420835, 272.26369861194064, 0.0), APoint(216.74700823420835, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(217.81562916839584, 273.32346648450834, 0.0), APoint(217.81562916839584, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.8842501025856, 272.26369861194064, 0.0), APoint(218.8842501025856, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.12941982651546, 273.32346648450834, 0.0), APoint(207.12941982651228, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.06079889232433, 272.26369861194064, 0.0), APoint(206.06079889232433, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.99217795813365, 273.32346648450834, 0.0), APoint(204.99217795813593, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.92355702394707, 272.26369861194064, 0.0), APoint(203.92355702394707, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(202.85493608975958, 273.32346648450834, 0.0), APoint(202.85493608975958, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(201.7863151555698, 272.26369861194064, 0.0), APoint(201.7863151555698, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.7176942213796, 273.32346648450834, 0.0), APoint(200.71769422138232, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(199.64907328719437, 272.26369861194064, 0.0), APoint(199.64907328719437, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.5804523530055, 273.32346648450834, 0.0), APoint(198.5804523530055, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(197.51183141881756, 272.26369861194064, 0.0), APoint(197.51183141881756, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.44321048462507, 273.32346648450834, 0.0), APoint(196.44321048462825, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(195.3745895504362, 269.4479851934493, 0.0), APoint(195.37458955043985, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.30596861625418, 272.2666483026921, 0.0), APoint(194.30596861625236, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(193.23734768207623, 267.6209881124309, 0.0), APoint(193.23734768206305, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.16872674787555, 271.20983012087345, 0.0), APoint(192.16872674787555, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.10010581367305, 265.79399103137644, 0.0), APoint(191.1001058136867, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(190.0314848794951, 270.1530119390542, 0.0), APoint(190.0314848794983, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(188.96286394531262, 263.9669939503591, 0.0), APoint(188.9628639453099, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(187.89424301112422, 269.0961937572363, 0.0), APoint(187.89424301112103, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(186.82562207691353, 262.1399968693085, 0.0), APoint(186.82562207693354, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(185.75700114274105, 268.0393755754184, 0.0), APoint(185.75700114274423, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(184.68838020855628, 260.3129997882928, 0.0), APoint(184.68838020855628, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(183.61975927437015, 267.5109664845086, 0.0), APoint(183.61975927436833, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.5511383401531, 258.48600270723875, 0.0), APoint(182.55113834017948, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.48251740599108, 267.5109664845086, 0.0), APoint(181.48251740599108, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(180.41389647180222, 254.64648209896183, 0.0), APoint(180.41389647180222, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(180.41389647182905, 254.6464820990001, 0.0), APoint(180.41389647180222, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(179.3452755376111, 267.5109664845086, 0.0), APoint(179.34527553761427, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(178.2766546033904, 251.6258469249379, 0.0), APoint(178.27665460342632, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.208033669237, 267.5109664845086, 0.0), APoint(177.208033669237, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(176.13941273504452, 251.74849278468298, 0.0), APoint(176.13941273504815, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(175.07079180085975, 267.5109664845086, 0.0), APoint(175.07079180085975, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(174.00217086663451, 250.8940565582, 0.0), APoint(174.00217086667226, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.9335499324843, 272.26369861194064, 0.0), APoint(172.9335499324843, 275.60069637734625, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.9335499324843, 275.60069637734625, 0.0), APoint(172.93354993248113, 263.8661142614273, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.93354993248113, 262.2999875309144, 0.0), APoint(172.9335499324843, 249.88684807843532, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(172.92142691736444, 263.39981540406325, 0.0), 0.4664564201237909, 0.0, 3.141592653589793)
entity.Color = 7

entity = acad.model.AddLine(APoint(173.3878833374888, 263.39981540406325, 0.0), APoint(172.45497049724236, 262.7662863882785, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(172.92142691736444, 262.7662863882785, 0.0), 0.4664564201237909, 3.141592653589793, 0.0)
entity.Color = 7

entity = acad.model.AddLine(APoint(172.9335499324843, 263.8661142614273, 0.0), APoint(172.9335499324843, 264.7798375281451, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.94432386308426, 262.3003922782585, 0.0), APoint(172.94432386308426, 261.54115175190327, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.93365816394817, 275.53782902954447, 0.0), APoint(244.93365816394544, 263.8032469136256, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.93365816394544, 262.23712018311267, 0.0), APoint(244.93365816394817, 249.8239807306336, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(244.92153514883057, 263.33694805626146, 0.0), 0.4664564201237909, 0.0, 3.141592653589793)
entity.Color = 7

entity = acad.model.AddLine(APoint(245.38799156895448, 263.33694805626146, 0.0), APoint(244.45507872870712, 262.7034190404768, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(244.92153514883057, 262.7034190404768, 0.0), 0.4664564201237909, 3.141592653589793, 0.0)
entity.Color = 7

entity = acad.model.AddLine(APoint(244.93365816394817, 263.8032469136256, 0.0), APoint(244.93365816394817, 264.7169701803434, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.94443209454948, 262.23752493045674, 0.0), APoint(244.94443209454948, 261.4782844041016, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.9528710367731, 273.32346648450834, 0.0), APoint(219.9528710367731, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.95943400937267, 273.32346648450834, 0.0), APoint(222.9594340093745, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.8908130751861, 272.26369861194064, 0.0), APoint(221.8908130751861, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.82219214099723, 273.32346648450834, 0.0), APoint(220.82219214099723, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.05837043335987, 269.4479851934494, 0.0), APoint(224.0583704333576, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.1269913675419, 272.2666483026921, 0.0), APoint(225.1269913675451, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.1956123017212, 267.6209881124309, 0.0), APoint(226.19561230173395, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(227.26423323592235, 271.20983012087345, 0.0), APoint(227.26423323592235, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.3328541701244, 265.79399103137644, 0.0), APoint(228.3328541701103, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.40147510430234, 270.1530119390542, 0.0), APoint(229.40147510429915, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(230.47009603848437, 263.9669939503592, 0.0), APoint(230.4700960384871, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(231.53871697267323, 269.0961937572364, 0.0), APoint(231.5387169726764, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(232.60733790688346, 262.1399968693085, 0.0), APoint(232.6073379068639, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(233.6759588410555, 268.0393755754184, 0.0), APoint(233.6759588410523, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(234.74457977524116, 260.3129997882929, 0.0), APoint(234.74457977524116, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(235.81320070942638, 267.5109664845086, 0.0), APoint(235.8132007094291, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.88182164364298, 258.48600270723887, 0.0), APoint(236.88182164361797, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.95044257780637, 267.5109664845086, 0.0), APoint(237.95044257780637, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.01906351199386, 254.64648209896183, 0.0), APoint(239.01906351199386, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.01906351196794, 254.6464820990001, 0.0), APoint(239.01906351199386, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.08768444618636, 267.5109664845086, 0.0), APoint(240.08768444618363, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(241.1563053804075, 251.6258469249379, 0.0), APoint(241.15630538037112, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.22492631456043, 267.5109664845086, 0.0), APoint(242.22492631456043, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.29354724875247, 251.74849278468298, 0.0), APoint(243.29354724874793, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.36216818293633, 267.5109664845086, 0.0), APoint(244.36216818293633, 274.3832343570768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(344.93487556371656, 125.99661698658241, 0.0), APoint(375.2157554761543, 125.99661698658218, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(344.9348755637152, 125.42590920137764, 0.0), APoint(375.2157554761543, 125.42590920137792, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('آرماتوربندی دال و شناژ', APoint(347.54533003915753, 127.43066788554711, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('مقطع', APoint(363.16604009873754, 122.17450940031199, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('2-2', APoint(356.18626412363346, 122.05086936042397, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('مقطع', APoint(225.90083531169807, 140.4994066639366, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(216.79688469293205, 139.1331307453936, 0.0), APoint(233.59097696382605, 139.13313074539366, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.7968846929316, 138.774739324616, 0.0), APoint(233.59097696382605, 138.774739324616, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('2-2', APoint(220.22398206534808, 140.3853608907583, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(206.83663942200747, 240.36805192973088, 0.0), APoint(216.23639829708418, 240.36805192973088, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.78969117079214, 239.7973441445262, 0.0), APoint(216.23639829708418, 239.7973441445262, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('نما', APoint(210.59123253430994, 240.80873106788772, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(204.70741408907043, 197.30947565572671, 0.0), APoint(245.68463405991315, 197.115752519331, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(228.23390423430556, 195.1292364399502, 0.0), APoint(228.23390423430556, 197.1982522622763, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.30252516848986, 196.18900431251797, 0.0), APoint(229.30252516849305, 197.19320026999543, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(230.37114610268145, 195.1292364399502, 0.0), APoint(230.37114610268145, 197.1881482777144, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(231.43976703687258, 196.18900431251797, 0.0), APoint(231.4397670368694, 197.1830962854334, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(232.50838797105962, 195.1292364399502, 0.0), APoint(232.50838797105962, 197.17804429315237, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(233.5770089052471, 196.18900431251797, 0.0), APoint(233.5770089052471, 197.1729923008715, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(234.64562983943551, 195.1292364399502, 0.0), APoint(234.64562983943551, 197.16794030859052, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(235.7142507736262, 196.18900431251797, 0.0), APoint(235.714250773623, 197.16288831630948, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(236.78287170781232, 195.1292364399502, 0.0), APoint(236.78287170781232, 197.1578363240285, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(237.85149264200118, 196.18900431251797, 0.0), APoint(237.85149264200118, 197.1527843317475, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(238.92011357618958, 195.1292364399502, 0.0), APoint(238.92011357618958, 197.14773233946647, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(227.16528330011852, 196.18900431251797, 0.0), APoint(227.1652833001176, 197.20330425455728, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.0966623659283, 195.1292364399502, 0.0), APoint(226.09666236592693, 197.20835624683826, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(225.02804143173717, 196.18900431251797, 0.0), APoint(225.02804143173944, 197.2134082391193, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(223.95942049755104, 195.1292364399502, 0.0), APoint(223.95942049755013, 197.2184602314003, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(222.8907995633631, 196.18900431251797, 0.0), APoint(222.89079956336127, 197.22351222368127, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.8221786291756, 195.1292364399502, 0.0), APoint(221.8221786291756, 197.2285642159623, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(220.75355769498356, 196.18900431251797, 0.0), APoint(220.75355769498674, 197.2336162082433, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(219.68493676079697, 195.1292364399502, 0.0), APoint(219.68493676079697, 197.23866820052433, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(218.61631582660948, 196.18900431251797, 0.0), APoint(218.61631582660948, 197.2437201928053, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(217.54769489242108, 195.1292364399502, 0.0), APoint(217.54769489242108, 197.24877218508618, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.4790739582295, 196.18900431251797, 0.0), APoint(216.47907395823313, 197.24877218508618, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.88809543598745, 157.3828462340885, 0.0), APoint(91.69416173486206, 157.3828462340885, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.90894162277164, 157.02445481331097, 0.0), APoint(91.69416173486206, 157.02445481331097, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('پلان', APoint(84.17189472048153, 158.76212824837512, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddText('مقطع', APoint(80.43956880076348, 60.63984467739118, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(72.41198738685307, 59.3301180327976, 0.0), APoint(87.72368283907826, 59.33011803279766, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.43552180255438, 58.97172661202012, 0.0), APoint(87.72368283907826, 58.97172661202001, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('1-1', APoint(73.97372668130038, 60.56774999780549, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(77.72399283695813, 134.94557844824334, 0.0), APoint(77.72399283695813, 72.02445643668318, 0.0))
entity.Color = 4


entity = acad.model.AddLine(APoint(89.70644040441812, 129.51093919296449, 0.0), APoint(89.70644040441812, 70.73665015866561, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 129.5541181096741, 0.0), APoint(90.75423209982318, 70.6970443310355, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('C.L.', APoint(74.91621160124487, 136.24193746297283, 0.0), 2.5)
entity.Color = 1

entity = acad.model.AddText('72.86', APoint(65.96961459937938, 125.65028739040292, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(118.8680321574152, 113.976511596884, 0.0), APoint(112.79991130282633, 117.79110114242167, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(36.3680321574152, 113.151511596884, 0.0), APoint(43.33776178696053, 117.79799801658032, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.33776178696053, 117.79799801658044, 0.0), APoint(77.72399283695813, 118.14186032708028, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.64035642685121, 117.41599771363548, 0.0), APoint(77.72924257447812, 117.61688657511166, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.70644040441994, 117.4970096020619, 0.0), APoint(77.72399283695813, 117.6168340777366, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.79991130282633, 117.79110114242167, 0.0), APoint(90.75423209982318, 118.01155793445167, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.08421524804453, 117.41599771363548, 0.0), APoint(90.74898236230365, 117.48658418248311, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.70644040441948, 118.02203585140569, 0.0), APoint(77.72399283695813, 118.14186032708028, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.08361411130863, 117.83826411433682, 0.0), APoint(108.08421524804453, 117.41599771363548, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.635106689330314, 117.9409714656041, 0.0), APoint(57.64035642685076, 117.41599771363548, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.58822750587933, 86.65497309898649, 0.0), APoint(126.58822750587933, 90.79824047936654, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(127.93822750587833, 86.65497309898649, 0.0), APoint(125.23822750587942, 86.65497309898649, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.58822750587933, 88.00497309898651, 0.0), APoint(127.93822750587833, 88.00497309898651, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(127.93822750587833, 88.00497309898651, 0.0), APoint(126.58822750587933, 86.65497309898649, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.58822750587933, 86.65497309898649, 0.0), APoint(125.23822750587942, 88.00497309898651, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(125.23822750587942, 88.00497309898651, 0.0), APoint(126.58822750587933, 88.00497309898651, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.58822750587933, 90.79824047936654, 0.0), APoint(134.68822750587697, 90.79824047936654, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(128.21935332337807, 79.11864367203276, 0.0), APoint(125.51935332338007, 79.11864367203276, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.86935332337953, 77.76864367203274, 0.0), APoint(128.21935332337807, 77.76864367203274, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(128.21935332337807, 77.76864367203274, 0.0), APoint(126.86935332337953, 79.11864367203276, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.86935332337953, 79.11864367203276, 0.0), APoint(126.86935332337953, 74.97537629165282, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(125.51935332338007, 77.76864367203274, 0.0), APoint(126.86935332337953, 77.76864367203274, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.86935332337953, 79.11864367203276, 0.0), APoint(125.51935332338007, 77.76864367203274, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.86935332337953, 74.97537629165282, 0.0), APoint(134.96935332337944, 74.97537629165282, 0.0))
entity.Color = 8


entity = acad.model.AddText('71.4', APoint(130.04656825892198, 76.21478786357733, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('72.2', APoint(128.3737502290519, 91.98447663885179, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(126.58822750587933, 108.3971584536676, 0.0), APoint(126.58822750587933, 112.54042583404771, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(127.93822750587833, 108.3971584536676, 0.0), APoint(125.23822750587942, 108.3971584536676, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.58822750587933, 109.74715845366768, 0.0), APoint(127.93822750587833, 109.74715845366768, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(127.93822750587833, 109.74715845366768, 0.0), APoint(126.58822750587933, 108.3971584536676, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.58822750587933, 108.3971584536676, 0.0), APoint(125.23822750587942, 109.74715845366768, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(125.23822750587942, 109.74715845366768, 0.0), APoint(126.58822750587933, 109.74715845366768, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(126.58822750587933, 112.54042583404771, 0.0), APoint(134.68822750587697, 112.54042583404771, 0.0))
entity.Color = 8


entity = acad.model.AddText('72.05', APoint(128.3737502290519, 113.72666199353301, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(29.188646833768416, 85.6177029606921, 0.0), APoint(29.188646833768416, 89.76097034107215, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.838646833769417, 85.6177029606921, 0.0), APoint(30.53864683376969, 85.6177029606921, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(29.188646833768416, 86.96770296069212, 0.0), APoint(27.838646833769417, 86.96770296069212, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.838646833769417, 86.96770296069212, 0.0), APoint(29.188646833768416, 85.6177029606921, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(29.188646833768416, 85.6177029606921, 0.0), APoint(30.53864683376969, 86.96770296069212, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(30.53864683376969, 86.96770296069212, 0.0), APoint(29.188646833768416, 86.96770296069212, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(29.188646833768416, 89.76097034107215, 0.0), APoint(21.088646833770326, 89.76097034107215, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.55752101627013, 78.08137353373837, 0.0), APoint(30.25752101626813, 78.08137353373837, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(28.907521016269584, 76.7313735337384, 0.0), APoint(27.55752101627013, 76.7313735337384, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.55752101627013, 76.7313735337384, 0.0), APoint(28.907521016269584, 78.08137353373837, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(28.907521016269584, 78.08137353373837, 0.0), APoint(28.907521016269584, 73.93810615335843, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(30.25752101626813, 76.7313735337384, 0.0), APoint(28.907521016269584, 76.7313735337384, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(28.907521016269584, 78.08137353373837, 0.0), APoint(30.25752101626813, 76.7313735337384, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(28.907521016269584, 73.93810615335843, 0.0), APoint(20.807521016269675, 73.93810615335843, 0.0))
entity.Color = 8


entity = acad.model.AddText('70.85', APoint(20.777925128345487, 75.17751772528294, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('71.65', APoint(22.450743158216483, 90.9472065005574, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(29.188646833768416, 107.35988831537327, 0.0), APoint(29.188646833768416, 111.50315569575332, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.838646833769417, 107.35988831537327, 0.0), APoint(30.53864683376969, 107.35988831537327, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(29.188646833768416, 108.70988831537329, 0.0), APoint(27.838646833769417, 108.70988831537329, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(27.838646833769417, 108.70988831537329, 0.0), APoint(29.188646833768416, 107.35988831537327, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(29.188646833768416, 107.35988831537327, 0.0), APoint(30.53864683376969, 108.70988831537329, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(30.53864683376969, 108.70988831537329, 0.0), APoint(29.188646833768416, 108.70988831537329, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(29.188646833768416, 111.50315569575332, 0.0), APoint(21.088646833770326, 111.50315569575332, 0.0))
entity.Color = 8


entity = acad.model.AddText('72.31', APoint(22.450743158216483, 112.68939185523857, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddCircle(APoint(404.8380820999073, 152.12822303556362, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(396.6883876623674, 138.1741269083485, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(408.6812068603017, 152.12822303556362, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(408.7290217439281, 138.18134280899892, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(404.79978053677587, 138.17773485867372, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(408.7290217439281, 142.32960881724728, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(404.75374372719534, 142.27306732653045, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddCircle(APoint(396.6883876623674, 142.22531845668652, 0.0), 0.2400000000008731)
entity.Color = 6

entity = acad.model.AddLine(APoint(121.11803215741656, 86.622642881101, 0.0), APoint(121.11803215741656, 79.12226789047565, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 85.75264288110066, 0.0), APoint(34.19302840769706, 78.25301785297825, 0.0))
entity.Color = 3
try:
    entity.LineType = 'HIDDEN'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 113.0990115968836, 0.0), APoint(34.11803215740838, 110.12886160063368, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.11803215741656, 113.99901159688392, 0.0), APoint(121.11803215741656, 110.99886160063392, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(338.7651379972099, 25.0, 0.0), APoint(338.7651379972099, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('موضوع نقشه', APoint(325.24199295895664, 21.799714221399825, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('نقشه همسان آبرو تک دهانه', APoint(306.4042280172498, 16.638741182673076, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddCircle(APoint(113.67680875801307, 13.522472181921444, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(113.6954527776561, 12.312148778790288, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddLine(APoint(11.631448686285239, 25.0, 0.0), APoint(11.631448686285239, 4.999999999999886, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(107.24191757088329, 210.4418041911152, 0.0), 1.6404919902232)
entity.Color = 8

entity = acad.model.AddLine(APoint(108.88135718932654, 210.38305295741, 0.0), APoint(108.01075731921219, 211.8909761655115, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.20100982176746, 209.1108811939889, 0.0), APoint(106.58932392666429, 211.9024030501499, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.94976276520492, 208.82753669794496, 0.0), APoint(105.69784351045519, 210.9959244541462, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.19329669713261, 212.08157551072722, 0.0), APoint(105.84614438857716, 211.3037967627438, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.31265190489148, 209.19892770651887, 0.0), APoint(107.782913013305, 208.8930828148615, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.79910477152544, 208.8622058894222, 0.0), APoint(108.8312962276027, 210.03549217363118, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.77138415211402, 209.7146553519705, 0.0), APoint(108.60691364730019, 211.3517490693107, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('امتداد آرماتورگذاری', APoint(104.5995941945007, 201.05945196963364, 0.0), 1.2)
entity.Color = 1

entity = acad.model.AddText('شناژ', APoint(109.21415134781387, 199.27417794338385, 0.0), 1.2)
entity.Color = 1

entity = acad.model.AddText('دال', APoint(63.92857004123107, 192.0623344474635, 0.0), 1.2)
entity.Color = 1

entity = acad.model.AddText('همسطح و مورب', APoint(313.1429416835854, 11.464809800513537, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('به اندازه', APoint(391.9758203544643, 183.64636633349699, 0.0), 2.25)
entity.Color = 1

entity = acad.model.AddText('بیشتر از مقادیر مندرج در نقشه شماره', APoint(326.17304463177675, 183.3673963529983, 0.0), 2.25)
entity.Color = 1

entity = acad.model.AddText('*', APoint(405.2973337893932, 183.2141000712155, 0.0), 2.625)
entity.Color = 1

entity = acad.model.AddText('c1', APoint(380.8998810642461, 185.11139214484535, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('cos(     )', APoint(378.3188168369352, 182.5039521159942, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(378.439720630437, 184.44893596492176, 0.0), APoint(385.69460605279255, 184.44893596492176, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(384.6462620797206, 183.58429867944437, 0.0), APoint(383.4467280669355, 182.4830018223659, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(383.4467280669355, 183.58429867944437, 0.0), APoint(384.6704958452019, 182.53141031118798, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(383.4467280669355, 183.03365025090523, 0.0), 0.5506484285392617, 1.5707963267948966, 4.71238898038469)
entity.Color = 1

entity = acad.model.AddText('-c1', APoint(386.2234724324294, 183.9645264447849, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('.منظور شود', APoint(375.10594050915824, 176.55772443054462, 0.0), 2.25)
entity.Color = 1

entity = acad.model.AddText('292-SB-D', APoint(392.06334397988167, 177.36932443520163, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('وزارت راه و شهرسازی - مرکز تحقیقات راه مسکن و شهرسازی', APoint(350.0534380347383, 14.572511580924534, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('نقشه های همسان آبروهای راه تا دهانه 10 متر نشریه شماره 1-292', APoint(348.8239903835097, 7.890691539354472, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(220.74147999192928, 269.8261334740793, 0.0), APoint(236.2914799918617, 256.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(198.74147999192928, 269.8261334740793, 0.0), APoint(183.24147999193428, 256.5761334740793, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('جزئیات الف', APoint(19.259631357859234, 120.02986833153568, 0.0), 1.75)
entity.Color = 1

entity = acad.model.AddCircle(APoint(35.42234060818919, 113.53782974353669, 0.0), 2.8560782053764338)
entity.Color = 8

entity = acad.model.AddLine(APoint(255.26216965907952, 160.1569763098173, 0.0), APoint(232.76216965908634, 160.1569763098173, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(255.26216965908634, 152.6569763098172, 0.0), APoint(232.76216965908634, 152.6569763098172, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.76516609528153, 182.2819763098173, 0.0), APoint(239.76516609528153, 160.1569763098173, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(232.76216965907952, 160.1569763098173, 0.0), APoint(232.76216965908634, 152.6569763098172, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(255.26216965907952, 160.1569763098173, 0.0), APoint(255.26216965908634, 152.6569763098172, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.01516609528153, 182.2819763098173, 0.0), APoint(253.26516609527698, 160.1569763098173, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('جزئیات دیوارهای هدایت آب', APoint(298.2578096517934, 71.91038753712746, 0.0), 3.0)
entity.Color = 1

entity = acad.model.AddText('مقطع', APoint(176.5158577004238, 38.023874834031574, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(168.1712378626189, 36.62681066297944, 0.0), APoint(184.25873710533142, 36.62681066297944, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(168.17427364620062, 36.268419242201844, 0.0), APoint(184.25873710533142, 36.268419242201674, 0.0))
entity.Color = 5
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('3-3', APoint(170.26308974957647, 37.85902144751435, 0.0), 2.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(181.16602653143264, 98.92379186092643, 0.0), APoint(177.66602653143264, 98.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.66602653143264, 98.92379186092643, 0.0), APoint(173.16602653143264, 96.67379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.16602653143264, 96.67379186092643, 0.0), APoint(160.58269319809915, 58.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143264, 98.92379186092643, 0.0), APoint(181.16602653143264, 58.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143264, 58.92379186092643, 0.0), APoint(160.58269319809915, 58.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319809915, 58.92379186092643, 0.0), APoint(160.58269319809915, 50.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143264, 58.92379186092643, 0.0), APoint(191.58269319809915, 58.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319809915, 58.92379186092643, 0.0), APoint(160.58269319809915, 48.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319809915, 48.92379186092643, 0.0), APoint(191.58269319809915, 48.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.58269319809915, 48.92379186092643, 0.0), APoint(191.58269319809915, 58.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.66602653143264, 98.92379186092643, 0.0), APoint(151.9304490792665, 105.34039198909107, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(167.42384745745903, 81.29164300551389, 0.0), APoint(165.89482353034828, 81.29164300551389, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(165.89482353034828, 81.29164300551389, 0.0), APoint(165.89482353034828, 76.70457122418168, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(167.42384745745903, 81.29164300551389, 0.0), APoint(165.89482353034828, 76.70457122418168, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.98873451038025, 196.16879634339398, 0.0), APoint(239.98873451037707, 197.1426803471855, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(241.05735544456593, 195.10902847082622, 0.0), APoint(241.05735544456593, 197.1376283549045, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.12597637875433, 196.16879634339398, 0.0), APoint(242.12597637875433, 197.13257636262352, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(243.1945973129432, 195.10902847082622, 0.0), APoint(243.1945973129432, 197.12752437034248, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(244.26321824713295, 196.14858837427, 0.0), APoint(244.26321824713114, 197.12247237806162, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(245.33183918131954, 195.08882050170223, 0.0), APoint(245.33183918131954, 197.11742038578063, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(215.41045302404427, 195.1443924167931, 0.0), APoint(215.41045302404427, 197.25382417736722, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(214.34183208985542, 196.2041602893609, 0.0), APoint(214.34183208985542, 197.2588761696482, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(213.27321115566747, 195.1443924167931, 0.0), APoint(213.27321115566747, 197.2639281619292, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(212.20459022147634, 196.2041602893609, 0.0), APoint(212.20459022147952, 197.2639281619292, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(211.13596928729112, 195.159548393636, 0.0), APoint(211.13596928729112, 197.26898015421017, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(210.06734835310226, 196.21931626620392, 0.0), APoint(210.06734835310226, 197.2740321464911, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(208.9987274189134, 195.159548393636, 0.0), APoint(208.9987274189134, 197.2790841387722, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.93010648472227, 196.21931626620392, 0.0), APoint(207.93010648472546, 197.2790841387722, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.86148555053705, 195.174704370479, 0.0), APoint(206.86148555053705, 197.28413613105312, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(205.79286461634956, 196.2344722430468, 0.0), APoint(205.79286461634956, 197.2891881233341, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.7242436821598, 195.174704370479, 0.0), APoint(204.7242436821598, 197.29424011561508, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('توضیحات', APoint(74.98512395632245, 22.30083814922626, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddCircle(APoint(74.70112806778988, 23.788064993747355, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(74.71977208743337, 22.57774159061637, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddText('شماره نقشه همسان', APoint(321.51274180805285, 6.3289799663040185, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddText('292-SB-1S-2/3', APoint(297.1715639958152, 6.479800353879966, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(338.7651379972099, 9.537644467135465, 0.0), APoint(296.64869948315936, 9.537644467135465, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('سازمان مدیریت برنامه ریزی کشور - امور نظام فنی اجرایی', APoint(350.3812911868647, 20.926001891046276, 0.0), 1.7)
entity.Color = 7

entity = acad.model.AddLine(APoint(320.69261141490006, 194.5304778217411, 0.0), APoint(320.69261141490006, 200.0579147034447, 0.0))



entity = acad.model.AddLine(APoint(320.69261141490006, 285.2804778217411, 0.0), APoint(408.4424045167534, 285.2804778217411, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 275.5304778217411, 0.0), APoint(408.4424045167534, 275.5304778217411, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 269.5304778217411, 0.0), APoint(408.4424045167534, 269.5304778217411, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 263.5304778217411, 0.0), APoint(408.4424045167534, 263.5304778217411, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 257.5304778217411, 0.0), APoint(408.4424045167534, 257.5304778217411, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 251.530477821741, 0.0), APoint(408.4424045167534, 251.530477821741, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 245.530477821741, 0.0), APoint(408.4424045167534, 245.530477821741, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 239.530477821741, 0.0), APoint(408.4424045167534, 239.530477821741, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 233.530477821741, 0.0), APoint(408.4424045167534, 233.530477821741, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 227.530477821741, 0.0), APoint(408.4424045167534, 227.530477821741, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 221.53047782174113, 0.0), APoint(408.4424045167534, 221.53047782174113, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 209.53047782174113, 0.0), APoint(408.4424045167534, 209.53047782174113, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 202.030477821741, 0.0), APoint(408.4424045167534, 202.030477821741, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(320.69261141490006, 285.2804778217411, 0.0), APoint(320.69261141490006, 194.5304778217411, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(327.44261141490097, 285.2804778217411, 0.0), APoint(327.44261141490006, 215.53047782174113, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(334.19261141490006, 285.2804778217411, 0.0), APoint(334.19261141490006, 215.53047782174113, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(340.94261141490006, 285.2804778217411, 0.0), APoint(340.94261141490006, 215.53047782174113, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.19240451675523, 285.2804778217411, 0.0), APoint(367.19240451675523, 215.53047782174113, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(375.4424045167534, 285.2804778217411, 0.0), APoint(375.4424045167534, 215.53047782174113, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(383.6924045167534, 285.2804778217411, 0.0), APoint(383.6924045167534, 215.53047782174113, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167534, 285.2804778217411, 0.0), APoint(391.9424045167534, 215.53047782174113, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167534, 285.2804778217411, 0.0), APoint(400.1924045167516, 215.53047782174113, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167516, 209.53047782174113, 0.0), APoint(400.1924045167516, 202.030477821741, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.4424045167534, 285.2804778217411, 0.0), APoint(408.4424045167534, 194.5304778217411, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('شماره', APoint(322.0863104274513, 279.38112851168285, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('قطر', APoint(329.2257135564596, 280.9594393556174, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('تعداد', APoint(335.1867702964764, 279.38015959310644, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('mm', APoint(329.87847795750076, 277.4555687533947, 0.0), 1.125)
entity.Color = 1

entity = acad.model.AddText('شکل آرماتور', APoint(346.66820195071796, 279.2079486952226, 0.0), 1.875)
entity.Color = 1

entity = acad.model.AddText('طول', APoint(369.8328992502011, 280.9954634549687, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('وزن کل', APoint(393.18727744914304, 282.4395964145922, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('طول کل', APoint(376.7079626048808, 280.99977427418287, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('وزن یکمتر', APoint(383.49721367705206, 281.0759927389771, 0.0), 1.274999999999999)
entity.Color = 1

entity = acad.model.AddText('وزن کل', APoint(400.95678790970305, 281.0316837878021, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('m', APoint(370.47990999607646, 276.915412132499, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('m', APoint(378.3644939416108, 276.915412132499, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('Kg/m', APoint(385.9544695478371, 276.9154121324988, 0.0), 1.274999999999999)
entity.Color = 1

entity = acad.model.AddText('Kg', APoint(394.86449394160627, 276.915412132499, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('Kg', APoint(403.11449394160627, 276.91541213249786, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('2', APoint(323.2163732246063, 265.37873384487307, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('1', APoint(323.2163732246063, 271.37873384487307, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('3', APoint(323.2163732246063, 259.3787338448732, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('4', APoint(323.2163732246063, 253.3787338448731, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('5', APoint(323.2163732246063, 247.3787338448731, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('6', APoint(323.2163732246063, 241.3787338448731, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('7', APoint(323.2163732246063, 235.3787338448731, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('8', APoint(323.2163732246063, 229.3787338448731, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('9', APoint(323.2163732246063, 223.3787338448731, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('20', APoint(329.10399982919625, 271.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(345.067844216459, 271.3870940896595, 0.0), APoint(345.067844216459, 272.24353212504707, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(345.067844216459, 272.24353212504707, 0.0), APoint(348.87348956246933, 272.24353212504707, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.87348956246933, 272.24353212504707, 0.0), APoint(351.45795789644944, 270.7724536353502, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(363.06755981983224, 270.7724536353502, 0.0), APoint(363.06755981983224, 271.79279669681443, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(351.45795789644944, 270.7724536353502, 0.0), APoint(363.06755981983224, 270.7724536353502, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('27', APoint(341.6226798152993, 271.1663370082133, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('27', APoint(346.029128755501, 272.47700168282347, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('27', APoint(349.8750125165552, 271.8083044686093, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('303', APoint(355.75054927572455, 270.97920294104927, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('27', APoint(363.4916343102632, 270.88542531145265, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddLine(APoint(362.9884062924075, 265.5706111532028, 0.0), APoint(362.9884062924075, 266.42704918859033, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(362.9884062924075, 266.42704918859033, 0.0), APoint(359.18276094639714, 266.42704918859033, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.18276094639714, 266.42704918859033, 0.0), APoint(356.59829261241794, 264.95597069889345, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(344.98869068903514, 264.95597069889345, 0.0), APoint(344.98869068903514, 265.9763137603578, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(356.59829261241794, 264.95597069889345, 0.0), APoint(344.98869068903514, 264.95597069889345, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('27', APoint(363.2255451534247, 265.34985407175657, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('303', APoint(359.3396217533664, 266.66051874636673, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('27', APoint(355.065887391891, 265.9918215321527, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('26', APoint(349.8057012331419, 265.16272000459264, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('27', APoint(341.65159854783633, 265.0689423749959, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.05438256718116, 241.4506042708776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.05438256718116, 235.4506042708777, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.05438256718116, 229.4506042708777, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.05438256718116, 223.4506042708777, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091388, 259.72979626710514, 0.0), APoint(359.67258082251647, 259.72979626710514, 0.0))
entity.Color = 1


entity = acad.model.AddText('19.9', APoint(352.49400297421016, 260.1026205989905, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091388, 252.4757955487324, 0.0), APoint(348.4624351091388, 254.0109376956912, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(348.4624351091388, 254.0109376956912, 0.0), APoint(359.67258082251647, 254.0109376956912, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(359.67258082251647, 252.4757955487324, 0.0), APoint(359.67258082251647, 254.0109376956912, 0.0))
entity.Color = 1


entity = acad.model.AddText('15', APoint(345.23768372110953, 252.8121946111759, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('350', APoint(352.82956682788335, 254.3837620275766, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('15', APoint(359.9875729588921, 252.8466027293093, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091388, 247.72979626710512, 0.0), APoint(359.67258082251647, 247.72979626710512, 0.0))
entity.Color = 1


entity = acad.model.AddText('19.5', APoint(352.49400297421016, 248.1026205989904, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('8*2', APoint(335.7891998808309, 241.4677613191986, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091388, 241.72979626710512, 0.0), APoint(359.67258082251647, 241.72979626710512, 0.0))
entity.Color = 1


entity = acad.model.AddText('19.5', APoint(352.49400297421016, 242.1026205989904, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('19.5', APoint(368.80417566903276, 241.49470393207167, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('312.0', APoint(377.3424045167534, 241.3258687642021, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167534, 241.3553104647697, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('192.36', APoint(393.8424045167534, 241.3452584875833, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('61*2', APoint(335.7891998808309, 235.1406992195677, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167534, 235.3553104647697, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(352.27672165581953, 235.5282278992127, 0.0), APoint(357.8494552464572, 235.5282278992127, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(353.49945530120476, 234.19341785158198, 0.0), APoint(353.49945530120476, 237.7225054947898, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(353.34945530120694, 237.7225054947898, 0.0), 0.15, 0.0, 1.5707963267948966)
entity.Color = 1

entity = acad.model.AddLine(APoint(357.99945524645864, 235.3782278992127, 0.0), APoint(357.99945524645864, 234.04943312707712, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(357.8494552464572, 235.3782278992127, 0.0), 0.15, 0.0, 1.5707963267948966)
entity.Color = 1

entity = acad.model.AddArc(APoint(357.8494552464572, 234.04943312707712, 0.0), 0.15, 4.71238898038469, 0.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(357.8494552464572, 233.89943312707712, 0.0), APoint(352.149455321457, 233.89943312707712, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(352.149455321457, 234.04943312707712, 0.0), 0.15, 3.1415926535902474, 4.71238898038469)
entity.Color = 1

entity = acad.model.AddLine(APoint(351.99945532145557, 237.7225054947898, 0.0), APoint(351.99945532145557, 234.04943312707698, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(353.34945530120694, 237.8725054947898, 0.0), APoint(352.1494553214525, 237.87250549478998, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(352.1494553214525, 237.72250549479, 0.0), 0.15, 1.5707963267948966, 3.1415926535902474)
entity.Color = 1

entity = acad.model.AddText('22', APoint(358.00933390082446, 234.22493257607013, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('50', APoint(348.3975740828764, 234.76630375089647, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('50', APoint(354.2954519055302, 235.67910068220698, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('22', APoint(348.2430401421325, 236.9312482083771, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('2.4', APoint(369.10725454831226, 235.4947039320717, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('297.68', APoint(377.3424045167534, 235.4352017132441, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('183.53', APoint(393.8424045167534, 235.40614848471887, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('3*2', APoint(335.7891998808309, 229.4677613191986, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091388, 229.72979626710512, 0.0), APoint(359.67258082251647, 229.72979626710512, 0.0))
entity.Color = 1


entity = acad.model.AddText('3.5', APoint(352.49400297421016, 230.1026205989904, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('3.5', APoint(369.10725454831226, 229.4947039320717, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('21.0', APoint(377.3424045167534, 229.325868764202, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167534, 229.3553104647697, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('12.95', APoint(402.0924045167519, 229.35531046476967, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('12*2', APoint(335.7891998808309, 223.66256247382637, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddLine(APoint(352.09188232290035, 224.51603668768388, 0.0), APoint(354.66155437324414, 224.51603668768388, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(354.66155437324414, 224.6660366876842, 0.0), 0.15, 4.71238898038469, 5.408328441522118)
entity.Color = 1

entity = acad.model.AddLine(APoint(355.44372693943933, 225.07853668768396, 0.0), APoint(357.07638271220185, 225.07853668768396, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(357.07638271220185, 224.9285366876837, 0.0), 0.15, 0.0, 1.5707963267948966)
entity.Color = 1

entity = acad.model.AddLine(APoint(352.1319022970947, 222.26603668768388, 0.0), APoint(357.07638271220185, 222.26603668768388, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(357.07638271220185, 222.4160366876841, 0.0), 0.15, 4.71238898038469, 0.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(357.2263827122033, 224.9285366876837, 0.0), APoint(357.2263827122033, 222.4160366876841, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(355.34756093242413, 225.0436544495402, 0.0), APoint(354.7577203802575, 224.55091892582732, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(355.44372693943933, 224.9285366876837, 0.0), 0.15, 1.5707963267948966, 2.266735787931156)
entity.Color = 1

entity = acad.model.AddText('25', APoint(357.41013744495376, 223.0415634948903, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('20', APoint(348.500546720943, 224.0125531580678, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('15', APoint(355.1454142341645, 225.26866019530237, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('40', APoint(348.45767800418434, 221.9428297157369, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('7', APoint(353.7863507135553, 224.7051716830443, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('1.1', APoint(369.10725454831226, 223.4947039320717, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('25.68', APoint(377.3424045167534, 223.38275789371897, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167534, 223.3553104647697, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('15.83', APoint(402.0924045167519, 223.34525848758298, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('وزن آرماتور برای یک متر طول آبرو', APoint(351.11857942806273, 211.21606623836772, 0.0), 1.8)
entity.Color = 1

entity = acad.model.AddText('وزن آرماتور برای ابتدا و انتها آبرو', APoint(361.76891620743754, 204.8192010401995, 0.0), 1.8)
entity.Color = 1

entity = acad.model.AddText('139.1', APoint(389.57853430497016, 211.4902574983032, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(400.1924045167543, 274.91126186483086, 0.0), APoint(400.81162047366456, 275.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 273.9831842145235, 0.0), APoint(401.7396981239717, 275.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 273.0551065642161, 0.0), APoint(402.6677757742791, 275.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 272.1270289139087, 0.0), APoint(403.5958534245865, 275.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 271.1989512636013, 0.0), APoint(404.5239310748939, 275.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167543, 270.27087361329416, 0.0), APoint(405.45200872520127, 275.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755084, 269.5304778217409, 0.0), APoint(406.3800863755084, 275.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258158, 269.5304778217409, 0.0), APoint(407.3081640258158, 275.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761232, 269.5304778217409, 0.0), APoint(408.2362416761232, 275.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264306, 269.5304778217409, 0.0), APoint(408.44240451675046, 274.80856301206074, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.092396976738, 269.5304778217409, 0.0), APoint(408.4424045167507, 273.8804853617536, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270447, 269.5304778217409, 0.0), APoint(408.44240451675046, 272.95240771144665, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735206, 269.5304778217409, 0.0), APoint(408.44240451675046, 272.02433006113927, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765945, 269.5304778217409, 0.0), APoint(408.44240451675046, 271.0962524108319, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796684, 269.5304778217409, 0.0), APoint(408.44240451675046, 270.1681747605245, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167543, 268.91126186482995, 0.0), APoint(400.81162047366547, 269.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 267.98318421452257, 0.0), APoint(401.73969812397263, 269.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 267.0551065642152, 0.0), APoint(402.66777577428, 269.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 266.1270289139078, 0.0), APoint(403.5958534245874, 269.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675387, 265.1989512636002, 0.0), APoint(404.5239310748948, 269.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 264.270873613293, 0.0), APoint(405.4520087252022, 269.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.38008637550934, 263.5304778217409, 0.0), APoint(406.38008637550934, 269.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258167, 263.5304778217409, 0.0), APoint(407.3081640258165, 269.53047782174065, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761241, 263.5304778217409, 0.0), APoint(408.2362416761241, 269.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264315, 263.5304778217409, 0.0), APoint(408.44240451675114, 268.8085630120605, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767389, 263.5304778217409, 0.0), APoint(408.4424045167518, 267.8804853617538, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.02047462704604, 263.53047782174133, 0.0), APoint(408.4424045167516, 266.9524077114469, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735343, 263.53047782174133, 0.0), APoint(408.4424045167525, 266.0243300611404, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992766036, 263.5304778217409, 0.0), APoint(408.4424045167532, 265.0962524108337, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796775, 263.5304778217409, 0.0), APoint(408.44240451675364, 264.16817476052677, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167543, 262.91126186482995, 0.0), APoint(400.81162047366547, 263.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 261.98318421452257, 0.0), APoint(401.73969812397263, 263.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 261.0551065642152, 0.0), APoint(402.66777577428, 263.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 260.1270289139078, 0.0), APoint(403.5958534245874, 263.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675387, 259.1989512636002, 0.0), APoint(404.5239310748948, 263.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 258.270873613293, 0.0), APoint(405.4520087252022, 263.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.38008637550934, 257.5304778217409, 0.0), APoint(406.38008637550934, 263.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258167, 257.5304778217409, 0.0), APoint(407.3081640258165, 263.53047782174065, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761241, 257.5304778217409, 0.0), APoint(408.2362416761241, 263.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264315, 257.5304778217409, 0.0), APoint(408.44240451675114, 262.8085630120605, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767384, 257.5304778217404, 0.0), APoint(408.4424045167518, 261.8804853617538, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270456, 257.5304778217409, 0.0), APoint(408.4424045167518, 260.9524077114471, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.948552277353, 257.5304778217409, 0.0), APoint(408.44240451675296, 260.02433006114086, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992766036, 257.5304778217409, 0.0), APoint(408.4424045167532, 259.0962524108337, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796775, 257.5304778217409, 0.0), APoint(408.44240451675364, 258.16817476052677, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167543, 256.91126186482995, 0.0), APoint(400.81162047366547, 257.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 255.9831842145226, 0.0), APoint(401.73969812397263, 257.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 255.0551065642152, 0.0), APoint(402.66777577428, 257.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 254.12702891390782, 0.0), APoint(403.5958534245874, 257.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 253.19895126360043, 0.0), APoint(404.5239310748948, 257.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 252.27087361329305, 0.0), APoint(405.4520087252022, 257.5304778217411, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755091, 251.53047782174067, 0.0), APoint(406.38008637550934, 257.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258165, 251.53047782174067, 0.0), APoint(407.3081640258165, 257.53047782174065, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761239, 251.53047782174067, 0.0), APoint(408.2362416761241, 257.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.16431932643127, 251.53047782174067, 0.0), APoint(408.44240451675114, 256.8085630120605, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767384, 251.53047782174045, 0.0), APoint(408.4424045167518, 255.88048536175384, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270456, 251.5304778217409, 0.0), APoint(408.4424045167518, 254.95240771144714, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.948552277353, 251.5304778217409, 0.0), APoint(408.4424045167525, 254.02433006114043, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992766036, 251.5304778217409, 0.0), APoint(408.4424045167532, 253.09625241083373, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796775, 251.5304778217409, 0.0), APoint(408.44240451675364, 252.1681747605268, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675387, 250.91126186482953, 0.0), APoint(400.81162047366524, 251.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675387, 249.98318421452237, 0.0), APoint(401.7396981239724, 251.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675387, 249.05510656421498, 0.0), APoint(402.66777577427956, 251.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675387, 248.1270289139076, 0.0), APoint(403.59585342458695, 251.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675387, 247.1989512636002, 0.0), APoint(404.52393107489434, 251.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675387, 246.27087361329282, 0.0), APoint(405.4520087252017, 251.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.38008637550934, 245.5304778217409, 0.0), APoint(406.3800863755091, 251.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258167, 245.5304778217409, 0.0), APoint(407.3081640258165, 251.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761241, 245.5304778217409, 0.0), APoint(408.2362416761239, 251.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264315, 245.5304778217409, 0.0), APoint(408.4424045167509, 250.80856301206032, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767389, 245.5304778217409, 0.0), APoint(408.4424045167516, 249.8804853617536, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.02047462704604, 245.53047782174136, 0.0), APoint(408.4424045167516, 248.9524077114469, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735343, 245.53047782174136, 0.0), APoint(408.4424045167525, 248.02433006114043, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992766036, 245.5304778217409, 0.0), APoint(408.4424045167532, 247.09625241083373, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796775, 245.5304778217409, 0.0), APoint(408.4424045167532, 246.16817476052634, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167543, 244.9112618648309, 0.0), APoint(400.81162047366433, 245.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 243.9831842145235, 0.0), APoint(401.7396981239715, 245.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 243.05510656421612, 0.0), APoint(402.66777577427865, 245.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 242.12702891390873, 0.0), APoint(403.59585342458604, 245.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 241.19895126360134, 0.0), APoint(404.5239310748934, 245.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167543, 240.27087361329419, 0.0), APoint(405.4520087252008, 245.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755084, 239.5304778217409, 0.0), APoint(406.3800863755082, 245.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258158, 239.5304778217409, 0.0), APoint(407.3081640258156, 245.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761232, 239.5304778217409, 0.0), APoint(408.236241676123, 245.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.1643193264306, 239.5304778217409, 0.0), APoint(408.44240451675046, 244.80856301206077, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.092396976738, 239.5304778217409, 0.0), APoint(408.4424045167507, 243.8804853617536, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270447, 239.5304778217409, 0.0), APoint(408.44240451675046, 242.95240771144668, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.94855227735206, 239.5304778217409, 0.0), APoint(408.44240451675046, 242.0243300611393, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992765945, 239.5304778217409, 0.0), APoint(408.44240451675046, 241.0962524108319, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796684, 239.5304778217409, 0.0), APoint(408.44240451675046, 240.16817476052452, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.19240451675387, 238.91126186482953, 0.0), APoint(400.81162047366524, 239.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 237.9831842145226, 0.0), APoint(401.7396981239724, 239.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 237.0551065642152, 0.0), APoint(402.66777577427956, 239.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 236.12702891390782, 0.0), APoint(403.59585342458695, 239.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 235.19895126360043, 0.0), APoint(404.52393107489434, 239.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 234.27087361329305, 0.0), APoint(405.4520087252017, 239.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755091, 233.53047782174067, 0.0), APoint(406.3800863755091, 239.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258165, 233.53047782174067, 0.0), APoint(407.30816402581627, 239.53047782174045, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761239, 233.53047782174067, 0.0), APoint(408.2362416761239, 239.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.16431932643127, 233.53047782174067, 0.0), APoint(408.44240451675114, 238.80856301206055, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767384, 233.53047782174045, 0.0), APoint(408.4424045167518, 237.88048536175384, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270456, 233.5304778217409, 0.0), APoint(408.4424045167516, 236.9524077114469, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.948552277353, 233.5304778217409, 0.0), APoint(408.4424045167525, 236.02433006114043, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992766036, 233.5304778217409, 0.0), APoint(408.4424045167532, 235.09625241083373, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796775, 233.5304778217409, 0.0), APoint(408.44240451675364, 234.1681747605268, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.9424045167507, 232.91126186482907, 0.0), APoint(392.5616204736625, 233.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675046, 231.98318421452169, 0.0), APoint(393.4896981239697, 233.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675046, 231.0551065642143, 0.0), APoint(394.41777577427683, 233.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675046, 230.1270289139069, 0.0), APoint(395.3458534245842, 233.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675046, 229.19895126359953, 0.0), APoint(396.2739310748916, 233.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675046, 228.27087361329214, 0.0), APoint(397.202008725199, 233.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(392.1300863755066, 227.5304778217409, 0.0), APoint(398.1300863755064, 233.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.058164025814, 227.5304778217409, 0.0), APoint(399.05816402581377, 233.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.9862416761214, 227.5304778217409, 0.0), APoint(399.98624167612115, 233.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.91431932642877, 227.5304778217409, 0.0), APoint(400.19240451675, 232.80856301206214, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.84239697673615, 227.5304778217409, 0.0), APoint(400.1924045167507, 231.88048536175543, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.7704746270433, 227.53047782174136, 0.0), APoint(400.19240451675046, 230.9524077114485, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(397.6985522773507, 227.53047782174136, 0.0), APoint(400.19240451675114, 230.0243300611418, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(398.6266299276581, 227.53047782174136, 0.0), APoint(400.19240451675114, 229.0962524108344, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(399.5547075779655, 227.53047782174136, 0.0), APoint(400.1924045167518, 228.1681747605277, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675023, 226.91126186482953, 0.0), APoint(392.5616204736616, 227.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675023, 225.98318421452237, 0.0), APoint(393.48969812396876, 227.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675023, 225.05510656421498, 0.0), APoint(394.4177757742759, 227.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675023, 224.1270289139076, 0.0), APoint(395.3458534245833, 227.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675023, 223.1989512636002, 0.0), APoint(396.2739310748907, 227.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(391.94240451675023, 222.27087361329282, 0.0), APoint(397.2020087251981, 227.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(392.1300863755057, 221.5304778217409, 0.0), APoint(398.13008637550547, 227.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.0581640258131, 221.5304778217409, 0.0), APoint(399.05816402581286, 227.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.98624167612047, 221.5304778217409, 0.0), APoint(399.98624167612024, 227.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.91431932642786, 221.5304778217409, 0.0), APoint(400.1924045167498, 226.80856301206282, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.84239697673524, 221.5304778217409, 0.0), APoint(400.1924045167498, 225.88048536175543, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.7704746270424, 221.53047782174136, 0.0), APoint(400.19240451674955, 224.9524077114485, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(397.69855227734934, 221.5304778217409, 0.0), APoint(400.19240451674955, 224.02433006114111, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(398.6266299276567, 221.5304778217409, 0.0), APoint(400.19240451674955, 223.09625241083373, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(399.5547075779641, 221.5304778217409, 0.0), APoint(400.19240451674955, 222.16817476052634, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('28.8', APoint(401.3121729414852, 204.65862849603838, 0.0), 1.875)
entity.Color = 1

entity = acad.model.AddText('20', APoint(329.05438256718116, 265.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('14', APoint(329.05438256718116, 259.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.05438256718116, 253.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('10', APoint(329.05438256718116, 247.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('14', APoint(335.80438256718026, 247.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('71', APoint(335.80438256718026, 253.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('17', APoint(335.80438256718026, 259.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('71', APoint(335.80438256718026, 265.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('71', APoint(335.7891998808309, 271.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('4.1', APoint(369.1072545483123, 271.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('291.1', APoint(377.3424045167534, 271.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('2.466', APoint(385.5924045167534, 271.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('717.9', APoint(393.8424045167534, 271.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('4.1', APoint(369.10725454831226, 265.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('291.1', APoint(377.3424045167534, 265.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('2.466', APoint(385.5924045167534, 265.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('717.9', APoint(393.8424045167534, 265.4506042708779, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('19.9', APoint(369.10725454831226, 259.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('339.12', APoint(377.3424045167534, 259.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('1.208', APoint(385.5924045167534, 259.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('409.8', APoint(393.8424045167534, 259.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('3.8', APoint(369.10725454831226, 253.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('269.8', APoint(377.3424045167534, 253.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167534, 253.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('166.34', APoint(393.8424045167534, 253.45060427087776, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('19.5', APoint(369.10725454831226, 247.45060427087782, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('273.0', APoint(377.3424045167534, 247.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('0.617', APoint(385.5924045167534, 247.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('168.31', APoint(393.8424045167534, 247.4506042708778, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('وزن کل آرماتور مورد نیاز', APoint(349.02859428883767, 196.7851681753013, 0.0), 1.8)
entity.Color = 1

entity = acad.model.AddText('(Kg)', APoint(375.6643191906205, 196.9690088113174, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('2584.9', APoint(381.425507037261, 196.76495762539963, 0.0), 1.875)
entity.Color = 1

entity = acad.model.AddLine(APoint(320.69261141490006, 194.5304778217411, 0.0), APoint(408.4424045167534, 194.5304778217411, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('10', APoint(323.2163732246063, 217.3787338448731, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('-', APoint(329.05438256718116, 217.4506042708777, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('-', APoint(335.7891998808309, 217.6625624738264, 0.0), 1.35)
entity.Color = 1

entity = acad.model.AddText('-', APoint(369.10725454831226, 217.4947039320717, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('-', APoint(377.3424045167534, 217.38275789371897, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('-', APoint(385.5924045167534, 217.3553104647697, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(320.69261141490006, 215.53047782174113, 0.0), APoint(408.4424045167534, 215.53047782174113, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('(1m)', APoint(393.5052494786596, 279.32898721149445, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(400.1924045167543, 220.91126186482998, 0.0), APoint(400.81162047366547, 221.53047782174113, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 219.9831842145226, 0.0), APoint(401.73969812397263, 221.53047782174113, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 219.0551065642152, 0.0), APoint(402.66777577427956, 221.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 218.12702891390782, 0.0), APoint(403.59585342458695, 221.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 217.19895126360043, 0.0), APoint(404.52393107489434, 221.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.1924045167541, 216.27087361329305, 0.0), APoint(405.4520087252017, 221.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(400.3800863755091, 215.53047782174067, 0.0), APoint(406.3800863755091, 221.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.3081640258165, 215.53047782174067, 0.0), APoint(407.3081640258165, 221.53047782174067, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(402.2362416761239, 215.53047782174067, 0.0), APoint(408.2362416761241, 221.5304778217409, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.16431932643127, 215.53047782174067, 0.0), APoint(408.4424045167543, 220.80856301206373, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.0923969767384, 215.53047782174045, 0.0), APoint(408.4424045167543, 219.88048536175634, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.0204746270456, 215.5304778217409, 0.0), APoint(408.4424045167541, 218.9524077114494, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(405.948552277353, 215.5304778217409, 0.0), APoint(408.4424045167541, 218.02433006114202, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(406.87662992766036, 215.5304778217409, 0.0), APoint(408.4424045167543, 217.09625241083486, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(407.80470757796775, 215.5304778217409, 0.0), APoint(408.4424045167543, 216.16817476052748, 0.0))

try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('-', APoint(393.8424045167534, 217.3553104647697, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(348.4624351091388, 218.0109376956912, 0.0), APoint(359.67258082251647, 218.0109376956912, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.67258082251647, 218.0109376956912, 0.0), APoint(359.67258082251647, 219.54607984265, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('-', APoint(352.82956682788335, 218.38376202757647, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddText('-', APoint(359.9875729588921, 217.98767638887, 0.0), 1.3125)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.1365827687382, 69.91519884606998, 0.0), APoint(408.60074281020616, 69.91519884606998, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.1365827687382, 35.750721869651215, 0.0), APoint(206.1365827687382, 69.91519884606998, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.1365827687382, 57.198482304145045, 0.0), APoint(408.60074281020616, 57.19848230414493, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('دیوار', APoint(207.99332054852266, 62.69278919685553, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('مقطع 3-3', APoint(317.32119305373044, 67.13036946344141, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('طول دیوار', APoint(215.73109651787354, 62.13227612738399, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(214.61667962934416, 69.91519884606998, 0.0), APoint(214.61667962934416, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(214.61667962934416, 65.72327429511927, 0.0), APoint(408.60074281020616, 65.72327429511927, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(253.11653101334332, 65.72327429511927, 0.0), APoint(253.11653101334332, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(240.0177523905336, 65.72327429511927, 0.0), APoint(240.0177523905336, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(226.33923757397906, 65.72327429511927, 0.0), APoint(226.33923757397906, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W', APoint(219.04763168903128, 57.98328077858946, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('m (min)', APoint(303.1623172948043, 58.35186234409662, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('ارتفاع پی', APoint(302.2548438433091, 62.33965700623878, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(314.6088922858403, 65.72327429511927, 0.0), APoint(314.6088922858403, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('کد زیر پی', APoint(256.6875330935459, 62.64854590121024, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('کد روی پی', APoint(288.6756630814257, 60.47499199449658, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(300.79504779205627, 65.72327429511927, 0.0), APoint(300.79504779205627, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W1', APoint(208.33137632174066, 53.59085731764719, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.1365827687382, 51.83654219552159, 0.0), APoint(408.60074281020616, 51.83654219552159, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W2', APoint(208.33137632174066, 48.22891720902385, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.1365827687382, 46.47460208689802, 0.0), APoint(408.60074281020616, 46.47460208689802, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W3', APoint(208.33137632174066, 42.86697710040039, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.1365827687382, 41.11266197827467, 0.0), APoint(408.60074281020616, 41.11266197827467, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W4', APoint(208.33137632174066, 37.50503699177716, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.1365827687382, 35.750721869651215, 0.0), APoint(408.60074281020616, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-106', APoint(217.7809723917303, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-109', APoint(259.67738365508967, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-112', APoint(305.8050273355434, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('عرض پی', APoint(331.46560020244624, 62.67234910235959, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('f (min)', APoint(331.92135323774573, 58.35186234409662, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-120', APoint(217.7809723917303, 48.22341059821781, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-123', APoint(259.67738365508967, 48.22341059821781, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-126', APoint(305.8050273355434, 48.22341059821781, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-134', APoint(217.7809723917303, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-136', APoint(259.67738365508967, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-139', APoint(305.8050273355434, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-147', APoint(217.7809723917303, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-150', APoint(259.67738365508967, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-153', APoint(305.8050273355434, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('در ابتدای دیوار', APoint(254.21463618300322, 58.361627954608934, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('در انتهای دیوار', APoint(271.7642330456961, 58.59366583997519, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(270.5046150042722, 65.72327429511927, 0.0), APoint(270.5046150042722, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(287.5785815639433, 65.72327429511927, 0.0), APoint(287.5785815639433, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('کد زیر پی', APoint(273.1203370969329, 62.64854590121024, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('i-110', APoint(277.76420268013726, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-124', APoint(277.76420268013726, 48.22341059821781, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-137', APoint(277.76420268013726, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-151', APoint(277.76420268013726, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-111', APoint(292.6268319940823, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-125', APoint(292.6268319940823, 48.22341059821781, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-138', APoint(292.6268319940823, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-152', APoint(292.6268319940823, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('m (max)', APoint(316.69038065818086, 58.35186234409662, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('ارتفاع پی', APoint(316.613602922705, 62.33965700623878, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddLine(APoint(328.9774573327709, 65.72327429511927, 0.0), APoint(328.9774573327709, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-113', APoint(319.33309069892084, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-127', APoint(319.33309069892084, 48.22341059821781, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-140', APoint(319.33309069892084, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-154', APoint(319.33309069892084, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(342.38456351767263, 65.72327429511927, 0.0), APoint(342.38456351767263, 35.750721869651215, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-114', APoint(333.04333757537506, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('عرض پی', APoint(345.026655308739, 62.67234910235959, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('f (max)', APoint(344.7955019659744, 58.35186234409662, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(355.62779937618006, 65.72327429511927, 0.0), APoint(355.62779937618006, 35.7507218696511, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(368.8710352346866, 65.72327429511927, 0.0), APoint(368.8710352346866, 35.7507218696511, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.1142710931931, 65.72327429511927, 0.0), APoint(382.1142710931931, 35.7507218696511, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.35750695169963, 65.72327429511927, 0.0), APoint(395.35750695169963, 35.7507218696511, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.60074281020616, 69.91519884606998, 0.0), APoint(408.60074281020616, 35.7507218696511, 0.0))
entity.Color = 4
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('i-115', APoint(345.9174863036028, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-129', APoint(345.9174863036028, 48.22341059821781, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-142', APoint(345.9174863036028, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-156', APoint(345.9174863036028, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('h (max)', APoint(228.3188012954074, 58.554713317464234, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('ارتفاع', APoint(229.8505444053385, 62.44120815475833, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('h (min)', APoint(241.97732403431883, 58.554713317464234, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('ارتفاع', APoint(243.3318254658393, 62.44120815475833, 0.0), 1.7)
entity.Color = 1

entity = acad.model.AddText('i-107', APoint(229.79158451580906, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-121', APoint(229.79158451580906, 48.22341059821781, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-134', APoint(229.79158451580906, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-148', APoint(229.79158451580906, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-149', APoint(242.87490078214387, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-135', APoint(242.87490078214387, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-122', APoint(242.87490078214387, 48.22341059821781, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-108', APoint(242.87490078214387, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-116', APoint(359.69367961878334, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-130', APoint(359.69367961878334, 48.22341059821781, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-143', APoint(359.69367961878334, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-157', APoint(359.69367961878334, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-117', APoint(372.3459401257537, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-118', APoint(386.1801513357973, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-132', APoint(386.1801513357973, 48.22341059821781, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-145', APoint(386.1801513357973, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-159', APoint(386.1801513357973, 37.499530380970896, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-119', APoint(398.8266390026288, 53.585350706841155, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s1', APoint(360.69928790119275, 62.26712392162142, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(max)', APoint(358.078299275076, 58.3676785580941, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s1', APoint(373.94252375969836, 62.26712392162142, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(min)', APoint(371.3215351335816, 58.3676785580941, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s2', APoint(387.1857596182049, 62.26712392162119, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(max)', APoint(384.56477099208905, 58.367678558093985, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('s2', APoint(400.4289954767114, 62.26712392162119, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('(min)', APoint(397.8080068505956, 58.367678558093985, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-133', APoint(398.8266390026288, 48.22341059821758, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-146', APoint(398.8266390026288, 42.86147048959424, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-160', APoint(398.8266390026288, 37.49953038097078, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-131', APoint(372.3459401257537, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-144', APoint(372.3459401257537, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-158', APoint(372.3459401257537, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-128', APoint(333.04333757537506, 48.223410598217924, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-141', APoint(333.04333757537506, 42.86147048959447, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('i-155', APoint(333.04333757537506, 37.49953038097101, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(142.0401764118662, 219.45436589333542, 0.0), APoint(142.00234096545088, 223.2036673666358, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.26644021611558, 219.2043658933309, 0.0), APoint(117.22860476970024, 222.9536673666313, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(143.01238087018936, 222.21380909858135, 0.0), APoint(116.23874650164572, 221.94362746189285, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(118.05835243832722, 242.62188310217473, 0.0), APoint(120.48488474537444, 240.19535079512747, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(142.75737401139384, 267.32090467524097, 0.0), APoint(145.18390631844105, 264.8943723681937, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(119.07067118300135, 240.19535079512747, 0.0), APoint(145.18390631844107, 266.3085859305668, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(27.35039953565528, 204.7363006616256, 0.0), APoint(27.396300024453883, 200.1877942586996, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.124135731406376, 204.98630066163022, 0.0), APoint(52.17003622020498, 200.43779425870423, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(26.386260119715395, 201.17765252675412, 0.0), APoint(53.15989448825948, 201.44783416344274, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.332223509193824, 181.56878345278625, 0.0), APoint(48.28588522320737, 184.6151217387727, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(26.633201936127662, 156.86976187972004, 0.0), APoint(23.58686365014121, 159.9161001657065, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.70009878558045, 184.6151217387727, 0.0), APoint(23.586863650141197, 158.5018866033334, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.80199862056637, 214.65443908498088, 0.0), APoint(97.3812965008225, 214.65443908498088, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.77358455728609, 219.44866826962337, 0.0), APoint(96.05339918839005, 219.6102193222144, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(87.4697360263531, 214.6544390849809, 0.0), 8.911560474469422, 6.2831853071795845, 0.2166973854516534)
entity.Color = 8

entity = acad.model.AddArc(APoint(87.4697360263531, 214.6544390849809, 0.0), 8.911560474469422, 0.30033039559551034, 0.5235987755981559)
entity.Color = 8

entity = acad.model.AddLine(APoint(70.46072467048496, 201.88859674451982, 0.0), APoint(71.13020237025466, 202.6498965457078, 0.0))



entity = acad.model.AddLine(APoint(71.13020237025466, 202.6498965457078, 0.0), APoint(70.74382069788483, 201.71262018249658, 0.0))



entity = acad.model.AddLine(APoint(70.46072467048496, 201.88859674451982, 0.0), APoint(70.74382069788483, 201.71262018249658, 0.0))



entity = acad.model.AddLine(APoint(71.13020237025466, 202.6498965457078, 0.0), APoint(70.6022726841849, 201.8006084635082, 0.0))



entity = acad.model.AddLine(APoint(70.6022726841849, 201.8006084635082, 0.0), APoint(68.50541216010606, 198.4273587673363, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.50541216010606, 198.4273587673363, 0.0), APoint(63.835422922426005, 195.61799268559082, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(0.0, 0.0, 0.0), APoint(419.9999999999268, 0.0, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(419.9999999999268, 0.0, 0.0), APoint(419.9999999999268, 297.0000000000072, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(419.9999999999268, 297.0000000000072, 0.0), APoint(0.0, 297.0000000000072, 0.0))
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

entity = acad.model.AddLine(APoint(415.0, 4.999999999999886, 0.0), APoint(415.0, 291.9999999999999, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(415.0, 291.9999999999999, 0.0), APoint(5.0, 291.9999999999999, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(5.0, 291.9999999999999, 0.0), APoint(5.0, 4.999999999999886, 0.0))
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

entity = acad.model.AddCircle(APoint(157.12160433300005, 13.765197280705138, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(157.14024835264308, 12.554873877574096, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(198.65312747755888, 13.608239394461918, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(198.67177149720192, 12.397915991330876, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(198.65312747755888, 23.94778561105113, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(198.67177149720192, 22.73746220792009, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(287.5198035687714, 23.36072055361794, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(287.5328543825215, 22.513494171426213, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(239.36913921287623, 13.430494721903642, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(239.38778323251927, 12.2201713187726, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddLine(APoint(206.91516609528617, 187.53197630981737, 0.0), APoint(242.76516609528426, 187.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.76516609528426, 187.53197630981737, 0.0), APoint(242.76516609528426, 184.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(242.76516609528426, 184.53197630981737, 0.0), APoint(206.91516609528617, 184.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.91516609528617, 184.53197630981737, 0.0), APoint(206.91516609528617, 187.53197630981737, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.50536782425307, 113.33217423550975, 0.0), APoint(37.74641317788552, 113.61944090167937, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.244267725079226, 113.20027395256034, 0.0), APoint(41.332714090889375, 113.30568022676648, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.98421298084635, 116.46561355463227, 0.0), APoint(44.2252583344788, 116.75288022080188, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.570513893850226, 116.15185287971931, 0.0), APoint(47.81155924748268, 116.43911954588893, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.15681480685363, 115.83809220480636, 0.0), APoint(51.39786016048608, 116.12535887097597, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.74311571985756, 115.52433152989343, 0.0), APoint(54.984161073490014, 115.81159819606304, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.329416632861296, 115.21057085498059, 0.0), APoint(58.57046198649375, 115.4978375211502, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.915717545865114, 114.89681018006735, 0.0), APoint(62.156762899497565, 115.18407684623696, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.50201845886882, 114.58304950515452, 0.0), APoint(65.74306381250128, 114.87031617132413, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.08831937187271, 114.26928883024159, 0.0), APoint(69.32936472550517, 114.5565554964112, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.67462028487637, 113.95552815532847, 0.0), APoint(72.91566563850883, 114.24279482149808, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.5671645284658, 117.40272814936387, 0.0), APoint(75.73008990182124, 117.59689504838498, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.26092119788025, 113.64176748041554, 0.0), APoint(76.50196655151271, 113.92903414658515, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.15346544146972, 117.08896747445091, 0.0), APoint(79.39451079510218, 117.37623414062053, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.06579279476819, 113.5884892032575, 0.0), APoint(80.08826746451643, 113.61527347167234, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.7397663544734, 116.77520679953813, 0.0), APoint(82.98081170810586, 117.06247346570774, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.32606726747721, 116.46144612462486, 0.0), APoint(86.56711262110967, 116.74871279079447, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.49866909348471, 115.83392477479916, 0.0), APoint(93.73971444711717, 116.12119144096877, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.08497000648828, 115.52016409988612, 0.0), APoint(97.32601536012073, 115.80743076605573, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.67127091949227, 115.20640342497309, 0.0), APoint(100.91231627312473, 115.4936700911427, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.257571832496, 114.89264275006029, 0.0), APoint(104.49861718612846, 115.1799094162299, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.84387274549964, 114.5788820751471, 0.0), APoint(108.0849180991321, 114.86614874131672, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.43017365850343, 114.26512140023432, 0.0), APoint(111.6712190121359, 114.55238806640394, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.0164745715074, 113.95136072532125, 0.0), APoint(115.25751992513986, 114.23862739149087, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.56716464389113, 117.40272916062948, 0.0), APoint(75.86602305331866, 117.37658243780518, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.49866920954244, 115.83392579117164, 0.0), APoint(93.79752761896997, 115.80777906834734, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.08497012267273, 115.52016511728007, 0.0), APoint(97.38382853210025, 115.49401839445578, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.67127103580302, 115.20640444338851, 0.0), APoint(100.97012944523054, 115.18025772056421, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.2575719489333, 114.89264376949694, 0.0), APoint(104.55643035836083, 114.86649704667265, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.84387286206359, 114.57888309560538, 0.0), APoint(108.14273127149112, 114.55273637278108, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.43017377519388, 114.26512242171381, 0.0), APoint(111.7290321846214, 114.23897569888952, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.01647468832417, 113.95136174782225, 0.0), APoint(115.15357499461452, 113.9393670252559, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.15346555702172, 117.0889684867379, 0.0), APoint(79.45232396644924, 117.0628217639136, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.739766470152, 116.77520781284633, 0.0), APoint(83.03862487957953, 116.74906109002204, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.3260673832823, 116.46144713895477, 0.0), APoint(86.62492579270982, 116.43530041613047, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.98421309378413, 116.46561455715357, 0.0), APoint(44.28307150321165, 116.43946783432928, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.57051400691441, 116.151853883262, 0.0), APoint(47.86937241634193, 116.12570716043771, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.15681492004469, 115.83809320937044, 0.0), APoint(51.45567332947221, 115.81194648654615, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.74311583317497, 115.52433253547888, 0.0), APoint(55.04197424260249, 115.49818581265458, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.32941674630525, 115.21057186158731, 0.0), APoint(58.62827515573277, 115.18442513876302, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.91571765943553, 114.89681118769575, 0.0), APoint(62.21457606886305, 114.87066446487145, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.50201857256582, 114.58305051380418, 0.0), APoint(65.80087698199334, 114.55690379097989, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.0883194856961, 114.26928983991262, 0.0), APoint(69.38717789512363, 114.24314311708832, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.67462039882639, 113.95552916602105, 0.0), APoint(72.97347880825392, 113.92938244319676, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.26092131195668, 113.64176849212949, 0.0), APoint(76.5597797213842, 113.61562176930519, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.505367935587614, 113.33217523643668, 0.0), APoint(37.80422634501514, 113.30602851361239, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(37.80419859213574, 113.30598535877967, 0.0), APoint(37.74638553786747, 113.61939874818907, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.351923571499896, 113.201350511025, 0.0), APoint(41.33268642272257, 113.30563803011881, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.283043710626565, 116.43942459555262, 0.0), APoint(44.22523065635829, 116.75283798496203, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.86934459548108, 116.12566387748281, 0.0), APoint(47.81153154121281, 116.43907726689221, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.45564548033608, 115.81190315941298, 0.0), APoint(51.39783242606781, 116.12531654882238, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.0419463651906, 115.49814244134338, 0.0), APoint(54.984133310922324, 115.81155583075278, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.628247250045675, 115.18438172327322, 0.0), APoint(58.5704341957774, 115.49779511268262, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.21454813490059, 114.87062100520394, 0.0), APoint(62.156735080632316, 115.18403439461335, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.80084901975502, 114.55686028713446, 0.0), APoint(65.74303596548675, 114.87027367654386, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.38714990461008, 114.2430995690643, 0.0), APoint(69.32933685034182, 114.5565129584737, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.97345078946513, 113.92933885099424, 0.0), APoint(72.91563773519687, 114.24275224040365, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.55975167431973, 113.61557813292431, 0.0), APoint(76.50193862005146, 113.92899152233372, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.86599502310047, 117.37653880583724, 0.0), APoint(75.82517214255816, 117.59784587079268, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.09312191861531, 113.58876249449622, 0.0), APoint(80.08823950490643, 113.61523080426413, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.45229590795543, 117.06277808776765, 0.0), APoint(79.39448285368717, 117.37619147717706, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.03859679281034, 116.74901736969828, 0.0), APoint(82.98078373854207, 117.06243075910768, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.6248976776649, 116.43525665162811, 0.0), APoint(86.56708462339664, 116.74867004103751, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.79749944737496, 115.80773521548835, 0.0), APoint(93.7396863931067, 116.12114860489775, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.38380033222938, 115.4939744974192, 0.0), APoint(97.32598727796112, 115.80738788682861, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.9701012170846, 115.18021377934825, 0.0), APoint(100.91228816281634, 115.49362716875765, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.55640210193904, 114.86645306127876, 0.0), APoint(104.49858904767078, 115.17986645068817, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.14270298679392, 114.5526923432096, 0.0), APoint(108.08488993252566, 114.866105732619, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.7290038716491, 114.23893162513912, 0.0), APoint(111.67119081738083, 114.55234501454852, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.31239314326552, 113.94095520674273, 0.0), APoint(115.2574917022353, 114.23858429647905, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.409691567151434, 116.54783121950334, 0.0), APoint(44.79913404430748, 116.95371396979776, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.74589822050932, 115.72023481553785, 0.0), APoint(50.13534069766536, 116.12611756583227, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.082104873867294, 114.8926384115727, 0.0), APoint(55.47154735102334, 115.29852116186713, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.41831152722502, 114.0650420076073, 0.0), APoint(60.80775400438107, 114.47092475790173, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.95595961933304, 113.44739087150333, 0.0), APoint(66.14396065773893, 113.64332835393624, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.7640345598133, 117.28044220320942, 0.0), APoint(76.07093992748709, 117.60030354864156, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.10024121317123, 116.45284579924424, 0.0), APoint(81.48968369032727, 116.85872854953867, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.436447866529, 115.62524939527889, 0.0), APoint(86.82589034368503, 116.03113214557331, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.77265451988684, 114.79765299131346, 0.0), APoint(92.16209699704288, 115.20353574160788, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.10886117324462, 113.97005658734801, 0.0), APoint(97.49830365040066, 114.37593933764244, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.45458420583311, 117.18545678295034, 0.0), APoint(112.84402668298915, 117.59133953324476, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.85315205410429, 116.47762296339442, 0.0), APoint(44.79791080644261, 116.95247224684204, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.18935675326011, 115.65002457582946, 0.0), APoint(50.13411550559842, 116.12487385927707, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.52556145241557, 114.82242618826372, 0.0), APoint(55.47032020475389, 115.29727547171133, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.86176615157149, 113.99482780069808, 0.0), APoint(60.8065249039098, 114.46967708414569, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.16513512745453, 113.4494826265842, 0.0), APoint(66.14272960306572, 113.6420786965799, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.20748527825448, 117.21022402943996, 0.0), APoint(76.1619997259968, 117.60121414662666, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.54368997740988, 116.38262564187465, 0.0), APoint(81.4884487297482, 116.85747492532226, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.87989467656581, 115.55502725430878, 0.0), APoint(86.82465342890413, 116.0298765377564, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.21609937572161, 114.72742886674394, 0.0), APoint(92.16085812805993, 115.20227815019155, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.55230407487755, 113.89983047917808, 0.0), APoint(97.49706282721587, 114.37467976262569, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.89802320156018, 117.11522670791928, 0.0), APoint(112.8427819538985, 117.59007599136689, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.45335787072017, 117.18416951334885, 0.0), APoint(112.89804159766022, 117.11520297802412, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.7628197761157, 117.27916705997778, 0.0), APoint(76.20750350305576, 117.21020052465305, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.77143396078067, 114.7963717859884, 0.0), APoint(92.21611768772073, 114.72740525066367, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.10763868900231, 113.96877336132528, 0.0), APoint(97.55232241594237, 113.89980682600054, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.09902450433754, 116.45156863531462, 0.0), APoint(81.54370823127759, 116.38260209998988, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.43522923255918, 115.62397021065149, 0.0), APoint(86.87991295949924, 115.55500367532676, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.40848640973397, 116.5465661819432, 0.0), APoint(44.85317013667403, 116.47759964661847, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.74469113795562, 115.71896775728008, 0.0), APoint(50.18937486489568, 115.65000122195535, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.08089586617727, 114.89136933261696, 0.0), APoint(55.525579593117335, 114.82240279729223, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.417100594398924, 114.06377090795384, 0.0), APoint(60.86178432133899, 113.9948043726291, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(40.980731036397586, 114.5398333616108, 0.0), APoint(41.330823696334036, 114.67422134269029, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.18184295563499, 116.15248913456465, 0.0), APoint(45.53193561557144, 116.28687711564413, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.3829548748724, 117.76514490751849, 0.0), APoint(49.63252432043846, 117.86094564191504, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.166378216227365, 114.13939468123797, 0.0), APoint(48.516470876163815, 114.27378266231746, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.36749013546477, 115.75205045419182, 0.0), APoint(52.71758279540122, 115.8864384352713, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.568602054702176, 117.36470622714566, 0.0), APoint(56.918694714638626, 117.49909420822515, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.3520253960572, 113.73895600086527, 0.0), APoint(55.70211805599365, 113.87334398194476, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.553137315294606, 115.35161177381912, 0.0), APoint(59.903229975231056, 115.4859997548986, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.75424923453201, 116.96426754677296, 0.0), APoint(64.10434189446846, 117.09865552785244, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.737452906641465, 113.41520580437623, 0.0), APoint(62.88776523582349, 113.47290530157161, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.73878449512445, 114.95117309344597, 0.0), APoint(67.0888771550609, 115.08556107452546, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.93989641436185, 116.56382886639982, 0.0), APoint(71.2899890742983, 116.6982168474793, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.92443167495419, 114.55073441307331, 0.0), APoint(74.27452433489064, 114.6851223941528, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.12554359419146, 116.16339018602706, 0.0), APoint(78.4756362541279, 116.29777816710654, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.11007885478357, 114.15029573270061, 0.0), APoint(81.46017151472002, 114.2846837137801, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.31119077402097, 115.76295150565446, 0.0), APoint(85.66128343395742, 115.89733948673394, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.51230269325838, 117.3756072786083, 0.0), APoint(89.7064404044181, 117.45012976376661, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.29572603461344, 113.7498570523273, 0.0), APoint(88.64581869454989, 113.88424503340678, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.49683795385062, 115.36251282528129, 0.0), APoint(92.84693061378707, 115.49690080636077, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.69794987308802, 116.97516859823513, 0.0), APoint(97.04804253302447, 117.10955657931461, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.68248513368019, 114.96207414490861, 0.0), APoint(100.03257779361664, 115.0964621259881, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.8835970529176, 116.57472991786246, 0.0), APoint(104.23368971285404, 116.70911789894194, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.86813231351044, 114.56163546453561, 0.0), APoint(107.2182249734469, 114.6960234456151, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.06924423274785, 116.17429123748946, 0.0), APoint(111.4193368926843, 116.30867921856894, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.0537794933398, 114.16119678416308, 0.0), APoint(114.40387215327625, 114.29558476524257, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.06924529367113, 116.17429158836987, 0.0), APoint(111.31795656543764, 116.00653371732865, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.05378055486928, 114.16119713587518, 0.0), APoint(114.30249182663579, 113.99343926483397, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.88359811166694, 116.57473026812531, 0.0), APoint(104.13230938343345, 116.40697239708409, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.86813337286509, 114.56163581563062, 0.0), APoint(107.1168446446316, 114.3938779445894, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.69795092966277, 116.97516894787978, 0.0), APoint(96.94666220142928, 116.80741107683856, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.68248619086091, 114.9620744953851, 0.0), APoint(99.93119746262742, 114.79431662434388, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.51230374765866, 117.37560762763516, 0.0), APoint(89.70644040441897, 117.24466079921902, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.49683900885697, 115.36251317514046, 0.0), APoint(92.74555028062348, 115.19475530409925, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.31119182685254, 115.7629518548957, 0.0), APoint(85.55990309861905, 115.59519398385449, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.29572708805068, 113.74985740240102, 0.0), APoint(88.41123895425092, 113.67194366485259, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.12554464484852, 116.16339053465069, 0.0), APoint(78.37425591661503, 115.99563266360947, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.11007990604666, 114.150296082156, 0.0), APoint(81.35879117781317, 113.98253821111479, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.93989746284412, 116.56382921440566, 0.0), APoint(71.18860873461063, 116.39607134336444, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.92443272404226, 114.55073476191097, 0.0), APoint(74.17314399580877, 114.38297689086976, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.754250280840246, 116.96426789416104, 0.0), APoint(64.00296155260676, 116.79651002311982, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.7387855420384, 114.95117344166636, 0.0), APoint(66.98749681380491, 114.78341557062514, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.568603098835936, 117.36470657391571, 0.0), APoint(56.817314370602446, 117.1969487028745, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.55313836003408, 115.35161212142103, 0.0), APoint(59.80184963180059, 115.18385425037981, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.38295591683177, 117.76514525367138, 0.0), APoint(49.63166718859828, 117.59738738263016, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.367491178029915, 115.7520508011767, 0.0), APoint(52.616202449796425, 115.58429293013548, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.35202643922806, 113.73895634868201, 0.0), APoint(55.60073771099457, 113.57119847764079, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.181843996025485, 116.15248948093159, 0.0), APoint(45.430555267791995, 115.98473160989037, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.16637925722363, 114.13939502843691, 0.0), APoint(48.41509052899014, 113.97163715739569, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(40.98073207521969, 114.5398337081919, 0.0), APoint(41.2294433469862, 114.37207583715069, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.22940871090834, 114.37207140541722, 0.0), APoint(41.33079009595743, 114.67421724817602, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.430520594558175, 115.98472716944893, 0.0), APoint(45.53190197960727, 116.28687301220774, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.415055822626904, 113.97163271608889, 0.0), APoint(48.516437207676, 114.2737785588477, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.631632478207976, 117.59738293348055, 0.0), APoint(49.720362489303895, 117.86182402360366, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.616167706276876, 115.58428848012093, 0.0), APoint(52.71754909132597, 115.88643432287974, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.60070293434576, 113.57119402676142, 0.0), APoint(55.70208431939486, 113.87333986952022, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.817279589926834, 117.19694424415307, 0.0), APoint(56.91866097497593, 117.49909008691188, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.80181481799548, 115.18384979079272, 0.0), APoint(59.90319620304457, 115.48599563355152, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.86881320882321, 113.41651940739791, 0.0), APoint(62.88773143111333, 113.47290118019158, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.00292670164531, 116.79650555482444, 0.0), APoint(64.1043080866944, 117.09865139758324, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.98746192971414, 114.78341110146461, 0.0), APoint(67.08884331476324, 115.08555694422341, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.188573813364, 116.39606686549644, 0.0), APoint(71.2899551984131, 116.69821270825524, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.17310904143277, 114.38297241213648, 0.0), APoint(74.27449042648186, 114.68511825489529, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.37422092508261, 115.99562817616814, 0.0), APoint(78.4756023101317, 116.29777401892694, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.35875615315135, 113.98253372280804, 0.0), APoint(81.46013753820044, 114.28467956556685, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.55986803680112, 115.59518948683956, 0.0), APoint(85.66124942185021, 115.89733532959836, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.5751007052894, 113.67358228236253, 0.0), APoint(88.64578464991905, 113.88424087623854, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.74551514852007, 115.1947507975123, 0.0), APoint(92.84689653356916, 115.4968966402711, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.94662703216984, 116.8074065615438, 0.0), APoint(97.04800841721894, 117.1095524043026, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.93116226023879, 114.7943121081844, 0.0), APoint(100.03254364528789, 115.0964579509432, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.13227414388803, 116.40696787221559, 0.0), APoint(104.23365552893712, 116.7091137149744, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.11680937195676, 114.39387341885565, 0.0), APoint(107.21819075700586, 114.69601926161445, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.31792125560683, 116.0065291828879, 0.0), APoint(111.41930264065593, 116.3086750256467, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.30245648367557, 113.99343472952785, 0.0), APoint(114.40383786872466, 114.29558057228665, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(40.822673032481646, 114.7806193262433, 0.0), APoint(40.822673032481646, 114.7806193262433, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.48040672245728, 116.81997011342251, 0.0), APoint(43.48040672245728, 116.81997011342251, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.419607445871506, 115.15550084426641, 0.0), APoint(43.419607445871506, 115.15550084426641, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.047590385586226, 117.1720230778578, 0.0), APoint(46.047590385586226, 117.1720230778578, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.35880816928501, 113.49103157511, 0.0), APoint(43.35880816928501, 113.49103157511, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.98679110899973, 115.50755380870139, 0.0), APoint(45.98679110899973, 115.50755380870139, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.573122998349156, 117.49211606726982, 0.0), APoint(48.573122998349156, 117.49211606726982, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.92599183241229, 113.84308453954418, 0.0), APoint(45.92599183241229, 113.84308453954418, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.51232372176172, 115.82764679811261, 0.0), APoint(48.51232372176172, 115.82764679811261, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.17005741173735, 117.86699758529183, 0.0), APoint(51.17005741173735, 117.86699758529183, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.451524445176176, 114.16317752895664, 0.0), APoint(48.451524445176176, 114.16317752895664, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.10925813515181, 116.20252831613585, 0.0), APoint(51.10925813515181, 116.20252831613585, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.048458858565326, 114.53805904697944, 0.0), APoint(51.048458858565326, 114.53805904697944, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.676441798280045, 116.55458128057083, 0.0), APoint(53.676441798280045, 116.55458128057083, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.615642521693545, 114.89011201141417, 0.0), APoint(53.615642521693545, 114.89011201141417, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.20197441104297, 116.8746742699826, 0.0), APoint(56.20197441104297, 116.8746742699826, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.14117513445672, 115.2102050008263, 0.0), APoint(56.14117513445672, 115.2102050008263, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.79890882443235, 117.24955578800552, 0.0), APoint(58.79890882443235, 117.24955578800552, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.08037585787022, 113.54573573166967, 0.0), APoint(56.08037585787022, 113.54573573166967, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.73810954784586, 115.58508651884888, 0.0), APoint(58.73810954784586, 115.58508651884888, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.677310271259095, 113.9206172496919, 0.0), APoint(58.677310271259095, 113.9206172496919, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.305293210973815, 115.93713948328329, 0.0), APoint(61.305293210973815, 115.93713948328329, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.24449393438732, 114.27267021412688, 0.0), APoint(61.24449393438732, 114.27267021412688, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.830825823736745, 116.2572324726953, 0.0), APoint(63.830825823736745, 116.2572324726953, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.77002654715026, 114.59276320353855, 0.0), APoint(63.77002654715026, 114.59276320353855, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.4277602371259, 116.63211399071777, 0.0), APoint(66.4277602371259, 116.63211399071777, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.36696096053915, 114.96764472156079, 0.0), APoint(66.36696096053915, 114.96764472156079, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.99494390025386, 116.98416695515218, 0.0), APoint(68.99494390025386, 116.98416695515218, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.93414462366741, 115.31969768599609, 0.0), APoint(68.93414462366741, 115.31969768599609, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.52047651301683, 117.30425994456452, 0.0), APoint(71.52047651301683, 117.30425994456452, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.87334534708137, 113.65522841683966, 0.0), APoint(68.87334534708137, 113.65522841683966, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.45967723643079, 115.6397906754081, 0.0), APoint(71.45967723643079, 115.6397906754081, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.39887795984475, 113.97532140625158, 0.0), APoint(71.39887795984475, 113.97532140625158, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.0566116498204, 116.0146721934308, 0.0), APoint(74.0566116498204, 116.0146721934308, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.9958123732339, 114.35020292427437, 0.0), APoint(73.9958123732339, 114.35020292427437, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.62379531294862, 116.36672515786576, 0.0), APoint(76.62379531294862, 116.36672515786576, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.56299603636285, 114.70225588870966, 0.0), APoint(76.56299603636285, 114.70225588870966, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.14932792571159, 116.68681814727765, 0.0), APoint(79.14932792571159, 116.68681814727765, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.088528649125, 115.02234887812104, 0.0), APoint(79.088528649125, 115.02234887812104, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.74626233910064, 117.06169966530025, 0.0), APoint(81.74626233910064, 117.06169966530025, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.68546306251372, 115.39723039614348, 0.0), APoint(81.68546306251372, 115.39723039614348, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.31344600222843, 117.41375262973487, 0.0), APoint(84.31344600222843, 117.41375262973487, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.6246637859275, 113.73276112698717, 0.0), APoint(81.6246637859275, 113.73276112698717, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.25264672564221, 115.74928336057856, 0.0), APoint(84.25264672564221, 115.74928336057856, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.19184744905544, 114.08481409142158, 0.0), APoint(84.19184744905544, 114.08481409142158, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.77817933840487, 116.06937634999001, 0.0), APoint(86.77817933840487, 116.06937634999001, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.71738006181839, 114.40490708083371, 0.0), APoint(86.71738006181839, 114.40490708083371, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.37511375179403, 116.44425786801293, 0.0), APoint(89.37511375179403, 116.44425786801293, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.31431447520798, 114.77978859885629, 0.0), APoint(89.31431447520798, 114.77978859885629, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.94229741492283, 116.79631083244756, 0.0), APoint(91.94229741492283, 116.79631083244756, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.88149813833579, 115.13184156329095, 0.0), APoint(91.88149813833579, 115.13184156329095, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.46783002768521, 117.11640382185938, 0.0), APoint(94.46783002768521, 117.11640382185938, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.40703075109937, 115.45193455270339, 0.0), APoint(94.40703075109937, 115.45193455270339, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.34623147451315, 113.78746528354684, 0.0), APoint(94.34623147451315, 113.78746528354684, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.00396516448879, 115.82681607072605, 0.0), APoint(97.00396516448879, 115.82681607072605, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.94316588790203, 114.16234680156907, 0.0), APoint(96.94316588790203, 114.16234680156907, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.57114882761674, 116.17886903516046, 0.0), APoint(99.57114882761674, 116.17886903516046, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.51034955103025, 114.51439976600405, 0.0), APoint(99.51034955103025, 114.51439976600405, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.09668144037967, 116.49896202457248, 0.0), APoint(102.09668144037967, 116.49896202457248, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.03588216379342, 114.83449275541618, 0.0), APoint(102.03588216379342, 114.83449275541618, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.69361585376906, 116.8738435425954, 0.0), APoint(104.69361585376906, 116.8738435425954, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.63281657718157, 115.20937427343787, 0.0), APoint(104.63281657718157, 115.20937427343787, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.26079951689628, 117.22589650702926, 0.0), APoint(107.26079951689628, 117.22589650702926, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.20000024031006, 115.56142723787293, 0.0), APoint(107.20000024031006, 115.56142723787293, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(109.78633212965948, 117.54598949644136, 0.0), APoint(109.78633212965948, 117.54598949644136, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.13920096372402, 113.8969579687165, 0.0), APoint(107.13920096372402, 113.8969579687165, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(109.72553285307345, 115.88152022728494, 0.0), APoint(109.72553285307345, 115.88152022728494, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(109.66473357648742, 114.21705095812865, 0.0), APoint(109.66473357648742, 114.21705095812865, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.32246726646306, 116.25640174530787, 0.0), APoint(112.32246726646306, 116.25640174530787, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.2616679898766, 114.59193247615177, 0.0), APoint(112.2616679898766, 114.59193247615177, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.82885165300554, 114.94398544058706, 0.0), APoint(114.82885165300554, 114.94398544058706, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(42.787753468392225, 117.03562284992728, 0.0), APoint(42.787753468392225, 117.03562284992728, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.03945260587666, 117.2004121676051, 0.0), APoint(44.03945260587666, 117.2004121676051, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.93311229110064, 117.44971719474539, 0.0), APoint(45.93311229110064, 117.44971719474539, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.47240578118092, 115.06356429051537, 0.0), APoint(41.47240578118092, 115.06356429051537, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(42.724104918665354, 115.22835360819319, 0.0), APoint(42.724104918665354, 115.22835360819319, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.617764603889334, 115.47765863533348, 0.0), APoint(44.617764603889334, 115.47765863533348, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.77551648736492, 115.89338455755434, 0.0), APoint(47.77551648736492, 115.89338455755434, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.027215624849354, 116.05817387523216, 0.0), APoint(49.027215624849354, 116.05817387523216, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.920875310073335, 116.30747890237245, 0.0), APoint(50.920875310073335, 116.30747890237245, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.07862719354892, 116.72320482459331, 0.0), APoint(54.07862719354892, 116.72320482459331, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.330326331033355, 116.88799414227113, 0.0), APoint(55.330326331033355, 116.88799414227113, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.223986016257335, 117.13729916941142, 0.0), APoint(57.223986016257335, 117.13729916941142, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.4087572314548, 113.25629504878144, 0.0), APoint(41.4087572314548, 113.25629504878144, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.30241691667878, 113.50560007592173, 0.0), APoint(43.30241691667878, 113.50560007592173, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.460168800154364, 113.92132599814259, 0.0), APoint(46.460168800154364, 113.92132599814259, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.7118679376388, 114.08611531582041, 0.0), APoint(47.7118679376388, 114.08611531582041, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.60552762286278, 114.3354203429607, 0.0), APoint(49.60552762286278, 114.3354203429607, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.763279506338364, 114.75114626518156, 0.0), APoint(52.763279506338364, 114.75114626518156, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.0149786438228, 114.91593558285938, 0.0), APoint(54.0149786438228, 114.91593558285938, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.90863832904678, 115.16524060999967, 0.0), APoint(55.90863832904678, 115.16524060999967, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.066390212522364, 115.58096653222053, 0.0), APoint(59.066390212522364, 115.58096653222053, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.3180893500068, 115.74575584989834, 0.0), APoint(60.3180893500068, 115.74575584989834, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.21174903523078, 115.99506087703864, 0.0), APoint(62.21174903523078, 115.99506087703864, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.36950091870636, 116.4107867992595, 0.0), APoint(65.36950091870636, 116.4107867992595, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.6212000561908, 116.57557611693731, 0.0), APoint(66.6212000561908, 116.57557611693731, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.51485974141478, 116.82488114407761, 0.0), APoint(68.51485974141478, 116.82488114407761, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.67261162489037, 117.24060706629847, 0.0), APoint(71.67261162489037, 117.24060706629847, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.9243107623748, 117.40539638397628, 0.0), APoint(72.9243107623748, 117.40539638397628, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.75104252531248, 113.60890797280898, 0.0), APoint(57.75104252531248, 113.60890797280898, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.002741662796915, 113.7736972904868, 0.0), APoint(59.002741662796915, 113.7736972904868, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.896401348020895, 114.02300231762709, 0.0), APoint(60.896401348020895, 114.02300231762709, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.05415323149649, 114.43872823984795, 0.0), APoint(64.05415323149649, 114.43872823984795, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.30585236898092, 114.60351755752576, 0.0), APoint(65.30585236898092, 114.60351755752576, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.1995120542049, 114.85282258466606, 0.0), APoint(67.1995120542049, 114.85282258466606, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.35726393768049, 115.26854850688692, 0.0), APoint(70.35726393768049, 115.26854850688692, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.60896307516492, 115.43333782456473, 0.0), APoint(71.60896307516492, 115.43333782456473, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.5026227603889, 115.68264285170503, 0.0), APoint(73.5026227603889, 115.68264285170503, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.66037464386449, 116.09836877392588, 0.0), APoint(76.66037464386449, 116.09836877392588, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.91207378134796, 116.26315809160356, 0.0), APoint(77.91207378134796, 116.26315809160356, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.80573346657194, 116.51246311874385, 0.0), APoint(79.80573346657194, 116.51246311874385, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.96348535004752, 116.92818904096471, 0.0), APoint(82.96348535004752, 116.92818904096471, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.21518448753196, 117.09297835864253, 0.0), APoint(84.21518448753196, 117.09297835864253, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.10884417275594, 117.34228338578282, 0.0), APoint(86.10884417275594, 117.34228338578282, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.18727507317675, 113.71058429229295, 0.0), APoint(72.18727507317675, 113.71058429229295, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.34502695665233, 114.12631021451381, 0.0), APoint(75.34502695665233, 114.12631021451381, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.59672609413677, 114.29109953219162, 0.0), APoint(76.59672609413677, 114.29109953219162, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.09660719172913, 116.20004509340993, 0.0), APoint(91.09660719172913, 116.20004509340993, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.25435907520472, 116.61577101563078, 0.0), APoint(94.25435907520472, 116.61577101563078, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.50605821268915, 116.7805603333086, 0.0), APoint(95.50605821268915, 116.7805603333086, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.39971789791313, 117.0298653604489, 0.0), APoint(97.39971789791313, 117.0298653604489, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.55746978138872, 117.44559128266975, 0.0), APoint(100.55746978138872, 117.44559128266975, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.49038577936072, 114.54040455933189, 0.0), APoint(78.49038577936072, 114.54040455933189, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.6481376628363, 114.95613048155275, 0.0), APoint(81.6481376628363, 114.95613048155275, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.89983680032074, 115.12091979923056, 0.0), APoint(82.89983680032074, 115.12091979923056, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.79349648554472, 115.37022482637086, 0.0), APoint(84.79349648554472, 115.37022482637086, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.9512483690203, 115.78595074859172, 0.0), APoint(87.9512483690203, 115.78595074859172, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.20294750650474, 115.95074006626953, 0.0), APoint(89.20294750650474, 115.95074006626953, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.63590068180993, 113.81389218918007, 0.0), APoint(86.63590068180993, 113.81389218918007, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.88759981929437, 113.97868150685788, 0.0), APoint(87.88759981929437, 113.97868150685788, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.93901138799387, 114.64371245621906, 0.0), APoint(92.93901138799387, 114.64371245621906, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.19071052547831, 114.80850177389688, 0.0), APoint(94.19071052547831, 114.80850177389688, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.08437021070229, 115.05780680103717, 0.0), APoint(96.08437021070229, 115.05780680103717, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.24212209417787, 115.47353272325803, 0.0), APoint(99.24212209417787, 115.47353272325803, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.49382123166231, 115.63832204093585, 0.0), APoint(100.49382123166231, 115.63832204093585, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.38748091688629, 115.88762706807614, 0.0), APoint(102.38748091688629, 115.88762706807614, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.54523280036187, 116.303352990297, 0.0), APoint(105.54523280036187, 116.303352990297, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.79693193784631, 116.46814230797482, 0.0), APoint(106.79693193784631, 116.46814230797482, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.69059162307029, 116.71744733511511, 0.0), APoint(108.69059162307029, 116.71744733511511, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.84834350654587, 117.13317325733597, 0.0), APoint(111.84834350654587, 117.13317325733597, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.10004264403031, 117.29796257501378, 0.0), APoint(113.10004264403031, 117.29796257501378, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.07213322967601, 113.91556850866426, 0.0), APoint(101.07213322967601, 113.91556850866426, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.2298851131516, 114.33129443088512, 0.0), APoint(104.2298851131516, 114.33129443088512, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.48158425063603, 114.49608374856294, 0.0), APoint(105.48158425063603, 114.49608374856294, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.37524393586001, 114.74538877570323, 0.0), APoint(107.37524393586001, 114.74538877570323, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(110.5329958193356, 115.16111469792409, 0.0), APoint(110.5329958193356, 115.16111469792409, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.78469495682003, 115.3259040156019, 0.0), APoint(111.78469495682003, 115.3259040156019, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.67835464204401, 115.5752090427422, 0.0), APoint(113.67835464204401, 115.5752090427422, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.52075883830872, 114.01887640555138, 0.0), APoint(115.52075883830872, 114.01887640555138, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(116.77245797579316, 114.1836657232292, 0.0), APoint(116.77245797579316, 114.1836657232292, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(115.73700085336422, 115.43561081684663, 0.0), APoint(115.73700085336422, 115.43561081684663, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(116.79124016063032, 114.7639863064131, 0.0), APoint(116.79124016063032, 114.7639863064131, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.06788867250208, 115.54838517551852, 0.0), APoint(113.06788867250208, 115.54838517551852, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(114.12212797976818, 114.87676066508499, 0.0), APoint(114.12212797976818, 114.87676066508499, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(110.3987764916403, 115.66115953419038, 0.0), APoint(110.3987764916403, 115.66115953419038, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.4530157989064, 114.98953502375684, 0.0), APoint(111.4530157989064, 114.98953502375684, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.7296643107781, 115.77393389286223, 0.0), APoint(107.7296643107781, 115.77393389286223, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.7839036180442, 115.1023093824287, 0.0), APoint(108.7839036180442, 115.1023093824287, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.06055212991593, 115.88670825153405, 0.0), APoint(105.06055212991593, 115.88670825153405, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.11479143718203, 115.21508374110051, 0.0), APoint(106.11479143718203, 115.21508374110051, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.39143994905383, 115.99948261020606, 0.0), APoint(102.39143994905383, 115.99948261020606, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.44567925631993, 115.32785809977253, 0.0), APoint(103.44567925631993, 115.32785809977253, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.72232776819202, 116.1122569688777, 0.0), APoint(99.72232776819202, 116.1122569688777, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.77656707545812, 115.44063245844417, 0.0), APoint(100.77656707545812, 115.44063245844417, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.05321558733003, 116.22503132754993, 0.0), APoint(97.05321558733003, 116.22503132754993, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.10745489459613, 115.5534068171164, 0.0), APoint(98.10745489459613, 115.5534068171164, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.38410340646794, 116.33780568622198, 0.0), APoint(94.38410340646794, 116.33780568622198, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.43834271373404, 115.66618117578845, 0.0), APoint(95.43834271373404, 115.66618117578845, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.71499122560583, 116.45058004489394, 0.0), APoint(91.71499122560583, 116.45058004489394, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.76923053287193, 115.77895553446041, 0.0), APoint(92.76923053287193, 115.77895553446041, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.04587904474404, 116.56335440356565, 0.0), APoint(89.04587904474404, 116.56335440356565, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.3893449906804, 113.79626142057957, 0.0), APoint(93.3893449906804, 113.79626142057957, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.37676686388177, 116.67612876223745, 0.0), APoint(86.37676686388177, 116.67612876223745, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.43100617114787, 116.00450425180392, 0.0), APoint(87.43100617114787, 116.00450425180392, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.70765468301967, 116.78890312090942, 0.0), APoint(83.70765468301967, 116.78890312090942, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.76189399028577, 116.11727861047589, 0.0), APoint(84.76189399028577, 116.11727861047589, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.05112062895603, 114.02181013792328, 0.0), APoint(88.05112062895603, 114.02181013792328, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.03854250215764, 116.90167747958152, 0.0), APoint(81.03854250215764, 116.90167747958152, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.09278180942374, 116.23005296914799, 0.0), APoint(82.09278180942374, 116.23005296914799, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.382008448094, 114.13458449659538, 0.0), APoint(85.382008448094, 114.13458449659538, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.36943032129571, 117.01445183825295, 0.0), APoint(78.36943032129571, 117.01445183825295, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.42366962856181, 116.34282732781942, 0.0), APoint(79.42366962856181, 116.34282732781942, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.71289626723207, 114.24735885526681, 0.0), APoint(82.71289626723207, 114.24735885526681, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.70031814043367, 117.12722619692505, 0.0), APoint(75.70031814043367, 117.12722619692505, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.75455744769977, 116.45560168649152, 0.0), APoint(76.75455744769977, 116.45560168649152, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.04378408636991, 114.36013321393882, 0.0), APoint(80.04378408636991, 114.36013321393882, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.03120595957151, 117.24000055559699, 0.0), APoint(73.03120595957151, 117.24000055559699, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.08544526683761, 116.56837604516346, 0.0), APoint(74.08544526683761, 116.56837604516346, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.37467190550787, 114.47290757261085, 0.0), APoint(77.37467190550787, 114.47290757261085, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.36209377870924, 117.35277491426879, 0.0), APoint(70.36209377870924, 117.35277491426879, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.41633308597534, 116.68115040383526, 0.0), APoint(71.41633308597534, 116.68115040383526, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.7055597246456, 114.58568193128265, 0.0), APoint(74.7055597246456, 114.58568193128265, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.69298159784758, 117.4655492729407, 0.0), APoint(67.69298159784758, 117.4655492729407, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.74722090511368, 116.79392476250717, 0.0), APoint(68.74722090511368, 116.79392476250717, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.03644754378394, 114.69845628995456, 0.0), APoint(72.03644754378394, 114.69845628995456, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.07810872425152, 116.90669912117906, 0.0), APoint(66.07810872425152, 116.90669912117906, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.36733536292178, 114.81123064862645, 0.0), APoint(69.36733536292178, 114.81123064862645, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.408996543389286, 117.01947347985089, 0.0), APoint(63.408996543389286, 117.01947347985089, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.69822318205954, 114.92400500729828, 0.0), APoint(66.69822318205954, 114.92400500729828, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.73988436252726, 117.13224783852299, 0.0), APoint(60.73988436252726, 117.13224783852299, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.02911100119752, 115.03677936597038, 0.0), APoint(64.02911100119752, 115.03677936597038, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.01653287439941, 117.91664670762827, 0.0), APoint(57.01653287439941, 117.91664670762827, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.0707721816655, 117.24502219719474, 0.0), APoint(58.0707721816655, 117.24502219719474, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.35999882033575, 115.14955372464213, 0.0), APoint(61.35999882033575, 115.14955372464213, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.4016600008033, 117.3577965558665, 0.0), APoint(55.4016600008033, 117.3577965558665, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.69088663947355, 115.26232808331389, 0.0), APoint(58.69088663947355, 115.26232808331389, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.732547819941175, 117.47057091453843, 0.0), APoint(52.732547819941175, 117.47057091453843, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.021774458611425, 115.37510244198582, 0.0), APoint(56.021774458611425, 115.37510244198582, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.063435639079, 117.58334527321038, 0.0), APoint(50.063435639079, 117.58334527321038, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.35266227774925, 115.48787680065777, 0.0), APoint(53.35266227774925, 115.48787680065777, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.394323458217336, 117.69611963188231, 0.0), APoint(47.394323458217336, 117.69611963188231, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.683550096887586, 115.6006511593297, 0.0), APoint(50.683550096887586, 115.6006511593297, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.72521127735524, 117.80889399055428, 0.0), APoint(44.72521127735524, 117.80889399055428, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.01443791602549, 115.71342551800167, 0.0), APoint(48.01443791602549, 115.71342551800167, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.34532573516336, 115.82619987667364, 0.0), APoint(45.34532573516336, 115.82619987667364, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(42.676213554301285, 115.93897423534563, 0.0), APoint(42.676213554301285, 115.93897423534563, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.371652105521086, 113.27122312082254, 0.0), APoint(44.371652105521086, 113.27122312082254, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.70253992465894, 113.38399747949441, 0.0), APoint(41.70253992465894, 113.38399747949441, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(39.03342774379682, 113.49677183816642, 0.0), APoint(39.03342774379682, 113.49677183816642, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(112.08242709032957, 117.7400371042152, 0.0), APoint(112.08242709032957, 117.7400371042152, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.9919753926678, 115.99025846649064, 0.0), APoint(113.9919753926678, 115.99025846649064, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(109.16649624361723, 117.23951219255379, 0.0), APoint(109.16649624361723, 117.23951219255379, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(111.07604454595545, 115.48973355482923, 0.0), APoint(111.07604454595545, 115.48973355482923, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.25056539690544, 116.7389872808922, 0.0), APoint(106.25056539690544, 116.7389872808922, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.16011369924367, 114.98920864316764, 0.0), APoint(108.16011369924367, 114.98920864316764, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.13655887787696, 117.33629645660608, 0.0), APoint(102.13655887787696, 117.33629645660608, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.33463455019341, 116.23846236923063, 0.0), APoint(103.33463455019341, 116.23846236923063, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.24418285253164, 114.48868373150607, 0.0), APoint(105.24418285253164, 114.48868373150607, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.22062803116513, 116.83577154494496, 0.0), APoint(99.22062803116513, 116.83577154494496, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.41870370348158, 115.73793745756952, 0.0), APoint(100.41870370348158, 115.73793745756952, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.3282520058198, 113.98815881984495, 0.0), APoint(102.3282520058198, 113.98815881984495, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.30469718445335, 116.33524663328294, 0.0), APoint(96.30469718445335, 116.33524663328294, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.5027728567698, 115.23741254590749, 0.0), APoint(97.5027728567698, 115.23741254590749, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.38876633774116, 115.83472172162152, 0.0), APoint(93.38876633774116, 115.83472172162152, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.58684201005761, 114.73688763424607, 0.0), APoint(94.58684201005761, 114.73688763424607, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.6709111633458, 114.23636272258405, 0.0), APoint(91.6709111633458, 114.23636272258405, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.84741043154015, 117.31646591128589, 0.0), APoint(84.84741043154015, 117.31646591128589, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.55690464431736, 114.83367189829833, 0.0), APoint(87.55690464431736, 114.83367189829833, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.7549803166338, 113.73583781092289, 0.0), APoint(88.7549803166338, 113.73583781092289, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.93147958482831, 116.815940999624, 0.0), APoint(81.93147958482831, 116.815940999624, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.64097379760551, 114.33314698663645, 0.0), APoint(84.64097379760551, 114.33314698663645, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.01554873811632, 116.31541608796253, 0.0), APoint(79.01554873811632, 116.31541608796253, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.72504295089352, 113.83262207497498, 0.0), APoint(81.72504295089352, 113.83262207497498, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.19006958906587, 117.56466981402555, 0.0), APoint(74.19006958906587, 117.56466981402555, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.0996178914041, 115.81489117630099, 0.0), APoint(76.0996178914041, 115.81489117630099, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.27413874235431, 117.0641449023639, 0.0), APoint(71.27413874235431, 117.0641449023639, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.18368704469253, 115.31436626463935, 0.0), APoint(73.18368704469253, 115.31436626463935, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.35820789564232, 116.56361999070248, 0.0), APoint(68.35820789564232, 116.56361999070248, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.26775619798055, 114.81384135297792, 0.0), APoint(70.26775619798055, 114.81384135297792, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.24420137661404, 117.16092916641588, 0.0), APoint(64.24420137661404, 117.16092916641588, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.44227704893049, 116.06309507904044, 0.0), APoint(65.44227704893049, 116.06309507904044, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.35182535126872, 114.31331644131588, 0.0), APoint(67.35182535126872, 114.31331644131588, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.32827052990185, 116.6604042547544, 0.0), APoint(61.32827052990185, 116.6604042547544, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.5263462022183, 115.56257016737895, 0.0), APoint(62.5263462022183, 115.56257016737895, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.43589450455652, 113.81279152965439, 0.0), APoint(64.43589450455652, 113.81279152965439, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.41233968319, 116.15987934309317, 0.0), APoint(58.41233968319, 116.15987934309317, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.61041535550645, 115.06204525571772, 0.0), APoint(59.61041535550645, 115.06204525571772, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.49640883647819, 115.65935443143135, 0.0), APoint(55.49640883647819, 115.65935443143135, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.69448450879464, 114.56152034405591, 0.0), APoint(56.69448450879464, 114.56152034405591, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.87098377698885, 117.64162353275756, 0.0), APoint(49.87098377698885, 117.64162353275756, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.58047798976605, 115.15882951977001, 0.0), APoint(52.58047798976605, 115.15882951977001, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.7785536620825, 114.06099543239456, 0.0), APoint(53.7785536620825, 114.06099543239456, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.955052930277034, 117.14109862109576, 0.0), APoint(46.955052930277034, 117.14109862109576, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.664547143054236, 114.65830460810821, 0.0), APoint(49.664547143054236, 114.65830460810821, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.862622815370685, 113.56047052073276, 0.0), APoint(50.862622815370685, 113.56047052073276, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.03912208356514, 116.64057370943429, 0.0), APoint(44.03912208356514, 116.64057370943429, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(46.74861629634234, 114.15777969644674, 0.0), APoint(46.74861629634234, 114.15777969644674, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.12319123685306, 116.14004879777268, 0.0), APoint(41.12319123685306, 116.14004879777268, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.83268544963026, 113.65725478478512, 0.0), APoint(43.83268544963026, 113.65725478478512, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(315.0261675199058, 137.7897318778633, 0.0), APoint(315.02616751990126, 151.9897318777838, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(314.42616751990016, 151.98973187778256, 0.0), 0.6000000000011028, 2.08425869155913e-12, 1.5707963267966967)
entity.Color = 6

entity = acad.model.AddLine(APoint(314.4261675198991, 152.58973187778366, 0.0), APoint(311.02616751991627, 152.58973187778366, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(311.0261675199154, 151.98973187778276, 0.0), 0.6000000000009038, 1.5707963267934755, 3.1415926535866197)
entity.Color = 6

entity = acad.model.AddLine(APoint(310.42616751991454, 151.98973187778466, 0.0), APoint(310.42616751988953, 138.38973187786496, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(311.02616751989035, 138.38973187786476, 0.0), 0.6000000000008185, 3.141592653589462, 4.712388980386205)
entity.Color = 6

entity = acad.model.AddLine(APoint(311.02616751989126, 137.78973187786397, 0.0), APoint(322.6261675197984, 137.7897318778622, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(322.626167519798, 138.3897318778616, 0.0), 0.5999999999993975, 4.712388980385352, 8.526512829129765e-13)
entity.Color = 6

entity = acad.model.AddLine(APoint(323.2261675197974, 138.38973187786212, 0.0), APoint(323.2261675197974, 141.9897318778631, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(322.6261675197977, 141.98973187786333, 0.0), 0.5999999999996817, 6.283185307179207, 1.5707963267937597)
entity.Color = 6

entity = acad.model.AddLine(APoint(322.6261675197984, 142.58973187786302, 0.0), APoint(310.4261675198991, 142.58973187787228, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 143.1897318778158, 0.0), APoint(316.02616751969526, 143.18973187781563, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(316.02616751969526, 143.18973187781563, 0.0), APoint(316.02616751969526, 153.18973187781563, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(316.02616751969526, 153.18973187781563, 0.0), APoint(377.74293745552313, 153.18973187781563, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.2889364553862, 153.18973187781563, 0.0), APoint(403.4582339857434, 153.18973187781563, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.4582339857434, 153.18973187781563, 0.0), APoint(403.4582339857434, 143.1897318778161, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.4582339857434, 143.1897318778161, 0.0), APoint(379.2889364553862, 143.1897318778161, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.82616751968317, 143.18973187781563, 0.0), APoint(323.82616751968317, 137.18973187781563, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.82616751968317, 137.18973187781563, 0.0), APoint(309.8261675197414, 137.1897318777838, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(309.8261675197414, 137.1897318777838, 0.0), APoint(309.82616751971227, 153.18973187781563, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(309.82616751971227, 153.18973187781563, 0.0), APoint(315.62616751967107, 153.18973187781563, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(315.62616751967107, 153.18973187781563, 0.0), APoint(315.62616751967107, 143.1897318778161, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(315.62616751967107, 143.1897318778161, 0.0), APoint(323.82616751968317, 143.18973187781563, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.2889364553862, 139.2402199981439, 0.0), APoint(379.2889364553862, 147.61546331162668, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.2889364553862, 147.61546331162668, 0.0), APoint(378.5389364553862, 148.11546331162668, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(378.5389364553862, 148.11546331162668, 0.0), APoint(380.0389364553862, 148.61546331162668, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(380.0389364553862, 148.61546331162668, 0.0), APoint(379.2889364553862, 149.11546331162668, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.2889364553862, 149.11546331162668, 0.0), APoint(379.2889364553862, 157.0144870709708, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 139.2402199981439, 0.0), APoint(377.74293745552313, 147.61546331162668, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 147.61546331162668, 0.0), APoint(376.99293745552404, 148.11546331162668, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(376.99293745552404, 148.11546331162668, 0.0), APoint(378.49293745552313, 148.61546331162668, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(378.49293745552313, 148.61546331162668, 0.0), APoint(377.74293745552313, 149.11546331162668, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 149.11546331162668, 0.0), APoint(377.74293745552313, 157.0144870709708, 0.0))
entity.Color = 2
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(377.74293745552313, 144.18973187781563, 0.0), APoint(341.74146404991325, 144.18973187781563, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('O10@30', APoint(324.82818160770944, 132.14628268532795, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('8010', APoint(331.1429190208453, 136.7856516326113, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('T', APoint(332.2785868068695, 136.71696219218018, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('1', APoint(314.2010857431244, 156.72500693808894, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('2', APoint(406.58493009067575, 157.22605080591808, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('4', APoint(330.9552398123192, 160.32911618109966, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('5', APoint(376.45095238387336, 161.07993616246392, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('3', APoint(376.52962994965634, 135.40436515106398, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('T', APoint(325.03889461404185, 132.14628268532795, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('7', APoint(335.3730725371707, 131.0379466123499, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('6', APoint(338.40945256743544, 135.94412856730162, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddLine(APoint(365.4585020662116, 110.56471267642729, 0.0), APoint(365.4585020662116, 113.69027078058514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(375.9585020662121, 110.56471267642729, 0.0), APoint(375.9585020662121, 113.69027078058514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(364.4585020662116, 112.69027078058514, 0.0), APoint(368.68469254240233, 112.69027078058514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(376.9585020662121, 112.69027078058514, 0.0), APoint(372.73231159002137, 112.69027078058514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(364.45850206621174, 102.66471267642885, 0.0), APoint(358.67944506520485, 102.66471267642885, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(365.0585020662103, 110.16471267642885, 0.0), APoint(358.67944506520485, 110.16471267642885, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.67944506520485, 101.66471267642885, 0.0), APoint(359.67944506520485, 105.41471267642885, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(359.67944506520485, 111.16471267642885, 0.0), APoint(359.67944506520485, 107.41471267642885, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(365.4585020662116, 101.66471267642879, 0.0), APoint(365.4585020662116, 98.17776216005512, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9585020662116, 101.66471267642879, 0.0), APoint(366.9585020662116, 98.17776216005512, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9585020662116, 99.17776216005512, 0.0), APoint(364.4585020662116, 99.17776216005512, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(365.4585020662116, 99.17776216005512, 0.0), APoint(362.4965973043071, 99.17776216005512, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

# Entity type AcDbSolid not supported
entity = acad.model.AddText('2*2cm', APoint(379.72412524349477, 113.94338701962363, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('O10@30', APoint(360.4596440793264, 91.2430916469728, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('T', APoint(360.64288155283964, 91.40780034331772, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('9', APoint(356.96758023337964, 90.5590023041139, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddText('3O10', APoint(378.2794721943138, 106.2925555858547, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('T', APoint(379.67498902490894, 106.0764412280522, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddText('8', APoint(385.24900162296586, 105.52399644738296, 0.0), 1.171875)
entity.Color = 1

entity = acad.model.AddLine(APoint(230.88442357239285, 197.19044929801782, 0.0), APoint(230.9626880596804, 197.19044929801782, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(230.88442357240604, 187.53197630981742, 0.0), APoint(230.96268805968043, 187.53197630981742, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.9626880596804, 198.19044929801782, 0.0), APoint(229.9626880596804, 193.61121280391762, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(229.96268805968043, 186.53197630981742, 0.0), APoint(229.96268805968043, 191.1112128039176, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 185.53197630981737, 0.0), APoint(209.7651660952879, 191.15796787958521, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.76516609528153, 185.53197630981737, 0.0), APoint(206.76516609528153, 191.15796787958521, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.76516609528153, 190.15796787958521, 0.0), APoint(210.7651660952879, 190.15796787958521, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 190.15796787958521, 0.0), APoint(213.6675470476697, 190.15796787958521, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(206.76516609528153, 185.59447630981737, 0.0), APoint(206.76516609528153, 193.78740241369184, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.5151660952879, 185.59447630981737, 0.0), APoint(204.5151660952879, 193.78740241369184, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(207.76516609528153, 192.78740241369184, 0.0), APoint(204.5151660952879, 192.78740241369184, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.5151660952879, 192.78740241369184, 0.0), APoint(200.21992800005066, 192.78740241369184, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 181.2819763098173, 0.0), APoint(209.7651660952879, 178.3253667748982, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(204.5151660952879, 181.2819763098173, 0.0), APoint(204.5151660952879, 178.3253667748982, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(210.7651660952879, 179.3253667748982, 0.0), APoint(203.5151660952879, 179.3253667748982, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 181.2819763098173, 0.0), APoint(209.7651660952879, 176.11240280644563, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(239.7651660952879, 181.2819763098173, 0.0), APoint(239.7651660952879, 176.11240280644563, 0.0))
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

entity = acad.model.AddLine(APoint(209.7651660952879, 161.15697630981742, 0.0), APoint(209.7651660952879, 164.90189832989296, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.76816253149036, 161.1569763098193, 0.0), APoint(216.76816253149036, 164.90189832989296, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(208.7651660952879, 163.90189832989296, 0.0), APoint(217.76816253149036, 163.90189832989296, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(209.7651660952879, 161.21947630981742, 0.0), APoint(209.7651660952879, 164.90189832989296, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.26516609529244, 161.21947630983044, 0.0), APoint(196.26516609529244, 164.90189832989296, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(210.7651660952879, 163.90189832989296, 0.0), APoint(195.26516609529244, 163.90189832989296, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.26516609529244, 161.28197630983044, 0.0), APoint(196.26516609529244, 164.90189832989296, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253149036, 161.15697630981742, 0.0), APoint(194.26816253149036, 164.90189832989296, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.26516609529244, 163.90189832989296, 0.0), APoint(197.06516609529245, 163.90189832989296, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253149036, 163.90189832989296, 0.0), APoint(193.46816253149035, 163.90189832989296, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.515166095288, 182.28197630981737, 0.0), APoint(199.56461429924752, 182.28197630981737, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(205.76516609528164, 184.53197630981742, 0.0), APoint(199.56461429924752, 184.53197630981742, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.56461429924752, 182.28197630981737, 0.0), APoint(200.56461429924752, 181.48197630981736, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(200.56461429924752, 184.53197630981742, 0.0), APoint(200.56461429924752, 185.33197630981743, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.02237927593626, 184.53197630981742, 0.0), APoint(220.07182747989512, 184.53197630981742, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(224.02237927593626, 187.53197630981765, 0.0), APoint(220.07182747989512, 187.53197630981765, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.07182747989512, 183.53197630981742, 0.0), APoint(221.07182747989512, 187.53197630981765, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(221.07182747989512, 187.53197630981765, 0.0), APoint(221.07182747989512, 190.47483345267534, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(195.26516609529256, 160.15697630981748, 0.0), APoint(191.12448669788475, 160.15697630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(203.515166095288, 184.53197630981742, 0.0), APoint(191.12448669788475, 184.5319763098174, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.12448669788478, 159.15697630981748, 0.0), APoint(192.12448669788478, 171.09447630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.12448669788478, 185.53197630981742, 0.0), APoint(192.12448669788478, 173.59447630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(193.26816253149047, 160.15697630981748, 0.0), APoint(191.12448669788475, 160.15697630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(193.2681625314832, 152.65697630981748, 0.0), APoint(191.12448669788475, 152.65697630981745, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.12448669788478, 161.15697630981748, 0.0), APoint(192.12448669788478, 157.65697630981748, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.12448669788478, 151.65697630981748, 0.0), APoint(192.12448669788478, 155.15697630981748, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(194.26816253148309, 151.65697630981742, 0.0), APoint(194.26816253148309, 148.7229991960395, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(216.76816253148309, 151.65697630981742, 0.0), APoint(216.76816253148309, 148.7229991960395, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(193.26816253148309, 149.7229991960395, 0.0), APoint(217.76816253148309, 149.7229991960395, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 84.75264288110066, 0.0), APoint(34.118032157416565, 81.51599936022694, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695813, 84.67051786235214, 0.0), APoint(77.72399283695813, 81.51599936022694, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.118032157416565, 82.51599936022694, 0.0), APoint(78.72399283695813, 82.51599936022694, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695813, 84.60801786235214, 0.0), APoint(77.72399283695813, 81.51599936022694, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.11803215741656, 85.18764288110089, 0.0), APoint(121.11803215741656, 81.51599936022694, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.72399283695813, 82.51599936022694, 0.0), APoint(122.11803215741656, 82.51599936022694, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(34.118032157416565, 77.25226789047542, 0.0), APoint(34.118032157416565, 72.66976331948865, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(121.11803215741656, 78.20439290922445, 0.0), APoint(121.11803215741656, 72.66976331948865, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.118032157416565, 73.66976331948865, 0.0), APoint(122.11803215741656, 73.66976331948865, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.6582339857546, 143.1897318778157, 0.0), APoint(395.6582339857546, 137.1897318778157, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.6582339857546, 137.1897318778157, 0.0), APoint(409.65823398569637, 137.1897318777838, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(409.65823398569637, 137.1897318777838, 0.0), APoint(409.658233985725, 153.1897318778157, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(409.658233985725, 153.1897318778157, 0.0), APoint(403.8582339857371, 153.1897318778157, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.8582339857371, 153.1897318778157, 0.0), APoint(403.8582339857371, 143.1897318778157, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(403.8582339857371, 143.1897318778157, 0.0), APoint(395.6582339857546, 143.1897318778157, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.4582339855201, 137.7897318778634, 0.0), APoint(404.4582339855201, 151.9897318777838, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(405.0582339855212, 151.98973187778256, 0.0), 0.6000000000011028, 1.5707963267930967, 3.141592653587709)
entity.Color = 6

entity = acad.model.AddLine(APoint(405.0582339855223, 152.58973187778366, 0.0), APoint(408.4582339855101, 152.58973187778366, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(408.45823398550914, 151.98973187778458, 0.0), 0.5999999999990848, 1.4210854715224352e-13, 1.570796326793286)
entity.Color = 6

entity = acad.model.AddLine(APoint(409.0582339855082, 151.98973187778466, 0.0), APoint(409.0582339855332, 138.38973187786513, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(408.4582339855321, 138.38973187786507, 0.0), 0.6000000000011028, 4.712388980382889, 9.47390314345059e-14)
entity.Color = 6

entity = acad.model.AddLine(APoint(408.458233985531, 137.78973187786397, 0.0), APoint(396.858233985623, 137.7897318778622, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(396.8582339856245, 138.38973187786047, 0.0), 0.5999999999982606, 3.141592653587046, 4.712388980382132)
entity.Color = 6

entity = acad.model.AddLine(APoint(396.25823398562625, 138.38973187786212, 0.0), APoint(396.25823398562625, 141.98973187786316, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(396.85823398562485, 141.98973187786456, 0.0), 0.5999999999986017, 1.5707963267980232, 3.141592653592114)
entity.Color = 6

entity = acad.model.AddLine(APoint(396.858233985623, 142.58973187786313, 0.0), APoint(409.0582339855232, 142.5897318778724, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(281.84448815124654, 13.360720553617943, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(281.85753896499665, 12.513494171426213, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(323.69733720395936, 23.36072055361794, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(323.7103880177095, 22.513494171426213, 0.0), 0.18591496827833676)
entity.Color = 7

entity = acad.model.AddCircle(APoint(158.052347178314, 23.76519728070531, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(158.07099119795703, 22.554873877574266, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddLine(APoint(177.66602653143264, 98.92379186092643, 0.0), APoint(181.66602653143264, 98.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.66602653143264, 98.92379186092643, 0.0), APoint(181.66602653143264, 100.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.66602653143264, 100.92379186092643, 0.0), APoint(177.66602653143264, 100.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.66602653143264, 100.92379186092643, 0.0), APoint(177.66602653143264, 98.92379186092643, 0.0))
entity.Color = 3
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.6337574237632, 105.37145439080115, 0.0), APoint(151.80586459073947, 105.37145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.9022430126892, 104.65145439080115, 0.0), APoint(152.6222430126892, 104.65145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.3422430126892, 104.65145439080115, 0.0), APoint(154.0622430126892, 104.65145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.18224301268896, 103.93145439080115, 0.0), APoint(151.90224301268896, 103.93145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.62224301268895, 103.93145439080115, 0.0), APoint(153.34224301268895, 103.93145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.06224301268895, 103.93145439080115, 0.0), APoint(154.78224301268895, 103.93145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.50224301268895, 103.93145439080115, 0.0), APoint(156.22224301268895, 103.93145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.94224301268895, 103.93145439080115, 0.0), APoint(157.58138913502808, 103.93145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.3422430126888, 103.21145439080115, 0.0), APoint(154.0622430126888, 103.21145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.7822430126888, 103.21145439080115, 0.0), APoint(155.5022430126888, 103.21145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.2222430126888, 103.21145439080115, 0.0), APoint(156.9422430126888, 103.21145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.8917890369812, 102.49145439080115, 0.0), APoint(156.22224301268918, 102.49145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.94224301268918, 102.49145439080115, 0.0), APoint(157.2351407553715, 102.49145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.9022430126892, 104.92145439080113, 0.0), APoint(152.6222430126892, 104.92145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.3422430126892, 104.92145439080113, 0.0), APoint(153.6107160108295, 104.92145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.20604035974793, 104.20145439080113, 0.0), APoint(151.90224301268947, 104.20145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.62224301268947, 104.20145439080113, 0.0), APoint(153.34224301268947, 104.20145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.06224301268946, 104.20145439080113, 0.0), APoint(154.78224301268946, 104.20145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.50224301268946, 104.20145439080113, 0.0), APoint(156.22224301268946, 104.20145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.9211159127808, 103.48145439080113, 0.0), APoint(152.6222430126888, 103.48145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.3422430126888, 103.48145439080113, 0.0), APoint(154.0622430126888, 103.48145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.7822430126888, 103.48145439080113, 0.0), APoint(155.5022430126888, 103.48145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.2222430126888, 103.48145439080113, 0.0), APoint(156.9422430126888, 103.48145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.50224301268958, 102.76145439080113, 0.0), APoint(156.22224301268957, 102.76145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.94224301268957, 102.76145439080113, 0.0), APoint(157.33471376461057, 102.76145439080113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.9022430126892, 105.19145439080111, 0.0), APoint(152.52780515877566, 105.19145439080111, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.3047442975976, 104.47145439080111, 0.0), APoint(151.90224301268947, 104.47145439080111, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.62224301268947, 104.47145439080111, 0.0), APoint(153.34224301268947, 104.47145439080111, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.06224301268946, 104.47145439080111, 0.0), APoint(154.78224301268946, 104.47145439080111, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.04153379666514, 103.75145439080111, 0.0), APoint(151.1822430126892, 103.75145439080111, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.9022430126892, 103.75145439080111, 0.0), APoint(152.6222430126892, 103.75145439080111, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.3422430126892, 103.75145439080111, 0.0), APoint(154.0622430126892, 103.75145439080111, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.7822430126892, 103.75145439080111, 0.0), APoint(155.5022430126892, 103.75145439080111, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.2222430126892, 103.75145439080111, 0.0), APoint(156.9422430126892, 103.75145439080111, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.6622430126892, 103.75145439080111, 0.0), APoint(157.69981479848502, 103.75145439080111, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.06224301268907, 103.03145439080112, 0.0), APoint(154.78224301268907, 103.03145439080112, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.50224301268906, 103.03145439080112, 0.0), APoint(156.22224301268906, 103.03145439080112, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.94224301268906, 103.03145439080112, 0.0), APoint(157.43428677384873, 103.03145439080112, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.6137296050183, 102.31145439080112, 0.0), APoint(156.94224301268943, 102.31145439080112, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.2722430126878, 103.64323657508032, 0.0), APoint(151.2722430126878, 103.84145439080052, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.99224301268714, 103.84145439080072, 0.0), APoint(151.99224301268714, 104.56145439080072, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.99224301268714, 105.28145439080072, 0.0), APoint(151.99224301268714, 105.32498503108411, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.7122430126874, 103.28420425098614, 0.0), APoint(152.7122430126874, 103.84145439080143, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.7122430126874, 104.56145439080143, 0.0), APoint(152.7122430126874, 105.14546886903611, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.43224301268765, 103.10468808893904, 0.0), APoint(153.43224301268765, 103.12145439080163, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.43224301268765, 103.84145439080163, 0.0), APoint(153.43224301268765, 104.56145439080163, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.1522430126879, 103.12145439080095, 0.0), APoint(154.1522430126879, 103.84145439080095, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.1522430126879, 104.56145439080095, 0.0), APoint(154.1522430126879, 104.78643654494195, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.87224301268725, 102.74565576484488, 0.0), APoint(154.87224301268725, 103.12145439080166, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.87224301268725, 103.84145439080166, 0.0), APoint(154.87224301268725, 104.56145439080166, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.5922430126875, 103.12145439080095, 0.0), APoint(155.5922430126875, 103.84145439080095, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.31224301268776, 102.40145439080115, 0.0), APoint(156.31224301268776, 103.12145439080115, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.31224301268776, 103.84145439080115, 0.0), APoint(156.31224301268776, 104.24788805880067, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.0322430126871, 102.2071072787036, 0.0), APoint(157.0322430126871, 102.40145439080095, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.0322430126871, 103.12145439080095, 0.0), APoint(157.0322430126871, 103.84145439080095, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.54224301268732, 103.57591801431283, 0.0), APoint(151.54224301268732, 103.84145439080052, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.54224301268732, 104.56145439080052, 0.0), APoint(151.54224301268732, 105.12112100462912, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.26224301268667, 103.84145439080072, 0.0), APoint(152.26224301268667, 104.56145439080072, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.98224301268692, 103.21688569021865, 0.0), APoint(152.98224301268692, 103.84145439080143, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.98224301268692, 104.56145439080143, 0.0), APoint(152.98224301268692, 105.07815030826862, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.70224301268718, 103.03736952817155, 0.0), APoint(153.70224301268718, 103.12145439080163, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.70224301268718, 103.84145439080163, 0.0), APoint(153.70224301268718, 104.56145439080163, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.42224301268743, 103.12145439080092, 0.0), APoint(154.42224301268743, 103.84145439080092, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.42224301268743, 104.56145439080092, 0.0), APoint(154.42224301268743, 104.71911798417443, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.14224301268678, 102.67833720407737, 0.0), APoint(155.14224301268678, 103.12145439080163, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.14224301268678, 103.84145439080163, 0.0), APoint(155.14224301268678, 104.53960182212734, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.86224301268703, 103.12145439080092, 0.0), APoint(155.86224301268703, 103.84145439080092, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.5822430126873, 102.40145439080112, 0.0), APoint(156.5822430126873, 103.12145439080112, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.5822430126873, 103.84145439080112, 0.0), APoint(156.5822430126873, 104.18056949803315, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.30224301268663, 103.12145439080118, 0.0), APoint(157.30224301268663, 103.84145439080118, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.0922430126875, 103.84145439080129, 0.0), APoint(151.0922430126875, 103.89016707668429, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.81224301268776, 103.508599453545, 0.0), APoint(151.81224301268776, 103.84145439080109, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(151.81224301268776, 104.56145439080109, 0.0), APoint(151.81224301268776, 105.28145439080109, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(152.5322430126871, 103.84145439080038, 0.0), APoint(152.5322430126871, 104.56145439080038, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.25224301268736, 103.14956712945082, 0.0), APoint(153.25224301268736, 103.841454390802, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.25224301268736, 104.561454390802, 0.0), APoint(153.25224301268736, 105.01083174750079, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.9722430126876, 102.97005096740375, 0.0), APoint(153.9722430126876, 103.12145439080132, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(153.9722430126876, 103.84145439080132, 0.0), APoint(153.9722430126876, 104.56145439080132, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.69224301268787, 103.12145439080152, 0.0), APoint(154.69224301268787, 103.84145439080152, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(154.69224301268787, 104.56145439080152, 0.0), APoint(154.69224301268787, 104.65179942340663, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.4122430126872, 102.61101864330956, 0.0), APoint(155.4122430126872, 103.12145439080132, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(155.4122430126872, 103.84145439080132, 0.0), APoint(155.4122430126872, 104.47228326135954, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.13224301268747, 103.12145439080152, 0.0), APoint(156.13224301268747, 103.84145439080152, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.85224301268772, 102.40145439080081, 0.0), APoint(156.85224301268772, 103.1214543908008, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(156.85224301268772, 103.8414543908008, 0.0), APoint(156.85224301268772, 104.11325093726444, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(157.57224301268707, 103.40553351898473, 0.0), APoint(157.57224301268707, 103.84145439080052, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.58269319809924, 58.92379186092646, 0.0), APoint(197.1396672655453, 58.92379186092646, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.58269319809924, 48.92379186092646, 0.0), APoint(197.1396672655453, 48.92379186092646, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.1396672655453, 59.92379186092646, 0.0), APoint(196.1396672655453, 55.04879186092646, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(196.1396672655453, 47.92379186092645, 0.0), APoint(196.1396672655453, 52.79879186092646, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319809915, 47.92379186092643, 0.0), APoint(160.58269319809915, 43.43974908911008, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.58269319809915, 47.92379186092643, 0.0), APoint(191.58269319809915, 43.43974908911008, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(159.58269319809915, 44.43974908911008, 0.0), APoint(192.58269319809915, 44.43974908911008, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('1', APoint(165.85453237145921, 81.52144430895295, 0.0), 1.85)
entity.Color = 1

entity = acad.model.AddText('3', APoint(163.78766794529193, 79.14044925248028, 0.0), 1.85)
entity.Color = 1

entity = acad.model.AddLine(APoint(159.5826931980992, 58.92379186092646, 0.0), APoint(158.120222630938, 58.92379186092646, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(176.6660265314327, 98.92379186092649, 0.0), APoint(158.12022263093797, 98.92379186092647, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(159.120222630938, 57.92379186092646, 0.0), APoint(159.12022263093797, 77.79879186092646, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(159.12022263093797, 99.92379186092647, 0.0), APoint(159.12022263093797, 80.04879186092646, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.6660265314327, 100.92379186092649, 0.0), APoint(189.8012800032152, 100.92379186092649, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.6660265314327, 98.92379186092649, 0.0), APoint(189.8012800032152, 98.92379186092649, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(188.8012800032152, 101.92379186092649, 0.0), APoint(188.8012800032152, 97.92379186092649, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(177.66602653143264, 101.92379186092643, 0.0), APoint(177.66602653143264, 105.09097843329903, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143264, 99.92379186092643, 0.0), APoint(181.16602653143264, 105.09097843329903, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(176.66602653143264, 104.09097843329903, 0.0), APoint(182.16602653143264, 104.09097843329903, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143264, 97.92379186092643, 0.0), APoint(181.16602653143264, 92.54065940423379, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.66602653143264, 97.92379186092643, 0.0), APoint(181.66602653143264, 92.54065940423379, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143264, 93.54065940423379, 0.0), APoint(180.36602653143262, 93.54065940423379, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.66602653143264, 93.54065940423379, 0.0), APoint(182.46602653143265, 93.54065940423379, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(191.58269319809915, 59.92379186092643, 0.0), APoint(191.58269319809915, 65.3812055398758, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143264, 59.92379186092643, 0.0), APoint(181.16602653143264, 65.3812055398758, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(192.58269319809915, 64.3812055398758, 0.0), APoint(180.16602653143264, 64.3812055398758, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.10985877318402, 98.92379186092661, 0.0), APoint(161.39493651342727, 98.92379186092663, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddArc(APoint(176.10985877319175, 98.9237918609266, 0.0), 13.714922259764483, 2.8972465583105773, 3.1415926535897922)
entity.Color = 8

entity = acad.model.AddLine(APoint(181.16602653143264, 59.92379186092643, 0.0), APoint(181.16602653143264, 65.3812055398758, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(160.58269319809915, 59.92379186092643, 0.0), APoint(160.58269319809915, 65.3812055398758, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(182.16602653143264, 64.3812055398758, 0.0), APoint(159.58269319809915, 64.3812055398758, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(173.16602653143264, 95.67379186092643, 0.0), APoint(173.16602653143264, 88.96899617366165, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(181.16602653143264, 95.67379186092643, 0.0), APoint(181.16602653143264, 88.96899617366165, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(172.16602653143264, 89.96899617366165, 0.0), APoint(182.16602653143264, 89.96899617366165, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddCircle(APoint(320.8364129777301, 7.868212973627521, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddCircle(APoint(320.85505699737314, 6.657889570496479, 0.0), 0.2655928118261954)
entity.Color = 7

entity = acad.model.AddLine(APoint(77.43451926712547, 208.95397907461606, 0.0), APoint(77.06675145278615, 209.57244204043715, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.44686480033461, 207.17737608628028, 0.0), APoint(74.07909698599528, 207.79583905210137, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.94387221349126, 209.28995187680255, 0.0), APoint(75.96464922061068, 208.70765880552, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.38597559326493, 207.7689035662095, 0.0), APoint(75.36519858614545, 208.35119663749202, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.0254864313175, 208.61057004707308, 0.0), APoint(77.14297172343451, 208.61242911590836, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.96211409393219, 212.6154338953527, 0.0), APoint(77.07959938604918, 212.61729296418798, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.95903878905756, 208.85954988729657, 0.0), APoint(76.93682539388502, 210.26334256631915, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.90357738288596, 212.36447632232594, 0.0), APoint(76.9257907780585, 210.96068364330335, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.00458715460546, 204.5774907645796, 0.0), APoint(77.122072446722, 204.57934983341482, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.9412148172215, 208.5823546128592, 0.0), APoint(77.05870010933805, 208.58421368169442, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.93813951234515, 204.82647060480306, 0.0), APoint(76.91592611717307, 206.23026328382565, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.88267810617474, 208.33139703983244, 0.0), APoint(76.9048915013468, 206.92760436080988, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.43521360184195, 210.68643673910032, 0.0), APoint(80.07555900241887, 211.30937677847686, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.4352136018433, 208.95438593153204, 0.0), APoint(77.07555900242023, 209.57732597090853, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.94905265147278, 211.02849220579566, 0.0), APoint(78.9675543481192, 210.46182389614518, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.38206535336636, 209.54644139822733, 0.0), APoint(78.36356365671995, 210.11310970787775, 0.0))
entity.Color = 7
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('W2', APoint(127.52438225076138, 222.5575400186115, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('W1', APoint(130.54173148496866, 252.37351787828118, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('W4', APoint(37.73339928294934, 201.7921857348517, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('W3', APoint(35.22400902178464, 170.84613875616338, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(352.70155933255865, 155.44175414109864, 0.0), APoint(351.70155933255865, 155.6084208077653, 0.0))



entity = acad.model.AddLine(APoint(351.70155933255865, 155.6084208077653, 0.0), APoint(352.70155933255865, 155.77508747443196, 0.0))



entity = acad.model.AddLine(APoint(352.70155933255865, 155.44175414109864, 0.0), APoint(352.70155933255865, 155.77508747443196, 0.0))



entity = acad.model.AddLine(APoint(351.70155933255865, 155.6084208077653, 0.0), APoint(352.70155933255865, 155.6084208077653, 0.0))



entity = acad.model.AddLine(APoint(352.70155933255865, 155.6084208077653, 0.0), APoint(354.7150066166414, 155.6084208077653, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(369.1284539007261, 155.77508747443332, 0.0), APoint(370.1284539007261, 155.60842080776666, 0.0))



entity = acad.model.AddLine(APoint(370.1284539007261, 155.60842080776666, 0.0), APoint(369.1284539007261, 155.4417541411, 0.0))



entity = acad.model.AddLine(APoint(369.1284539007261, 155.77508747443332, 0.0), APoint(369.1284539007261, 155.4417541411, 0.0))



entity = acad.model.AddLine(APoint(370.1284539007261, 155.60842080776666, 0.0), APoint(369.1284539007261, 155.60842080776666, 0.0))



entity = acad.model.AddLine(APoint(369.1284539007261, 155.60842080776666, 0.0), APoint(367.11500661664286, 155.60842080776666, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(352.6949417565892, 139.89770174249736, 0.0), APoint(351.69521456423035, 140.06599707409077, 0.0))



entity = acad.model.AddLine(APoint(351.69521456423035, 140.06599707409077, 0.0), APoint(352.6954847186001, 140.2310346336188, 0.0))



entity = acad.model.AddLine(APoint(352.6949417565892, 139.89770174249736, 0.0), APoint(352.6954847186001, 140.2310346336188, 0.0))



entity = acad.model.AddLine(APoint(351.69521456423035, 140.06599707409077, 0.0), APoint(352.6952132375946, 140.06436818805807, 0.0))



entity = acad.model.AddLine(APoint(352.6952132375946, 140.06436818805807, 0.0), APoint(354.7086578505682, 140.06108851189947, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(369.1223574942634, 140.20427709449427, 0.0), APoint(370.1220846866222, 140.0359817629008, 0.0))



entity = acad.model.AddLine(APoint(370.1220846866222, 140.0359817629008, 0.0), APoint(369.1218145322525, 139.87094420337283, 0.0))



entity = acad.model.AddLine(APoint(369.1223574942634, 140.20427709449427, 0.0), APoint(369.1218145322525, 139.87094420337283, 0.0))



entity = acad.model.AddLine(APoint(370.1220846866222, 140.0359817629008, 0.0), APoint(369.12208601325796, 140.03761064893357, 0.0))



entity = acad.model.AddLine(APoint(369.12208601325796, 140.03761064893357, 0.0), APoint(367.10864140028434, 140.04089032509228, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.1174378109637, 139.70877711830957, 0.0), APoint(321.26368239231806, 140.25547581312333, 0.0))



entity = acad.model.AddLine(APoint(321.26368239231806, 140.25547581312333, 0.0), APoint(322.2485965542197, 140.01522204840077, 0.0))



entity = acad.model.AddLine(APoint(322.1174378109637, 139.70877711830957, 0.0), APoint(322.2485965542197, 140.01522204840077, 0.0))



entity = acad.model.AddLine(APoint(321.26368239231806, 140.25547581312333, 0.0), APoint(322.1830171825917, 139.86199958335516, 0.0))



entity = acad.model.AddLine(APoint(322.1830171825917, 139.86199958335516, 0.0), APoint(330.19855096694437, 136.43134293203047, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(330.19855096694437, 136.43134293203047, 0.0), APoint(337.75079053510535, 136.43134293203047, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(327.95097976619866, 149.28969887931956, 0.0), APoint(328.0123015168592, 148.2777614204449, 0.0))



entity = acad.model.AddLine(APoint(328.0123015168592, 148.2777614204449, 0.0), APoint(327.62609852281554, 149.21511142186884, 0.0))



entity = acad.model.AddLine(APoint(327.95097976619866, 149.28969887931956, 0.0), APoint(327.62609852281554, 149.21511142186884, 0.0))



entity = acad.model.AddLine(APoint(328.0123015168592, 148.2777614204449, 0.0), APoint(327.78853914450707, 149.2524051505942, 0.0))



entity = acad.model.AddLine(APoint(327.78853914450707, 149.2524051505942, 0.0), APoint(325.9461187781917, 157.2774517187582, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(325.9461187781917, 157.2774517187582, 0.0), APoint(316.05419461064184, 157.2774517187582, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(392.8891088300697, 150.3805550742041, 0.0), APoint(392.57975204881404, 149.41511415955995, 0.0))



entity = acad.model.AddLine(APoint(392.57975204881404, 149.41511415955995, 0.0), APoint(392.55927086957666, 150.4287010078738, 0.0))



entity = acad.model.AddLine(APoint(392.8891088300697, 150.3805550742041, 0.0), APoint(392.55927086957666, 150.4287010078738, 0.0))



entity = acad.model.AddLine(APoint(392.57975204881404, 149.41511415955995, 0.0), APoint(392.7241898498232, 150.40462804103896, 0.0))



entity = acad.model.AddLine(APoint(392.7241898498232, 150.40462804103896, 0.0), APoint(393.8005418173366, 157.77849558658727, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(393.8005418173366, 157.77849558658727, 0.0), APoint(405.764187294586, 157.77849558658727, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(345.13274521893595, 153.28828822517053, 0.0), APoint(345.12829259502314, 152.27450424822177, 0.0))



entity = acad.model.AddLine(APoint(345.12829259502314, 152.27450424822177, 0.0), APoint(344.80370973322755, 153.2349331855234, 0.0))



entity = acad.model.AddLine(APoint(345.13274521893595, 153.28828822517053, 0.0), APoint(344.80370973322755, 153.2349331855234, 0.0))



entity = acad.model.AddLine(APoint(345.12829259502314, 152.27450424822177, 0.0), APoint(344.9682274760817, 153.26161070534698, 0.0))



entity = acad.model.AddLine(APoint(344.9682274760817, 153.26161070534698, 0.0), APoint(343.73260771560126, 160.8815609617689, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(343.73260771560126, 160.8815609617689, 0.0), APoint(332.91995582269055, 160.8815609617689, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028434945, 155.62040439582847, 0.0), APoint(360.92038028434945, 161.69936638179462, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028434945, 161.69936638179462, 0.0), APoint(375.72958592492296, 161.69936638179462, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028434945, 142.03577191769944, 0.0), APoint(360.92038028434945, 135.9568099317333, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.92038028434945, 135.9568099317333, 0.0), APoint(375.8082634907055, 135.9568099317333, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.52137507683335, 137.05185368297936, 0.0), APoint(316.8261675198455, 137.789731877863, 0.0))



entity = acad.model.AddLine(APoint(316.8261675198455, 137.789731877863, 0.0), APoint(317.72310813695844, 137.31721171199615, 0.0))



entity = acad.model.AddLine(APoint(317.52137507683335, 137.05185368297936, 0.0), APoint(317.72310813695844, 137.31721171199615, 0.0))



entity = acad.model.AddLine(APoint(316.8261675198455, 137.789731877863, 0.0), APoint(317.6222416068959, 137.18453269748775, 0.0))



entity = acad.model.AddLine(APoint(317.6222416068959, 137.18453269748775, 0.0), APoint(324.9522749420562, 131.61202350679292, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(324.9522749420562, 131.61202350679292, 0.0), APoint(334.68506503997014, 131.61202350679292, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('0.35', APoint(369.04183539954516, 112.19027078058514, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddText('0.25', APoint(358.0127783985381, 105.9147126764287, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddText('0.05', APoint(358.8061211138309, 98.67776216005512, 0.0), 1.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(376.40829467347373, 110.52863943608405, 0.0), APoint(379.829958626839, 113.77400312111996, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(379.829958626839, 113.77400312111996, 0.0), APoint(387.1255387366291, 113.77400312111996, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.727434834383, 96.74607572292847, 0.0), APoint(374.4585020662121, 97.44844206631598, 0.0))



entity = acad.model.AddLine(APoint(374.4585020662121, 97.44844206631598, 0.0), APoint(373.9947464717967, 96.54693858522106, 0.0))



entity = acad.model.AddLine(APoint(373.727434834383, 96.74607572292847, 0.0), APoint(373.9947464717967, 96.54693858522106, 0.0))



entity = acad.model.AddLine(APoint(374.4585020662121, 97.44844206631598, 0.0), APoint(373.8610906530899, 96.64650715407477, 0.0))



entity = acad.model.AddLine(APoint(373.8610906530899, 96.64650715407477, 0.0), APoint(369.7376786314453, 91.1114470847831, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(369.7376786314453, 91.1114470847831, 0.0), APoint(359.4208712720606, 91.1114470847831, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(230.3626880596804, 196.79044929801782, 0.0), APoint(229.5626880596804, 197.59044929801783, 0.0))



entity = acad.model.AddLine(APoint(229.56268805968043, 187.93197630981743, 0.0), APoint(230.36268805968044, 187.13197630981742, 0.0))



entity = acad.model.AddText('Hs=0.25', APoint(227.64125948825185, 191.6112128039175, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(207.16516609528153, 190.55796787958522, 0.0), APoint(206.36516609528152, 189.7579678795852, 0.0))



entity = acad.model.AddLine(APoint(209.3651660952879, 189.7579678795852, 0.0), APoint(210.1651660952879, 190.55796787958522, 0.0))



entity = acad.model.AddText('0.3', APoint(211.09611847624112, 190.65796787958521, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(206.36516609528152, 192.38740241369183, 0.0), APoint(207.16516609528153, 193.18740241369184, 0.0))



entity = acad.model.AddLine(APoint(204.9151660952879, 193.18740241369184, 0.0), APoint(204.1151660952879, 192.38740241369183, 0.0))



entity = acad.model.AddText('0.25', APoint(200.50564228576494, 193.28740241369184, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(209.3651660952879, 178.9253667748982, 0.0), APoint(210.1651660952879, 179.72536677489822, 0.0))



entity = acad.model.AddLine(APoint(204.9151660952879, 179.72536677489822, 0.0), APoint(204.1151660952879, 178.9253667748982, 0.0))



entity = acad.model.AddText('0.55', APoint(205.71159466671648, 179.8253667748982, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(210.1651660952879, 177.51240280644564, 0.0), APoint(209.3651660952879, 176.71240280644562, 0.0))



entity = acad.model.AddLine(APoint(239.3651660952879, 176.71240280644562, 0.0), APoint(240.1651660952879, 177.51240280644564, 0.0))



entity = acad.model.AddText('2.12', APoint(223.97945180957362, 177.61240280644563, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(210.1651660952879, 164.30189832989296, 0.0), APoint(209.3651660952879, 163.50189832989295, 0.0))



entity = acad.model.AddLine(APoint(216.36816253149036, 163.50189832989295, 0.0), APoint(217.16816253149037, 164.30189832989296, 0.0))



entity = acad.model.AddText('0.7', APoint(211.873807170532, 164.40189832989296, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(209.3651660952879, 163.50189832989295, 0.0), APoint(210.1651660952879, 164.30189832989296, 0.0))



entity = acad.model.AddLine(APoint(196.66516609529245, 164.30189832989296, 0.0), APoint(195.86516609529244, 163.50189832989295, 0.0))



entity = acad.model.AddText('1.1', APoint(201.80088038100448, 164.40189832989296, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(196.66516609529245, 164.30189832989296, 0.0), APoint(195.86516609529244, 163.50189832989295, 0.0))



entity = acad.model.AddLine(APoint(193.86816253149036, 163.50189832989295, 0.0), APoint(194.66816253149037, 164.30189832989296, 0.0))



entity = acad.model.AddText('0.0', APoint(194.08809288481996, 164.40189832989296, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(200.96461429924753, 181.88197630981736, 0.0), APoint(200.16461429924752, 182.68197630981737, 0.0))



entity = acad.model.AddLine(APoint(200.16461429924752, 184.93197630981743, 0.0), APoint(200.96461429924753, 184.13197630981742, 0.0))



entity = acad.model.AddText('0.30', APoint(198.0646142992475, 182.6569763098173, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(220.67182747989511, 184.93197630981743, 0.0), APoint(221.47182747989513, 184.13197630981742, 0.0))



entity = acad.model.AddLine(APoint(221.47182747989513, 187.13197630981765, 0.0), APoint(220.67182747989511, 187.93197630981766, 0.0))



entity = acad.model.AddText('0.3', APoint(220.5718274798951, 190.47483345267534, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(191.72448669788477, 160.5569763098175, 0.0), APoint(192.52448669788478, 159.75697630981747, 0.0))



entity = acad.model.AddLine(APoint(192.52448669788478, 184.13197630981742, 0.0), APoint(191.72448669788477, 184.93197630981743, 0.0))



entity = acad.model.AddText('0.55', APoint(191.33877241217047, 171.59447630981737, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(192.52448669788478, 159.75697630981747, 0.0), APoint(191.72448669788477, 160.5569763098175, 0.0))



entity = acad.model.AddLine(APoint(191.72448669788477, 153.0569763098175, 0.0), APoint(192.52448669788478, 152.25697630981747, 0.0))



entity = acad.model.AddText('0.8', APoint(191.0530581264562, 155.6569763098174, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(194.6681625314831, 150.1229991960395, 0.0), APoint(193.86816253148308, 149.3229991960395, 0.0))



entity = acad.model.AddLine(APoint(216.36816253148308, 149.3229991960395, 0.0), APoint(217.1681625314831, 150.1229991960395, 0.0))



entity = acad.model.AddText('1.8', APoint(205.08959110291167, 150.2229991960395, 0.0), 1.5)
entity.Color = 1

entity = acad.model.AddLine(APoint(75.80977665059508, 120.45179028096756, 0.0), APoint(72.422787176165, 124.53895060080151, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.422787176165, 124.53895060080151, 0.0), APoint(65.20766424672229, 124.52392338144148, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('A=8.3', APoint(53.9686315448064, 83.01599936022694, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('B=10.1', APoint(97.18291725909211, 83.01599936022694, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('L=18.38', APoint(75.67637378933908, 74.16976331948865, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddLine(APoint(108.99942033948224, 208.87339986711547, 0.0), APoint(108.7766922411588, 209.8624246251448, 0.0))



entity = acad.model.AddLine(APoint(108.7766922411588, 209.8624246251448, 0.0), APoint(109.308145769204, 208.99909680484356, 0.0))



entity = acad.model.AddLine(APoint(108.99942033948224, 208.87339986711547, 0.0), APoint(109.308145769204, 208.99909680484356, 0.0))



entity = acad.model.AddLine(APoint(108.7766922411588, 209.8624246251448, 0.0), APoint(109.15378305434312, 208.9362483359795, 0.0))



entity = acad.model.AddLine(APoint(109.15378305434312, 208.9362483359795, 0.0), APoint(110.60219448877433, 205.37879140352882, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(110.60219448877433, 205.37879140352882, 0.0), APoint(105.93220525109427, 202.5694253217833, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.449122366406755, 117.62756887841576, 0.0), APoint(30.726912704093138, 119.17146402882042, 0.0))
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

entity = acad.model.AddLine(APoint(196.53966726554532, 58.52379186092646, 0.0), APoint(195.7396672655453, 59.323791860926455, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(195.7396672655453, 49.323791860926455, 0.0), APoint(196.53966726554532, 48.52379186092646, 0.0))
entity.Color = 7


entity = acad.model.AddText('m', APoint(195.24681012268812, 53.298791860926386, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(160.98269319809916, 44.83974908911008, 0.0), APoint(160.18269319809914, 44.03974908911008, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(191.18269319809914, 44.03974908911008, 0.0), APoint(191.98269319809916, 44.83974908911008, 0.0))
entity.Color = 7


entity = acad.model.AddText('f', APoint(175.7255503409563, 44.93974908911008, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(158.720222630938, 59.323791860926455, 0.0), APoint(159.520222630938, 58.52379186092646, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(159.52022263093798, 98.52379186092647, 0.0), APoint(158.72022263093797, 99.32379186092648, 0.0))
entity.Color = 7


entity = acad.model.AddText('h', APoint(158.55474644046177, 78.2987918609264, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(189.2012800032152, 100.52379186092648, 0.0), APoint(188.4012800032152, 101.32379186092649, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(188.4012800032152, 99.32379186092649, 0.0), APoint(189.2012800032152, 98.52379186092648, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.20', APoint(189.33064969115253, 99.2987918609264, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(178.06602653143264, 104.49097843329903, 0.0), APoint(177.26602653143263, 103.69097843329902, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(180.76602653143263, 103.69097843329902, 0.0), APoint(181.56602653143264, 104.49097843329903, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.35', APoint(177.7470814287667, 104.60707126311934, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(180.76602653143263, 93.14065940423379, 0.0), APoint(181.56602653143264, 93.9406594042338, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(182.06602653143264, 93.9406594042338, 0.0), APoint(181.26602653143263, 93.14065940423379, 0.0))
entity.Color = 7


entity = acad.model.AddText('0.05', APoint(181.16602653143264, 91.50846522139454, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(191.18269319809914, 63.981205539875795, 0.0), APoint(191.98269319809916, 64.7812055398758, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(181.56602653143264, 64.7812055398758, 0.0), APoint(180.76602653143263, 63.981205539875795, 0.0))



entity = acad.model.AddText('b', APoint(185.7791217695278, 64.8812055398758, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddText('max 14', APoint(156.6938338885118, 100.19778398280062, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(180.76602653143263, 63.981205539875795, 0.0), APoint(181.56602653143264, 64.7812055398758, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(160.98269319809916, 64.7812055398758, 0.0), APoint(160.18269319809914, 63.981205539875795, 0.0))
entity.Color = 7


entity = acad.model.AddText('s1', APoint(169.95174081714686, 64.8812055398758, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(173.56602653143264, 90.36899617366166, 0.0), APoint(172.76602653143263, 89.56899617366165, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(180.76602653143263, 89.56899617366165, 0.0), APoint(181.56602653143264, 90.36899617366166, 0.0))
entity.Color = 7


entity = acad.model.AddText('s2', APoint(176.06483605524218, 90.46899617366165, 0.0), 1.25)
entity.Color = 1

entity = acad.model.AddLine(APoint(77.0513116751324, 209.35384054623822, 0.0), APoint(76.94387221349125, 209.28995187680252, 0.0))



entity = acad.model.AddLine(APoint(74.2785361316238, 207.7050148967738, 0.0), APoint(74.38597559326494, 207.7689035662095, 0.0))



entity = acad.model.AddText('S', APoint(75.57077208615235, 208.10176876704188, 0.0), 0.65)
entity.Color = 7

entity = acad.model.AddLine(APoint(76.961016521861, 208.73456553398398, 0.0), APoint(76.95903878905756, 208.85954988729654, 0.0))



entity = acad.model.AddLine(APoint(76.90159965008252, 212.4894606756385, 0.0), APoint(76.90357738288596, 212.36447632232594, 0.0))



entity = acad.model.AddText('S', APoint(76.6071516314246, 210.90642665578284, 0.0), 0.65)
entity.Color = 7

entity = acad.model.AddLine(APoint(76.94011724514853, 204.7014862514905, 0.0), APoint(76.93813951234513, 204.82647060480306, 0.0))



entity = acad.model.AddLine(APoint(76.88070037337134, 208.456381393145, 0.0), APoint(76.88267810617474, 208.33139703983244, 0.0))



entity = acad.model.AddText('S', APoint(76.58625235471284, 206.87334737328945, 0.0), 0.65)
entity.Color = 7

entity = acad.model.AddLine(APoint(80.05730582694584, 211.09099220579566, 0.0), APoint(79.94905265147278, 211.02849220579566, 0.0))



entity = acad.model.AddLine(APoint(77.2738121778933, 209.48394139822733, 0.0), APoint(77.38206535336636, 209.54644139822733, 0.0))



entity = acad.model.AddText('S', APoint(78.56590852208764, 209.8610555828932, 0.0), 0.65)
entity.Color = 7

entity = acad.model.AddLine(APoint(141.41851682296016, 221.59769433739626, 0.0), APoint(142.60634674462557, 222.80974222308242, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(117.83261054887492, 222.5597422230779, 0.0), APoint(116.64478062720951, 221.34769433739174, 0.0))



entity = acad.model.AddLine(APoint(119.7777779641879, 241.7509857137379, 0.0), APoint(119.7777779641879, 240.05392943889015, 0.0))



entity = acad.model.AddLine(APoint(144.47679953725452, 264.7529510119564, 0.0), APoint(144.47679953725452, 266.45000728680407, 0.0))



entity = acad.model.AddLine(APoint(27.98012416694459, 201.79376728793918, 0.0), APoint(26.792294245279187, 200.58171940225301, 0.0))



entity = acad.model.AddLine(APoint(51.56603044103028, 200.83171940225765, 0.0), APoint(52.75386036269569, 202.0437672879438, 0.0))



entity = acad.model.AddLine(APoint(48.99299200439391, 183.05948682016228, 0.0), APoint(48.99299200439391, 184.75654309501002, 0.0))



entity = acad.model.AddLine(APoint(24.29397043132775, 160.0575215219438, 0.0), APoint(24.29397043132775, 158.36046524709607, 0.0))



entity = acad.model.AddLine(APoint(96.13129650082249, 214.90443908498085, 0.0), APoint(96.63129650082249, 214.40443908498085, 0.0))



entity = acad.model.AddLine(APoint(95.52888013555162, 219.01871297126834, 0.0), APoint(94.84586743365944, 219.20172567316067, 0.0))



entity = acad.model.AddLine(APoint(314.40633683626623, 152.12533055395352, 0.0), APoint(314.64921188713754, 152.36820560482488, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.44915799781415, 151.99137502020486, 0.0), APoint(314.78316742088623, 152.32538444327687, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.5451488149612, 151.91058914205524, 0.0), APoint(314.8639532990358, 152.22939362612988, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.70748429445547, 151.89614792625287, 0.0), APoint(314.8783945148382, 152.06705814663562, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.5560153122291, 142.24378610965942, 0.0), APoint(322.7968536019732, 142.48462439940354, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.59800817970284, 142.10900228183652, 0.0), APoint(322.93163742979607, 142.4426315319298, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.69343484687295, 142.02765225371, 0.0), APoint(323.01298745792263, 142.3472048647597, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.8543939011152, 142.0118346126556, 0.0), APoint(323.028805098977, 142.1862458105174, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.5560443128842, 138.1779511184919, 0.0), APoint(322.79218963291544, 138.4140964385231, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.5961407242037, 138.0412708345147, 0.0), APoint(322.9288699168926, 138.3740000272037, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.69030660523504, 137.95866002024948, 0.0), APoint(323.0114807311578, 138.27983414617225, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(322.84831921760133, 137.93989593731908, 0.0), APoint(323.03024481408823, 138.12182153380604, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.5680184371057, 152.17609945131906, 0.0), APoint(310.755318229366, 152.36339924357938, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.58888485717466, 152.02018917609138, 0.0), APoint(310.91122850459374, 152.3425328235104, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.67244078018166, 151.92696840380174, 0.0), APoint(311.00444927688335, 152.2589769005034, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.81058594961496, 151.88833687793834, 0.0), APoint(311.0430808027468, 152.12083173107015, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.51640973799647, 138.1591318237755, 0.0), APoint(310.777590746718, 138.42031283249702, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.56686454703197, 138.03280993751437, 0.0), APoint(310.9039126329791, 138.3698580234615, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.66846490885024, 137.957633604036, 0.0), APoint(310.9790889664575, 138.26825766164325, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.84721684789184, 137.95960884778094, 0.0), APoint(310.9771137227126, 138.08950572260167, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.50698570621995, 138.08384380017634, 0.0), APoint(314.8007892885365, 138.37764738249285, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.5726046529977, 137.97268605165746, 0.0), APoint(314.91194703705537, 138.3120284357151, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.6879354619881, 137.91124016535122, 0.0), APoint(314.97339292336164, 138.19669762672476, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.5319973256918, 142.4173600985901, 0.0), APoint(310.66762848015196, 142.5529912530502, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.53235822804027, 142.24094430564193, 0.0), APoint(310.84404427310005, 142.55263035070172, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.6082145916781, 142.14002397398318, 0.0), APoint(310.94496460475887, 142.47677398706386, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(310.7354085128061, 142.0904411998145, 0.0), APoint(310.99454737892756, 142.34958006593592, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.2944224956233, 144.05326110491907, 0.0), APoint(317.4204410544736, 144.1792796637694, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.2908580981393, 143.87292001213848, 0.0), APoint(317.60078214725417, 144.18284406125338, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.3655926679533, 143.77087788665585, 0.0), APoint(317.7028242727368, 144.10810949143934, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.4913552522549, 143.71986377566083, 0.0), APoint(317.7538383837318, 143.98234690713775, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.2843295237278, 151.644566030779, 0.0), APoint(317.5812491920782, 151.94148569912943, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.3515843163542, 151.53504412810878, 0.0), APoint(317.69077109474847, 151.87423090650302, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(317.4686458170538, 151.47532893351172, 0.0), APoint(317.75048628934553, 151.75716940580344, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.5073240267628, 144.07897830067634, 0.0), APoint(323.5947238587166, 144.16637813263014, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.4874731649553, 143.8823507435722, 0.0), APoint(323.7913514158207, 144.1862289944376, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.558577965152, 143.77667884847222, 0.0), APoint(323.8970233109207, 144.11512419424093, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.67994608422185, 143.72127027224548, 0.0), APoint(323.95243188714744, 143.99375607517106, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.4816556010523, 151.65470777272122, 0.0), APoint(323.77110745013675, 151.94415962180568, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.54506441089626, 151.54133988726852, 0.0), APoint(323.8844753355894, 151.88075081196172, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(323.6581434124544, 151.47764219353007, 0.0), APoint(323.9481730293279, 151.76767181040356, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.6844257045848, 143.89211894781937, 0.0), APoint(329.9815832115738, 144.1892764548084, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.75180738008476, 143.78272392802273, 0.0), APoint(330.09097823137046, 144.12189477930838, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.8690054907388, 143.72314534338008, 0.0), APoint(330.1505568160131, 144.0046966686544, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.67937232957905, 151.66524016586567, 0.0), APoint(329.9605750569928, 151.94644289327942, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.7387865426701, 151.54787768366003, 0.0), APoint(330.0779375391984, 151.8870286801884, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(329.84802932165917, 151.48034376735254, 0.0), APoint(330.1454714555059, 151.77778590119928, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.881739200995, 143.90224810884735, 0.0), APoint(336.171454050547, 144.19196295839936, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.9452793473108, 143.7890115598665, 0.0), APoint(336.2846905995279, 144.12842281208356, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(336.0584894863827, 143.7254450036417, 0.0), APoint(336.34825715575266, 144.01521267301166, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.8775152340484, 151.67619873495278, 0.0), APoint(336.1496164879062, 151.94829998881056, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(335.9327512693998, 151.55465807500747, 0.0), APoint(336.2711571478515, 151.8930639534592, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(336.0382751495177, 151.48340525982871, 0.0), APoint(336.34240996303026, 151.7875400733413, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(336.2340726711707, 151.50242608618507, 0.0), APoint(336.3233891366739, 151.5917425516883, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.07944228229235, 143.9127668547624, 0.0), APoint(342.36093530462904, 144.19425987709906, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.13899335106555, 143.7955412282389, 0.0), APoint(342.4781609311525, 144.1347088083259, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.2483628532324, 143.7281340351091, 0.0), APoint(342.54556812428234, 144.0253393061591, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.0761287110698, 151.68762787659185, 0.0), APoint(342.33818734626425, 151.9496865117863, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.126960199408, 151.5616826696334, 0.0), APoint(342.46413255322267, 151.8988550234481, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.2288575947071, 151.48680336963588, 0.0), APoint(342.53901185322025, 151.796957628149, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(342.4086714181167, 151.48984049774884, 0.0), APoint(342.5359747251073, 151.61714380473938, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.277570217563, 143.9237104546507, 0.0), APoint(348.54999170474196, 144.1961319418297, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.33294991414306, 143.8023134559341, 0.0), APoint(348.67138870345855, 144.14075224524964, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.43859700237215, 143.73118384886664, 0.0), APoint(348.742518310526, 144.0351051570205, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.63508397898886, 143.75089413018668, 0.0), APoint(348.722808029206, 143.8386181804038, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.27526923994697, 151.69958407008673, 0.0), APoint(348.5262311527705, 151.95054598291026, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.32141602668776, 151.56895416153088, 0.0), APoint(348.65686106132637, 151.90439919616944, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.4197573914032, 151.49051883094967, 0.0), APoint(348.7352963919076, 151.80605783145404, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(348.58828413984133, 151.48226888409113, 0.0), APoint(348.7435463387661, 151.63753108301592, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.476167060758, 143.93512296246342, 0.0), APoint(354.7385791969295, 144.19753509863494, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.5271506091635, 143.80932981557234, 0.0), APoint(354.8643723438206, 144.14655155022936, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.62916848055346, 143.73457099166563, 0.0), APoint(354.93913116772734, 144.04453367883946, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.8094207483721, 143.73804656418758, 0.0), APoint(354.93565559520533, 143.86428141102084, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.4750103141045, 151.71214080886193, 0.0), APoint(354.71367441399605, 151.95080490875353, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.5161225907746, 151.57647639023543, 0.0), APoint(354.84933883262255, 151.90969263208336, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.61095853433727, 151.49453563850142, 0.0), APoint(354.93127958435656, 151.81485668852076, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(354.7705157130855, 151.47731612195307, 0.0), APoint(354.9484991009049, 151.65529950977245, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.6752888178039, 143.947060384127, 0.0), APoint(360.92664177526615, 144.1984133415893, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.7215980928457, 143.81659296387215, 0.0), APoint(361.057109195521, 144.1521040665475, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.820057900361, 143.73827607609084, 0.0), APoint(361.1354260833024, 144.0536442590322, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.98891880924464, 143.73036028967783, 0.0), APoint(361.14334186971536, 143.88478335014855, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.675450376249, 151.72539653562416, 0.0), APoint(360.9004186872337, 151.95036484660886, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.7110849646427, 151.58425442872118, 0.0), APoint(361.04156079413667, 151.91473025821517, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.8024477015523, 151.49884047033416, 0.0), APoint(361.12697475252367, 151.82336752130558, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(360.9544571145783, 151.47407318806358, 0.0), APoint(361.15174203479427, 151.67135810827955, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.8750083041294, 143.9595955350702, 0.0), APoint(367.1141066243241, 144.19869385526493, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9162961650167, 143.82410670066093, 0.0), APoint(367.2495954587334, 144.1574059943776, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.0112491573651, 143.74228299771266, 0.0), APoint(367.33141916168165, 144.06245300202926, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.17108103248836, 143.7253381775393, 0.0), APoint(367.348363981855, 143.90262112690596, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.8767263573562, 151.73948818134903, 0.0), APoint(367.0863270415106, 151.94908886550343, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.90630957543624, 151.59229470413243, 0.0), APoint(367.23352051872723, 151.91950564742342, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9942138185675, 151.50342225196715, 0.0), APoint(367.32239297089245, 151.8316014042921, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.13964489441895, 151.47207663252192, 0.0), APoint(367.3537385903377, 151.68617032844065, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.0754229473019, 143.97282584286046, 0.0), APoint(373.30087631653146, 144.19827921209003, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.1112498554858, 143.83187605574773, 0.0), APoint(373.4418261036442, 144.1624523039061, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.202728847273, 143.74657835223826, 0.0), APoint(373.5271238071537, 144.07097331211895, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.35497403709485, 143.7220468467635, 0.0), APoint(373.55165531262844, 143.91872812229704, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.07903860102954, 151.75461608964008, 0.0), APoint(373.2711991332172, 151.94677662182772, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.10180436505993, 151.6006051583739, 0.0), APoint(373.4252100644833, 151.92401085779724, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.1862477261012, 151.50827182411854, 0.0), APoint(373.5175433987387, 151.83956749675605, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.325804218641, 151.47105162136165, 0.0), APoint(373.5547636014956, 151.70001100421626, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.047487656579, 143.92927909200904, 0.0), APoint(382.31509451943356, 144.1968859548636, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.100729609547, 143.8057443496804, 0.0), APoint(382.43862926176223, 144.14364400189564, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.2045759945261, 143.73281403936295, 0.0), APoint(382.51155957207965, 144.03979761691647, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.39213841098837, 143.74359976052853, 0.0), APoint(382.5007738509141, 143.85223520045423, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.0457324772163, 151.70569850569842, 0.0), APoint(382.2907881692093, 151.95075419769142, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.0894443226538, 151.57263365583924, 0.0), APoint(382.4238530190684, 151.90704235225388, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.1860511226749, 151.49246376056368, 0.0), APoint(382.504022914344, 151.81043555223278, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(382.349934431984, 151.47957037457618, 0.0), APoint(382.51691630033145, 151.64655224292366, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.2463355625577, 143.94094266260544, 0.0), APoint(388.50343094883766, 144.1980380488854, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.29505165711095, 143.81288206186213, 0.0), APoint(388.63149154958097, 144.14932195433215, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.3953065333438, 143.7363602427983, 0.0), APoint(388.70801336864486, 144.04906707809937, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.5695512624588, 143.73382827661663, 0.0), APoint(388.71054533482646, 143.8748223489843, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.2458041118406, 151.7185858049404, 0.0), APoint(388.4779008699676, 151.9506825630674, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.28427637633905, 151.5802813741422, 0.0), APoint(388.6162053007658, 151.91221029856894, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.377395879616, 151.4966241821225, 0.0), APoint(388.69986249278554, 151.81909079529203, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(388.533085880043, 151.47553748725286, 0.0), APoint(388.72094918765515, 151.663400794865, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.4457418096862, 143.9531645743517, 0.0), APoint(394.69120903708836, 144.1986318017538, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.4896222204235, 143.82026828979235, 0.0), APoint(394.8241053216476, 144.15475139101648, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.5863466984802, 143.7402160725524, 0.0), APoint(394.9041575388876, 144.0580269129598, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(394.75053132791106, 143.7276240066866, 0.0), APoint(394.9167496047534, 143.89384228352895, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.1386480815388, 151.71713865806976, 0.0), APoint(395.3722345369108, 151.95072511344176, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.1777167901096, 151.5794306713439, 0.0), APoint(395.50994252363665, 151.91165640487094, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.2712170387621, 151.49615422469972, 0.0), APoint(395.5932189702809, 151.81815615621852, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(395.42774011801254, 151.4759006086536, 0.0), APoint(395.61347258632696, 151.66163307696803, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.544876776845, 143.981231729645, 0.0), APoint(401.76128016447785, 144.19763511727785, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.57713022150506, 143.83670847900842, 0.0), APoint(401.9058034151144, 144.16538167261783, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.66651372126637, 143.74931528347312, 0.0), APoint(401.99319661064976, 144.07599817285646, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.8146609954936, 143.72068586240374, 0.0), APoint(402.0218260317191, 143.92785089862923, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.54987799605533, 151.7644075419074, 0.0), APoint(401.73021741568084, 151.94474696153284, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.56802089647954, 151.60577374703496, 0.0), APoint(401.8888512105532, 151.9266040611086, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.65035978436407, 151.51133593962282, 0.0), APoint(401.9832890179654, 151.84426517322413, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(401.78662558809987, 151.47082504806195, 0.0), APoint(402.02379990952625, 151.70799936948833, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.48868468528514, 142.3081834663608, 0.0), APoint(314.73757575772396, 142.5570745387996, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.53397373353835, 142.1766958193174, 0.0), APoint(314.86906340476736, 142.5117854905464, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.6316955000284, 142.09764089051075, 0.0), APoint(314.94811833357403, 142.41406372405638, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(314.7985116016268, 142.0876802968125, 0.0), APoint(314.95807892727225, 142.24724762245796, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.5980260445782, 108.2562064043262, 0.0), APoint(373.92621297811326, 108.58439333786123, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.6034025025759, 108.08480616702724, 0.0), APoint(374.09761321541225, 108.57901687986362, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.6568138631586, 107.96144083231329, 0.0), APoint(374.2209785501262, 108.52560551928087, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.7401350464728, 107.86798532033086, 0.0), APoint(374.3144340621086, 108.44228433596672, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(373.8516383754565, 107.80271195401792, 0.0), APoint(374.3797074284215, 108.33078100698296, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(374.0007176425828, 107.77501452584758, 0.0), APoint(374.4074048565919, 108.18170173985669, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.0373131132459, 108.23623119896942, 0.0), APoint(367.3468888279924, 108.545806913716, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.0372100219705, 108.05935141239743, 0.0), APoint(367.52376861456446, 108.54591000499133, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.08819038222936, 107.93355507735964, 0.0), APoint(367.6495649496022, 108.49492964473251, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.1695840947027, 107.83817209453633, 0.0), APoint(367.74494793242553, 108.41353593225915, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.27898711227414, 107.77079841681115, 0.0), APoint(367.81232161015066, 108.3041329146877, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.4246699387286, 107.7397045479689, 0.0), APoint(367.84341547899294, 108.15845008823331, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.6918125639049, 107.83007047784861, 0.0), APoint(367.75304954911326, 107.89130746305699, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.0473251048886, 104.18037919878952, 0.0), APoint(367.1863154297002, 104.3193695236011, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.9895345159853, 103.94581191458957, 0.0), APoint(367.42088271390014, 104.37716011250436, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.0241975262064, 103.80369822951403, 0.0), APoint(367.56299639897566, 104.34249710228329, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.0938676334341, 103.69659164144511, 0.0), APoint(367.6701029870446, 104.27282699505554, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.19140675115693, 103.61735406387129, 0.0), APoint(367.74934056461836, 104.17528787733275, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.31999794958494, 103.56916856700263, 0.0), APoint(367.797526061487, 104.04669667890474, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(367.5037313384845, 103.57612526060555, 0.0), APoint(367.79056936788413, 103.86296329000521, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.704579345738075, 117.7081506832063, 0.0), APoint(47.839443496204744, 117.84301483367295, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.707130313672884, 117.53392495584447, 0.0), APoint(48.018005814686184, 117.84480045685777, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.766364559770665, 117.41638250664562, 0.0), APoint(48.19656813316763, 117.84658608004258, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(47.94433206583051, 117.41757331740882, 0.0), APoint(48.375130451649085, 117.8483717032274, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.122299571890366, 117.41876412817204, 0.0), APoint(48.553692770130525, 117.8501573264122, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.300267077950224, 117.41995493893526, 0.0), APoint(48.73225508861199, 117.85194294959703, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.47823458401008, 117.42114574969848, 0.0), APoint(48.91081740709343, 117.85372857278183, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.656202090069925, 117.42233656046169, 0.0), APoint(49.08937972557489, 117.85551419596665, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(48.83416959612978, 117.4235273712249, 0.0), APoint(49.26794204405634, 117.85729981915146, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.01213710218963, 117.42471818198811, 0.0), APoint(49.446504362537794, 117.85908544233628, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.190104608249484, 117.42590899275133, 0.0), APoint(49.62506668101925, 117.8608710655211, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.36807211430933, 117.42709980351454, 0.0), APoint(49.80362899950069, 117.8626566887059, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.546039620369186, 117.42829061427776, 0.0), APoint(49.98219131798214, 117.86444231189071, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.724007126429036, 117.42948142504099, 0.0), APoint(50.16075363646359, 117.86622793507553, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(49.90197463248888, 117.4306722358042, 0.0), APoint(50.33931595494504, 117.86801355826034, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.07994213854874, 117.4318630465674, 0.0), APoint(50.5178782734265, 117.86979918144516, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.25790964460858, 117.4330538573306, 0.0), APoint(50.69644059190794, 117.87158480462998, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.43587715066844, 117.43424466809384, 0.0), APoint(50.87500291038939, 117.87337042781479, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.6138446567283, 117.43543547885704, 0.0), APoint(51.053565228870845, 117.8751560509996, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.79181216278814, 117.43662628962025, 0.0), APoint(51.2321275473523, 117.87694167418442, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(50.969779668848, 117.43781710038348, 0.0), APoint(51.41068986583374, 117.87872729736921, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.14774717490784, 117.43900791114669, 0.0), APoint(51.58925218431519, 117.88051292055403, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.3257146809677, 117.4401987219099, 0.0), APoint(51.76781450279665, 117.88229854373884, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.50368218702755, 117.44138953267313, 0.0), APoint(51.94637682127809, 117.88408416692367, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.681649693087394, 117.44258034343633, 0.0), APoint(52.12493913975955, 117.88586979010849, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(51.85961719914725, 117.44377115419955, 0.0), APoint(52.30350145824099, 117.88765541329329, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.037584705207095, 117.44496196496276, 0.0), APoint(52.48206377672244, 117.8894410364781, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.21555221126695, 117.44615277572598, 0.0), APoint(52.660626095203895, 117.89122665966292, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.3935197173268, 117.44734358648918, 0.0), APoint(52.83918841368535, 117.89301228284774, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.571487223386654, 117.4485343972524, 0.0), APoint(53.01775073216679, 117.89479790603254, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.7494547294465, 117.44972520801561, 0.0), APoint(53.19631305064824, 117.89658352921735, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(52.927422235506356, 117.45091601877883, 0.0), APoint(53.3748753691297, 117.89836915240217, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.1053897415662, 117.45210682954203, 0.0), APoint(53.55343768761114, 117.90015477558697, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.28335724762605, 117.45329764030527, 0.0), APoint(53.73200000609258, 117.90194039877179, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.4613247536859, 117.45448845106846, 0.0), APoint(53.91056232457406, 117.90372602195661, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.63929225974576, 117.45567926183168, 0.0), APoint(54.08912464305551, 117.90551164514143, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.81725976580561, 117.45687007259491, 0.0), APoint(54.267686961536945, 117.90729726832623, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(53.99522727186545, 117.45806088335812, 0.0), APoint(54.4462492800184, 117.90908289151105, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.173194777925296, 117.45925169412132, 0.0), APoint(54.62481159849985, 117.91086851469586, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.351162283985154, 117.46044250488453, 0.0), APoint(54.80337391698129, 117.91265413788068, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.529129790045026, 117.46163331564776, 0.0), APoint(54.98193623546275, 117.9144397610655, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.70709729610485, 117.46282412641096, 0.0), APoint(55.160498553944194, 117.91622538425031, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(54.88506480216472, 117.4640149371742, 0.0), APoint(55.33906087242566, 117.91801100743514, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.063032308224564, 117.4652057479374, 0.0), APoint(55.51762319090709, 117.91979663061993, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.24099981428441, 117.46639655870061, 0.0), APoint(55.696185509388556, 117.92158225380476, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.418967320344265, 117.46758736946383, 0.0), APoint(55.87474782786998, 117.92336787698954, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.59693482640412, 117.46877818022705, 0.0), APoint(56.05331014635145, 117.92515350017437, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.77490233246397, 117.46996899099025, 0.0), APoint(56.231872464832904, 117.92693912335919, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(55.952869838523824, 117.47115980175347, 0.0), APoint(56.41043478331436, 117.928724746544, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.13083734458367, 117.47235061251668, 0.0), APoint(56.58899710179581, 117.93051036972882, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.308804850643526, 117.4735414232799, 0.0), APoint(56.76755942027725, 117.93229599291362, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.48677235670337, 117.4747322340431, 0.0), APoint(56.946121738758706, 117.93408161609844, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.66473986276323, 117.47592304480632, 0.0), APoint(57.124684057240145, 117.93586723928324, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(56.84270736882307, 117.47711385556953, 0.0), APoint(57.3032463757216, 117.93765286246806, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.02067487488293, 117.47830466633275, 0.0), APoint(57.48180869420307, 117.93943848565289, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.19864238094277, 117.47949547709595, 0.0), APoint(57.66037101268451, 117.94122410883769, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.37660988700262, 117.48068628785919, 0.0), APoint(57.838933331165954, 117.94300973202252, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.55457739306248, 117.48187709862239, 0.0), APoint(58.01749564964741, 117.94479535520733, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.732544899122324, 117.4830679093856, 0.0), APoint(58.19605796812885, 117.94658097839212, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.91051240518218, 117.48425872014883, 0.0), APoint(58.3746202866103, 117.94836660157694, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.088479911242025, 117.48544953091204, 0.0), APoint(58.553182605091756, 117.95015222476175, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.266447417301876, 117.48664034167525, 0.0), APoint(58.7317449235732, 117.95193784794658, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.44441492336172, 117.48783115243846, 0.0), APoint(58.91030724205466, 117.9537234711314, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.62238242942158, 117.48902196320168, 0.0), APoint(59.0888695605361, 117.9555090943162, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.800349935481435, 117.4902127739649, 0.0), APoint(59.267431879017565, 117.95729471750103, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.97831744154128, 117.4914035847281, 0.0), APoint(59.44599419749899, 117.95908034068582, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.15628494760112, 117.49259439549131, 0.0), APoint(59.62455651598046, 117.96086596387065, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.33425245366098, 117.49378520625453, 0.0), APoint(59.8031188344619, 117.96265158705545, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.51221995972084, 117.49497601701775, 0.0), APoint(59.98168115294335, 117.96443721024026, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.69018746578068, 117.49616682778095, 0.0), APoint(60.160243471424806, 117.96622283342508, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.868154971840525, 117.49735763854416, 0.0), APoint(60.338805789906246, 117.96800845660988, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.04612247790038, 117.49854844930738, 0.0), APoint(60.517368108387714, 117.96979407979471, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.22408998396024, 117.4997392600706, 0.0), APoint(60.695930426869154, 117.97157970297951, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.402057490020084, 117.5009300708338, 0.0), APoint(60.87449274535061, 117.97336532616433, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.58002499607994, 117.50212088159702, 0.0), APoint(61.05305506383206, 117.97515094934914, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.757992502139786, 117.50331169236023, 0.0), APoint(61.231617382313516, 117.97693657253396, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(60.935960008199636, 117.50450250312346, 0.0), APoint(61.41017970079496, 117.97872219571877, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.113927514259494, 117.50569331388667, 0.0), APoint(61.5887420192764, 117.98050781890359, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.29189502031934, 117.50688412464987, 0.0), APoint(61.76730433775786, 117.9822934420884, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.46986252637918, 117.50807493541308, 0.0), APoint(61.94586665623931, 117.98407906527322, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.64783003243905, 117.50926574617631, 0.0), APoint(62.12442897472075, 117.98586468845801, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.82579753849888, 117.51045655693952, 0.0), APoint(62.302991293202204, 117.98765031164282, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.00376504455873, 117.51164736770274, 0.0), APoint(62.48155361168365, 117.98943593482765, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.18173255061858, 117.51283817846594, 0.0), APoint(62.660115930165105, 117.99122155801247, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.359700056678435, 117.51402898922916, 0.0), APoint(62.838678248646545, 117.99300718119727, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.53766756273829, 117.51521979999238, 0.0), APoint(63.017240567128, 117.99479280438209, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.715635068798136, 117.51641061075559, 0.0), APoint(63.19580288560944, 117.99657842756689, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(62.89360257485798, 117.51760142151879, 0.0), APoint(63.37436520409089, 117.9983640507517, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.07157008091785, 117.51879223228202, 0.0), APoint(63.55292752257236, 118.00014967393653, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.249537586977695, 117.51998304304523, 0.0), APoint(63.731489841053815, 118.00193529712135, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.42750509303754, 117.52117385380843, 0.0), APoint(63.91005215953527, 118.00372092030616, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.60547259909738, 117.52236466457164, 0.0), APoint(64.08861447801671, 118.00550654349097, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.783440105157254, 117.52355547533487, 0.0), APoint(64.26717679649815, 118.00729216667577, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(63.9614076112171, 117.52474628609808, 0.0), APoint(64.4457391149796, 118.00907778986058, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.13937511727694, 117.52593709686128, 0.0), APoint(64.62430143346106, 118.0108634130454, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.31734262333681, 117.52712790762452, 0.0), APoint(64.80286375194251, 118.01264903623021, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.49531012939666, 117.52831871838772, 0.0), APoint(64.98142607042398, 118.01443465941504, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.67327763545649, 117.52950952915094, 0.0), APoint(65.15998838890539, 118.01622028259985, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(64.85124514151636, 117.53070033991418, 0.0), APoint(65.33855070738684, 118.01800590578463, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.0292126475762, 117.53189115067738, 0.0), APoint(65.51711302586833, 118.01979152896948, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.20718015363605, 117.53308196144059, 0.0), APoint(65.69567534434975, 118.0215771521543, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.38514765969589, 117.53427277220379, 0.0), APoint(65.8742376628312, 118.02336277533911, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.56311516575576, 117.53546358296703, 0.0), APoint(66.05279998131266, 118.02514839852392, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.7410826718156, 117.53665439373023, 0.0), APoint(66.23136229979411, 118.02693402170874, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(65.91905017787545, 117.53784520449344, 0.0), APoint(66.40992461827555, 118.02871964489354, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.09701768393532, 117.53903601525667, 0.0), APoint(66.58848693675701, 118.03050526807836, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.27498518999514, 117.54022682601985, 0.0), APoint(66.76704925523845, 118.03229089126316, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.45295269605501, 117.54141763678308, 0.0), APoint(66.9456115737199, 118.03407651444797, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.63092020211486, 117.5426084475463, 0.0), APoint(67.12417389220137, 118.0358621376328, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.8088877081747, 117.54379925830949, 0.0), APoint(67.30273621068282, 118.03764776081762, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(66.98685521423457, 117.54499006907272, 0.0), APoint(67.48129852916426, 118.03943338400242, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.16482272029442, 117.54618087983594, 0.0), APoint(67.65986084764572, 118.04121900718724, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.34279022635425, 117.54737169059914, 0.0), APoint(67.83842316612716, 118.04300463037204, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.52075773241413, 117.54856250136237, 0.0), APoint(68.01698548460861, 118.04479025355685, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.69872523847397, 117.54975331212557, 0.0), APoint(68.19554780309007, 118.04657587674167, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(67.87669274453381, 117.55094412288878, 0.0), APoint(68.37411012157152, 118.04836149992649, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.05466025059367, 117.552134933652, 0.0), APoint(68.55267244005299, 118.05014712311132, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.23262775665353, 117.55332574441522, 0.0), APoint(68.73123475853441, 118.0519327462961, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.41059526271337, 117.55451655517842, 0.0), APoint(68.90979707701584, 118.05371836948092, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.58856276877322, 117.55570736594163, 0.0), APoint(69.08835939549732, 118.05550399266573, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.76653027483306, 117.55689817670486, 0.0), APoint(69.26692171397877, 118.05728961585055, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(68.94449778089293, 117.55808898746807, 0.0), APoint(69.44548403246023, 118.05907523903537, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.12246528695277, 117.5592797982313, 0.0), APoint(69.62404635094168, 118.06086086222018, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.30043279301262, 117.5604706089945, 0.0), APoint(69.80260866942311, 118.062646485405, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.47840029907246, 117.56166141975771, 0.0), APoint(69.98117098790456, 118.06443210858981, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.65636780513232, 117.56285223052093, 0.0), APoint(70.159733306386, 118.06621773177461, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(69.83433531119216, 117.56404304128414, 0.0), APoint(70.33829562486746, 118.06800335495943, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.01230281725202, 117.56523385204736, 0.0), APoint(70.51685794334891, 118.06978897814425, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.19027032331186, 117.56642466281056, 0.0), APoint(70.69542026183038, 118.07157460132908, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.36823782937172, 117.56761547357378, 0.0), APoint(70.87398258031182, 118.07336022451388, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.54620533543158, 117.568806284337, 0.0), APoint(71.05254489879327, 118.07514584769869, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.72417284149142, 117.5699970951002, 0.0), APoint(71.23110721727473, 118.07693147088351, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(70.90214034755127, 117.57118790586341, 0.0), APoint(71.40966953575617, 118.07871709406831, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.08010785361114, 117.57237871662664, 0.0), APoint(71.58823185423762, 118.08050271725313, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.25807535967097, 117.57356952738984, 0.0), APoint(71.76679417271907, 118.08228834043794, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.43604286573083, 117.57476033815306, 0.0), APoint(71.94535649120053, 118.08407396362276, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.6140103717907, 117.57595114891629, 0.0), APoint(72.123918809682, 118.08585958680759, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.79197787785053, 117.57714195967948, 0.0), APoint(72.30248112816344, 118.08764520999239, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(71.96994538391039, 117.5783327704427, 0.0), APoint(72.48104344664489, 118.0894308331772, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.14791288997026, 117.57952358120593, 0.0), APoint(72.65960576512632, 118.09121645636202, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.32588039603007, 117.58071439196911, 0.0), APoint(72.83816808360777, 118.09300207954684, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.50384790208994, 117.58190520273234, 0.0), APoint(73.01673040208922, 118.09478770273165, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.68181540814979, 117.58309601349555, 0.0), APoint(73.19529272057068, 118.09657332591647, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(72.85978291420962, 117.58428682425877, 0.0), APoint(73.37385503905212, 118.09835894910127, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.03775042026949, 117.585477635022, 0.0), APoint(73.55241735753357, 118.10014457228608, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.21571792632933, 117.58666844578521, 0.0), APoint(73.73097967601502, 118.1019301954709, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.39368543238918, 117.58785925654841, 0.0), APoint(73.90954199449646, 118.1037158186557, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.57165293844905, 117.58905006731165, 0.0), APoint(74.08810431297793, 118.10550144184053, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.74962044450889, 117.59024087807485, 0.0), APoint(74.26666663145939, 118.10728706502535, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(73.92758795056874, 117.59143168883806, 0.0), APoint(74.44522894994084, 118.10907268821016, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.10555545662858, 117.59262249960126, 0.0), APoint(74.62379126842228, 118.11085831139496, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.28352296268842, 117.59381331036447, 0.0), APoint(74.80235358690373, 118.11264393457978, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.4614904687483, 117.5950041211277, 0.0), APoint(74.98091590538519, 118.1144295577646, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.63945797480814, 117.5961949318909, 0.0), APoint(75.15947822386663, 118.1162151809494, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.81742548086798, 117.59738574265411, 0.0), APoint(75.33804054234808, 118.11800080413421, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(74.99539298692785, 117.59857655341735, 0.0), APoint(75.51660286082954, 118.11978642731903, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.1733604929877, 117.59976736418055, 0.0), APoint(75.695165179311, 118.12157205050386, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.35132799904754, 117.60095817494376, 0.0), APoint(75.87372749779244, 118.12335767368866, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.5292955051074, 117.602148985707, 0.0), APoint(76.05228981627388, 118.12514329687349, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.70726301116724, 117.60333979647021, 0.0), APoint(76.23085213475534, 118.12692892005828, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.88523051722709, 117.60453060723341, 0.0), APoint(76.40941445323679, 118.12871454324309, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.06319802328696, 117.60572141799662, 0.0), APoint(76.58797677171825, 118.13050016642791, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.2411655293468, 117.60691222875985, 0.0), APoint(76.7665390901997, 118.13228578961272, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.41913303540665, 117.60810303952306, 0.0), APoint(76.94510140868113, 118.13407141279754, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.59710054146649, 117.60929385028626, 0.0), APoint(77.12366372716258, 118.13585703598235, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.77506804752633, 117.61048466104947, 0.0), APoint(77.30222604564405, 118.13764265916718, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.9530355535862, 117.6116754718127, 0.0), APoint(77.48078836412547, 118.13942828235197, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.13100305964605, 117.61286628257591, 0.0), APoint(77.65935068260694, 118.1412139055368, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.30897056570589, 117.61405709333911, 0.0), APoint(77.72399283695742, 118.02907936459064, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695813, 118.02907936459135, 0.0), APoint(77.83565715625413, 118.14074368388735, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.48693807176575, 117.61524790410233, 0.0), APoint(77.72399283695775, 117.85230266929433, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695815, 117.85230266929473, 0.0), APoint(78.01068358724089, 118.13899341957747, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.66490557782562, 117.61643871486557, 0.0), APoint(77.72399283695805, 117.67552597399799, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.72399283695815, 117.67552597399809, 0.0), APoint(78.18571001822767, 118.13724315526761, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.84090847956723, 117.61566492131054, 0.0), APoint(78.36073644921443, 118.13549289095774, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.015934910554, 117.61391465700066, 0.0), APoint(78.53576288020119, 118.13374262664786, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.19096134154076, 117.61216439269079, 0.0), APoint(78.71078931118797, 118.131992362338, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.36598777252753, 117.61041412838092, 0.0), APoint(78.88581574217476, 118.13024209802815, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.5410142035143, 117.60866386407105, 0.0), APoint(79.06084217316152, 118.12849183371827, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.71604063450108, 117.6069135997612, 0.0), APoint(79.23586860414828, 118.1267415694084, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(78.89106706548785, 117.60516333545132, 0.0), APoint(79.41089503513506, 118.12499130509853, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.06609349647461, 117.60341307114145, 0.0), APoint(79.58592146612182, 118.12324104078866, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.24111992746137, 117.6016628068316, 0.0), APoint(79.76094789710857, 118.1214907764788, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.41614635844815, 117.59991254252171, 0.0), APoint(79.93597432809537, 118.11974051216893, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.59117278943492, 117.59816227821184, 0.0), APoint(80.11100075908212, 118.11799024785904, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.7661992204217, 117.59641201390198, 0.0), APoint(80.28602719006889, 118.1162399835492, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.94122565140844, 117.59466174959209, 0.0), APoint(80.46105362105567, 118.11448971923932, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.11625208239522, 117.59291148528226, 0.0), APoint(80.63608005204243, 118.11273945492947, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.29127851338198, 117.59116122097238, 0.0), APoint(80.81110648302919, 118.11098919061959, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.46630494436876, 117.58941095666252, 0.0), APoint(80.98613291401595, 118.10923892630971, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.64133137535552, 117.58766069235264, 0.0), APoint(81.16115934500274, 118.10748866199987, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.8163578063423, 117.58591042804278, 0.0), APoint(81.33618577598952, 118.10573839769, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.99138423732906, 117.5841601637329, 0.0), APoint(81.51121220697628, 118.10398813338013, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.16641066831582, 117.58240989942303, 0.0), APoint(81.68623863796304, 118.10223786907025, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.34143709930261, 117.58065963511318, 0.0), APoint(81.86126506894982, 118.10048760476039, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.51646353028937, 117.5789093708033, 0.0), APoint(82.03629149993658, 118.09873734045051, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.69148996127615, 117.57715910649344, 0.0), APoint(82.21131793092334, 118.09698707614064, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.86651639226291, 117.57540884218356, 0.0), APoint(82.38634436191012, 118.09523681183077, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.04154282324969, 117.5736585778737, 0.0), APoint(82.5613707928969, 118.09348654752091, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.21656925423646, 117.57190831356384, 0.0), APoint(82.73639722388367, 118.09173628321105, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.39159568522324, 117.57015804925398, 0.0), APoint(82.91142365487043, 118.08998601890117, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.56662211621, 117.5684077849441, 0.0), APoint(83.08645008585721, 118.08823575459131, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.74164854719675, 117.56665752063424, 0.0), APoint(83.26147651684397, 118.08648549028146, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(82.91667497818352, 117.56490725632437, 0.0), APoint(83.43650294783072, 118.08473522597157, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.09170140917033, 117.56315699201451, 0.0), APoint(83.61152937881752, 118.08298496166171, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.26672784015705, 117.56140672770462, 0.0), APoint(83.78655580980427, 118.08123469735185, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.44175427114385, 117.55965646339476, 0.0), APoint(83.96158224079105, 118.07948443304198, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.61678070213063, 117.5579061990849, 0.0), APoint(84.13660867177782, 118.07773416873209, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.79180713311737, 117.55615593477503, 0.0), APoint(84.31163510276458, 118.07598390442224, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(83.96683356410414, 117.55440567046516, 0.0), APoint(84.48666153375135, 118.07423364011237, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.14185999509093, 117.55265540615531, 0.0), APoint(84.66168796473814, 118.07248337580252, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.31688642607767, 117.55090514184542, 0.0), APoint(84.8367143957249, 118.07073311149264, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.49191285706446, 117.54915487753557, 0.0), APoint(85.01174082671166, 118.06898284718277, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.66693928805121, 117.54740461322568, 0.0), APoint(85.18676725769843, 118.0672325828729, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(84.841965719038, 117.54565434891583, 0.0), APoint(85.3617936886852, 118.06548231856303, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.01699215002476, 117.54390408460596, 0.0), APoint(85.53682011967199, 118.06373205425318, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.19201858101152, 117.54215382029608, 0.0), APoint(85.71184655065873, 118.06198178994329, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.3670450119983, 117.54040355598622, 0.0), APoint(85.88687298164552, 118.06023152563344, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.54207144298508, 117.53865329167635, 0.0), APoint(86.06189941263229, 118.05848126132356, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.71709787397182, 117.53690302736646, 0.0), APoint(86.23692584361905, 118.05673099701369, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(85.89212430495861, 117.53515276305662, 0.0), APoint(86.41195227460582, 118.05498073270383, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.06715073594539, 117.53340249874675, 0.0), APoint(86.58697870559261, 118.05323046839398, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.24217716693215, 117.53165223443688, 0.0), APoint(86.76200513657935, 118.05148020408407, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.41720359791891, 117.529901970127, 0.0), APoint(86.93703156756614, 118.04972993977422, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.59223002890567, 117.52815170581715, 0.0), APoint(87.1120579985529, 118.04797967546438, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.76725645989245, 117.52640144150729, 0.0), APoint(87.28708442953968, 118.04622941115448, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(86.94228289087923, 117.52465117719743, 0.0), APoint(87.46211086052642, 118.04447914684462, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.11730932186599, 117.52290091288755, 0.0), APoint(87.6371372915132, 118.04272888253476, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.29233575285276, 117.52115064857769, 0.0), APoint(87.81216372249999, 118.04097861822491, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.46736218383953, 117.51940038426781, 0.0), APoint(87.98719015348675, 118.03922835391504, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.64238861482629, 117.51765011995793, 0.0), APoint(88.16221658447351, 118.03747808960516, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.81741504581306, 117.51589985564807, 0.0), APoint(88.33724301546029, 118.0357278252953, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(87.99244147679984, 117.51414959133821, 0.0), APoint(88.51226944644705, 118.03397756098542, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.16746790778659, 117.51239932702832, 0.0), APoint(88.68729587743384, 118.03222729667557, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.34249433877338, 117.51064906271847, 0.0), APoint(88.86232230842059, 118.03047703236568, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.51752076976014, 117.5088987984086, 0.0), APoint(89.03734873940736, 118.02872676805582, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.69254720074692, 117.50714853409873, 0.0), APoint(89.21237517039414, 118.02697650374596, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(88.8675736317337, 117.50539826978888, 0.0), APoint(89.3874016013809, 118.02522623943608, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.04260006272045, 117.503648005479, 0.0), APoint(89.56242803236768, 118.02347597512622, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.21762649370723, 117.50189774116913, 0.0), APoint(89.70644040441813, 117.99071165188003, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.392652924694, 117.50014747685927, 0.0), APoint(89.70644040441813, 117.8139349565834, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(89.56767935568077, 117.49839721254939, 0.0), APoint(89.70644040441813, 117.63715826128676, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 117.97784317550528, 0.0), APoint(90.78761304927508, 118.01122412495715, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 117.80106648020865, 0.0), APoint(90.96263948026183, 118.00947386064729, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.75423209982318, 117.62428978491201, 0.0), APoint(91.1376659112486, 118.00772359633743, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.79309253125187, 117.48637352104406, 0.0), APoint(91.31269234223538, 118.00597333202757, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(90.96915265230552, 117.48565694680107, 0.0), APoint(91.48771877322216, 118.0042230677177, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.14521277335913, 117.48494037255804, 0.0), APoint(91.66274520420892, 118.00247280340783, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.32127289441276, 117.48422379831503, 0.0), APoint(91.8377716351957, 118.00072253909796, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.49733301546638, 117.48350722407201, 0.0), APoint(92.01279806618246, 117.99897227478809, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.67339313651999, 117.48279064982898, 0.0), APoint(92.18782449716925, 117.99722201047824, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(91.84945325757364, 117.482074075586, 0.0), APoint(92.36285092815599, 117.99547174616835, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.02551337862725, 117.48135750134297, 0.0), APoint(92.53787735914277, 117.99372148185849, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.2015734996809, 117.48064092709998, 0.0), APoint(92.71290379012952, 117.9919712175486, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.37763362073451, 117.47992435285695, 0.0), APoint(92.8879302211163, 117.99022095323875, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.55369374178815, 117.47920777861395, 0.0), APoint(93.06295665210308, 117.98847068892889, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.72975386284176, 117.47849120437093, 0.0), APoint(93.23798308308984, 117.98672042461901, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(92.9058139838954, 117.47777463012793, 0.0), APoint(93.41300951407663, 117.98497016030916, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.08187410494902, 117.47705805588491, 0.0), APoint(93.58803594506338, 117.98321989599927, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.25793422600267, 117.47634148164192, 0.0), APoint(93.76306237605016, 117.98146963168941, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.43399434705628, 117.4756249073989, 0.0), APoint(93.93808880703693, 117.97971936737954, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.61005446810991, 117.47490833315588, 0.0), APoint(94.1131152380237, 117.97796910306967, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.78611458916353, 117.47419175891287, 0.0), APoint(94.28814166901049, 117.97621883875982, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.96217471021714, 117.47347518466984, 0.0), APoint(94.46316809999723, 117.97446857444993, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.13823483127078, 117.47275861042687, 0.0), APoint(94.63819453098401, 117.9727183101401, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.31429495232439, 117.47204203618384, 0.0), APoint(94.81322096197077, 117.97096804583022, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.49035507337801, 117.47132546194082, 0.0), APoint(94.98824739295753, 117.96921778152034, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.66641519443164, 117.47060888769781, 0.0), APoint(95.16327382394432, 117.9674675172105, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(94.84247531548529, 117.46989231345482, 0.0), APoint(95.33830025493107, 117.9657172529006, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.0185354365389, 117.46917573921179, 0.0), APoint(95.51332668591786, 117.96396698859076, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.19459555759252, 117.46845916496878, 0.0), APoint(95.68835311690461, 117.96221672428086, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.37065567864616, 117.46774259072578, 0.0), APoint(95.8633795478914, 117.96046645997102, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.54671579969977, 117.46702601648275, 0.0), APoint(96.03840597887815, 117.95871619566113, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.7227759207534, 117.46630944223975, 0.0), APoint(96.21343240986492, 117.95696593135126, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(95.89883604180702, 117.46559286799672, 0.0), APoint(96.3884588408517, 117.9552156670414, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.07489616286067, 117.46487629375373, 0.0), APoint(96.56348527183846, 117.95346540273152, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.25095628391428, 117.4641597195107, 0.0), APoint(96.73851170282522, 117.95171513842165, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.42701640496793, 117.46344314526772, 0.0), APoint(96.913538133812, 117.94996487411179, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.60307652602152, 117.46272657102467, 0.0), APoint(97.08856456479879, 117.94821460980194, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.77913664707516, 117.46200999678167, 0.0), APoint(97.26359099578553, 117.94646434549205, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(96.95519676812879, 117.46129342253866, 0.0), APoint(97.43861742677231, 117.94471408118218, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.1312568891824, 117.46057684829563, 0.0), APoint(97.6136438577591, 117.94296381687234, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.30731701023605, 117.45986027405264, 0.0), APoint(97.78867028874585, 117.94121355256244, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.48337713128967, 117.45914369980963, 0.0), APoint(97.96369671973264, 117.9394632882526, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.65943725234328, 117.45842712556663, 0.0), APoint(98.13872315071939, 117.9377130239427, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(97.83549737339689, 117.4577105513236, 0.0), APoint(98.31374958170616, 117.93596275963287, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.01155749445054, 117.45699397708061, 0.0), APoint(98.48877601269292, 117.934212495323, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.18761761550415, 117.45627740283759, 0.0), APoint(98.66380244367969, 117.93246223101312, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.3636777365578, 117.4555608285946, 0.0), APoint(98.83882887466648, 117.93071196670327, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.53973785761141, 117.45484425435157, 0.0), APoint(99.01385530565322, 117.92896170239338, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.71579797866504, 117.45412768010856, 0.0), APoint(99.18888173664001, 117.92721143808353, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(98.89185809971866, 117.45341110586554, 0.0), APoint(99.36390816762678, 117.92546117377366, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.06791822077231, 117.45269453162256, 0.0), APoint(99.53893459861355, 117.9237109094638, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.24397834182592, 117.45197795737953, 0.0), APoint(99.71396102960031, 117.92196064515392, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.42003846287953, 117.4512613831365, 0.0), APoint(99.88898746058707, 117.92021038084404, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.59609858393317, 117.4505448088935, 0.0), APoint(100.06401389157385, 117.91846011653418, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.77215870498678, 117.44982823465047, 0.0), APoint(100.23904032256063, 117.91670985222432, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(99.94821882604043, 117.44911166040748, 0.0), APoint(100.4140667535474, 117.91495958791445, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.12427894709404, 117.44839508616445, 0.0), APoint(100.58909318453416, 117.91320932360458, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.30033906814766, 117.44767851192144, 0.0), APoint(100.76411961552093, 117.9114590592947, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.4763991892013, 117.44696193767844, 0.0), APoint(100.93914604650772, 117.90970879498485, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.65245931025494, 117.44624536343544, 0.0), APoint(101.11417247749446, 117.90795853067496, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(100.82851943130855, 117.44552878919241, 0.0), APoint(101.28919890848125, 117.90620826636511, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.00457955236217, 117.44481221494942, 0.0), APoint(101.46422533946802, 117.90445800205524, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.18063967341581, 117.4440956407064, 0.0), APoint(101.63925177045479, 117.90270773774537, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.35669979446942, 117.44337906646336, 0.0), APoint(101.81427820144154, 117.90095747343551, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.53275991552304, 117.44266249222038, 0.0), APoint(101.9893046324283, 117.89920720912563, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.70882003657665, 117.44194591797735, 0.0), APoint(102.16433106341509, 117.89745694481579, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(101.8848801576303, 117.44122934373436, 0.0), APoint(102.33935749440187, 117.89570668050592, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.06094027868392, 117.44051276949133, 0.0), APoint(102.51438392538863, 117.89395641619605, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.23700039973757, 117.43979619524835, 0.0), APoint(102.68941035637539, 117.89220615188617, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.41306052079118, 117.43907962100532, 0.0), APoint(102.86443678736217, 117.89045588757631, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.5891206418448, 117.4383630467623, 0.0), APoint(103.03946321834894, 117.88870562326645, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.76518076289842, 117.43764647251929, 0.0), APoint(103.21448964933569, 117.88695535895656, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(102.94124088395206, 117.43692989827629, 0.0), APoint(103.38951608032248, 117.88520509464671, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.11730100500569, 117.43621332403328, 0.0), APoint(103.56454251130926, 117.88345483033685, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.29336112605931, 117.43549674979026, 0.0), APoint(103.73956894229602, 117.88170456602697, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.46942124711295, 117.43478017554726, 0.0), APoint(103.91459537328281, 117.87995430171712, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.64548136816654, 117.43406360130422, 0.0), APoint(104.08962180426956, 117.87820403740723, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.8215414892202, 117.43334702706123, 0.0), APoint(104.26464823525633, 117.87645377309737, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(103.99760161027383, 117.43263045281823, 0.0), APoint(104.43967466624308, 117.87470350878748, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.17366173132746, 117.43191387857522, 0.0), APoint(104.61470109722987, 117.87295324447763, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.34972185238107, 117.43119730433219, 0.0), APoint(104.78972752821662, 117.87120298016774, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.5257819734347, 117.43048073008919, 0.0), APoint(104.9647539592034, 117.86945271585789, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.70184209448831, 117.42976415584616, 0.0), APoint(105.13978039019017, 117.86770245154801, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(104.87790221554195, 117.42904758160319, 0.0), APoint(105.31480682117693, 117.86595218723816, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.05396233659556, 117.42833100736016, 0.0), APoint(105.4898332521637, 117.8642019229283, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.23002245764918, 117.42761443311714, 0.0), APoint(105.66485968315045, 117.86245165861841, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.40608257870282, 117.42689785887414, 0.0), APoint(105.83988611413724, 117.86070139430856, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.58214269975645, 117.42618128463113, 0.0), APoint(106.01491254512402, 117.8589511299987, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.75820282081007, 117.42546471038811, 0.0), APoint(106.18993897611078, 117.85720086568882, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(105.93426294186371, 117.42474813614511, 0.0), APoint(106.36496540709754, 117.85545060137895, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.11032306291733, 117.4240315619021, 0.0), APoint(106.53999183808433, 117.8537003370691, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.28638318397094, 117.42331498765907, 0.0), APoint(106.7150182690711, 117.85195007275922, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.46244330502459, 117.42259841341608, 0.0), APoint(106.89004470005787, 117.85019980844936, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.63850342607819, 117.42188183917304, 0.0), APoint(107.06507113104463, 117.84844954413948, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.81456354713184, 117.42116526493005, 0.0), APoint(107.2400975620314, 117.84669927982961, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(106.99062366818545, 117.42044869068702, 0.0), APoint(107.41512399301817, 117.84494901551975, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.1666837892391, 117.41973211644404, 0.0), APoint(107.59015042400496, 117.8431987512099, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.34274391029271, 117.41901554220101, 0.0), APoint(107.76517685499171, 117.8414484869, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.51880403134633, 117.418298967958, 0.0), APoint(107.94020328597848, 117.83969822259014, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.69486415239996, 117.41758239371498, 0.0), APoint(108.08365950461344, 117.80637774592846, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(107.8709242734536, 117.41686581947198, 0.0), APoint(108.08391080544924, 117.62985235146762, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(108.04698439450722, 117.41614924522897, 0.0), APoint(108.08416210628504, 117.45332695700678, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.60070077665, 152.1635798930525, 0.0), APoint(404.8027252424106, 152.36560435881304, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.62731976016124, 152.01342218126712, 0.0), APoint(404.952882954196, 152.3389853753019, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.7136648721603, 151.9229905979695, 0.0), APoint(405.0433145374936, 152.2526402633028, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.85637193228433, 151.88892096279687, 0.0), APoint(405.0773841726662, 152.10993320317874, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.4484136970053, 138.17766186861877, 0.0), APoint(396.6848527020966, 138.41410087371003, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.4886283311225, 138.0410998074394, 0.0), APoint(396.8214147632759, 138.37388623959274, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.58287156942174, 137.95856635044188, 0.0), APoint(396.9039482202734, 138.27964300129358, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.74106012754555, 137.93997821326911, 0.0), APoint(396.9225363574462, 138.12145444316974, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.44155264597435, 152.1153444658508, 0.0), APoint(408.6940854300141, 152.36787724989057, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.48835320408, 151.9853683286598, 0.0), APoint(408.82406156720515, 152.32107669178495, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.5871732101807, 151.90741163946385, 0.0), APoint(408.902018256401, 152.2222566856842, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.75706520781335, 151.9005269417999, 0.0), APoint(408.90890295406496, 152.0523646880515, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.48960298641845, 138.1980358778606, 0.0), APoint(408.7123286750668, 138.42076156650893, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.52434968074874, 138.05600587689423, 0.0), APoint(408.85435867603314, 138.38601487217863, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.61518089037963, 137.97006039122854, 0.0), APoint(408.9403041616988, 138.29518366254771, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.76612544116256, 137.9442282467148, 0.0), APoint(408.96613630621255, 138.1442391117648, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.5605846692429, 138.15810485721107, 0.0), APoint(404.819410538232, 138.41693072620012, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.61003432022096, 138.03077781289252, 0.0), APoint(404.94673758255055, 138.36748107522206, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.7108517675732, 137.95481856494806, 0.0), APoint(405.02269683049497, 138.26666362786986, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.8869248278535, 137.95411492993173, 0.0), APoint(405.0234004655113, 138.09059056758957, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.4963716899163, 142.27066857318113, 0.0), APoint(408.7879619879943, 142.56225887125913, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.5608564872724, 142.15837667524056, 0.0), APoint(408.9002538859349, 142.49777407390303, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(408.6750196945793, 142.09576318725087, 0.0), APoint(408.9628673739246, 142.38361086659611, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.53795487509615, 142.3781157501836, 0.0), APoint(404.6486953035422, 142.48885617862965, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.5280526505227, 142.19143683031348, 0.0), APoint(404.8353742234123, 142.4987584032031, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.60118637987557, 142.08779386436973, 0.0), APoint(404.93901718935615, 142.4256246738503, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(404.72496788458113, 142.03479867377868, 0.0), APoint(404.99201237994714, 142.3018431691447, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.449135300452, 142.2442474638881, 0.0), APoint(396.6694586551652, 142.46457081860132, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.48293302723994, 142.10126849537937, 0.0), APoint(396.81243762367393, 142.43077309181336, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.57320549211965, 142.01476426496245, 0.0), APoint(396.8989418540908, 142.34050062693368, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(396.72305310109, 141.9878351786362, 0.0), APoint(396.9258709404171, 142.1906530179633, 0.0))
entity.Color = 6
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(366.05850206621164, 113.29027078058513, 0.0), APoint(364.8585020662116, 112.09027078058514, 0.0))



entity = acad.model.AddLine(APoint(375.35850206621205, 112.09027078058514, 0.0), APoint(376.5585020662121, 113.29027078058513, 0.0))



entity = acad.model.AddLine(APoint(359.0794450652048, 103.26471267642884, 0.0), APoint(360.27944506520487, 102.06471267642885, 0.0))



entity = acad.model.AddLine(APoint(360.27944506520487, 109.56471267642885, 0.0), APoint(359.0794450652048, 110.76471267642884, 0.0))



entity = acad.model.AddLine(APoint(366.3585020662116, 98.57776216005513, 0.0), APoint(367.55850206621164, 99.77776216005512, 0.0))



entity = acad.model.AddLine(APoint(366.05850206621164, 99.77776216005512, 0.0), APoint(364.8585020662116, 98.57776216005513, 0.0))



entity = acad.model.AddLine(APoint(34.718032157416566, 83.11599936022694, 0.0), APoint(33.51803215741656, 81.91599936022695, 0.0))



entity = acad.model.AddLine(APoint(77.12399283695814, 81.91599936022695, 0.0), APoint(78.32399283695813, 83.11599936022694, 0.0))



entity = acad.model.AddLine(APoint(78.32399283695813, 83.11599936022694, 0.0), APoint(77.12399283695814, 81.91599936022695, 0.0))



entity = acad.model.AddLine(APoint(120.51803215741657, 81.91599936022695, 0.0), APoint(121.71803215741656, 83.11599936022694, 0.0))



entity = acad.model.AddLine(APoint(34.718032157416566, 74.26976331948865, 0.0), APoint(33.51803215741656, 73.06976331948866, 0.0))



entity = acad.model.AddLine(APoint(120.51803215741657, 73.06976331948866, 0.0), APoint(121.71803215741656, 74.26976331948865, 0.0))



entity = acad.model.AddLine(APoint(163.23935261674055, 101.51440127888563, 0.0), APoint(162.36530401992897, 102.96906242513643, 0.0))
entity.Color = 7


entity = acad.model.AddLine(APoint(161.79493651342725, 99.52379186092662, 0.0), APoint(162.99493651342723, 98.32379186092663, 0.0))
entity.Color = 7


entity = acad.model.AddArc(APoint(77.15875113677353, 209.4177292156739, 0.0), 0.06250000000000798, 3.6780676243874266, 0.5364749707976333)


entity = acad.model.AddArc(APoint(77.15875113677353, 209.4177292156739, 0.0), 0.06250000000000798, 0.5364749707976333, 3.6780676243874266)


entity = acad.model.AddArc(APoint(74.17109666998266, 207.64112622733813, 0.0), 0.06250000000000798, 0.5364749707976333, 3.6780676243874266)


entity = acad.model.AddArc(APoint(74.17109666998266, 207.64112622733813, 0.0), 0.06250000000000798, 3.6780676243874266, 0.5364749707976333)


entity = acad.model.AddArc(APoint(76.96299425466442, 208.60958118067143, 0.0), 0.06250000000001317, 1.5866188494146465, 4.72821150300444)


entity = acad.model.AddArc(APoint(76.96299425466442, 208.60958118067143, 0.0), 0.06250000000001317, 4.72821150300444, 1.5866188494146465)


entity = acad.model.AddArc(APoint(76.89962191727909, 212.61444502895105, 0.0), 0.06250000000001317, 4.72821150300444, 1.5866188494146465)


entity = acad.model.AddArc(APoint(76.89962191727909, 212.61444502895105, 0.0), 0.06250000000001317, 1.5866188494146465, 4.72821150300444)


entity = acad.model.AddArc(APoint(76.94209497795191, 204.57650189817795, 0.0), 0.06250000000001295, 1.586618849414419, 4.7282115030042124)


entity = acad.model.AddArc(APoint(76.94209497795191, 204.57650189817795, 0.0), 0.06250000000001295, 4.7282115030042124, 1.586618849414419)


entity = acad.model.AddArc(APoint(76.87872264056796, 208.58136574645755, 0.0), 0.06250000000001295, 4.7282115030042124, 1.586618849414419)


entity = acad.model.AddArc(APoint(76.87872264056796, 208.58136574645755, 0.0), 0.06250000000001295, 1.586618849414419, 4.7282115030042124)


entity = acad.model.AddArc(APoint(80.16555900241889, 211.15349220579566, 0.0), 0.06249999999999282, 3.665191429188158, 0.5235987755983652)


entity = acad.model.AddArc(APoint(80.16555900241889, 211.15349220579566, 0.0), 0.06249999999999282, 0.5235987755983652, 3.665191429188158)


entity = acad.model.AddArc(APoint(77.16555900242025, 209.42144139822733, 0.0), 0.06249999999999282, 0.5235987755983652, 3.665191429188158)


entity = acad.model.AddArc(APoint(77.16555900242025, 209.42144139822733, 0.0), 0.06249999999999282, 3.665191429188158, 0.5235987755983652)


entity = acad.model.AddLine(APoint(81.36247269631372, 118.93768070292367, 0.0), APoint(93.80654205576525, 118.93768070292367, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(93.80654205576525, 118.93768070292367, 0.0), APoint(92.29299356482466, 119.35481727010279, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('-2 %', APoint(83.28338523671505, 119.52914341798692, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddLine(APoint(74.12637648617624, 118.93768070292367, 0.0), APoint(61.68230712672471, 118.93768070292367, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(61.68230712672471, 118.93768070292367, 0.0), APoint(63.195855617607094, 119.35481727010279, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('2 %', APoint(66.55928598923151, 119.68523175063251, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('DOWN', APoint(20.84343490445349, 96.67850435676787, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(117.72913097175365, 114.80029574945286, 0.0), APoint(113.46026251796343, 117.64620805197956, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(113.46026251796343, 117.64620805197956, 0.0), APoint(117.72913097175365, 117.64620805197956, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(117.72913097175365, 117.64620805197956, 0.0), APoint(117.72913097175365, 114.80029574945286, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('3', APoint(114.80941006904345, 118.38311975069689, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('1', APoint(117.81793375059328, 115.06301067296943, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('UP', APoint(126.81206858877977, 97.02109307313238, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(218.64403483821025, 198.47831831688086, 0.0), APoint(235.8671998799191, 198.47831831688086, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(235.8671998799191, 198.47831831688086, 0.0), APoint(232.8401028980379, 199.31259145077343, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('3 %', APoint(222.1468235795992, 198.92929040968443, 0.0), 1.7249999999999992)
entity.Color = 1

entity = acad.model.AddText('DOWN', APoint(22.73272254799485, 185.96785877586683, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('i-094', APoint(81.97557694699285, 168.26555371369759, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('UP', APoint(148.63549219696006, 239.7056894632342, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddText('i-093', APoint(80.49896720633896, 248.89035549436184, 0.0), 3.0)
entity.Color = 5

entity = acad.model.AddLine(APoint(44.71813641215931, 189.2069032198129, 0.0), APoint(46.00680962818069, 189.95060192705637, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(46.00680962818069, 189.95060192705637, 0.0), APoint(43.973935633197016, 190.49644642037111, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(28.26949214218198, 168.82878184465955, 0.0), APoint(30.46863345962811, 166.86201483149364, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(30.46863345962811, 166.86201483149364, 0.0), APoint(28.36611671648234, 166.76228401808442, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(41.059810658867264, 157.18067905210415, 0.0), APoint(42.1602249598036, 156.1792526738123, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(41.059810658867264, 157.18067905210415, 0.0), APoint(41.15954144956523, 155.07816278775618, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(57.041224714041164, 222.53826179876546, 0.0), APoint(59.08359266303387, 222.02908987172196, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(59.08359266303387, 222.02908987172196, 0.0), APoint(58.317683763666544, 223.33008892181417, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(79.5677454975762, 184.86340309069521, 0.0), APoint(80.11257919367235, 186.8979940604019, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(80.11257919367235, 186.8979940604019, 0.0), APoint(80.8572886981342, 185.60760386965813, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(124.20275686482546, 235.02811202907623, 0.0), APoint(124.74722930188045, 237.0613539368773, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(126.7801032968614, 236.5155094435628, 0.0), APoint(124.20275686482546, 235.02811202907623, 0.0))
entity.Color = 1


entity = acad.model.AddLine(APoint(75.80977665059508, 120.45179028096756, 0.0), APoint(76.19476497624295, 120.77082631202806, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(76.19476497624295, 120.77082631202806, 0.0), APoint(77.72399283695813, 118.14186032708028, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(77.72399283695813, 118.14186032708028, 0.0), APoint(75.4247883249472, 120.13275424990705, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(75.4247883249472, 120.13275424990705, 0.0), APoint(75.80977665059508, 120.45179028096757, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(43.918563069275336, 190.28966677489072, 0.0), APoint(44.093293957943914, 190.46439766355928, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.85391233590536, 190.0482393462241, 0.0), APoint(44.23265183993777, 190.42697885025652, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.789261602535376, 189.80681191755747, 0.0), APoint(44.37200972193163, 190.38956003695375, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.7246108691654, 189.56538448889086, 0.0), APoint(44.51136760392551, 190.35214122365096, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.659960135795416, 189.32395706022425, 0.0), APoint(44.65072548591935, 190.31472241034817, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.59530940242544, 189.08252963155763, 0.0), APoint(44.79008336791324, 190.27730359704543, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.53065866905547, 188.84110220289102, 0.0), APoint(44.929441249907114, 190.23988478374267, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.4660079356855, 188.5996747742244, 0.0), APoint(45.06879913190096, 190.20246597043987, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.611189216183135, 188.5680793594254, 0.0), APoint(45.208157013894834, 190.1650471571371, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.02920398343774, 188.80931743138336, 0.0), APoint(45.34751489588869, 190.12762834383432, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.44721875069234, 189.05055550334134, 0.0), APoint(45.48687277788255, 190.09020953053155, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(44.86523351794632, 189.2917935752987, 0.0), APoint(45.62623065987641, 190.0527907172288, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.28324828519922, 189.53303164725494, 0.0), APoint(45.76558854187027, 190.015371903926, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(45.701263052452106, 189.7742697192112, 0.0), APoint(45.90494642386413, 189.9779530906232, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.270466683751494, 168.80793944457784, 0.0), APoint(28.281009087346845, 168.81848184817318, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.27836312683874, 168.63905919236845, 0.0), APoint(28.37432773570302, 168.73502380123273, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.28625956992599, 168.47017894015906, 0.0), APoint(28.467646384059194, 168.65156575429228, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.294156013013236, 168.30129868794967, 0.0), APoint(28.560965032415368, 168.5681077073518, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.302052456100483, 168.13241843574028, 0.0), APoint(28.65428368077154, 168.48464966041132, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.30994889918773, 167.9635381835309, 0.0), APoint(28.747602329127716, 168.40119161347087, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.31784534227498, 167.7946579313215, 0.0), APoint(28.84092097748386, 168.31773356653036, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.32574178536221, 167.6257776791121, 0.0), APoint(28.93423962584002, 168.23427551958991, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.333638228449473, 167.45689742690274, 0.0), APoint(29.027558274196195, 168.15081747264946, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.341534671536692, 167.28801717469332, 0.0), APoint(29.12087692255237, 168.06735942570901, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.34943111462394, 167.11913692248393, 0.0), APoint(29.214195570908544, 167.98390137876854, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.357327557711187, 166.95025667027454, 0.0), APoint(29.307514219264718, 167.90044333182806, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.365224000798435, 166.78137641806515, 0.0), APoint(29.400832867620892, 167.8169852848876, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.53071589628783, 166.7700916182579, 0.0), APoint(29.49415151597705, 167.73352723794713, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.716295371428274, 166.77889439810173, 0.0), APoint(29.58747016433321, 167.65006919100665, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.90187484656869, 166.7876971779455, 0.0), APoint(29.680788812689386, 167.5666111440662, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(29.08745432170913, 166.7964999577893, 0.0), APoint(29.77410746104556, 167.48315309712572, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(29.27303379684956, 166.8053027376331, 0.0), APoint(29.867426109401734, 167.39969505018524, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(29.458613271990004, 166.8141055174769, 0.0), APoint(29.960744757757894, 167.3162370032448, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(29.644192747130447, 166.82290829732068, 0.0), APoint(30.054063406114068, 167.23277895630432, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(29.82977222227089, 166.8317110771645, 0.0), APoint(30.147382054470228, 167.14932090936384, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(30.015351697411305, 166.84051385700826, 0.0), APoint(30.240700702826402, 167.0658628624234, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(30.200931172551748, 166.84931663685208, 0.0), APoint(30.334019351182576, 166.9824048154829, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(30.386510647692177, 166.85811941669587, 0.0), APoint(30.427337999538736, 166.89894676854243, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.066846111349065, 157.0323582259429, 0.0), APoint(41.141147114312545, 157.10665922890638, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.07485160717141, 156.8635870264686, 0.0), APoint(41.23369818419103, 157.0224336034882, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.08285710299373, 156.69481582699427, 0.0), APoint(41.32624925406951, 156.93820797807007, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.090862598816045, 156.52604462751995, 0.0), APoint(41.41880032394799, 156.85398235265188, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.09886809463839, 156.35727342804566, 0.0), APoint(41.51135139382647, 156.76975672723376, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.10687359046074, 156.18850222857137, 0.0), APoint(41.60390246370497, 156.6855311018156, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.11487908628305, 156.01973102909704, 0.0), APoint(41.696453533583444, 156.60130547639744, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.122884582105364, 155.85095982962272, 0.0), APoint(41.789004603461926, 156.5170798509793, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.13089007792771, 155.68218863014843, 0.0), APoint(41.88155567334041, 156.43285422556113, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.13889557375004, 155.51341743067414, 0.0), APoint(41.97410674321889, 156.34862860014297, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.14690106957236, 155.34464623119982, 0.0), APoint(42.06665781309737, 156.26440297472482, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.15490656539469, 155.1758750317255, 0.0), APoint(42.159208882975854, 156.18017734930666, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.23767731461637, 155.08186908565054, 0.0), APoint(42.25175995285441, 156.0959517238886, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.42325678975681, 155.09067186549436, 0.0), APoint(42.344311022732974, 156.01172609847052, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.608836264897256, 155.09947464533815, 0.0), APoint(42.43686209261153, 155.92750047305242, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.794415740037685, 155.10827742518194, 0.0), APoint(42.52941316249011, 155.84327484763438, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(41.97999521517812, 155.11708020502576, 0.0), APoint(42.62196423236867, 155.7590492222163, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(42.165574690318564, 155.12588298486958, 0.0), APoint(42.71451530224722, 155.6748235967982, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(42.35115416545899, 155.13468576471337, 0.0), APoint(42.8070663721258, 155.59059797138016, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(42.53673364059944, 155.14348854455716, 0.0), APoint(42.89961744200437, 155.5063723459621, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(42.72231311573988, 155.15229132440095, 0.0), APoint(42.99216851188294, 155.42214672054402, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(42.90789259088032, 155.16109410424477, 0.0), APoint(43.08471958176149, 155.33792109512592, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.72494851149617, 236.9781500248606, 0.0), APoint(124.79525665741454, 237.04845817077899, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(43.09347206602075, 155.16989688408856, 0.0), APoint(43.17727065164006, 155.25369546970785, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.6602977781261, 236.73672259619389, 0.0), APoint(124.93461453940837, 237.0110393574762, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.59564704475605, 236.49529516752722, 0.0), APoint(125.07397242140223, 236.9736205441734, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.53099631138598, 236.2538677388605, 0.0), APoint(125.213330303396, 236.93620173087055, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.46634557801596, 236.01244031019385, 0.0), APoint(125.35268818538987, 236.89878291756776, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.40169484464592, 235.77101288152716, 0.0), APoint(125.49204606738373, 236.86136410426496, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.33704411127584, 235.52958545286046, 0.0), APoint(125.63140394937759, 236.8239452909622, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.27239337790581, 235.28815802419382, 0.0), APoint(125.77076183137137, 236.78652647765938, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.20774264453576, 235.0467305955271, 0.0), APoint(125.91011971336522, 236.74910766435656, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(124.58853488182919, 235.25074613752392, 0.0), APoint(126.04947759535904, 236.71168885105376, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.00654964908347, 235.49198420948153, 0.0), APoint(126.18883547735291, 236.67427003775097, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.42456441633772, 235.73322228143917, 0.0), APoint(126.32819335934673, 236.63685122444818, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.84257918359197, 235.97446035339675, 0.0), APoint(126.46755124134057, 236.59943241114536, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.26059395084619, 236.21569842535436, 0.0), APoint(126.60690912333442, 236.5620135978426, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.67860871810043, 236.45693649731194, 0.0), APoint(126.74626700532826, 236.52459478453977, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.10808416571487, 186.88120812488356, 0.0), APoint(80.11707683853007, 186.89020079769875, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.0434334323449, 186.63978069621697, 0.0), APoint(80.18176521004568, 186.77811247391776, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.97878269897498, 186.3983532675504, 0.0), APoint(80.2464535815613, 186.6660241501367, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.91413196560504, 186.15692583888384, 0.0), APoint(80.31114195307688, 186.55393582635568, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.84948123223512, 185.91549841021725, 0.0), APoint(80.37583032459247, 186.4418475025746, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.78483049886515, 185.67407098155067, 0.0), APoint(80.44051869610809, 186.3297591787936, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.72017976549519, 185.4326435528841, 0.0), APoint(80.50520706762369, 186.21767085501256, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.65552903212526, 185.1912161242175, 0.0), APoint(80.56989543913932, 186.10558253123156, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.59087829875533, 184.94978869555092, 0.0), APoint(80.63458381065492, 185.9934942074505, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.65729053752187, 184.83942423902084, 0.0), APoint(80.69927218217052, 185.8814058836695, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.79672793713796, 184.80208494334028, 0.0), APoint(80.76396055368615, 185.76931755988846, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(79.93616533675404, 184.76474564765974, 0.0), APoint(80.82864892520175, 185.65722923610744, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.0756027363701, 184.72740635197914, 0.0), APoint(80.8933366851901, 185.54514030079918, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.21504013598621, 184.69006705629863, 0.0), APoint(80.95802395933433, 185.43305087964674, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.35447753560227, 184.65272776061806, 0.0), APoint(81.02271123347852, 185.3209614584943, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.49391493521838, 184.61538846493752, 0.0), APoint(81.08739850762274, 185.20887203734188, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.63335233483443, 184.57804916925696, 0.0), APoint(81.15208578176691, 185.09678261618944, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.77278973445053, 184.5407098735764, 0.0), APoint(81.21677305591115, 184.984693195037, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(80.9122271340666, 184.50337057789585, 0.0), APoint(81.28146033005532, 184.87260377388458, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.0516645336827, 184.46603128221528, 0.0), APoint(81.34614760419956, 184.76051435273214, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.19110193329877, 184.42869198653474, 0.0), APoint(81.41083487834373, 184.6484249315797, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.33053933291484, 184.39135269085415, 0.0), APoint(81.47552215248797, 184.53633551042728, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(81.46997673253094, 184.35401339517364, 0.0), APoint(81.54020942663215, 184.42424608927485, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.501332232883584, 224.37853259290884, 0.0), APoint(57.609256974571366, 224.48645733459662, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.44239986733113, 224.14282353205977, 0.0), APoint(57.67641359665497, 224.37683726138357, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.38346750177871, 223.9071144712107, 0.0), APoint(57.7435702187386, 224.26721718817058, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.32453513622626, 223.67140541036161, 0.0), APoint(57.81072684082223, 224.15759711495758, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.26560277067378, 223.43569634951248, 0.0), APoint(57.87788346290586, 224.04797704174456, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.20667040512136, 223.1999872886634, 0.0), APoint(57.945040084989486, 223.93835696853154, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.14773803956888, 222.9642782278143, 0.0), APoint(58.012196707073116, 223.82873689531854, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.088805674016456, 222.72856916696526, 0.0), APoint(58.079353329156774, 223.71911682210555, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.068480104256054, 222.5314669019082, 0.0), APoint(58.146509951240375, 223.60949674889252, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.20998016858725, 222.49619027094275, 0.0), APoint(58.21366657332398, 223.4998766756795, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.35148023291842, 222.4609136399773, 0.0), APoint(58.280823195407635, 223.3902566024665, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.492980297249616, 222.42563700901184, 0.0), APoint(58.34723517393293, 223.27989188569518, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.63448036158081, 222.3903603780464, 0.0), APoint(58.41274116038184, 223.16862117684744, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.77598042591194, 222.35508374708093, 0.0), APoint(58.47824714683071, 223.0573504679997, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(57.917480490243136, 222.3198071161155, 0.0), APoint(58.54375313327965, 222.94607975915198, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.05898055457433, 222.28453048515004, 0.0), APoint(58.60925911972856, 222.83480905030427, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.2004806189055, 222.2492538541846, 0.0), APoint(58.674765106177475, 222.72353834145656, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.3419806832367, 222.21397722321913, 0.0), APoint(58.74027109262639, 222.61226763260882, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.483480747567896, 222.17870059225368, 0.0), APoint(58.8057770790753, 222.50099692376108, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.624980811899064, 222.14342396128822, 0.0), APoint(58.87128306552418, 222.38972621491334, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.76648087623026, 222.10814733032277, 0.0), APoint(58.93678905197312, 222.27845550606565, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(58.90798094056143, 222.0728706993573, 0.0), APoint(59.002295038422034, 222.1671847972179, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(59.0494810048926, 222.03759406839185, 0.0), APoint(59.06780102487092, 222.05591408837017, 0.0))
entity.Color = 1
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(27.88079269928982, 108.66774244985288, 0.0), APoint(27.92293856481023, 108.70988831537329, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(27.969181046938097, 108.57935410220452, 0.0), APoint(28.09971526010687, 108.70988831537329, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.05756939458638, 108.49096575455619, 0.0), APoint(28.2764919554035, 108.7098883153733, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.14595774223467, 108.40257740690784, 0.0), APoint(28.45326865070014, 108.7098883153733, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.234346089882948, 108.31418905925948, 0.0), APoint(28.630045345996763, 108.70988831537329, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.32273443753124, 108.22580071161113, 0.0), APoint(28.8068220412934, 108.70988831537329, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.41112278517953, 108.13741236396278, 0.0), APoint(28.98359873659004, 108.70988831537329, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.499511132827806, 108.04902401631442, 0.0), APoint(29.160375431886678, 108.70988831537329, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.587899480476096, 107.96063566866607, 0.0), APoint(29.18864683376843, 108.5613830219584, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.676287828124373, 107.87224732101771, 0.0), APoint(29.18864683376843, 108.38460632666177, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.764676175772664, 107.78385897336936, 0.0), APoint(29.18864683376843, 108.20782963136513, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.853064523420954, 107.69547062572101, 0.0), APoint(29.18864683376843, 108.03105293606849, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.941452871069224, 107.60708227807265, 0.0), APoint(29.188646833768424, 107.85427624077187, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(29.029841218717515, 107.51869393042432, 0.0), APoint(29.188646833768424, 107.67749954547523, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(29.11822956636579, 107.43030558277596, 0.0), APoint(29.188646833768424, 107.50072285017859, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(27.88146678269239, 86.92488301176913, 0.0), APoint(27.924286731615407, 86.96770296069214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(27.96985513034068, 86.83649466412078, 0.0), APoint(28.101063426912045, 86.96770296069214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.058243477988956, 86.74810631647242, 0.0), APoint(28.277840122208676, 86.96770296069214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.146631825637247, 86.65971796882407, 0.0), APoint(28.454616817505315, 86.96770296069214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.235020173285534, 86.57132962117572, 0.0), APoint(28.63139351280195, 86.96770296069214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.32340852093381, 86.48294127352736, 0.0), APoint(28.808170208098588, 86.96770296069214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.4117968685821, 86.39455292587901, 0.0), APoint(28.984946903395226, 86.96770296069214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.500185216230385, 86.30616457823066, 0.0), APoint(29.161723598691864, 86.96770296069214, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.588573563878676, 86.2177762305823, 0.0), APoint(29.188646833768438, 86.81784950047208, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.676961911526956, 86.12938788293395, 0.0), APoint(29.18864683376842, 86.64107280517543, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.76535025917524, 86.04099953528561, 0.0), APoint(29.188646833768427, 86.46429610987879, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.85373860682353, 85.95261118763726, 0.0), APoint(29.188646833768427, 86.28751941458215, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.942126954471806, 85.8642228399889, 0.0), APoint(29.188646833768427, 86.11074271928551, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(29.030515302120097, 85.77583449234055, 0.0), APoint(29.188646833768427, 85.93396602398887, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(29.118903649768384, 85.6874461446922, 0.0), APoint(29.188646833768424, 85.75718932869225, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(27.587452241273347, 76.7313735337384, 0.0), APoint(28.907521016269598, 78.05144230873466, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(27.764228936569985, 76.7313735337384, 0.0), APoint(28.907521016269598, 77.87466561343803, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(27.941005631866624, 76.7313735337384, 0.0), APoint(28.907521016269598, 77.69788891814139, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.117782327163262, 76.7313735337384, 0.0), APoint(28.90752101626959, 77.52111222284475, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.2945590224599, 76.7313735337384, 0.0), APoint(28.90752101626959, 77.34433552754811, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.471335717756535, 76.73137353373842, 0.0), APoint(28.90752101626958, 77.16755883225146, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.648112413053173, 76.73137353373842, 0.0), APoint(28.90752101626958, 76.99078213695482, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(28.82488910834981, 76.73137353373842, 0.0), APoint(28.90752101626958, 76.81400544165818, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.51066550727845, 120.05839272203096, 0.0), APoint(76.2051852040871, 120.75291241883961, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.60540593844057, 119.97635645789644, 0.0), APoint(76.27019704759573, 120.6411475670516, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.70014636960268, 119.89432019376191, 0.0), APoint(76.33520889110437, 120.52938271526361, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.79488680076477, 119.81228392962737, 0.0), APoint(76.400220734613, 120.4176178634756, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.88962723192688, 119.73024766549284, 0.0), APoint(76.46523257812161, 120.30585301168757, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(75.984367663089, 119.64821140135832, 0.0), APoint(76.53024442163024, 120.19408815989956, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.07910809425111, 119.5661751372238, 0.0), APoint(76.59525626513887, 120.08232330811155, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.1738485254132, 119.48413887308925, 0.0), APoint(76.66026810864751, 119.97055845632356, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.26858895657533, 119.40210260895473, 0.0), APoint(76.72527995215613, 119.85879360453553, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.36332938773744, 119.3200663448202, 0.0), APoint(76.79029179566476, 119.74702875274753, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.45806981889956, 119.23803008068569, 0.0), APoint(76.85530363917339, 119.63526390095952, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.55281025006167, 119.15599381655116, 0.0), APoint(76.92031548268203, 119.52349904917152, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.64755068122376, 119.07395755241662, 0.0), APoint(76.98532732619064, 119.4117341973835, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.74229111238587, 118.99192128828209, 0.0), APoint(77.05033916969924, 119.29996934559546, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.83703154354797, 118.90988502414754, 0.0), APoint(77.11535101320788, 119.18820449380749, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(76.93177197471007, 118.82784876001304, 0.0), APoint(77.18036285671653, 119.0764396420195, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.02651240587218, 118.74581249587851, 0.0), APoint(77.24537470022514, 118.96467479023144, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.12125283703429, 118.66377623174398, 0.0), APoint(77.31038654373378, 118.85290993844345, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.2159932681964, 118.58173996760942, 0.0), APoint(77.3753983872424, 118.74114508665542, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.31073369935851, 118.49970370347492, 0.0), APoint(77.44041023075101, 118.62938023486743, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.40547413052063, 118.4176674393404, 0.0), APoint(77.50542207425966, 118.51761538307943, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.50021456168274, 118.33563117520588, 0.0), APoint(77.57043391776826, 118.40585053129139, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.59495499284482, 118.25359491107132, 0.0), APoint(77.6354457612769, 118.2940856795034, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(77.68969542400694, 118.1715586469368, 0.0), APoint(77.70045760478553, 118.18232082771539, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.2708675728256, 109.71451838672154, 0.0), APoint(125.30350763977174, 109.74715845366768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.35925592047391, 109.62613003907322, 0.0), APoint(125.48028433506838, 109.74715845366768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.44764426812222, 109.53774169142488, 0.0), APoint(125.65706103036501, 109.74715845366768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.53603261577052, 109.44935334377658, 0.0), APoint(125.83383772566165, 109.74715845366768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.62442096341886, 109.36096499612825, 0.0), APoint(126.01061442095829, 109.74715845366768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.71280931106716, 109.27257664847994, 0.0), APoint(126.18739111625493, 109.74715845366768, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.80119765871548, 109.18418830083162, 0.0), APoint(126.36416781155155, 109.7471584536677, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.88958600636377, 109.09579995318327, 0.0), APoint(126.54094450684819, 109.7471584536677, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.97797435401209, 109.00741160553495, 0.0), APoint(126.58822750587935, 109.61766475740221, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.0663627016604, 108.91902325788662, 0.0), APoint(126.58822750587935, 109.44088806210557, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.15475104930871, 108.8306349102383, 0.0), APoint(126.58822750587936, 109.26411136680895, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.24313939695703, 108.74224656258998, 0.0), APoint(126.58822750587936, 109.08733467151231, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.33152774460535, 108.65385821494166, 0.0), APoint(126.58822750587936, 108.91055797621567, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.41991609225364, 108.56546986729332, 0.0), APoint(126.58822750587936, 108.73378128091903, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.50830443990196, 108.477081519645, 0.0), APoint(126.58822750587936, 108.5570045856224, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.27154165622818, 87.97165894863778, 0.0), APoint(125.30485580657691, 88.00497309898651, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.3599300038765, 87.88327060098946, 0.0), APoint(125.48163250187355, 88.00497309898651, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.44831835152482, 87.79488225334114, 0.0), APoint(125.65840919717019, 88.00497309898651, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.53670669917312, 87.70649390569284, 0.0), APoint(125.83518589246682, 88.00497309898651, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.62509504682143, 87.6181055580445, 0.0), APoint(126.01196258776346, 88.00497309898651, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.71348339446976, 87.52971721039617, 0.0), APoint(126.1887392830601, 88.00497309898651, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.80187174211807, 87.44132886274787, 0.0), APoint(126.36551597835674, 88.00497309898651, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.89026008976639, 87.35294051509955, 0.0), APoint(126.54229267365336, 88.00497309898653, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.9786484374147, 87.26455216745123, 0.0), APoint(126.58822750587936, 87.87413123591588, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.06703678506302, 87.17616381980291, 0.0), APoint(126.58822750587936, 87.69735454061924, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.15542513271131, 87.08777547215456, 0.0), APoint(126.58822750587936, 87.5205778453226, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.24381348035963, 86.99938712450624, 0.0), APoint(126.58822750587936, 87.34380115002597, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.33220182800795, 86.91099877685792, 0.0), APoint(126.58822750587936, 87.16702445472933, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.42059017565626, 86.82261042920959, 0.0), APoint(126.58822750587936, 86.99024775943269, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.50897852330458, 86.73422208156127, 0.0), APoint(126.58822750587936, 86.81347106413605, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.67512809742136, 77.76864367203275, 0.0), APoint(126.86935332337956, 78.96286889799094, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(125.851904792718, 77.76864367203275, 0.0), APoint(126.86935332337956, 78.7860922026943, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.02868148801464, 77.76864367203275, 0.0), APoint(126.86935332337956, 78.60931550739767, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.20545818331126, 77.76864367203277, 0.0), APoint(126.86935332337956, 78.43253881210103, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.3822348786079, 77.76864367203277, 0.0), APoint(126.86935332337956, 78.25576211680439, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.55901157390454, 77.76864367203277, 0.0), APoint(126.86935332337953, 78.07898542150775, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(126.73578826920118, 77.76864367203277, 0.0), APoint(126.86935332337953, 77.90220872621111, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.22661973673513, 117.37936797007673, 0.0), APoint(33.93832781644096, 116.29255310038599, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(33.93832781644096, 116.29255310038599, 0.0), APoint(32.671624996078386, 117.87576978675479, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(32.22661973673513, 117.37936797007673, 0.0), APoint(32.449122366406755, 117.62756887841576, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(32.449122366406755, 117.62756887841576, 0.0), APoint(32.671624996078386, 117.87576978675479, 0.0))
entity.Color = 8


entity = acad.model.AddLine(APoint(32.30194882916019, 117.33153926684255, 0.0), APoint(32.74920911405854, 117.77879955174089, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.41007375903013, 117.26288750141586, 0.0), APoint(32.827780995817896, 117.68059473820361, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.51819868890008, 117.19423573598917, 0.0), APoint(32.90635287757727, 117.58238992466636, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.62632361877004, 117.12558397056247, 0.0), APoint(32.98492475933666, 117.48418511112911, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.73444854863998, 117.05693220513578, 0.0), APoint(33.063496641096016, 117.38598029759183, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.842573478509934, 116.98828043970911, 0.0), APoint(33.14206852285538, 117.28777548405456, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(32.95069840837988, 116.91962867428242, 0.0), APoint(33.22064040461474, 117.18957067051728, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.05882333824982, 116.85097690885573, 0.0), APoint(33.29921228637413, 117.09136585698003, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.16694826811977, 116.78232514342903, 0.0), APoint(33.3777841681335, 116.99316104344277, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.27507319798973, 116.71367337800235, 0.0), APoint(33.456356049892875, 116.8949562299055, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.38319812785967, 116.64502161257566, 0.0), APoint(33.53492793165225, 116.79675141636824, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.49132305772963, 116.57636984714898, 0.0), APoint(33.61349981341162, 116.69854660283097, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.599447987599575, 116.50771808172229, 0.0), APoint(33.692071695170995, 116.60034178929371, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.70757291746952, 116.4390663162956, 0.0), APoint(33.770643576930354, 116.50213697575643, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.81569784733948, 116.37041455086892, 0.0), APoint(33.84921545868974, 116.40393216221918, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddLine(APoint(33.92382277720944, 116.30176278544224, 0.0), APoint(33.927787340449115, 116.30572734868191, 0.0))
entity.Color = 8
try:
    entity.LineType = 'Continuous'
    entity.LineTypeScale = 1.0
except:
    pass

entity = acad.model.AddText('*', APoint(346.8835749075681, 272.6678206162468, 0.0), 2.625)
entity.Color = 1

entity = acad.model.AddText('*', APoint(356.82509529477215, 270.7724536353502, 0.0), 2.625)
entity.Color = 1

entity = acad.model.AddText('*', APoint(350.79349165072654, 264.95597069889345, 0.0), 2.625)
entity.Color = 1

entity = acad.model.AddText('*', APoint(360.2723558204325, 266.86556917184157, 0.0), 2.625)
entity.Color = 1

entity = acad.model.AddLine(APoint(51.8640449130603, 180.5828379036829, 0.0), APoint(46.70871649223977, 180.5828379036829, 0.0))
entity.Color = 3


entity = acad.model.AddArc(APoint(49.87700224228706, 179.84563162191546, 0.0), 1.873395286472879, 2.737142352785758, 4.374432718953813)
entity.Color = 3

entity = acad.model.AddText('45.0', APoint(43.954294796070826, 177.39732076889516, 0.0), 2.0)
entity.Color = 1

entity = acad.model.AddText('45.0', APoint(94.08113390005482, 216.34957488856105, 0.0), 2.0)
entity.Color = 1

try:
    acad_doc = acad.app.ActiveDocument
    acad_doc.SaveAs(file_path)
    print(f'[INFO] Drawing saved successfully at {file_path}')
except Exception as e:
    print(f'[Error] Failed saving drawing: {e}')
