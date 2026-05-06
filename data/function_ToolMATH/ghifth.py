def congruence_modulus(a: int, b: int, c: int, m: int):
    for x in range(m):
        if (a * x + b) % m == c:
            return x
    return None
