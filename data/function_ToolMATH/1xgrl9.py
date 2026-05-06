def modular_inverse_a(a: int, n: int):
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return None
