from numpy import log, pi
from numpy import log10 as lg

k = 8.617333262 * 10 ** -5  # eV / K
k1 = 1.380649 * 10 ** -23 # J / K


def calculating_h(T, M1, M2, d1, d2, Ecv, p):
    Ea = 1.5 * k * T
    avg_share_transmit_energy = (4 * M1 * M2) / ((M1 + M2) ** 2)
    E02 = Ecv / 2
    Lambda = (4 * k1 * T) / ((pi * (d1 + d2) ** 2) * p * (1 + M2 / M1) ** 0.5)
    Nk = lg(Ea / E02) / lg(1 - avg_share_transmit_energy)
    print(Nk)
    print(Lambda)
    Lk = Lambda * Nk
    h = round(Lk * 100, 1) #cm
    return Lambda, h, Lk



