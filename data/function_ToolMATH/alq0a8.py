def simplify_fraction_br(numerator: float, denominator: float):
    import sympy as sp
    frac = sp.Rational(numerator, denominator)
    return frac
