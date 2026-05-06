def subtract_equations_d(eq1_terms: tuple, eq2_terms: tuple) -> tuple:
    return tuple(a - b for a, b in zip(eq1_terms, eq2_terms))
