import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Target = "Cu"
Gases = ["O", "N", "Ne", "Ar", "Kr", "Xe"]
"""
Gas = "O"
constants = pd.read_csv("constants.csv", index_col=0)
current = list(map(str, constants.at[Gas, Target].split(',')))

a0 = 0.0529177
e = 1
if current[0] == "No such pair":
    pass
else:
    Z1 = int(current[0]) # Gas
    M1 = float(current[1]) # Gas
    Z2 = int(current[2]) # Target
    M2 = float(current[3]) # Target
    lamda = float(current[4])
    q = float(current[5])
    mu = float(current[6])
    Eth = int(float(current[7])) + 1


S01 = []
E01 = []
for Energy in range(Eth, 10000):
    aL = (((9 * np.pi ** 2) / 128) ** (1/3)) * a0 * ((Z1 ** (2/3) + Z2 ** (2/3)) ** (-1/2))

    epsilon = (aL * M2) / (Z1 * Z2 * e ** 2 * (M1 + M2))

    new_epsilon = epsilon * int(Energy)

    sn = ((0.5 * np.log(1 + 1.2288 * new_epsilon)) / (
                new_epsilon + 0.1728 * np.sqrt(
            new_epsilon) + 0.008 * new_epsilon ** 0.1504))

    S1 = q * sn * ((((int(Energy) / Eth) - 1) ** mu) / (lamda + ((int(Energy) / Eth) - 1) ** mu))
    E01.append(Energy)
    S01.append(S1)
"""
"""
#_____________________________________________________________________________
Gas = "N"
constants = pd.read_csv("constants.csv", index_col=0)
current = list(map(str, constants.at[Gas, Target].split(',')))
a0 = 0.0529177
e = 1
if current[0] == "No such pair":
    pass
else:
    Z1 = int(current[0]) # Gas
    M1 = float(current[1])/1000 # Gas
    Z2 = int(current[2]) # Target
    M2 = float(current[3])/1000 # Target
    lamda = float(current[4])
    q = float(current[5])
    mu = float(current[6])
    Eth = int(float(current[7])) + 1

S02 = []
E02 = []
for Energy in range(Eth, 100000):
    aL = (((9 * np.pi ** 2) / 128) ** (1/3)) * a0 * ((Z1 ** (2/3) + Z2 ** (2/3)) ** (-1/2))

    epsilon = (aL * M2) / (Z1 * Z2 * e ** 2 * (M1 + M2))

    new_epsilon = epsilon * Energy

    sn = (0.5 * np.log(1 + 1.2288 * new_epsilon)) / (
                new_epsilon + 0.1728 * np.sqrt(
            new_epsilon) + 0.008 * new_epsilon ** 0.1504)

    S1 = q * sn * ((((Energy / Eth) - 1) ** mu) / (lamda + ((Energy / Eth) - 1) ** mu))
    E02.append(Energy)
    S02.append(S1)
"""
"""
#_____________________________________________________________________________
Gas = "Ne"
constants = pd.read_csv("constants.csv", index_col=0)
current = list(map(str, constants.at[Gas, Target].split(',')))

a0 = 0.0529177
e = 1
if current[0] == "No such pair":
    pass
else:
    Z1 = int(current[0]) # Gas
    M1 = float(current[1]) # Gas
    Z2 = int(current[2]) # Target
    M2 = float(current[3]) # Target
    lamda = float(current[4])
    q = float(current[5])
    mu = float(current[6])
    Eth = int(float(current[7])) + 1

S03 = []
E03 = []
for Energy in range(Eth, 1000000):
    aL = (((9 * np.pi ** 2) / 128) ** (1/3)) * a0 * ((Z1 ** (2/3) + Z2 ** (2/3)) ** (-1/2))

    epsilon = (aL * M2) / (Z1 * Z2 * e ** 2 * (M1 + M2))

    new_epsilon = epsilon * int(Energy)

    sn = ((0.5 * np.log(1 + 1.2288 * new_epsilon)) / (
                new_epsilon + 0.1728 * np.sqrt(
            new_epsilon) + 0.008 * new_epsilon ** 0.1504))

    S1 = q * sn * ((((int(Energy) / Eth) - 1) ** mu) / (lamda + ((int(Energy) / Eth) - 1) ** mu))
    E03.append(Energy)
    S03.append(S1)
"""
"""
#_____________________________________________________________________________
Gas = "Ar"
constants = pd.read_csv("constants.csv", index_col=0)
current = list(map(str, constants.at[Gas, Target].split(',')))

a0 = 0.0529177
e = 1
if current[0] == "No such pair":
    pass
else:
    Z1 = int(current[0]) # Gas
    M1 = float(current[1]) # Gas
    Z2 = int(current[2]) # Target
    M2 = float(current[3]) # Target
    lamda = float(current[4])
    q = float(current[5])
    mu = float(current[6])
    Eth = int(float(current[7])) + 1

S04 = []
E04 = []
for Energy in range(Eth, 1000000):
    aL = (((9 * np.pi ** 2) / 128) ** (1/3)) * a0 * ((Z1 ** (2/3) + Z2 ** (2/3)) ** (-1/2))

    epsilon = (aL * M2) / (Z1 * Z2 * e ** 2 * (M1 + M2))

    new_epsilon = epsilon * int(Energy)

    sn = ((0.5 * np.log(1 + 1.2288 * new_epsilon)) / (
                new_epsilon + 0.1728 * np.sqrt(
            new_epsilon) + 0.008 * new_epsilon ** 0.1504))

    S1 = q * sn * ((((int(Energy) / Eth) - 1) ** mu) / (lamda + ((int(Energy) / Eth) - 1) ** mu))
    E04.append(Energy)
    S04.append(S1)
"""
"""
#_____________________________________________________________________________
Gas = "Kr"
constants = pd.read_csv("constants.csv", index_col=0)
current = list(map(str, constants.at[Gas, Target].split(',')))

a0 = 0.0529177
e = 1
if current[0] == "No such pair":
    pass
else:
    Z1 = int(current[0]) # Gas
    M1 = float(current[1]) # Gas
    Z2 = int(current[2]) # Target
    M2 = float(current[3]) # Target
    lamda = float(current[4])
    q = float(current[5])
    mu = float(current[6])
    Eth = int(float(current[7])) + 1

S05 = []
E05 = []
for Energy in range(Eth, 1000000):
    aL = (((9 * np.pi ** 2) / 128) ** (1/3)) * a0 * ((Z1 ** (2/3) + Z2 ** (2/3)) ** (-1/2))

    epsilon = (aL * M2) / (Z1 * Z2 * e ** 2 * (M1 + M2))

    new_epsilon = epsilon * int(Energy)

    sn = ((0.5 * np.log(1 + 1.2288 * new_epsilon)) / (
                new_epsilon + 0.1728 * np.sqrt(
            new_epsilon) + 0.008 * new_epsilon ** 0.1504))

    S1 = q * sn * ((((int(Energy) / Eth) - 1) ** mu) / (lamda + ((int(Energy) / Eth) - 1) ** mu))
    E05.append(Energy)
    S05.append(S1)
"""
"""
#_____________________________________________________________________________
Gas = "Xe"
constants = pd.read_csv("constants.csv", index_col=0)
current = list(map(str, constants.at[Gas, Target].split(',')))

a0 = 0.0529177
e = 1
if current[0] == "No such pair":
    pass
else:
    Z1 = int(current[0]) # Gas
    M1 = float(current[1]) # Gas
    Z2 = int(current[2]) # Target
    M2 = float(current[3]) # Target
    lamda = float(current[4])
    q = float(current[5])
    mu = float(current[6])
    Eth = int(float(current[7])) + 1

S06 = []
E06 = []
for Energy in range(Eth, 1000000):
    aL = (((9 * np.pi ** 2) / 128) ** (1/3)) * a0 * ((Z1 ** (2/3) + Z2 ** (2/3)) ** (-1/2))

    epsilon = (aL * M2) / (Z1 * Z2 * e ** 2 * (M1 + M2))

    new_epsilon = epsilon * int(Energy)

    sn = ((0.5 * np.log(1 + 1.2288 * new_epsilon)) / (
                new_epsilon + 0.1728 * np.sqrt(
            new_epsilon) + 0.008 * new_epsilon ** 0.1504))

    S1 = q * sn * ((((int(Energy) / Eth) - 1) ** mu) / (lamda + ((int(Energy) / Eth) - 1) ** mu))
    E06.append(Energy)
    S06.append(S1)
"""
#---------------------------------------------------------------------------------------------------
"CuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCuCu"
# N
S02_Cu = [0.06622, 0.15289, 0.26249, 0.32331, 0.41408, 0.46255, 0.65108, 0.89871, 1.48382, 1.70125, 2.02168, 2.20028, 2.40246,
          2.40246, 2.49006, 2.49006, 2.58086, 2.64897]
E02_Cu = [20.38481, 31.03047, 80.37287, 101.26852, 102.12312, 179.32863, 332.58129, 588.94263, 1110.76053, 1611.07882, 1624.67472,
          2094.92212, 2530.95645, 3109.57281, 3587.1086, 4137.97937, 5126.89018, 8259.82418]
S02_Cu_2 = [1.5992, 1.80982, 1.99552, 1.5992]
E02_Cu_2 = [5083.98639, 9979.01307, 14968.64476, 19139.66388]
S02_Cu_3 = [1.28159, 1.25271, 1.48382, 1.41309, 1.0926]
E02_Cu_3 = [19919.11656, 30513.29102, 39345.08709, 45387.29565, 49992.52926]
# Ne
S03_Cu = [0.35764, 0.73204, 1.01707, 1.63075, 1.79807, 1.9004]
E03_Cu = [93.94114, 184.00374, 286.79594, 676.89308, 788.2604, 949.83023]
S03_Cu_2 = [2.55578, 2.85496, 3.1173, 2.88298, 3.37066, 3.22046, 2.73664]
E03_Cu_2 = [10015.76916, 18468.14849, 24979.40657, 30577.46374, 38527.10915, 46059.70667, 50229.40448]
S03_Cu_3 = [2.07503, 2.73664, 2.41816, 1.94422, 1.82165, 1.24053, 1.31113, 0.90164, 0.97175, 0.66176, 0.52007, 0.67044]
E03_Cu_3 = [76260.43357, 96086.91137, 144358.85564, 195255.01163, 298789.24681, 389544.04474, 503879.44501, 585242.37817,
            705199.57809, 763004.97953, 879255.23654, 986955.21293]
# Ar
S04_Cu = [0.02567, 0.07071, 0.20211, 0.41367, 0.61991, 1.08164, 7.36772, 7.93537, 6.39865, 4.34982, 3.19669, 2.1812]
E04_Cu = [30.28975, 40.32843, 50.01879, 69.27182, 101.9088, 143.75356, 7845.43066, 10695.4012, 44630.8375, 298005.61874, 480615.13749, 979210.16332]
S04_Cu_2 = [0.95342, 1.21352, 1.7851, 2.42904, 3.17305, 3.31755, 4.03866, 4.89831, 6.64057]
E04_Cu_2 = [302.26176, 363.26117, 473.59879, 642.25849, 1008.9688, 1515.85246, 1965.92759, 4460.74024, 5153.88871]
S04_Cu_3 = [5.43468, 5.85339, 6.21148, 5.53646, 4.6676, 4.75502, 4.30166, 3.9351]
E04_Cu_3 = [6275.8616, 9256.9726, 14812.22969, 26188.5416, 43588.35085, 63288.23625, 88807.3488, 134831.12121]
# Kr
S05_Cu = [0.03963, 0.12021, 0.19547, 0.3238, 0.93938, 1.39731, 1.99533, 2.7557]
E05_Cu = [24.4858, 55.41319, 76.54133, 99.52841, 196.48953, 301.46903, 396.14651, 595.16178]
S05_Cu_2 = [4.70238, 6.49434, 6.89164, 7.76063, 9.4125, 9.98832, 10.13769]
E05_Cu_2 = [2002.40119, 3008.36337, 3870.96588, 6065.22219, 10015.76916, 14466.24578, 19773.18558]
S05_Cu_3 = [12.29554, 13.59138, 12.66605, 12.85547, 11.75999, 10.91876, 9.98832, 9.55327, 8.11404, 7.31324,
            7.64628, 6.39865, 7.09931]
E05_Cu_3 = [77065.73307, 101002.92283, 152143.58647, 201506.15731, 253894.4951, 305935.27999, 402015.41001, 506532.90654,
            603979.08218, 722065.57858, 819070.28011, 919398.20102, 1.04018E6]
# Xe
S06_Cu = [3.39039E-4, 0.0013, 0.00373, 0.00888, 0.01771, 0.03045, 0.06373, 0.10097, 0.14259, 0.21448, 0.41367, 0.54846]
E06_Cu = [25.20344, 30.36939, 35.73945, 39.69797, 45.03112, 50.01879, 59.48493, 70.92856, 79.6166, 89.36884, 123.76832, 149.13712]
S06_Cu_2 = [9.84114, 11.98024, 13.4409, 14.36941, 16.60715, 19.91904]
E06_Cu_2 = [4037.08151, 5923.55079, 8011.99881, 12164.1598, 15734.47257, 22785.79751]
S06_Cu_3 = [21.61354, 23.45218, 25.92383, 23.45218, 22.01833, 19.62554, 17.49279, 16.36245, 14.10524, 12.38714, 12.80785,
            11.041, 9.84114]
E06_Cu_3 = [75463.54906, 102069.49955, 128605.91656, 153346.96412, 207412.02977, 249925.29821, 304332.64473, 415977.02354,
            518647.46887, 624954.70231, 727776.74656, 825548.70547, 1.01855E6]

"TiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTiTi"
# Ar
S04_Ti = [0.01931, 0.0479, 0.07604, 0.11493, 0.1556, 0.2113, 0.26743, 0.31356, 0.33849, 0.4258, 0.56252]
E04_Ti = [60.14466, 81.73513, 98.95505, 123.63837, 147.81143, 199.61009, 246.27672, 298.16218, 346.12548, 400.11956, 611.64066]
S04_Ti_2 = [1.19047, 1.41731, 1.60185, 1.77748, 1.88965, 1.99055, 2.02743]
E04_Ti_2 = [3000.4734, 3901.58323, 4988.76103, 6014.46609, 6894.51387, 7919.95343, 9097.90936]
# N
S02_Ti = [0.5195, 0.5962, 0.52751]
E02_Ti = [396.7712, 500.97669, 708.54096]
S02_Ti_2 = [0.56425, 0.62995, 0.67382, 0.69263, 0.74087, 0.74087, 0.74999]
E02_Ti_2 = [1500.01254, 2021.42175, 2483.55049, 2969.11991, 3542.17548, 4155.4029, 4693.88934]
S02_Ti_3 = [0.63771]
E02_Ti_3 = [5448.96312]

# Ne
S03_Ti = [0.08487, 0.12908, 0.22017, 0.27402, 0.31295, 0.37652, 0.38949, 0.46015]
E03_Ti = [101.4815, 152.22352, 202.14218, 254.16134, 298.78925, 351.25332, 401.80432, 602.71152]

# Xe
S06_Ti = [2.1493E-4, 8.14017E-4, 0.0025, 0.00519, 0.01374, 0.02112, 0.04309]
E06_Ti = [29.62889, 39.59385, 49.78291, 59.76678, 76.904, 99.16316, 149.68645]
S06_Ti_2 = [0.13249, 0.23652, 0.39306, 0.39951, 0.52007]
E06_Ti_2 = [202.5673, 294.42732, 393.45087, 507.33167, 579.12688]


"MoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMoMo"
# Ar
S04_Mo = [0.02644, 0.09536, 0.13292, 0.41139, 0.58665, 0.68366, 0.85309, 0.97492]
E04_Mo = [56.70869, 74.36188, 94.8833, 193.82454, 285.29356, 379.64664, 483.39991, 590.18124]
S04_Mo_2 = [0.87276, 1.16233, 1.65751, 1.89423, 2.41816, 2.41816, 2.52271, 2.36367, 2.41816, 2.25834]
E04_Mo_2 = [1076.30239, 2134.90995, 3229.41671, 4060.47314, 6233.15647, 8417.48753, 12921.52787, 16246.74722, 21304.29432, 23515.29141]
S04_Mo_3 = [0.79931, 0.97492, 1.58882, 2.21465, 3.22046]
E04_Mo_3 = [199.61009, 497.82911, 1016.94923, 2573.8542, 10126.85176]

# Kr
S05_Mo = [0.07114, 0.32016, 0.5338, 0.74164, 0.88998, 1.06451]
E05_Mo = [99.16316, 200.87214, 300.04734, 400.96105, 491.59317, 602.71152]
S05_Mo_2 = [2.04818, 2.36367, 2.93985, 3.60919, 3.55091, 3.8772, 4.16511, 4.26113]
E05_Mo_2 = [3000.4734, 4001.19559, 6014.46609, 7837.19376, 9792.10163, 13704.44063, 17820.19322, 22171.90044]
S05_Mo_3 = [0.68589, 1.60442, 1.89423, 2.87361, 4.83807, 5.78687]
E05_Mo_3 = [213.491, 517.0156, 1047.30456, 2639.56795, 10561.42764, 20993.2797]

# Ne
S03_Mo = [0.10107, 0.23881, 0.33437, 0.39204, 0.48717, 0.55229]
E03_Mo = [99.79013, 200.02989, 298.16218, 397.60566, 499.92529, 602.71152]
S03_Mo_2 = [0.20937, 0.24398, 0.36317, 0.59256, 0.82968, 0.94635]
E03_Mo_2 = [99.79013, 150.00125, 300.67837, 993.71712, 3038.53493, 10084.39005]
S03_Mo_3 = [0.39566, 0.5962, 1.09607, 1.47032, 1.86096, 2.03988]
E03_Mo_3 = [209.9328, 514.84777, 1042.91323, 2606.50399, 10561.42764, 20905.25524]

# Xe
S06_Mo = [1.47648E-4, 2.89032E-4, 4.73481E-4, 6.20806E-4, 0.00126, 0.0019, 0.00208, 0.00326, 0.00522, 0.00766, 0.01023,
          0.01585, 0.02101, 0.03184, 0.04113, 0.04206, 0.05453, 0.06663, 0.07787]
E06_Mo = [25.41613, 29.81622, 30.19444, 34.90464, 40.43448, 39.67712, 45.29204, 50.09767, 49.78291, 58.77066, 69.81972,
          79.19953, 89.83946, 100.8439, 100.21031, 123.63837, 148.43381, 175.23189, 202.5673]
S06_Mo_2 = [0.0973, 0.29185, 0.59291, 0.69292, 0.73258, 0.77452]
E06_Mo_2 = [149.3723, 197.52426, 296.91199, 402.64935, 483.39991, 603.97908]
S06_Mo_3 = [2.66518, 2.8812, 3.69451, 4.88016, 5.41454, 5.78859, 6.18847, 6.39865, 7.1522, 7.56162]
E06_Mo_3 = [2099.32797, 3109.57281, 4243.62722, 6220.07499, 8488.52275, 10320.15289, 12337.88949, 16626.57975, 20256.73017, 23713.73706]

# N
S02_Mo = [0.04414, 0.09176, 0.15571, 0.22017, 0.28568, 0.32373, 0.38146, 0.41678, 0.45419, 0.39666, 0.47229, 0.43339]
E02_Mo = [300.67837, 600.18436, 1099.15362, 1597.59669, 2099.32797, 3051.3291, 4060.47314, 5105.39322, 6065.22219, 7055.70064,
          7235.8416, 8225.19088]


plt.plot(E06, S06)
plt.scatter(E06_Cu, S06_Cu, color='red')
plt.scatter(E06_Cu_2, S06_Cu_2, color='green')
plt.scatter(E06_Cu_3, S06_Cu_3, color='blue')
plt.yscale("log")
plt.xscale("log")
plt.ylabel("Y, атом/ион")
plt.xlabel("E, эВ")
plt.legend(["Расчёт", "Эксперимент 1", "Эксперимент 2", "Эксперимент 3"])
plt.ylim(top=50, bottom=10**-4)
plt.show()
