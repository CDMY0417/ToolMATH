def is_perfect_power(n: int, k: int) -> bool:
    root = int(round(n ** (1.0 / k)))
    return root ** k == n
