def sum_of_squares_of_fractions(fractions: list[float]) -> float:
    return sum((1/f)**2 for f in fractions)
