import test as tp1
import Toolkit_Project as tp
import numpy as np

A = 2  # in^2
E = 30 * 10 ** 6  # psi
node = [0]
Element = [0]
node.append(tp1.Point(11.5, 8.5, "01"))
node.append(tp1.Point(11.5, 6, "02"))
node.append(tp1.Point(12.75, 3, "03"))
node.append(tp1.Point(4.75, 3, "04"))
node.append(tp1.Point(6, 6, "05"))
node.append(tp1.Point(7, 7, "06"))
node.append(tp1.Point(6, 8.5, "07"))
node.append(tp1.Point(7.75, 11.5, "08"))
node.append(tp1.Point(6, 16, "09"))
node.append(tp1.Point(7.75, 17, "10"))
node.append(tp1.Point(10.5, 17, "11"))
node.append(tp1.Point(11.5, 16, "12"))
node.append(tp1.Point(8.75, 13, "13"))
node.append(tp1.Point(9.75, 11.5, "14"))
node.append(tp1.Point(8.75, 8.5, "15"))
node.append(tp1.Point(10.5, 7, "16"))
node.append(tp1.Point(0, 0, "17"))
node.append(tp1.Point(3, 0, "18"))
node.append(tp1.Point(6, 0, "19"))
node.append(tp1.Point(11.5, 0, "20"))
node.append(tp1.Point(14.5, 0, "21"))
node.append(tp1.Point(17.5, 0, "22"))
Element.append(tp1.Element(node[17], node[18], A=A, E=E))
Element.append(tp1.Element(node[18], node[19], A=A, E=E))
Element.append(tp1.Element(node[4], node[18], A=A, E=E))
Element.append(tp1.Element(node[4], node[19], A=A, E=E))
Element.append(tp1.Element(node[4], node[17], A=A, E=E))
Element.append(tp1.Element(node[7], node[17], A=A, E=E))
Element.append(tp1.Element(node[5], node[19], A=A, E=E))
Element.append(tp1.Element(node[4], node[5], A=A, E=E))
Element.append(tp1.Element(node[4], node[7], A=A, E=E))
Element.append(tp1.Element(node[6], node[19], A=A, E=E))
Element.append(tp1.Element(node[5], node[6], A=A, E=E))
Element.append(tp1.Element(node[5], node[7], A=A, E=E))
Element.append(tp1.Element(node[6], node[7], A=A, E=E))
Element.append(tp1.Element(node[6], node[8], A=A, E=E))
Element.append(tp1.Element(node[6], node[15], A=A, E=E))
Element.append(tp1.Element(node[8], node[15], A=A, E=E))
Element.append(tp1.Element(node[7], node[8], A=A, E=E))
Element.append(tp1.Element(node[7], node[9], A=A, E=E))
Element.append(tp1.Element(node[8], node[9], A=A, E=E))
Element.append(tp1.Element(node[8], node[10], A=A, E=E))
Element.append(tp1.Element(node[9], node[10], A=A, E=E))
Element.append(tp1.Element(node[10], node[11], A=A, E=E))
Element.append(tp1.Element(node[10], node[13], A=A, E=E))
Element.append(tp1.Element(node[8], node[13], A=A, E=E))
Element.append(tp1.Element(node[11], node[13], A=A, E=E))
Element.append(tp1.Element(node[13], node[14], A=A, E=E))
Element.append(tp1.Element(node[11], node[14], A=A, E=E))
Element.append(tp1.Element(node[8], node[14], A=A, E=E))
Element.append(tp1.Element(node[11], node[12], A=A, E=E))
Element.append(tp1.Element(node[12], node[14], A=A, E=E))
Element.append(tp1.Element(node[12], node[1], A=A, E=E))
Element.append(tp1.Element(node[14], node[1], A=A, E=E))
Element.append(tp1.Element(node[14], node[16], A=A, E=E))
Element.append(tp1.Element(node[15], node[16], A=A, E=E))
Element.append(tp1.Element(node[1], node[16], A=A, E=E))
Element.append(tp1.Element(node[16], node[20], A=A, E=E))
Element.append(tp1.Element(node[2], node[20], A=A, E=E))
Element.append(tp1.Element(node[1], node[2], A=A, E=E))
Element.append(tp1.Element(node[1], node[3], A=A, E=E))
Element.append(tp1.Element(node[1], node[22], A=A, E=E))
Element.append(tp1.Element(node[2], node[3], A=A, E=E))
Element.append(tp1.Element(node[3], node[20], A=A, E=E))
Element.append(tp1.Element(node[3], node[21], A=A, E=E))
Element.append(tp1.Element(node[3], node[22], A=A, E=E))
Element.append(tp1.Element(node[20], node[21], A=A, E=E))
Element.append(tp1.Element(node[21], node[22], A=A, E=E))
Element.append(tp1.Element(node[14], node[15], A=A, E=E))
Element.append(tp1.Element(node[16], node[2], A=A, E=E))
Element[1].make_element_K_with_help(node[17], node[18])
Element[2].make_element_K_with_help(node[18], node[19])
Element[3].make_element_K_with_help(node[4], node[18])
Element[4].make_element_K_with_help(node[4], node[19])
Element[5].make_element_K_with_help(node[4], node[17])
Element[6].make_element_K_with_help(node[7], node[17])
Element[7].make_element_K_with_help(node[5], node[19])
Element[8].make_element_K_with_help(node[4], node[5])
Element[9].make_element_K_with_help(node[4], node[7])
Element[10].make_element_K_with_help(node[6], node[19])
Element[11].make_element_K_with_help(node[5], node[6])
Element[12].make_element_K_with_help(node[5], node[7])
Element[13].make_element_K_with_help(node[6], node[7])
Element[14].make_element_K_with_help(node[6], node[8])
Element[15].make_element_K_with_help(node[6], node[15])
Element[16].make_element_K_with_help(node[8], node[15])
Element[17].make_element_K_with_help(node[7], node[8])
Element[18].make_element_K_with_help(node[7], node[9])
Element[19].make_element_K_with_help(node[8], node[9])
Element[20].make_element_K_with_help(node[8], node[10])
Element[21].make_element_K_with_help(node[9], node[10])
Element[22].make_element_K_with_help(node[10], node[11])
Element[23].make_element_K_with_help(node[10], node[13])
Element[24].make_element_K_with_help(node[8], node[13])
Element[25].make_element_K_with_help(node[11], node[13])
Element[26].make_element_K_with_help(node[13], node[14])
Element[27].make_element_K_with_help(node[11], node[14])
Element[28].make_element_K_with_help(node[8], node[14])
Element[29].make_element_K_with_help(node[11], node[12])
Element[30].make_element_K_with_help(node[12], node[14])
Element[31].make_element_K_with_help(node[1], node[12])
Element[32].make_element_K_with_help(node[1], node[14])
Element[33].make_element_K_with_help(node[14], node[16])
Element[34].make_element_K_with_help(node[15], node[16])
Element[35].make_element_K_with_help(node[1], node[16])
Element[36].make_element_K_with_help(node[16], node[20])
Element[37].make_element_K_with_help(node[2], node[20])
Element[38].make_element_K_with_help(node[1], node[18])
Element[39].make_element_K_with_help(node[1], node[19])
Element[40].make_element_K_with_help(node[1], node[22])
Element[41].make_element_K_with_help(node[2], node[19])
Element[42].make_element_K_with_help(node[3], node[20])
Element[43].make_element_K_with_help(node[3], node[21])
Element[44].make_element_K_with_help(node[3], node[22])
Element[45].make_element_K_with_help(node[20], node[21])
Element[46].make_element_K_with_help(node[21], node[22])
Element[47].make_element_K_with_help(node[14], node[15])
Element[48].make_element_K_with_help(node[2], node[16])

K = np.zeros(44 * 44)  # n*n total
K_help = tp.make_K_help(44)  # n total
for i in range(1, len(Element)):
    K = tp.merge_K(K, K_help, Element[i])

K_modified = np.array([])
new_K_help = tp.make_K_help(32, 1, 1)  # show where is the modified K
for p, v in np.ndenumerate(K_help):
    if v in new_K_help:
        K_modified = np.append(K_modified, K[p])

K_modified = K_modified.reshape([32, 32])  # shape the modified.



















A = 2  # in^2
E = 30 * 10 ** 6  # psi
node = [0]
Elemen = [0]
node.append(tp.Point(11.5, 8.5, 1))
node.append(tp.Point(11.5, 6, 2))
node.append(tp.Point(12.75, 3, 3))
node.append(tp.Point(4.75, 3, 4))
node.append(tp.Point(6, 6, 5))
node.append(tp.Point(7, 7, 6))
node.append(tp.Point(6, 8.5, 7))
node.append(tp.Point(7.75, 11.5, 8))
node.append(tp.Point(6, 16, 9))
node.append(tp.Point(7.75, 17, 10))
node.append(tp.Point(10.5, 17, 11))
node.append(tp.Point(11.5, 16, 12))
node.append(tp.Point(8.75, 13, 13))
node.append(tp.Point(9.75, 11.5, 14))
node.append(tp.Point(8.75, 8.5, 15))
node.append(tp.Point(10.5, 7, 16))
node.append(tp.Point(0, 0, 17))
node.append(tp.Point(3, 0, 18))
node.append(tp.Point(6, 0, 19))
node.append(tp.Point(11.5, 0, 20))
node.append(tp.Point(14.5, 0, 21))
node.append(tp.Point(17.5, 0, 22))
Elemen.append(tp.Element(node[17], node[18], A=A, E=E))
Elemen.append(tp.Element(node[18], node[19], A=A, E=E))
Elemen.append(tp.Element(node[4], node[18], A=A, E=E))
Elemen.append(tp.Element(node[4], node[19], A=A, E=E))
Elemen.append(tp.Element(node[4], node[17], A=A, E=E))
Elemen.append(tp.Element(node[7], node[17], A=A, E=E))
Elemen.append(tp.Element(node[5], node[19], A=A, E=E))
Elemen.append(tp.Element(node[4], node[5], A=A, E=E))
Elemen.append(tp.Element(node[4], node[7], A=A, E=E))
Elemen.append(tp.Element(node[6], node[19], A=A, E=E))
Elemen.append(tp.Element(node[5], node[6], A=A, E=E))
Elemen.append(tp.Element(node[5], node[7], A=A, E=E))
Elemen.append(tp.Element(node[6], node[7], A=A, E=E))
Elemen.append(tp.Element(node[6], node[8], A=A, E=E))
Elemen.append(tp.Element(node[6], node[15], A=A, E=E))
Elemen.append(tp.Element(node[8], node[15], A=A, E=E))
Elemen.append(tp.Element(node[7], node[8], A=A, E=E))
Elemen.append(tp.Element(node[7], node[9], A=A, E=E))
Elemen.append(tp.Element(node[8], node[9], A=A, E=E))
Elemen.append(tp.Element(node[8], node[10], A=A, E=E))
Elemen.append(tp.Element(node[9], node[10], A=A, E=E))
Elemen.append(tp.Element(node[10], node[11], A=A, E=E))
Elemen.append(tp.Element(node[10], node[13], A=A, E=E))
Elemen.append(tp.Element(node[8], node[13], A=A, E=E))
Elemen.append(tp.Element(node[11], node[13], A=A, E=E))
Elemen.append(tp.Element(node[13], node[14], A=A, E=E))
Elemen.append(tp.Element(node[11], node[14], A=A, E=E))
Elemen.append(tp.Element(node[8], node[14], A=A, E=E))
Elemen.append(tp.Element(node[11], node[12], A=A, E=E))
Elemen.append(tp.Element(node[12], node[14], A=A, E=E))
Elemen.append(tp.Element(node[12], node[1], A=A, E=E))
Elemen.append(tp.Element(node[14], node[1], A=A, E=E))
Elemen.append(tp.Element(node[14], node[16], A=A, E=E))
Elemen.append(tp.Element(node[15], node[16], A=A, E=E))
Elemen.append(tp.Element(node[1], node[16], A=A, E=E))
Elemen.append(tp.Element(node[16], node[20], A=A, E=E))
Elemen.append(tp.Element(node[2], node[20], A=A, E=E))
Elemen.append(tp.Element(node[1], node[2], A=A, E=E))
Elemen.append(tp.Element(node[1], node[3], A=A, E=E))
Elemen.append(tp.Element(node[1], node[22], A=A, E=E))
Elemen.append(tp.Element(node[2], node[3], A=A, E=E))
Elemen.append(tp.Element(node[3], node[20], A=A, E=E))
Elemen.append(tp.Element(node[3], node[21], A=A, E=E))
Elemen.append(tp.Element(node[3], node[22], A=A, E=E))
Elemen.append(tp.Element(node[20], node[21], A=A, E=E))
Elemen.append(tp.Element(node[21], node[22], A=A, E=E))
Elemen.append(tp.Element(node[14], node[15], A=A, E=E))
Elemen.append(tp.Element(node[16], node[2], A=A, E=E))
Elemen[1].make_element_K_with_help(node[17], node[18])
Elemen[2].make_element_K_with_help(node[18], node[19])
Elemen[3].make_element_K_with_help(node[4], node[18])
Elemen[4].make_element_K_with_help(node[4], node[19])
Elemen[5].make_element_K_with_help(node[4], node[17])
Elemen[6].make_element_K_with_help(node[7], node[17])
Elemen[7].make_element_K_with_help(node[5], node[19])
Elemen[8].make_element_K_with_help(node[4], node[5])
Elemen[9].make_element_K_with_help(node[4], node[7])
Elemen[10].make_element_K_with_help(node[6], node[19])
Elemen[11].make_element_K_with_help(node[5], node[6])
Elemen[12].make_element_K_with_help(node[5], node[7])
Elemen[13].make_element_K_with_help(node[6], node[7])
Elemen[14].make_element_K_with_help(node[6], node[8])
Elemen[15].make_element_K_with_help(node[6], node[15])
Elemen[16].make_element_K_with_help(node[8], node[15])
Elemen[17].make_element_K_with_help(node[7], node[8])
Elemen[18].make_element_K_with_help(node[7], node[9])
Elemen[19].make_element_K_with_help(node[8], node[9])
Elemen[20].make_element_K_with_help(node[8], node[10])
Elemen[21].make_element_K_with_help(node[9], node[10])
Elemen[22].make_element_K_with_help(node[10], node[11])
Elemen[23].make_element_K_with_help(node[10], node[13])
Elemen[24].make_element_K_with_help(node[8], node[13])
Elemen[25].make_element_K_with_help(node[11], node[13])
Elemen[26].make_element_K_with_help(node[13], node[14])
Elemen[27].make_element_K_with_help(node[11], node[14])
Elemen[28].make_element_K_with_help(node[8], node[14])
Elemen[29].make_element_K_with_help(node[11], node[12])
Elemen[30].make_element_K_with_help(node[12], node[14])
Elemen[31].make_element_K_with_help(node[1], node[12])
Elemen[32].make_element_K_with_help(node[1], node[14])
Elemen[33].make_element_K_with_help(node[14], node[16])
Elemen[34].make_element_K_with_help(node[15], node[16])
Elemen[35].make_element_K_with_help(node[1], node[16])
Elemen[36].make_element_K_with_help(node[16], node[20])
Elemen[37].make_element_K_with_help(node[2], node[20])
Elemen[38].make_element_K_with_help(node[1], node[18])
Elemen[39].make_element_K_with_help(node[1], node[19])
Elemen[40].make_element_K_with_help(node[1], node[22])
Elemen[41].make_element_K_with_help(node[2], node[19])
Elemen[42].make_element_K_with_help(node[3], node[20])
Elemen[43].make_element_K_with_help(node[3], node[21])
Elemen[44].make_element_K_with_help(node[3], node[22])
Elemen[45].make_element_K_with_help(node[20], node[21])
Elemen[46].make_element_K_with_help(node[21], node[22])
Elemen[47].make_element_K_with_help(node[14], node[15])
Elemen[48].make_element_K_with_help(node[2], node[16])

K1 = np.zeros(44 * 44)  # n*n total
K1_help = tp.make_K_help(44)  # n total
for i in range(1, len(Elemen)):
    K1 = tp.merge_K(K1, K1_help, Elemen[i])

K1_modified = np.array([])
new_K1_help = tp.make_K_help(32, 1, 1)  # show where is the modified K
for p, v in np.ndenumerate(K1_help):
    if v in new_K1_help:
        K1_modified = np.append(K1_modified, K1[p])

K1_modified = K1_modified.reshape([32, 32])  # shape the modified.


# for i in range(1, len(Elemen)):
#     for j in range(len(Elemen[i].K)):
#         if Elemen[i].K[j] - Element[i].K[j] < 1:
#             pass
#         else:
#             print(i)
#             print(Elemen[i])
#             print(Element[i])
#             break
if K1_modified.any() == K_modified.any():
    print(True)
else:
    print(False)

