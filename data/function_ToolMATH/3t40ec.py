def sum_of_coefficients(polynomial: list[list[float]]) -> float:
    coefficients = [term[0] for term in polynomial]
    return sum(coefficients)
