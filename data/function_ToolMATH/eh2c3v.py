def solve_linear_fractional_equation(a: int, b: int, c: int) -> int:
    x = b * (a * c) // (a - c)
    return x
