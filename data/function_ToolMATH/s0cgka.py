def circular_function_expansion(n: int):
    from sympy import I, exp, simplify
    from sympy.abc import x
    expr = (exp(I*x) - exp(-I*x))/(2*I)
    expanded_expr = simplify(expr**n)
    return expanded_expr.as_coefficients_dict()
