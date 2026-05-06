def evaluate_polynomial_modulo(coeffs: list[int], x: int, m: int) -> int:
    result = 0
    power = 1
    for coeff in coeffs:
        result = (result + coeff * power) % m
        power = (power * x) % m
    return result
