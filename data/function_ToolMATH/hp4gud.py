def sum_of_consecutive_integers_e(n: int, k: int) -> int:
    return k * (n + (n + k - 1)) // 2
