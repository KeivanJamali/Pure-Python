from sympy import *

p_0, w, w_1, w_2, m, l, E, I, t = symbols("p_0, omega, omega_1, omega_2, m, l, E, I, t")
k_1, k_2 = 0.6097*(E*I/l**3), 24*(E*I/l**3)
k = Matrix([[k_1+k_2, -k_2], [-k_2, k_2]])
m_total = Matrix([[m, 0], [0, 2*m]])
phi = Matrix([[0.9833, -2.034], [1, 1]])
q = Matrix([(p_0 * sin(w*t))/(2.9669*m*(w_1**2 - w**2)), (p_0 * sin(w*t))/(6.1372*m*(w_2**2 - w**2))])

u = Matrix([[0], [0]])
for i in range(2):
    u += phi.col(i) * q[i]

# we have u

f = Matrix([[0], [0]])
w_s = Matrix([[w_1], [w_2]])
for i in range(2):
    f += (w_s[i]**2) * m_total * phi.col(i) * q[i]

# we have f
