def find_holes(numerator: str, denominator: str):
    # Simplify the rational function to find holes
    from sympy import simplify, symbols
    x = symbols('x')
    function = simplify(numerator + '/(' + denominator + ')')
    cancelled_parts = simplify(numerator) / function.as_numer_denom()[0]
    return [val.evalf() for val in cancelled_parts.as_poly().all_roots()]
