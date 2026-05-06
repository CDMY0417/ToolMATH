def solve_linear_system_b(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int):
    import sympy as sp
    x, y = sp.symbols('x y')
    eq1 = a1*x + b1*y - c1
    eq2 = a2*x + b2*y - c2
    solution = sp.solve((eq1, eq2), (x, y))
    return solution[x], solution[y]
