def approximate_sqrt_upper_bound(num: int) -> int:
    upper = int(num ** 0.5) + (1 if (int(num ** 0.5) ** 2) < num else 0)
    return upper
