def multinomial_coefficient_c(n: int, k1: int, k2: int, k3: int):
    from math import factorial
    return factorial(n) // (factorial(k1) * factorial(k2) * factorial(k3))
