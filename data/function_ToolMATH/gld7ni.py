def match_coefficients(polynomial1: tuple, polynomial2: tuple):
    return [eq1 - eq2 for eq1, eq2 in zip(polynomial1, polynomial2)]
