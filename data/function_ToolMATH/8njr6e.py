def polynomial_remainder_theorem(coefficients: list[int], a: int) -> int:
    remainder = 0
    power = len(coefficients) - 1
    for coef in coefficients:
        remainder += coef * (a ** power)
        power -= 1
    return remainder
