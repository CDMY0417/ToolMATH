def greatest_common_factor_l(a: str, b: str) -> str:
    import sympy as sp
    a_term = sp.sympify(a)
    b_term = sp.sympify(b)
    gcf = sp.gcd(a_term, b_term)
    return str(gcf)
