def linear_combination_of_equations(a1: float, b1: float, c1: float, a2: float, b2: float, c2: float, m: float, n: float):
    # Compute m*(a1 x + b1 y = c1) + n*(a2 x + b2 y = c2)
    return m*c1 + n*c2
