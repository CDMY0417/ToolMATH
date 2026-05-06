def expand_circle_equation(h: int, k: int, r_squared: int) -> tuple:
    A = -2 * h
    B = -2 * k
    C = h**2 + k**2 - r_squared
    return A, B, C
