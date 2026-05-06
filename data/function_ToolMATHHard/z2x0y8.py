def solve_c_from_linear_relations(k1: float, k2: float, k3: float):
    # a - b = k1 (c + d), b = a + k2, d = c + k3
    # Substitute b and d into first equation
    # a - (a + k2) = k1 (c + c + k3)
    # -k2 = k1 (2c + k3)
    return (-k2 - k1*k3) / (2*k1)
