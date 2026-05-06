def evaluate_polynomial_at_points_a(coefficients: list[int], points: list[int]) -> list[int]:
    results = []
    for point in points:
        value = 0
        for power, coeff in enumerate(coefficients):
            value += coeff * (point ** power)
        results.append(value)
    return results
