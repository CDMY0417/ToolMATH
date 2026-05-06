def modular_inverse_o(a: int, m: int):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
