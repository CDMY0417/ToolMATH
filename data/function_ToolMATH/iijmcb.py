def solve_quadratic_q(a: float, b: float, c: float):
    d = b**2 - 4*a*c
    if d < 0:
        return []  # No real roots
    elif d == 0:
        return [-b / (2*a)]
    else:
        sqrt_d = d**0.5
        return [(-b + sqrt_d) / (2*a), (-b - sqrt_d) / (2*a)]
