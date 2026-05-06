def vieta_polynomial_roots(sum_roots: int, sum_of_products: int, product_of_roots: int):
    from sympy import symbols, Eq, solve
    x = symbols('x')
    polynomial = x**3 - sum_roots*x**2 + sum_of_products*x - product_of_roots
    roots = solve(Eq(polynomial, 0), x)
    return roots
