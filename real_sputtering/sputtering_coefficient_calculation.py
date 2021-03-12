import numpy as np
import pandas as pd


def calculation(Target, Gas, Energy):
    constants = pd.read_csv("constants.csv", index_col=0)
    current = list(map(str, constants.at[Gas, Target].split(',')))

    a0 = 0.0529177
    e = 1
    if current[0] == "No such pair":
        return current[0]
    else:
        Z1 = int(current[0]) # Gas
        M1 = float(current[1]) # Gas
        Z2 = int(current[2]) # Target
        M2 = float(current[3]) # Target
        lamda = float(current[4])
        q = float(current[5])
        mu = float(current[6])
        Eth = float(current[7])
        d1 = (int(current[8]) * 10 ** (-12)) * 2  # Target
        d2 = (int(current[9]) * 10 ** (-12)) * 2  # Gas
        Ecv = float(current[10]) # энергия связи

        aL = (((9 * np.pi ** 2) / 128) ** (1/3)) * a0 * ((Z1 ** (2/3) + Z2 ** (2/3)) ** (-1/2))

        epsilon = (aL * M1) / (Z1 * Z2 * e ** 2 * (M1 + M2))

        new_epsilon = epsilon * int(Energy)

        sn = ((0.5 * np.log(1 + 1.2288 * new_epsilon)) / (
                new_epsilon + 0.1728 * np.sqrt(
            new_epsilon) + 0.008 * new_epsilon ** 0.1504))

        S1 = q * sn * ((((int(Energy) / Eth) - 1) ** mu) / (lamda + ((int(Energy) / Eth) - 1) ** mu))

        return S1, M1, M2, d1, d2, Ecv


