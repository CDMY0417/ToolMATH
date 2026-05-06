def solve_quadratic_equation_b(c: int, value: int):
    sqrt_value = int(value ** 0.5)
    x1 = sqrt_value - c
    x2 = -sqrt_value - c
    return x1, x2
