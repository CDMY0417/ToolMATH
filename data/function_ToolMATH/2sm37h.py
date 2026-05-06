def smallest_greater_than(a: int, m: int, threshold: int) -> int:
    n = a
    while n <= threshold:
        n += m
    return n
