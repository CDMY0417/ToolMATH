def modular_inverse_k(a: int, m: int) -> int:
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1
