import numpy as np

def evaluate_polynomial_at_roots_of_unity(coefficients: list[float], n: int):
    p = np.polynomial.Polynomial(coefficients)
    roots_of_unity = [np.exp(2j * np.pi * k / n) for k in range(n)]
    evaluations = [p(root) for root in roots_of_unity]
    return evaluations
