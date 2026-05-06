def simplify_numerator(numerator: list[float], subtraction_term: list[float]) -> list[float]:
    return [a - b for a, b in zip(numerator, subtraction_term)]
