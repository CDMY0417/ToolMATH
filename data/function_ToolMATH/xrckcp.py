def sequence_value(n: int) -> float:
    a = 1 / 2
    for _ in range(n):
        a = 1 + (a - 1) ** 2
    return a
