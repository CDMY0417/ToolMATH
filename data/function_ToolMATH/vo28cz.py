def simplify_sqrt_term(c: int, a: int, n: int) -> int:
    factor = a ** (n // 2)
    new_c = c * factor
    return new_c * (a ** (n % 2))
