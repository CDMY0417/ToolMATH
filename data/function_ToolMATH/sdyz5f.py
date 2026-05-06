def rationalize_denominator_a(numerator: float, denominator: float):
    from sympy import sqrt, Rational
    numer = sqrt(numerator)
    denom = sqrt(denominator)
    expr = numer / denom
    expr_rationalized = expr * sqrt(denominator) / sqrt(denominator)
    return expr_rationalized
