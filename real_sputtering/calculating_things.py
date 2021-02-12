from numpy import log, pi
from numpy import log10 as lg

k = 8.617333262 * 10 ** -5  # eV / K
k1 = 1.380649 * 10 ** -23 # J / K


def calculating_h(T, Z1, M1, Z2, M2, d1, d2, material):
    if material == "Cu":
        Ecv = 3.5
    elif material == "Ti":
        Ecv = 4.855
    elif material == "Mo":
        Ecv = 6.81
    Ea = 1.5 * k * T
    avg_share_transmit_energy = (4 * M1 * M2) / ((M1 + M2) ** 2)
    E02 = Ecv / 2
    Lambda = (4 * k1 * T) / ((pi * (d1 + d2) ** 2) * 1 * (1 + M2 / M1) ** 0.5)
    Nk = lg(Ea / E02) / lg(1 - avg_share_transmit_energy)
    Lk = Lambda * Nk
    h = round(Lk * 1.5 * 100, 1)
    return h



