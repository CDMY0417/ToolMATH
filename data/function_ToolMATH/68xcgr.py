def modulo_product(a: int, b: int, c: int, m: int) -> int:
    return (a % m) * (b % m) * (c % m) % m
