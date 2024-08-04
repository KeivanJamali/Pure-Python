import pandas as pd

file = r"D:\All Python\Pure-Python\P2\12-Work-GITI\03-AutoCAD-Project\raw_data\input_form.csv"
data = pd.read_csv(file, header=None)
data.fillna("")

n = int(data.iloc[0, 1])
D = float(data.iloc[1, 1])
L = float(data.iloc[2, 1])
Hs = float(data.iloc[3, 1])
H = float(data.iloc[4, 1])
H_min = float(data.iloc[5, 1])
CL = float(data.iloc[6, 1])
dever_right = float(data.iloc[7, 1])
dever_left = float(data.iloc[8, 1])
ax_nature = float(data.iloc[9, 1])
z_nature = float(data.iloc[10, 1])
z_toli = float(data.iloc[11, 1])
z_shirvani = int(data.iloc[12, 1])
ret = float(data.iloc[13, 1])
ball_degre = float(data.iloc[14, 1])
A = float(data.iloc[15, 1])
B = float(data.iloc[16, 1])


city_top = data.iloc[17, 1]
city_down = data.iloc[18, 1]

if data.iloc[19, 1] == True:
    left = "UP"
    right = "DOWN"
elif data.iloc[19, 1] == False:
    left = "DOWN"
    right = "UP"

explanation1 = data.iloc[20, 1]
explanation2 = data.iloc[21, 1]
explanation3 = data.iloc[22, 1]

mozo_nagshe1 = data.iloc[23, 1]
mozo_nagshe2 = data.iloc[24, 1]
mozo_nagshe3 = data.iloc[25, 1]
number_nagshe = data.iloc[26, 1]

karfarma = data.iloc[27, 1]
mohandes_moshaver = data.iloc[28, 1]

peymankar = data.iloc[29, 1]
onvan_project = data.iloc[30, 1]

date_eblagh = data.iloc[31, 1]

abro_dahane = data.iloc[32, 1]
mahal_abro = data.iloc[33, 1]

hadaksar_ertefa_abro = data.iloc[34, 1]
zavie_torb = data.iloc[35, 1]

tozihat1 = data.iloc[35, 1]
tozihat2 = data.iloc[36, 1]
tozihat3 = data.iloc[37, 1]
tozihat4 = data.iloc[38, 1]

print("[INFO] All input data were read successfuly.")