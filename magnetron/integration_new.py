import scipy.integrate as integrate
from numpy import sqrt, pi


def integral(s):
    J = 1
    h = 0.1 # высота
    l = 0
    d = ((J * h ** 2) / pi) * \
        ((h ** 2 + l ** 2 + s ** 2) /
         ((h ** 2 + l ** 2 + s ** 2) ** 2 +
          (2 * l * h) ** 2) ** 1.5) * s
    return d


h = 0.1 # высота
l = 0
r = 0.0225
Jm = 1
old_d = Jm * ((1 + (l / h) ** 2 + (r / h) ** 2) /
              ((1 - (l / h) ** 2 + (r / h) ** 2) ** 2 +
               (2 * r / h) ** 2) ** (3 / 2))
print(old_d)
result = integrate.quad(integral, 0.022, 0.023)
result2 = integrate.quad(integral, 0.02, 0.025)
result3 = integrate.quad(integral, 0.0224, 0.0226)
print(result)
print(result2)
print(result3)
