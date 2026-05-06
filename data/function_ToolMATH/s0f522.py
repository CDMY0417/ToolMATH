def format_polynomial(coefficients: tuple, variables: tuple):
    terms = [f'{coeff}{var}' for coeff, var in zip(coefficients, variables)]
    return '+'.join(terms)
