from numpy import e
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import numpy as np


# константы не изменяемые
k_0 = 0.008
m = 0.786
R = 0.35
T_w = 2000
T_0 = 10000
c = 3e10
_p = 4
z_max = 1
z_min = 0
SHAG_RK = 1e-4
EPS = 1e-6

def T(z):
        return (T_w - T_0) * (z ** _p) + T_0

def k(z):
    return k_0 * ((T(z) / 300) ** 2)

def u_p(z):
    return (3.084e-4) / (e ** ((4.799e+4) / T(z)) - 1)

def U_z(z, f):
    return -(3 * R * f * k(z)) / c

def F_z(z, f, u):
    if abs(z - 0) < 1e-4:
        return ((R * c) / 2) * k(z) * (u_p(z) - u)
    else:
        return R * c * k(z) * (u_p(z) - u) - (f / z)

def divF(z, u):
    return c * k(z) * (u_p(z) - u)




def k_n(z):
        return c / (3 * R * k(z))

def half_kappa(z):
    return (k_n(z + SHAG_RK / 2) + k_n(z - SHAG_RK / 2)) / 2

def f_n(z):
    return c * k(z) * u_p(z)

def p_n(z):
    return c * k(z)

def V_n(z):
    return ((z + SHAG_RK / 2)**2 - (z - SHAG_RK / 2)**2) / 2

def V_n_plus(z):
    return ((z + SHAG_RK / 2)**2 - (z)**2) / 2

def V_n_minus(z):
    return ((z)**2 - (z - SHAG_RK / 2)**2) / 2


# Простая аппроксимация
def approc_plus_half(func, n):
    return (func(n) + func(n + SHAG_RK)) / 2

def approc_minus_half(func, n):
    return (func(n - SHAG_RK) + func(n)) / 2

def A(z):
    return (z - SHAG_RK / 2) * (half_kappa(z - SHAG_RK / 2)) #/ (R * SHAG_RK) #/ R

def C(z):
    return ((z + SHAG_RK / 2) * half_kappa(z + SHAG_RK / 2)) # / (R * SHAG_RK) #/ R

def B(z):
    return A(z) + C(z) + p_n(z) * z * SHAG_RK ** 2 * R #* V_n(z)) #* z * SHAG_RK * SHAG_RK * R )

def D(z):
    return f_n(z) * z * SHAG_RK ** 2 * R # V_n(z) #* z * SHAG_RK * SHAG_RK * R )


# Краевые условия
# При х = 0
def left_boundary_condition(z0, F0, h):
    K0 = -half_kappa(z0 + h / 2) * (z0 + h / 2) + c * R * h * h / 8 * k(z0 + h / 2) * (z0 + h / 2)
    M0 = half_kappa(z0 + h / 2) * (z0 + h / 2) + c * R * h * h / 8 * k(z0 + h / 2) * (z0 + h / 2)
    P0 = c * R * h * h / 4 * k(z0 + h / 2) * u_p(z0 + h / 2) * (z0 + h / 2)

    return K0, M0, P0


# При x = N
def right_boundary_condition(z, h):
    KN = half_kappa(z - h / 2) * (z - h / 2) + m * c * z * h / 2 + c * R * h * h / 8 * k(z - h / 2) * (z - h / 2) + R * c * h * h * k(z) / 4
    MN = -half_kappa(z - h / 2) * (z - h / 2) + c * R * h * h / 8 * k(z - h / 2) * (z - h / 2)
    PN = c * R * h * h / 4 * (k(z - h / 2) * u_p(z - h / 2) * (z - h / 2) + k(z) * u_p(z))

    return KN, MN, PN


def right_hod():
    # Прямой ход
    h = SHAG_RK
    K0, M0, P0 = left_boundary_condition(0, 0, SHAG_RK)
    KN, MN, PN = right_boundary_condition(1, SHAG_RK)  
    
    eps = [0, -K0 / M0]
    eta = [0, P0 / M0]
    x = h
    n = 1

    while x < z_max + h / 2:
        eps.append(C(x) / (B(x) - A(x) * eps[n]))
        eta.append((A(x) * eta[n] + D(x)) / (B(x) - A(x) * eps[n]))
        n += 1
        x += h

    # Обратный ход
    u = [0] * (n)
    
    u[n-1] = (PN - MN * eta[n]) / (KN + MN * eps[n]) 

    for i in range(n - 2, -1, -1):
        u[i] = eps[i + 1] * u[i + 1] + eta[i + 1]# /8.001

    return u


def center_formula(y, z, h):
    res = []
    res.append((-3 * y[0] + 4 * y[1] - y[2]) / 2 / h)

    for i in range(1, len(y) - 1):
        r = (y[i + 1] - y[i - 1]) / 2 / h
        res.append(r)

    res.append((3 * y[-1] - 4 * y[-2] + y[-3]) / 2 / h)

    return res


def F_res_deriv(u, z):
    f = [0]
    u_res = center_formula(u, z, SHAG_RK)

    for i in range(1, len(z)):
        r = -c / 3 / R / k(z[i]) * u_res[i]
        f.append(r)

    return f


def F_res_integ(z, un, un1, f):
    return half_kappa(z - SHAG_RK / 2) * (un - un1) / SHAG_RK




# График
def draw():
    name = ['U(z)', 'F(z)']
    u_res = right_hod()
    z_res = [i for i in np.arange(0, 1 + SHAG_RK, SHAG_RK)]
    
    f_res = [0] * len(z_res)
    up_res = [0] * len(z_res)
    divF_ = [0] * len(z_res)

    f3_res = F_res_deriv(u_res, z_res)

    for i in range(0, len(z_res) - 1):
        up_res[i] = u_p(z_res[i])
        divF_[i] = divF(z_res[i], u_res[i])

    for i in range(1, len(z_res)):
        f_res[i] = F_res_integ(z_res[i], u_res[i - 1], u_res[i], f_res[i - 1])

    tb = PrettyTable()
    tb.add_column("Z", z_res)
    tb.add_column("F", f_res)
    tb.add_column("F deriv", f3_res)
    tb.add_column("U", u_res)
    tb.add_column("divF", divF_)

    with open('result.txt', 'w') as f:
        f.write(str(tb))

    plt.subplot(2, 2, 1)
    plt.plot(z_res, u_res, 'r', label='u')
    plt.plot(z_res, up_res, 'g', label='u_p')
    plt.legend()
    plt.title(name[0])
    plt.grid()

    plt.subplot(2, 2, 2)
    plt.plot(z_res, f_res, 'g')
    plt.title(name[1])
    plt.grid()

    plt.subplot(2, 2, 3)
    plt.plot(z_res, divF_, 'b')
    plt.title("divF")
    plt.grid()

    plt.subplot(2, 2, 4)
    plt.plot(z_res, f3_res, 'g')
    plt.title("F(z) deriv")
    plt.grid()
    
    plt.show()



def main():    
    print(draw())

if __name__ == "__main__":
    main()
