def find_vertical_asymptotes_a(denominator: str):
    # Vertical asymptotes occur where the denominator is zero
    from sympy import symbols, solve
    x = symbols('x')
    return solve(denominator, x)
