def solve_quadratic_inequality(coeff_a: float, coeff_b: float, coeff_c: float):
    import sympy as sp
    x = sp.symbols('x')
    inequality = coeff_a * x**2 + coeff_b * x + coeff_c <= 0
    solution = sp.solve(inequality, x)
    return solution
