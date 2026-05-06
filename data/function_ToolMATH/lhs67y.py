def expand_binomials(a1: int, b1: int, a2: int, b2: int) -> str:
    return f'{a1}*x**2 + ({a1}*{b2} + {b1}*{a2})*x + {b1}*{b2}'
