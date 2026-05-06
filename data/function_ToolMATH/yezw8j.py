def harmonic_number(n: int) -> float:
    H_n = 0.0
    for i in range(1, n + 1):
        H_n += 1 / i
    return H_n
