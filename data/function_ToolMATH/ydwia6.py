def smallest_multiple_greater_than_c(n: int, threshold: int) -> int:
    remainder = threshold % n
    if remainder == 0:
        return threshold
    return threshold + (n - remainder)
