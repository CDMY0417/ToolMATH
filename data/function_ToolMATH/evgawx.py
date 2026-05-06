def multiply_polynomial_by_binomial(polynomial: tuple[float, float, float], binomial: tuple[float, float]):
    (a, b, c) = polynomial
    (d, e) = binomial
    return (a*d, a*e + b*d, b*e + c*d, c*e)
