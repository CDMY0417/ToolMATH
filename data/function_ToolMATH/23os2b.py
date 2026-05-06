def multiply_fractions_with_number(fractions: list[float], number: float) -> float:
    result = number
    for fraction in fractions:
        result *= fraction
    return result
