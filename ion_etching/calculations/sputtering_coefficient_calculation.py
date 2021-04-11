import numpy as np
import pandas as pd


def calculation(Target, Gas, Energy):
    constants = pd.read_csv("../resources/material_constants.csv", index_col=0)
    current = list(map(str, constants.at[Gas, Target].split(',')))

    a0 = 0.0529177 * 10 ** -9
    e = 1.6 * 10 ** -19
    eps0 = 8.85 * 10 ** -12
    if current[0] == "No such pair":
        return current[0]
    else:
        Z1 = int(current[0])  # Gas
        M1 = float(current[1]) * 10 ** -3  # Gas
        Z2 = int(current[2])  # Target
        M2 = float(current[3]) * 10 ** -3  # Target
        lamda = float(current[4])
        q = float(current[5])
        mu = float(current[6])
        Eth = float(current[7])
        Ecv = float(current[10])  # энергия связи

        aL = (((9 * np.pi ** 2) / 128) ** (1 / 3)) * a0 * ((Z1 ** (2 / 3) + Z2 ** (2 / 3)) ** (-1 / 2))

        # epsilon = (aL * M1) / (Z1 * Z2 * e ** 2 * (M1 + M2))
        F = (4 * np.pi * eps0 * aL * M2) / (Z1 * Z2 * e * (M1 + M2))

        new_epsilon = F * int(Energy)

        sn = ((0.5 * np.log(1 + 1.2288 * new_epsilon)) / (
                new_epsilon + 0.1728 * np.sqrt(
            new_epsilon) + 0.008 * new_epsilon ** 0.1504))
        S1 = q * sn * ((((int(Eth) / Ecv) - 1) ** mu) / (lamda + ((int(Eth) / Ecv) - 1) ** mu))
        return S1, M2
