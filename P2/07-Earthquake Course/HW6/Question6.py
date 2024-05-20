from sympy import *
for z in range(2):
    kg, kN, m, s, ton = symbols("kg, kN, m, s, ton")
    a_1 = 0.8
    a_2 = 0.68
    mass = (4+2*a_2) # * ton
    k = (1200+1100*a_1) # * kN/m

    k_1 = 3*k
    k_2 = 3*k
    k_3 = k if z==0 else 2*k
    mass_total = Matrix([[mass, 0, 0], [0, 2*mass, 0], [0, 0, mass]])
    k_total = Matrix([[k_1+k_2, -k_2, 0], [-k_2, k_2+k_3, -k_3], [0, -k_3, k_3]])

    w_n = symbols("w_n")
    result_1 = det(k_total - mass_total * w_n **2)
    answers_to_result_1 = solveset(result_1, w_n)

    w = [answers_to_result_1.args[3], answers_to_result_1.args[4], answers_to_result_1.args[5]]
    pprint(w)

    phi_11, phi_21, phi_22, phi_12, phi_13, phi_23 = symbols(
        "phi_11, phi_21, phi_22, phi_12, phi_31, phi_23"
    )
    phi = Matrix([[phi_11, phi_12, phi_13], [phi_21, phi_22, phi_23], [1, 1, 1]])

    for i in range(3):
        f1 = k_total - (w[i] ** 2) * mass_total
        f2 = f1 * phi.col(i)
        phi_1v = solveset(f2[2], phi.col(i)[1]).args[0]
        phi_2v = solveset(f2[0].subs(phi.col(i)[1], phi_1v), phi.col(i)[0]).args[0]
        phi = phi.subs(phi.col(i)[1], phi_1v)
        phi = phi.subs(phi.col(i)[0], phi_2v)

    pprint(phi)