def simplify_polynomial_a(polynomial: str) -> str:
    from sympy import symbols, simplify
    x = symbols('x')
    return str(simplify(polynomial))
