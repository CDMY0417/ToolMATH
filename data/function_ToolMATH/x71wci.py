def polynomial_transformation(coefficients: list[float]) -> list[float]:
    from sympy import symbols, expand
    x, y = symbols('x y')
    polynomial = sum(coefficient * x**i for i, coefficient in enumerate(coefficients))
    transformed_polynomial = expand(polynomial.subs(x, y - 1))
    expanded_coefficients = [transformed_polynomial.coeff(y, i) for i in range(transformed_polynomial.as_poly().degree() + 1)]
    return expanded_coefficients
