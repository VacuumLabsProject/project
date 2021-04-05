from numpy import sqrt, exp


# tube's viscous mode conductivity
def calculating_U_viscous(d, l, P1, P2):
    Ulong = 1360 * ((d ** 4) / l) * ((P1 + P2) / 2)
    alpha = P1 / P2
    if alpha >= 0.528:
        Uhole = 602 * d ** 2 * ((alpha ** 0.714) / (1 - alpha))
    elif alpha >= 0.1:
        Uhole = 157 * d ** 2 * (1 / (1 - alpha))
    else:
        Uhole = 157 * d ** 2
    Ushort = (sqrt(1 + 0.12 * Ulong * ((P2 - P1) / l)) - 1) / (
                0.06 * ((P2 - P1) / l))
    Uvisc = choosing_U_viscous(d, l, Ulong, Ushort, Uhole)
    return Uvisc


def choosing_U_viscous(d, l, Ulong, Ushort, Uhole):
    if l / d > 100:
        U = Ulong
    elif l / d > 0.1:
        U = Ushort
    else:
        U = Uhole
    return U


# tube's molecular mode conductivity
def calculatung_U_molecular(d, l):
    Ulong = 121 * d ** 3 / l
    Uhole = 91 * d ** 2
    K = 1 / (1 + 0.752 * (l / d))
    a = (15 * (l / d) + 12 * (l / d) ** 2) / (
                20 + 38 * (l / d) + 12 * (l / d) ** 2)
    if l / d > 20:
        Ushort = Uhole * K
    else:
        Ushort = Ulong * a
    Umolec = choosing_U_molecular(d, l, Ulong, Ushort, Uhole)
    return Umolec


def choosing_U_molecular(d, l, Ulong, Ushort, Uhole):
    if l / d > 100:
        U = Ulong
    elif l / d >= 0.1:
        U = Ushort
    else:
        U = Uhole
    return U


def calculating_U_total(d, l, P1, P2):
    Uvisc = calculating_U_viscous(d, l, P1, P2)
    Umolec = calculatung_U_molecular(d, l)
    pd = ((P1 + P2) / 2) * d
    Z = (1 + 196 * pd) / (1 + 249 * pd)
    if pd >= 0.63:
        U = Uvisc
    elif pd > 6.3 * 10 ** -3:
        U = Uvisc * Z * Umolec
    else:
        U = Umolec
    return U


Un = []


def calculating_pressure(Pcurr, t, p02, name, S01, S02,
                         V, Qin1, Qin2,
                         d1, l1, d2, l2):
    if name == "forvacuum":
        Ucurr = calculating_U_total(d1, l1, 0, Pcurr)
        Un.append(Ucurr)
        Seff = (S01 * Ucurr) / (S01 + Ucurr)
        Pmin = Qin1 / Seff
        Pcurr = Pmin + (100000 - Pmin) * exp(-0.07 * (Seff / V) * t)
        # print Un
        return Pcurr

    elif name == "turbomolec":
        Ucurr = calculating_U_total(d2, l2, 0, Pcurr)
        Un.append(Ucurr)
        Seff = (S02 * Ucurr) / (S02 + Ucurr)
        Pmin = Qin2 / Seff
        Pcurr = Pmin + (p02 - Pmin) * exp(-0.01 * (Seff / V) * t)
        # print(Un)
        return Pcurr


def calculate_overflow(t, pcur):
    P = 100000 - (100000 - pcur) * exp(-0.5 * t)
    return P