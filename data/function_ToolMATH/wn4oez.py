def subtract_equations_e(eq1: tuple, eq2: tuple, result1: int, result2: int):
    subtracted_terms = tuple(x - y for x, y in zip(eq1, eq2))
    result_difference = result1 - result2
    return subtracted_terms, result_difference
