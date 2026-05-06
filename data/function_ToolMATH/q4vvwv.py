def compute_polynomial_with_factorial(n: int, a: float, b: float, c: float, d: float, e: float, f: float):
    from math import factorial
    return a + n * b + (n * (n - 1) / 2) * c + (n ** 2) * d + (2 ** (n - 1)) * e + factorial(n) * f
