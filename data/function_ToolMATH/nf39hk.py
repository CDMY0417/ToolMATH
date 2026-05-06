def next_perfect_sixth_power(n: int) -> int:
    k = int(n ** (1/6)) + 1
    return k ** 6
