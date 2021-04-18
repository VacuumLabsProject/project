import scipy.integrate as integrate
from numpy import sqrt
import matplotlib.pyplot as plt

# old formulae for magnetron
"""
Jnap_0 = Jm * (1 + (self.r_ring / self.h) ** 2) ** (-2)
Jnap_r = Jm * ((1 + (self.r / self.h) ** 2 + (self.r_ring / self.h) ** 2) / (
                    (1 - (self.r / self.h) ** 2 + (self.r_ring / self.h) ** 2) ** 2 + 4 * (
                        self.r_ring / self.h) ** 2) ** (3 / 2))
"""


def integral(r):
    ro = 0 # center (l)
    l = 0.1 # m (h)
    #ro = [0, 0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.08, 0.1, 0.15, 0.2, 0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 10]

    d = (2 * (l ** 2)) * (((l ** 2) + (ro ** 2) + (r ** 2)) / (((((l ** 2) + (ro ** 2) + (r ** 2)) ** 2) + ((2 * ro * l) ** 2)) ** 1.5)) * r
    return d


d = [0.08256880733944952, 0.08250745278590971, 0.08232387691064028,
     0.0810590152393089, 0.07681285922788116, 0.06321592332873185,
     0.02661063466196855, 0.01208690335666116, 0.00786358745706335,
     0.003351357493774276, 0.001701319169931538, 0.0009491134429920718,
     0.0001079473333429291, 2.482119107116725e-05, 8.32106063488716e-06,
     1.715845748619952e-06, 5.513251594920036e-07]
"""
l = 0.1
r = 0.03
# ro = 2
ro = [0, 0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.08, 0.1, 0.15, 0.2, 0.25, 0.5, 0.75, 1, 1.5, 2]
Jnap_r = []
for i in ro:
    Jnap_r.append((1 / 2) * (1 - (
                    (1 + ((i / l) ** 2) - ((r / l) ** 2)) / sqrt((1 - (
                        i / l) ** 2 + (r / l) ** 2) ** 2 + 4 * (i / l) ** 2))))



mistake = []
for j in range(len(ro)):
    mistake.append((ro[j], abs(d[j] - Jnap_r[j])))
#print(mistake)
"""
result = integrate.quad(integral, 0.0224, 0.0226)
"""
print(result)
print(Jnap_r[7])
a = result[0] - Jnap_r[7]
print(abs(a))
plt.plot(ro, Jnap_r, ro, d)
plt.grid()
plt.show()
"""
ro = 0
l = 0.1
r = 0.0225
Jnap_2 = (1 * ((1 + (ro / l) ** 2 + (r / l) ** 2) / (
            (1 - (ro / l) ** 2 + (
                        r / l) ** 2) ** 2 + 4 * (
                    r / l) ** 2) ** (3 / 2)))

print(Jnap_2)
print(result)

