def evaluate_polynomial_p(coefficients: list[int], x: int) -> int:
    result = 0
    n = len(coefficients)
    for i in range(n):
        result += coefficients[i] * (x ** (n - i - 1))
    return result
