def find_vertical_asymptote(numerator: str, denominator: str):
    from sympy import solve, Symbol
    x = Symbol('x')
    solutions = solve(denominator, x)
    return solutions
