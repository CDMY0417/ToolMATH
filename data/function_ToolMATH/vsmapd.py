def distributive_multiplication_a(coefficients: tuple, monomial: int):
    return tuple(coef * monomial for coef in coefficients)
