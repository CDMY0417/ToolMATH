def calculate_asymptotes(numerator_degree: int, denominator_degree: int):
    horizontal_asymptotes = 1 if numerator_degree < denominator_degree else 0
    oblique_asymptotes = 1 if numerator_degree == denominator_degree + 1 else 0
    return horizontal_asymptotes, oblique_asymptotes
