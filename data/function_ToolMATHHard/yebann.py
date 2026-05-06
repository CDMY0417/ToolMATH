import sympy as sp

def sum_irreducible_factors_at_two(coeffs):
    """Return sum of irreducible monic factor values at x=2."""
    x = sp.symbols('x')
    poly = sum(coeffs[i]*x**(len(coeffs)-1-i) for i in range(len(coeffs)))
    factors = sp.factor_list(poly)[1]
    total = 0
    for fac, exp in factors:
        total += fac.subs(x, 2)
    return int(total)
