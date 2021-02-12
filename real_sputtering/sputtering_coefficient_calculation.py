import numpy as np


def no_such_pair(a):
    a.append("No such pair")
    return a


def calculation(Target, Gas, Energy):
    MoO = [8, 15.999, 42, 95.95, 0.1762, 2.1069, 2.4821, 23.9169]
    MoN = [7, 14.007, 42, 95.95, 0.1157, 1.79, 1.8032, 28.2561]
    MoNe = [2, 4.0026, 42, 95.95, 0.2205, 2.8995, 2.6514, 23.617]
    MoAr = [18, 39.948, 42, 95.95, 0.1339, 6.3606, 1.9562, 28.2149]
    MoKr = [36, 83.798, 42, 95.95, 0.1412, 11.9419, 1.6911, 38.6337]
    MoXe = [54, 131.29, 42, 95.95, 0.2401, 32.5719, 1.6694, 47.4030]

    CuN = [7, 14.007, 29, 63.546, 0.1595, 3.4102, 2.1567, 15.6557]
    CuNe = [2, 4.0026, 29, 63.546, 0.2009, 5.0380, 2.4014, 15.5801]
    CuAr = [18, 39.948, 29, 63.546, 1.9417, 14.8712, 2.3907, 12.9166]
    CuKr = [36, 83.798, 29, 63.546, 0.3072, 16.6183, 2.3257, 21.3482]
    CuXe = [54, 131.29, 29, 63.546, 0.2782, 24.4581, 2.2393, 23.6265]

    TiN = [7, 14.007, 22, 47.867, 0.2321, 1.8168, 2.0297, 16.5403]
    TiNe = [2, 4.0026, 22, 47.867, 0.2317, 2.6253, 1.8113, 19.564]
    TiAr = [18, 39.948, 22, 47.867, 0.3152, 4.8957, 1.8291, 25.019]
    TiKr = [36, 83.798, 22, 47.867, 0.4445, 8.4878, 2.2691, 30.9784]
    TiXe = [54, 131.29, 22, 47.867, 0.2234, 12.989, 1.8943, 39.6382]

    a0 = 0.0529177
    e = 1
    d1 = 0 # Gas
    d2 = 0 # Target

    current = []
    if Target == "Mo":
        d1 = (145 * 10 ** -12) * 2
        if Gas == "O":
            current = MoO
            d2 = (60 * 10 ** -12) * 2
        elif Gas == "N":
            current = MoN
            d2 = (65 * 10 ** -12) * 2
        elif Gas == "Ne":
            current = MoNe
            d2 = (38 * 10 ** -12) * 2
        elif Gas == "Ar":
            current = MoAr
            d2 = (71 * 10 ** -12) * 2
        elif Gas == "Kr":
            current = MoKr
            d2 = (88 * 10 ** -12) * 2
        elif Gas == "Xe":
            current = MoXe
            d2 = (108 * 10 ** -12) * 2

    elif Target == "Cu":
        d1 = (135 * 10 ** -12) * 2
        if Gas == "O":
            no_such_pair(current)
            return current[0]
        elif Gas == "N":
            current = CuN
            d2 = (65 * 10 ** -12) * 2
        elif Gas == "Ne":
            current = CuNe
            d2 = (38 * 10 ** -12) * 2
        elif Gas == "Ar":
            current = CuAr
            d2 = (71 * 10 ** -12) * 2
        elif Gas == "Kr":
            current = CuKr
            d2 = (88 * 10 ** -12) * 2
        elif Gas == "Xe":
            current = CuXe
            d2 = (108 * 10 ** -12) * 2

    elif Target == "Ti":
        d1 = (140 * 10 ** -12) * 2
        if Gas == "O":
            no_such_pair(current)
            return current[0]
        elif Gas == "N":
            current = TiN
            d2 = (65 * 10 ** -12) * 2
        elif Gas == "Ne":
            current = TiNe
            d2 = (38 * 10 ** -12) * 2
        elif Gas == "Ar":
            current = TiAr
            d2 = (71 * 10 ** -12) * 2
        elif Gas == "Kr":
            current = TiKr
            d2 = (88 * 10 ** -12) * 2
        elif Gas == "Xe":
            current = TiXe
            d2 = (108 * 10 ** -12) * 2

    Z1 = int(current[0]) # Gas
    M1 = float(current[1]) # Gas
    Z2 = int(current[2]) # Target
    M2 = float(current[3]) # Target
    lamda = float(current[4])
    q = float(current[5])
    mu = float(current[6])
    Eth = float(current[7])

    aL = (((9 * np.pi ** 2) / 128) ** (1/3)) * a0 * ((Z1 ** (2/3) + Z2 ** (2/3)) ** (-1/2))

    epsilon = (aL * M1) / (Z1 * Z2 * e ** 2 * (M1 + M2))

    new_epsilon = epsilon * int(Energy)

    sn = ((0.5 * np.log(1 + 1.2288 * new_epsilon)) / (
                new_epsilon + 0.1728 * np.sqrt(
            new_epsilon) + 0.008 * new_epsilon ** 0.1504))

    S1 = q * sn * ((((int(Energy) / Eth) - 1) ** mu) / (lamda + ((int(Energy) / Eth) - 1) ** mu))

    return S1, Z1, M1, Z2, M2, d1, d2


